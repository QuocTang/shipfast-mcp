"""Thao tác trên hồ sơ quy trình của dự án: trạng thái, cấp mã, mở wave, ghi quyết định, kiểm hồ sơ."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

from . import __version__
from .scaffold import PENDING_DIR, load_manifest, resolve_project

WAVES_DIR = "docs/04_waves"
WAVES_FILE = f"{WAVES_DIR}/WAVES.md"
BACKLOG_FILE = f"{WAVES_DIR}/BACKLOG.md"
WAVE_TEMPLATE_DIR = f"{WAVES_DIR}/_template"
DECISIONS_DIR = "docs/05_decisions"
DECISIONS_INDEX = f"{DECISIONS_DIR}/README.md"

WAVE_RE = re.compile(r"^W(\d{2,})$")
DECISION_KINDS = {"SP": "Sản phẩm", "KT": "Kỹ thuật", "QT": "Quy trình"}
GLOBAL_KINDS = {"BL", "FB", "SP", "KT", "QT", "OPS", "HOTFIX", "PO", "W"}
WAVE_KINDS = {"ISSUE", "P", "CR", "Q", "CL", "QA"}
MODES = {"po": "PO chốt", "direct": "Chốt thẳng", "delegated": "Delegation"}
# Tiêu đề bảng wave; "| Đợt" là nhãn của bản 0.1.x, dự án cũ vẫn giữ trong file dữ liệu.
WAVES_HEADER = ("| Wave", "| Đợt")
# Nhãn trạng thái hiện hành, kèm nhãn tương đương của bản 0.1.x.
STATES = {
    "Intake": ("Intake", "Gom việc"),
    "Discussion": ("Discussion", "Thảo luận"),
    "Scope lock": ("Scope lock", "Chốt phạm vi"),
    "Build": ("Build", "Thi công"),
    "Cleanup": ("Cleanup", "Dọn dẹp"),
    "Acceptance": ("Acceptance", "Nghiệm thu"),
    "On hold": ("On hold", "Tạm hoãn"),
    "Closed": ("Closed", "Đã đóng"),
}


def _read(root: Path, rel: str) -> str:
    path = root / rel
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _max_number(text: str, pattern: str) -> int:
    nums = [int(m) for m in re.findall(pattern, text)]
    return max(nums, default=0)


def _wave_dirs(root: Path) -> list[str]:
    base = root / WAVES_DIR
    if not base.exists():
        return []
    return sorted(p.name for p in base.iterdir() if p.is_dir() and WAVE_RE.match(p.name))


def _table_rows(text: str, header_startswith: str | tuple[str, ...]) -> list[list[str]]:
    """Lấy các dòng dữ liệu của bảng markdown đầu tiên có dòng tiêu đề bắt đầu bằng header_startswith."""
    lines = text.splitlines()
    rows: list[list[str]] = []
    for i, line in enumerate(lines):
        if line.startswith(header_startswith) and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").strip()) <= {"-", ":"}:
            for row in lines[i + 2 :]:
                if not row.startswith("|"):
                    break
                rows.append([c.strip() for c in row.strip().strip("|").split("|")])
            break
    return rows


def _norm_wave(wave: str) -> str:
    wave = wave.strip().upper()
    if not wave.startswith("W"):
        wave = "W" + wave
    digits = wave[1:]
    if not digits.isdigit():
        raise ValueError("wave phải có dạng W03 hoặc 3")
    return f"W{int(digits):02d}"


def _code_corpus(root: Path, kind: str) -> str:
    """Gom văn bản ở đúng nơi ghi của từng loại mã (README.md §3), bỏ qua ví dụ trong tài liệu quy trình."""
    if kind in DECISION_KINDS:
        dec = root / DECISIONS_DIR
        names = " ".join(p.name for p in dec.glob("*.md")) if dec.exists() else ""
        index = " ".join(r[0] for r in _table_rows(_read(root, DECISIONS_INDEX), "| Mã") if r)
        return names + "\n" + index
    if kind in ("PO", "OPS", "HOTFIX"):
        return _read(root, WAVES_FILE)
    waves = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for w in _wave_dirs(root)
        for p in (root / WAVES_DIR / w).rglob("*.md")
    )
    return "\n".join([_read(root, BACKLOG_FILE), _read(root, WAVES_FILE), waves])


def next_code(project_dir: str, kind: str, wave: str = "") -> dict:
    """Cấp mã kế tiếp theo hệ mã của quy trình (docs/04_waves/README.md §3).

    kind toàn dự án: BL, FB, SP, KT, QT, OPS, HOTFIX, PO (việc PO giao ngoài wave), W (wave mới).
    kind trong wave (cần wave): ISSUE (Wxx-nn), P (Wxx-Pnn), CR, Q, CL, QA.
    Trả {"code": ...}. Ném ValueError khi kind không hỗ trợ hoặc thiếu wave.
    """
    root = resolve_project(project_dir)
    kind = kind.strip().upper()
    if kind == "W":
        nums = [int(WAVE_RE.match(d).group(1)) for d in _wave_dirs(root)]
        nums += [int(r[0][1:]) for r in _table_rows(_read(root, WAVES_FILE), WAVES_HEADER) if r and WAVE_RE.match(r[0])]
        return {"code": f"W{max(nums, default=0) + 1:02d}"}
    if kind in GLOBAL_KINDS:
        width = 2 if kind in ("OPS", "HOTFIX", "PO") else 3
        n = _max_number(_code_corpus(root, kind), rf"\b{kind}-(\d+)\b") + 1
        return {"code": f"{kind}-{n:0{width}d}"}
    if kind not in WAVE_KINDS:
        raise ValueError(f"kind phải thuộc {sorted(GLOBAL_KINDS | WAVE_KINDS)}")
    if not wave:
        raise ValueError(f"kind {kind} cần tham số wave, ví dụ W03")
    w = _norm_wave(wave)
    num = w[1:]
    patterns = {
        "ISSUE": (rf"\b{w}-(\d{{2,}})\b", f"{w}-{{n:02d}}"),
        "P": (rf"\b{w}-P(\d+)\b", f"{w}-P{{n:02d}}"),
        "CR": (rf"\bCR-{w}-(\d+)\b", f"CR-{w}-{{n:02d}}"),
        "Q": (rf"\bQ-{w}-(\d+)\b", f"Q-{w}-{{n:02d}}"),
        "CL": (rf"\bCL-{w}-(\d+)\b", f"CL-{w}-{{n:02d}}"),
        "QA": (rf"\bQA{num}-(\d+)\b", f"QA{num}-{{n}}"),
    }
    pattern, fmt = patterns[kind]
    wave_dir = root / WAVES_DIR / w
    wave_text = (
        "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in wave_dir.rglob("*.md"))
        if wave_dir.exists()
        else ""
    )
    return {"code": fmt.format(n=_max_number(wave_text, pattern) + 1)}


def status(project_dir: str) -> dict:
    """Tóm tắt trạng thái quy trình của dự án để phiên mới làm tiếp được.

    Trả: phiên bản khung, bảng wave, wave chưa đóng kèm số vấn đề còn "Chờ",
    số việc backlog đang mở, quyết định còn "Giả định", xung đột nâng cấp chưa xử lý.
    """
    root = resolve_project(project_dir)
    manifest = load_manifest(root)
    result: dict = {
        "shipfast_installed": manifest.get("version") if manifest else None,
        "shipfast_available": __version__,
    }
    if manifest is None:
        result["hint"] = "Dự án chưa scaffold shipfast. Repo mới: prompt init. Dự án đang chạy: prompt adopt."
        return result
    if manifest.get("version") != __version__:
        result["hint"] = "Có phiên bản khung mới; chạy tool upgrade (dry_run) để xem thay đổi."
    waves = []
    for row in _table_rows(_read(root, WAVES_FILE), WAVES_HEADER):
        if len(row) >= 4 and row[0]:
            waves.append({"wave": row[0], "lead": row[1], "name": row[2], "state": row[3]})
    result["waves"] = waves
    open_waves = []
    for w in _wave_dirs(root):
        readme = _read(root, f"{WAVES_DIR}/{w}/README.md")
        m = re.search(r"^\| Trạng thái \| (.+?) \|", readme, re.M)
        state = m.group(1) if m else "?"
        if _state_key(state) == "Closed":
            continue
        discussion = _read(root, f"{WAVES_DIR}/{w}/1-discussion.md")
        waiting = [r[0] for r in _table_rows(discussion, "| Mã") if r and r[-1].startswith("Chờ") and r[0].startswith(w)]
        open_waves.append({"wave": w, "state": state, "issues_waiting_po": waiting})
    result["open_waves"] = open_waves
    backlog_open = [r for r in _table_rows(_read(root, BACKLOG_FILE), "| Mã") if r and r[0].startswith("BL-")]
    result["backlog_open"] = len(backlog_open)
    assumed = [r[0] for r in _table_rows(_read(root, DECISIONS_INDEX), "| Mã") if len(r) > 2 and "Giả định" in r[2]]
    result["decisions_assumed"] = assumed
    pending = root / PENDING_DIR
    if pending.exists():
        result["upgrade_conflicts"] = sorted(p.relative_to(pending).as_posix() for p in pending.rglob("*") if p.is_file())
    return result


def open_wave(project_dir: str, title: str, goal: str, mode: str = "po", lead: str = "Orchestrator") -> dict:
    """Mở wave mới từ `docs/04_waves/_template/` của chính dự án và thêm dòng vào bảng wave.

    mode: "po" (PO chốt từng vấn đề), "direct" (chốt thẳng, wave nhỏ), "delegated" (delegation, cần QT-nnn).
    Trả mã wave và danh sách file đã tạo. Ném ValueError khi thiếu mẫu hoặc mode sai.
    """
    root = resolve_project(project_dir)
    if mode not in MODES:
        raise ValueError(f"mode phải thuộc {sorted(MODES)}")
    template = root / WAVE_TEMPLATE_DIR
    if not template.exists():
        raise ValueError(f"Không có {WAVE_TEMPLATE_DIR}; scaffold bằng tool scaffold trước")
    code = next_code(str(root), "W")["code"]
    target = root / WAVES_DIR / code
    target.mkdir(parents=True)
    today = date.today().isoformat()
    created = []
    for src in sorted(template.glob("*.md")):
        if src.name.startswith("debate-") and mode != "delegated":
            continue
        text = src.read_text(encoding="utf-8").replace("Wxx", code).replace("YYYY-MM-DD", today)
        if src.name == "README.md":
            text = text.replace("<tên wave>", title).replace(
                "<một câu: sau wave này người dùng hoặc PO có được gì>", goal
            ).replace("Orchestrator / <mã bộ phận>", lead).replace(
                "PO chốt / Chốt thẳng (lý do) / Delegation (`QT-nnn`)", MODES[mode]
            )
        name = src.name
        if name.startswith("debate-"):
            (target / "debate").mkdir(exist_ok=True)
            name = f"debate/{name.removeprefix('debate-').removesuffix('.md')}-_mau.md"
        if name in ("README.md", "1-discussion.md") or name.startswith("debate/"):
            (target / name).write_text(text, encoding="utf-8")
            created.append(f"{WAVES_DIR}/{code}/{name}")
    waves = root / WAVES_FILE
    if waves.exists():
        lines = waves.read_text(encoding="utf-8").splitlines()
        row = f"| {code} | {lead} | {title} | 📥 Intake | {goal} | — | — | [{code}/]({code}/README.md) |"
        insert_at = _table_end(lines, WAVES_HEADER)
        if insert_at is not None:
            lines.insert(insert_at, row)
            waves.write_text("\n".join(lines) + "\n", encoding="utf-8")
            created.append(f"{WAVES_FILE} (thêm dòng {code})")
    return {
        "wave": code,
        "created": created,
        "next": "File 2-scope, 3-build, 4-cleanup, 5-acceptance chép từ _template/ khi tới bước tương ứng.",
    }


def _table_end(lines: list[str], header_startswith: str | tuple[str, ...]) -> int | None:
    for i, line in enumerate(lines):
        if line.startswith(header_startswith):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            return j
    return None


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "decision"


def new_decision(
    project_dir: str,
    kind: str,
    title: str,
    short_name: str,
    context: str = "",
    decision: str = "",
    status: str = "Giả định",
    wave: str = "—",
    decided_by: str = "",
) -> dict:
    """Ghi một quyết định mới vào `docs/05_decisions/` theo mẫu của dự án và cập nhật mục lục.

    kind: SP, KT hoặc QT. short_name: tên ngắn tiếng Anh cho tên file.
    status: "Giả định" (Orchestrator đặt tạm) hoặc "Hiệu lực" (PO đã chốt).
    Trả mã và đường dẫn file. Ném ValueError khi kind hoặc status sai.
    """
    root = resolve_project(project_dir)
    kind = kind.strip().upper()
    if kind not in DECISION_KINDS:
        raise ValueError(f"kind phải thuộc {sorted(DECISION_KINDS)}")
    if status not in ("Giả định", "Hiệu lực"):
        raise ValueError('status phải là "Giả định" hoặc "Hiệu lực"')
    code = next_code(str(root), kind)["code"]
    rel = f"{DECISIONS_DIR}/{code}-{_slugify(short_name)}.md"
    template = root / DECISIONS_DIR / "_template.md"
    text = template.read_text(encoding="utf-8") if template.exists() else "# <MÃ> — <tên quyết định>\n"
    today = date.today().isoformat()
    by = decided_by or ("PO" if status == "Hiệu lực" else "Orchestrator (giả định)")
    text = (
        text.replace("<MÃ>", code)
        .replace("<tên quyết định>", title)
        .replace("Sản phẩm / Kỹ thuật / Quy trình", DECISION_KINDS[kind])
        .replace("Giả định / Hiệu lực / Bị thay thế bởi <mã> / Huỷ", status)
        .replace("YYYY-MM-DD", today)
        .replace("PO / Orchestrator (giả định)", by)
        .replace("Wxx-nn / —", wave)
        .replace("<mã> / —", "—")
    )
    if context:
        text = text.replace("<Vấn đề cần quyết, ràng buộc đang có.>", context)
    if decision:
        text = text.replace("<Chọn phương án nào, phát biểu ngắn, kiểm được.>", decision)
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    index = root / DECISIONS_INDEX
    if index.exists():
        lines = index.read_text(encoding="utf-8").splitlines()
        at = _table_end(lines, "| Mã")
        if at is not None:
            lines.insert(at, f"| [{code}]({Path(rel).name}) | {title} | {status} | {today} | {wave} | — |")
            index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"code": code, "file": rel, "next": "Điền phần Phương án đã xét và Hệ quả trong file vừa tạo."}


LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def check(project_dir: str) -> dict:
    """Kiểm hồ sơ quy trình, trả danh sách vấn đề theo nhóm.

    Nhóm: biến khung còn sót, link nội bộ gãy, wave đã đóng thiếu rút kinh nghiệm,
    wave đã đóng còn vấn đề "Chờ", trạng thái wave lệch giữa bảng wave và README wave,
    mục lục quyết định lệch file, xung đột nâng cấp chưa xử lý.
    """
    root = resolve_project(project_dir)
    issues: dict[str, list[str]] = {}

    def add(group: str, item: str) -> None:
        issues.setdefault(group, []).append(item)

    docs_files = [root / "CLAUDE.md", *(root / "docs").rglob("*.md")] if (root / "docs").exists() else []
    for f in docs_files:
        if not f.exists() or "_template" in f.parts:
            continue
        rel = f.relative_to(root).as_posix()
        text = f.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"\{\{[A-Z_]+\}\}", text):
            add("bien_khung_con_sot", rel)
        for link in LINK_RE.findall(text):
            if "://" in link or link.startswith("mailto:"):
                continue
            if not (f.parent / link).exists():
                add("link_gay", f"{rel} → {link}")

    waves_table = {r[0]: r[3] for r in _table_rows(_read(root, WAVES_FILE), WAVES_HEADER) if len(r) >= 4}
    for w in _wave_dirs(root):
        readme = _read(root, f"{WAVES_DIR}/{w}/README.md")
        m = re.search(r"^\| Trạng thái \| (.+?) \|", readme, re.M)
        state = m.group(1).strip() if m else ""
        table_state = waves_table.get(w)
        if table_state is None:
            add("wave_thieu_trong_bang", w)
        elif state and _state_key(state) != _state_key(table_state):
            add("trang_thai_lech", f"{w}: README «{state}» / WAVES.md «{table_state}»")
        if _state_key(state) == "Closed":
            acceptance = _read(root, f"{WAVES_DIR}/{w}/5-acceptance.md")
            retro = _table_rows(acceptance, "| Tốt")
            if not any(any(c for c in r) for r in retro):
                add("dong_wave_thieu_rut_kinh_nghiem", w)
            discussion = _read(root, f"{WAVES_DIR}/{w}/1-discussion.md")
            waiting = [r[0] for r in _table_rows(discussion, "| Mã") if r and r[-1].startswith("Chờ") and r[0].startswith(w)]
            if waiting:
                add("dong_wave_con_cho", f"{w}: {', '.join(waiting)}")

    index_codes = {re.sub(r"\[([^\]]+)\].*", r"\1", r[0]) for r in _table_rows(_read(root, DECISIONS_INDEX), "| Mã") if r}
    dec_dir = root / DECISIONS_DIR
    if dec_dir.exists():
        file_codes = {p.name.split("-")[0] + "-" + p.name.split("-")[1] for p in dec_dir.glob("[A-Z][A-Z]-[0-9]*.md")}
        for c in sorted(file_codes - index_codes):
            add("quyet_dinh_thieu_muc_luc", c)
        for c in sorted(index_codes - file_codes):
            add("muc_luc_thieu_file", c)

    pending = root / PENDING_DIR
    if pending.exists():
        for p in pending.rglob("*"):
            if p.is_file():
                add("xung_dot_nang_cap", p.relative_to(pending).as_posix())
    return {"ok": not issues, "issues": issues}


def _state_key(state: str) -> str:
    """Quy nhãn trạng thái (mới hoặc của bản 0.1.x) về khoá hiện hành; không khớp thì trả nguyên."""
    for key, labels in STATES.items():
        if any(label in state for label in labels):
            return key
    return state
