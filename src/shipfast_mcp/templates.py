"""Đọc kho tri thức đóng gói kèm và dựng nội dung file cho dự án đích."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from . import __version__

KNOWLEDGE = Path(__file__).parent / "knowledge"
PROJECT_TEMPLATE = KNOWLEDGE / "project"
SKILLS = KNOWLEDGE / "skills"
GUIDES = KNOWLEDGE / "guide"
DEPARTMENT = KNOWLEDGE / "department"

GITIGNORE_SOURCE = "gitignore.append"

# File chỉ tạo một lần rồi thuộc về dự án; nâng cấp không đụng tới.
SEED = {
    "docs/GLOSSARY.md",
    "docs/01_design/README.md",
    "docs/02_build/CONTRACTS.md",
    "docs/03_release/OPERATIONS.md",
    "docs/03_release/RELEASE-NOTES.md",
    "docs/04_waves/WAVES.md",
    "docs/04_waves/BACKLOG.md",
    "docs/05_decisions/README.md",
    "docs/05_decisions/QT-001-adopt-shipfast.md",
    "docs/technical/README.md",
}

# Hồ sơ wave khởi tạo; chỉ dựng ở chế độ init.
INIT_ONLY_PREFIX = "docs/04_waves/W01/"

CODE_LANGS = {"vi": "tiếng Việt", "en": "tiếng Anh"}


@dataclass(frozen=True)
class TemplateFile:
    """Một file sẽ dựng vào dự án.

    target: đường dẫn tương đối trong dự án.
    source: file nguồn trong kho tri thức.
    kind: "managed" (nâng cấp bằng three-way merge) hoặc "seed" (chỉ tạo một lần).
    render: có thay biến {{...}} hay không.
    """

    target: str
    source: Path
    kind: str
    render: bool


def make_vars(
    name: str,
    display_name: str,
    description: str = "",
    branch: str = "main",
    code_lang: str = "vi",
    today: str | None = None,
) -> dict[str, str]:
    """Tạo bộ biến thay vào khung.

    Ném ValueError khi slug sai định dạng hoặc code_lang không hỗ trợ.
    """
    slug = name.strip()
    if not slug or not slug[0].isalpha() or not all(c.islower() or c.isdigit() or c == "-" for c in slug):
        raise ValueError("name phải là slug: chữ thường không dấu, số, gạch ngang, bắt đầu bằng chữ cái")
    if code_lang not in CODE_LANGS:
        raise ValueError(f"code_lang phải là một trong {sorted(CODE_LANGS)}")
    return {
        "TEN_DU_AN": display_name.strip() or slug,
        "SLUG": slug,
        "MO_TA": description.strip() or "(chưa điền)",
        "NHANH_CHINH": branch.strip() or "main",
        "NGAY": today or date.today().isoformat(),
        "PHIEN_BAN": __version__,
        "NGON_NGU_CODE": CODE_LANGS[code_lang],
    }


def render(text: str, variables: dict[str, str]) -> str:
    """Thay mọi {{KHOA}} bằng giá trị trong variables; khoá không có thì giữ nguyên."""
    for key, value in variables.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def list_files(mode: str) -> list[TemplateFile]:
    """Liệt kê file khung theo thứ tự cố định.

    mode: "init" (dự án mới, có hồ sơ W01) hoặc "adopt" (dự án đang chạy, không có W01).
    """
    files: list[TemplateFile] = []
    for src in sorted(PROJECT_TEMPLATE.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(PROJECT_TEMPLATE).as_posix()
        if rel == GITIGNORE_SOURCE:
            continue
        if rel.startswith(INIT_ONLY_PREFIX) and mode != "init":
            continue
        kind = "seed" if rel in SEED or rel.startswith(INIT_ONLY_PREFIX) else "managed"
        files.append(TemplateFile(rel, src, kind, render=True))
    for src in sorted(SKILLS.rglob("*")):
        if not src.is_file():
            continue
        rel = ".claude/skills/" + src.relative_to(SKILLS).as_posix()
        files.append(TemplateFile(rel, src, "managed", render=False))
    return files


def content_of(tf: TemplateFile, variables: dict[str, str]) -> str:
    """Trả nội dung đã dựng của một file khung."""
    text = tf.source.read_text(encoding="utf-8")
    return render(text, variables) if tf.render else text


def gitignore_lines() -> list[str]:
    """Các dòng cần có trong .gitignore của dự án."""
    text = (PROJECT_TEMPLATE / GITIGNORE_SOURCE).read_text(encoding="utf-8")
    return [line for line in text.splitlines() if line.strip()]
