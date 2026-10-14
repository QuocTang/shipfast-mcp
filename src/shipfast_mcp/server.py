"""MCP server: đưa kho tri thức shipfast ra ngoài thành skill, tài liệu, prompt và tool."""

from __future__ import annotations

from typing import Annotated, Literal

from fastmcp import FastMCP
from fastmcp.server.providers.skills import SkillsDirectoryProvider
from pydantic import Field

from . import __version__, project, scaffold
from .templates import GUIDES, SKILLS

INSTRUCTIONS = """\
shipfast: quy trình làm việc theo wave giữa PO (người dùng), Orchestrator (phiên AI chính) và subagent, \
dùng được cho mọi stack.

- Repo mới: dùng prompt `init` (hoặc đọc skill://shipfast-init/SKILL.md). Dự án đang chạy: prompt `adopt`.
- Dự án đã có `.shipfast/manifest.json`: đọc `CLAUDE.md` và `docs/04_waves/README.md` của dự án, gọi tool `status` \
trước khi làm việc. Luật quy trình nằm trong skill://shipfast-process/SKILL.md.
- Nâng khung lên phiên bản mới: tool `upgrade` (chạy dry_run trước). Không cần repo gốc để so sánh.
- Tài liệu cho người: tool `read_guide`.
Mọi tool ghi file nhận `project_dir` là đường dẫn tuyệt đối tới gốc repo dự án.
"""

ProjectDir = Annotated[str, Field(description="Đường dẫn tuyệt đối tới gốc repo dự án")]

mcp = FastMCP("shipfast", instructions=INSTRUCTIONS, version=__version__)
mcp.add_provider(SkillsDirectoryProvider(roots=SKILLS))

GUIDE_TOPICS = {p.stem: p for p in sorted(GUIDES.glob("*.md"))}


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": False})
def scaffold_project(
    project_dir: ProjectDir,
    name: Annotated[str, Field(description="Slug dự án: chữ thường không dấu, số, gạch ngang")],
    display_name: Annotated[str, Field(description="Tên hiển thị của dự án")],
    description: Annotated[str, Field(description="Mô tả sản phẩm một hai câu; để trống nếu chưa chốt")] = "",
    branch: Annotated[str, Field(description="Nhánh chính của repo")] = "main",
    code_lang: Annotated[Literal["vi", "en"], Field(description="Ngôn ngữ comment và commit message")] = "vi",
    mode: Annotated[Literal["init", "adopt"], Field(description="init: repo mới, kèm hồ sơ W01. adopt: dự án đang chạy")] = "init",
    dry_run: Annotated[bool, Field(description="true: chỉ báo sẽ tạo gì, không ghi file")] = True,
) -> dict:
    """Scaffold quy trình shipfast vào dự án: CLAUDE.md, docs/ (wave, backlog, decision log, tổ chức), skill trong .claude/skills/.

    Không ghi đè file đã có. Ghi .shipfast/ để sau này nâng cấp tự gộp. Luôn chạy dry_run trước và trình PO danh sách.
    """
    return scaffold.scaffold(project_dir, name, display_name, description, branch, code_lang, mode, dry_run)


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False, "idempotentHint": True})
def upgrade(
    project_dir: ProjectDir,
    dry_run: Annotated[bool, Field(description="true: chỉ báo thay đổi, không ghi file")] = True,
) -> dict:
    """Nâng khung quy trình của dự án lên phiên bản shipfast đang chạy, không cần repo gốc.

    File dự án chưa sửa thì thay bằng bản mới; file dự án đã sửa thì three-way merge; xung đột thì để bản gộp ở
    .shipfast/pending/ và giữ nguyên file thật. File dữ liệu của dự án (bảng wave, backlog, decision log) không bị đụng.
    """
    return scaffold.upgrade(project_dir, dry_run)


@mcp.tool(annotations={"readOnlyHint": True})
def status(project_dir: ProjectDir) -> dict:
    """Trạng thái quy trình: phiên bản khung, bảng wave, wave đang mở và vấn đề chờ PO, backlog, quyết định giả định."""
    return project.status(project_dir)


@mcp.tool(annotations={"readOnlyHint": True})
def next_code(
    project_dir: ProjectDir,
    kind: Annotated[
        Literal["BL", "FB", "SP", "KT", "QT", "OPS", "HOTFIX", "PO", "W", "ISSUE", "P", "CR", "Q", "CL", "QA"],
        Field(description="Loại mã. ISSUE, P, CR, Q, CL, QA là mã trong wave, cần wave"),
    ],
    wave: Annotated[str, Field(description="Mã wave, ví dụ W03; chỉ cần cho mã trong wave")] = "",
) -> dict:
    """Cấp mã kế tiếp (BL-012, W03-04, CR-W03-02, KT-005…) bằng cách quét hồ sơ, tránh trùng số."""
    return project.next_code(project_dir, kind, wave)


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False})
def open_wave(
    project_dir: ProjectDir,
    title: Annotated[str, Field(description="Tên wave")],
    goal: Annotated[str, Field(description="Một câu: sau wave này người dùng hoặc PO có được gì")],
    mode: Annotated[
        Literal["po", "direct", "delegated"],
        Field(description="po: PO chốt từng vấn đề. direct: chốt thẳng cho wave nhỏ. delegated: delegation, cần QT-nnn"),
    ] = "po",
    lead: Annotated[str, Field(description="Chủ trì: Orchestrator hoặc mã bộ phận")] = "Orchestrator",
) -> dict:
    """Mở wave mới: tạo docs/04_waves/Wxx/ từ mẫu của dự án, thêm dòng vào bảng wave ở trạng thái Intake."""
    return project.open_wave(project_dir, title, goal, mode, lead)


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False})
def new_decision(
    project_dir: ProjectDir,
    kind: Annotated[Literal["SP", "KT", "QT"], Field(description="SP sản phẩm, KT kỹ thuật, QT quy trình")],
    title: Annotated[str, Field(description="Tên quyết định, tiếng Việt")],
    short_name: Annotated[str, Field(description="Tên ngắn tiếng Anh cho tên file, ví dụ cookie-session-auth")],
    context: Annotated[str, Field(description="Bối cảnh")] = "",
    decision: Annotated[str, Field(description="Phát biểu quyết định, ngắn, kiểm được")] = "",
    status: Annotated[Literal["Giả định", "Hiệu lực"], Field(description="Hiệu lực chỉ khi PO đã chốt")] = "Giả định",
    wave: Annotated[str, Field(description="Mã vấn đề nguồn, ví dụ W03-02")] = "—",
) -> dict:
    """Ghi quyết định mới vào docs/05_decisions/ theo mẫu của dự án, cấp mã và cập nhật mục lục."""
    return project.new_decision(project_dir, kind, title, short_name, context, decision, status, wave)


@mcp.tool(annotations={"readOnlyHint": False, "destructiveHint": False})
def create_department(
    project_dir: ProjectDir,
    code: Annotated[str, Field(description="Mã viết hoa, ví dụ PLATFORM, TRUST")],
    name: Annotated[str, Field(description="Tên bộ phận, ví dụ Nền tảng")],
    domain: Annotated[str, Field(description="Lĩnh vực phụ trách, một câu")],
    owns: Annotated[str, Field(description="Vùng thư mục sở hữu, ví dụ `src/`, `tests/`")],
    decision: Annotated[str, Field(description="Mã QT lập bộ phận nếu đã ghi")] = "",
    model: Annotated[str, Field(description="Model của subagent: inherit, sonnet, opus, haiku hoặc mã model; việc soạn tài liệu, rà soát, khảo sát nên dùng model nhẹ")] = "inherit",
) -> dict:
    """Lập bộ phận theo dự án: hồ sơ docs/departments/<mã>/, subagent .claude/agents/dept-<mã>.md, thêm vào ORGANIZATION.md.

    Sau khi lập, mọi việc thuộc lĩnh vực của bộ phận được giao cho subagent này; Orchestrator chỉ điều phối.
    """
    return project.create_department(project_dir, code, name, domain, owns, decision, model)


@mcp.tool(annotations={"readOnlyHint": True})
def check(project_dir: ProjectDir) -> dict:
    """Kiểm hồ sơ: biến khung sót, link gãy, wave đóng thiếu rút kinh nghiệm hoặc còn vấn đề Chờ, bảng wave lệch, decision log lệch."""
    return project.check(project_dir)


@mcp.tool(annotations={"readOnlyHint": True})
def read_guide(
    topic: Annotated[str, Field(description="Tên bài; để trống để xem danh sách")] = "",
) -> str:
    """Đọc tài liệu hướng dẫn shipfast cho người: bắt đầu từ đâu, tổ chức, ý nghĩa, phát triển và nâng cấp."""
    if not topic:
        lines = ["Các bài hướng dẫn:"]
        for name, path in GUIDE_TOPICS.items():
            first = path.read_text(encoding="utf-8").splitlines()[0].lstrip("# ")
            lines.append(f"- {name}: {first}")
        return "\n".join(lines)
    if topic not in GUIDE_TOPICS:
        raise ValueError(f"Không có bài {topic}. Có: {', '.join(GUIDE_TOPICS)}")
    return GUIDE_TOPICS[topic].read_text(encoding="utf-8")


for _name, _path in GUIDE_TOPICS.items():
    mcp.resource(f"shipfast://guide/{_name}", name=f"guide-{_name}", mime_type="text/markdown")(
        (lambda p: lambda: p.read_text(encoding="utf-8"))(_path)
    )


def _skill(name: str) -> str:
    return (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")


@mcp.prompt
def init(project_dir: str = "") -> str:
    """Khởi tạo dự án mới theo quy trình shipfast: chạy wave W01, AI đề xuất và phản biện stack, PO chốt."""
    where = f"Thư mục dự án: {project_dir}\n\n" if project_dir else ""
    return f"{where}Làm theo skill dưới đây.\n\n{_skill('shipfast-init')}"


@mcp.prompt
def adopt(project_dir: str = "") -> str:
    """Áp quy trình shipfast vào dự án đang chạy, giữ tài liệu và quyết định sẵn có."""
    where = f"Thư mục dự án: {project_dir}\n\n" if project_dir else ""
    return f"{where}Làm theo skill dưới đây.\n\n{_skill('shipfast-adopt')}"


@mcp.prompt(name="upgrade")
def upgrade_prompt(project_dir: str = "") -> str:
    """Nâng khung quy trình của dự án lên phiên bản shipfast mới, gộp với phần dự án đã sửa."""
    where = f"Thư mục dự án: {project_dir}\n\n" if project_dir else ""
    return f"{where}Làm theo skill dưới đây.\n\n{_skill('shipfast-upgrade')}"


def main() -> None:
    """Điểm vào của lệnh `shipfast-mcp`: chạy server qua stdio."""
    mcp.run(show_banner=False)


if __name__ == "__main__":
    main()
