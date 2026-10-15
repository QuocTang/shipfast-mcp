# Quyết định thiết kế — shipfast-mcp

| Mã | Quyết định | Trạng thái | Ngày |
|---|---|---|---|
| D-001 | Python, FastMCP 4, chạy qua `uvx`, transport stdio | Hiệu lực | 2026-10-13 |
| D-002 | Kho tri thức đóng gói trong package, là nguồn duy nhất; độc lập với ts-project-template | Hiệu lực | 2026-10-13 |
| D-003 | Tool ghi file trực tiếp vào dự án, có `dry_run`, không ghi đè | Hiệu lực | 2026-10-13 |
| D-004 | Kho tri thức viết theo định dạng skill; MCP phục vụ qua `skill://` và chép vào `.claude/skills/` của dự án | Hiệu lực | 2026-10-13 |
| D-005 | Nâng cấp bằng three-way merge dựa trên `.shipfast/base/` | Hiệu lực | 2026-10-13 |
| D-006 | Release: GitHub public (kiêm marketplace Claude Code), PyPI và MCP Registry | Hiệu lực | 2026-10-13 |
| D-007 | Plugin Claude Code chỉ khai MCP server, không mang skill | Hiệu lực | 2026-10-13 |
| D-008 | Không dùng Roots, Sampling, Logging của MCP | Hiệu lực | 2026-10-13 |
| D-009 | License MIT | Hiệu lực | 2026-10-13 |
| D-010 | Thuật ngữ chuyên ngành giữ tiếng Anh; vai chính gọi là Orchestrator | Hiệu lực | 2026-10-13 |
| D-012 | Site tài liệu HTML tĩnh trong `site/`, Tailwind biên dịch trước, đăng qua GitHub Pages; trình bày mô hình, MCP là một công cụ | Hiệu lực | 2026-10-14 |
| D-013 | Ngân sách ngữ cảnh là luật của quy trình; bộ phận chọn model theo việc | Hiệu lực | 2026-10-14 |
| D-014 | Bộ phận tự mang model, mức suy nghĩ, kỷ luật riêng; quy trình không phụ thuộc profile bên ngoài | Hiệu lực | 2026-10-15 |
| D-011 | Bộ phận lập theo dự án từ W01, nhận việc theo lĩnh vực; Orchestrator chỉ điều phối | Hiệu lực | 2026-10-13 |

## D-001 — Runtime

Python ≥ 3.12, FastMCP 4.x (hỗ trợ cả đặc tả `2026-07-28` lẫn client cũ), lệnh `shipfast-mcp`, chạy qua `uvx`. Transport stdio vì tool cần ghi file trên máy dev.

## D-002 — Nguồn tri thức

`src/shipfast_mcp/knowledge/` là nguồn duy nhất của quy trình. Viết lại từ phần quy trình của ts-project-template cho trung tính với mọi stack, gộp cách làm đã chạy thật ở devai-tracker. Không đồng bộ ngược với ts-project-template.

## D-003 — Ghi file

`scaffold_project`, `upgrade`, `open_wave`, `new_decision` ghi trực tiếp. `scaffold_project` và `upgrade` mặc định `dry_run=true`. Không ghi đè file đã có; xung đột nâng cấp ghi ra `.shipfast/pending/`.

## D-004 — Định dạng skill

Skill tự kích hoạt theo mô tả nên giữ luật quy trình trong suốt phiên tốt hơn prompt hay resource MCP. Skill được chép vào dự án để nhóm dùng chung và dự án vẫn làm việc được khi MCP tắt; phiên bản skill đi cùng phiên bản khung của dự án.

## D-005 — Nâng cấp

Dự án commit `.shipfast/manifest.json` (phiên bản, biến, loại file) và `.shipfast/base/` (bản khung lần trước của file `managed`). `upgrade` so ba bản bằng `git merge-file`. File `seed` (bảng wave, backlog, decision log, thiết kế…) không bị thay đổi. File dự án đã xoá không bị tạo lại.

## D-006 — Release

Repo GitHub public chứa mã và `.claude-plugin/marketplace.json`. Gói PyPI `shipfast-mcp`, đẩy bằng GitHub Actions trusted publishing khi gắn tag `vX.Y.Z`. MCP Registry đăng bằng workflow `registry.yml` (xác thực GitHub OIDC) sau khi workflow release thành công; README giữ dòng `mcp-name` để Registry xác minh gói PyPI. Nguồn: https://github.com/modelcontextprotocol/registry/blob/main/docs/modelcontextprotocol-io/github-actions.mdx

## D-007 — Plugin

Plugin `shipfast` chỉ khai MCP server với phiên bản ghim. Skill đến dự án qua `scaffold_project`/`upgrade`, tránh hai bản skill cùng kích hoạt (bản của plugin và bản trong dự án).

## D-008 — Tính năng MCP không dùng

Roots, Sampling, Logging đã bị đặc tả `2026-07-28` khai tử. Thư mục dự án truyền qua tham số `project_dir`; log ra stderr.

## D-009 — License

MIT cho mã và tài liệu.

## D-010 — Thuật ngữ

Thuật ngữ chuyên ngành giữ tiếng Anh, câu văn tiếng Việt. Bảng đối chiếu: `src/shipfast_mcp/knowledge/guide/changelog.md` mục 0.2.0. Tool đọc được cả nhãn của bản 0.1.x trong file dữ liệu dự án.

## D-011 — Bộ phận và Orchestrator

Ở W01, Orchestrator đề xuất bộ phận theo sản phẩm (W01-09), PO duyệt, tool `create_department` tạo hồ sơ `docs/departments/<mã>/` và subagent `.claude/agents/dept-<mã>.md`. Việc thuộc lĩnh vực nào giao bộ phận đó; Orchestrator chỉ tự làm việc nhỏ của vai điều phối (`knowledge/project/docs/ORGANIZATION.md` §5). Lĩnh vực mới thì đề xuất lập thêm. Subagent viết theo định dạng của Claude Code; client khác dùng hồ sơ trong `docs/departments/`.

## D-012 — Landing page

`site/src/index.html` là HTML tĩnh viết sẵn (không render phía trình duyệt), CSS biên dịch bằng Tailwind CLI, font Inter tự host, chuyển động chỉ bằng CSS và `IntersectionObserver` (không thư viện), tắt khi giảm chuyển động hoặc khi trình duyệt tự động (`navigator.webdriver`). Workflow `pages.yml` build và đăng khi `site/` đổi trên `main`. Site trình bày mô hình làm việc theo kiểu playbook: trang tổng quan liệt kê từng quy trình, mỗi quy trình một trang chi tiết; shipfast-mcp chỉ là một trong hai cách áp dụng (cách còn lại là áp thủ công). Trang sinh từ `site/gen/content.py` bằng `site/gen/build.py`.

## D-013 — Ngân sách ngữ cảnh

Phân tích transcript thật (transcora, vibe-ai-insights, 13–14/10/2026): chi phí chủ yếu là đọc lại ngữ cảnh mỗi lượt; phiên Orchestrator tự khảo sát và build làm ngữ cảnh trung bình 400–500k và kéo dài hàng nghìn lượt. Luật đặt ở `knowledge/project/docs/ORGANIZATION.md` §5.1; `create_department` nhận `model` để bộ phận soạn tài liệu, rà soát, khảo sát dùng model nhẹ. Luật chung của subagent nằm trong file `dept-<mã>.md` (Claude Code dùng làm lời dặn hệ thống), nên lời giao việc không chép lại; `refresh_departments` làm mới file này khi mẫu đổi.

## D-014 — Model, mức suy nghĩ, kỷ luật riêng của bộ phận

Bộ phận quyết định cả ai làm lẫn làm thế nào, để quy trình dùng được độc lập, không cần profile agent bên ngoài. File `dept-<mã>.md` ghi `model`, `effort` (trường frontmatter của subagent Claude Code, giá trị `low`…`max`) và mục "Kỷ luật riêng của bộ phận"; `create_department` nhận `model`, `effort`, `discipline`; `refresh_departments` giữ ba giá trị này. Đây là mặc định của bộ phận; việc khác mặc định thì Orchestrator truyền `model`, `effort` khi gọi subagent theo bảng "Model và mức suy nghĩ theo việc" ở `knowledge/project/docs/ORGANIZATION.md` §5.1. Nguồn: https://code.claude.com/docs/en/sub-agents (mục Supported frontmatter fields).
