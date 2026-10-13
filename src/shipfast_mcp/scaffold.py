"""Dựng khung vào dự án và nâng cấp khung bằng gộp ba phía.

Mỗi dự án giữ `.shipfast/manifest.json` (phiên bản, biến, loại từng file) và
`.shipfast/base/` (bản khung đã dựng lần gần nhất). Nhờ bản gốc này, nâng cấp
tự gộp được thay đổi của khung với thay đổi của dự án mà không cần repo gốc.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path

from . import __version__
from .templates import content_of, gitignore_lines, list_files, make_vars

STATE_DIR = ".shipfast"
MANIFEST = f"{STATE_DIR}/manifest.json"
BASE_DIR = f"{STATE_DIR}/base"
PENDING_DIR = f"{STATE_DIR}/pending"
WAVES_BOARD = "docs/04_waves/WAVES.md"
W01_ROW = "| W01 | Điều hành | Khởi tạo dự án | 🗣️ Thảo luận | Khung quy trình, stack đã chốt, khung code chạy được | — | — | [W01/](W01/README.md) |"


@dataclass
class Report:
    """Kết quả một lượt dựng hoặc nâng cấp; mỗi danh sách là đường dẫn tương đối."""

    dry_run: bool
    project_dir: str
    version_from: str | None = None
    version_to: str = __version__
    created: list[str] = field(default_factory=list)
    updated: list[str] = field(default_factory=list)
    merged: list[str] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    kept: list[str] = field(default_factory=list)
    skipped_existing: list[str] = field(default_factory=list)
    unchanged: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v not in ([], None)}


def resolve_project(project_dir: str) -> Path:
    """Chuẩn hoá thư mục dự án.

    Ném ValueError khi đường dẫn không tuyệt đối, không tồn tại hoặc không phải thư mục.
    """
    path = Path(project_dir).expanduser()
    if not path.is_absolute():
        raise ValueError("project_dir phải là đường dẫn tuyệt đối tới gốc repo dự án")
    if not path.is_dir():
        raise ValueError(f"Không tìm thấy thư mục {path}")
    return path.resolve()


def load_manifest(root: Path) -> dict | None:
    """Đọc manifest của dự án; chưa dựng khung thì trả None."""
    path = root / MANIFEST
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _save_state(root: Path, manifest: dict, bases: dict[str, str]) -> None:
    for rel, text in bases.items():
        _write(root / BASE_DIR / rel, text)
    _write(root / MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def _add_w01_row(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| Đợt"):
            lines.insert(i + 2, W01_ROW)
            break
    return "\n".join(lines) + "\n"


def _merge_gitignore(root: Path, report: Report) -> None:
    path = root / ".gitignore"
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    have = {line.strip() for line in current.splitlines()}
    missing = [line for line in gitignore_lines() if line.strip() not in have]
    if not missing:
        return
    report.updated.append(".gitignore")
    if report.dry_run:
        return
    prefix = "" if not current or current.endswith("\n") else "\n"
    _write(path, current + prefix + "\n".join(missing) + "\n")


def scaffold(
    project_dir: str,
    name: str,
    display_name: str,
    description: str = "",
    branch: str = "main",
    code_lang: str = "vi",
    mode: str = "init",
    dry_run: bool = True,
) -> dict:
    """Dựng khung tài liệu, quy trình và skill vào dự án. Không ghi đè file đã có.

    mode: "init" cho repo mới (kèm hồ sơ đợt W01), "adopt" cho dự án đang chạy.
    Trả báo cáo: file sẽ tạo / đã tạo, file bỏ qua vì đã có.
    Ném ValueError khi tham số sai hoặc dự án đã có manifest (dùng upgrade).
    """
    root = resolve_project(project_dir)
    if mode not in ("init", "adopt"):
        raise ValueError('mode phải là "init" hoặc "adopt"')
    if load_manifest(root) is not None:
        raise ValueError("Dự án đã dựng khung shipfast; dùng tool upgrade để cập nhật")
    variables = make_vars(name, display_name, description, branch, code_lang)
    report = Report(dry_run=dry_run, project_dir=str(root))
    files_meta: dict[str, str] = {}
    bases: dict[str, str] = {}
    for tf in list_files(mode):
        text = content_of(tf, variables)
        if mode == "init" and tf.target == WAVES_BOARD:
            text = _add_w01_row(text)
        target = root / tf.target
        if target.exists():
            report.skipped_existing.append(tf.target)
            continue
        report.created.append(tf.target)
        files_meta[tf.target] = tf.kind
        if tf.kind == "managed":
            bases[tf.target] = text
        if not dry_run:
            _write(target, text)
    _merge_gitignore(root, report)
    if report.skipped_existing:
        report.notes.append(
            "File đã có được giữ nguyên. Đối chiếu với khung qua resource hoặc tool read_guide, gộp thủ công khi cần."
        )
    if not dry_run:
        manifest = {"version": __version__, "mode": mode, "vars": variables, "files": files_meta}
        _save_state(root, manifest, bases)
    return report.as_dict()


def _merge3(current: str, base: str, new: str) -> tuple[str, bool]:
    """Gộp ba phía bằng `git merge-file`. Trả (nội dung, có xung đột hay không)."""
    if shutil.which("git") is None:
        return new, True
    with tempfile.TemporaryDirectory() as tmp:
        paths = []
        for label, text in (("current", current), ("base", base), ("new", new)):
            p = Path(tmp) / label
            p.write_text(text, encoding="utf-8")
            paths.append(str(p))
        proc = subprocess.run(
            ["git", "merge-file", "-p", "-L", "du-an", "-L", "ban-goc", "-L", "shipfast-moi", *paths],
            capture_output=True,
            text=True,
        )
    if proc.returncode < 0 or proc.returncode > 127:
        raise RuntimeError(f"git merge-file lỗi: {proc.stderr.strip()}")
    return proc.stdout, proc.returncode != 0


def upgrade(project_dir: str, dry_run: bool = True) -> dict:
    """Nâng khung của dự án lên phiên bản shipfast đang chạy.

    File "managed": dự án chưa sửa thì thay bằng bản mới; dự án đã sửa thì gộp ba phía
    (bản gốc lần trước, bản dự án, bản mới). Gộp xung đột thì không đụng file của dự án,
    ghi bản có dấu xung đột vào `.shipfast/pending/<đường dẫn>` để người quyết.
    File "seed" không bao giờ bị thay. File khung mới thì tạo.
    Ném ValueError khi dự án chưa dựng khung.
    """
    root = resolve_project(project_dir)
    manifest = load_manifest(root)
    if manifest is None:
        raise ValueError("Dự án chưa dựng khung shipfast; dùng tool scaffold trước")
    variables = dict(manifest["vars"])
    variables["PHIEN_BAN"] = __version__
    report = Report(dry_run=dry_run, project_dir=str(root), version_from=manifest.get("version"))
    files_meta: dict[str, str] = dict(manifest.get("files", {}))
    bases: dict[str, str] = {}
    pending_root = root / PENDING_DIR
    if not dry_run and pending_root.exists():
        shutil.rmtree(pending_root)

    for tf in list_files(manifest.get("mode", "init")):
        new = content_of(tf, variables)
        target = root / tf.target
        known = tf.target in files_meta
        if not target.exists():
            if known:
                report.kept.append(f"{tf.target} (dự án đã xoá, giữ nguyên)")
                continue
            report.created.append(tf.target)
            files_meta[tf.target] = tf.kind
            if tf.kind == "managed":
                bases[tf.target] = new
            if not dry_run:
                _write(target, new)
            continue
        if not known:
            report.skipped_existing.append(tf.target)
            continue
        if tf.kind == "seed" or files_meta[tf.target] == "seed":
            continue
        current = target.read_text(encoding="utf-8")
        base_path = root / BASE_DIR / tf.target
        base = base_path.read_text(encoding="utf-8") if base_path.exists() else None
        if current == new:
            report.unchanged.append(tf.target)
            bases[tf.target] = new
            continue
        if base is not None and current == base:
            report.updated.append(tf.target)
            bases[tf.target] = new
            if not dry_run:
                _write(target, new)
            continue
        if base is not None and new == base:
            report.kept.append(tf.target)
            continue
        merged, conflict = _merge3(current, base if base is not None else "", new)
        if conflict:
            report.conflicts.append(tf.target)
            if not dry_run:
                _write(pending_root / tf.target, merged)
            continue
        report.merged.append(tf.target)
        bases[tf.target] = new
        if not dry_run:
            _write(target, merged)

    _merge_gitignore(root, report)
    if report.conflicts:
        report.notes.append(
            "Xung đột: mở `.shipfast/pending/<file>`, chọn nội dung giữa các dấu <<<<<<< du-an / >>>>>>> shipfast-moi, "
            "chép vào file thật, rồi chạy lại upgrade. File thật chưa bị đổi."
        )
    if not dry_run:
        manifest["version"] = __version__
        manifest["files"] = files_meta
        _save_state(root, manifest, bases)
    return report.as_dict()
