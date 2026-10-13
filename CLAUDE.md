# CLAUDE.md — shipfast-mcp

MCP server (Python, FastMCP) phân phối quy trình làm việc theo wave. Mô tả và cách dùng: `README.md`.

## Nơi ghi quyết định

Quyết định thiết kế của repo này ghi ở `docs/decisions/README.md`, mỗi quyết định một mục có mã `D-nnn`. Code trỏ mã, không chép nội dung.

## Bố cục

| Đường dẫn | Nội dung |
|---|---|
| `src/shipfast_mcp/server.py` | Khai báo tool, prompt, resource |
| `src/shipfast_mcp/scaffold.py` | Scaffold, nâng cấp three-way merge, `.shipfast/` |
| `src/shipfast_mcp/project.py` | `status`, `next_code`, `open_wave`, `new_decision`, `check` |
| `src/shipfast_mcp/templates.py` | Danh sách file khung, loại `managed` / `seed`, biến `{{...}}` |
| `src/shipfast_mcp/knowledge/project/` | Khung dựng vào dự án đích (giữ đúng cây thư mục đích) |
| `src/shipfast_mcp/knowledge/skills/` | Skill chép vào `.claude/skills/` của dự án và phục vụ qua `skill://` |
| `src/shipfast_mcp/knowledge/guide/` | Tài liệu cho người, nguồn của landing site sau này |
| `plugin/`, `.claude-plugin/marketplace.json` | Plugin Claude Code (chỉ khai MCP server) |
| `server.json` | Khai báo cho MCP Registry |

## Luật

- Kho tri thức không gắn stack, không chứa chi tiết nội bộ của dự án hay tổ chức nào (host, app key, cổng cố định, env).
- Không đổi chữ trong dòng giữ chỗ của khung (`(chưa điền…)`, `(dự án bổ sung…)`): dự án nào cũng sửa các dòng này, đổi chữ ở đó là gây xung đột khi `upgrade`.
- Thêm file khung mới: đặt vào `knowledge/project/`; file dữ liệu của dự án (chỉ tạo một lần) thì thêm vào `SEED` trong `templates.py`.
- Đổi phiên bản: sửa cùng lúc `pyproject.toml`, `plugin/.claude-plugin/plugin.json` (cả `version` và tham số `uvx`), `server.json`.
- Sau khi sửa kho tri thức hoặc code: `uv run pytest`; build và dry run qua `uvx --from dist/*.whl shipfast-mcp` khi đổi đóng gói.
- File tạm trong `tmp/`. Không commit, push khi người dùng chưa yêu cầu. Nhánh theo luật chung của người dùng.
