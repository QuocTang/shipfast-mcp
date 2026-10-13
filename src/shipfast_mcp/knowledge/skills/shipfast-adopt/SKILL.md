---
name: shipfast-adopt
description: Áp quy trình shipfast vào một dự án đang chạy (đã có code, có thể đã có tài liệu, decision log, quy trình riêng) mà không phá cái đang có. Dùng khi người dùng nói "áp quy trình vào dự án này", "cài shipfast cho repo đang có", gọi prompt adopt của MCP shipfast, hoặc repo đã có code nhưng chưa có .shipfast/.
---

# shipfast-adopt

Mục tiêu: dự án đang chạy có khung quy trình shipfast, giữ nguyên tài liệu và quyết định đang có, mỗi thông tin vẫn chỉ sống ở một chỗ. Việc này chạy như một wave chốt thẳng nhỏ do Orchestrator chủ trì.

## Bước

1. **Khảo sát chỉ đọc** (không đọc file env): stack, lệnh build/test, `README`, `CLAUDE.md` hoặc `AGENTS.md`, thư mục tài liệu, nơi đang ghi quyết định, backlog, quy trình làm việc hiện có. Ghi tóm tắt vào `tmp/shipfast-adopt.md`.
2. **Dry run**: tool `scaffold_project` với `mode="adopt"`, `dry_run=true`. Danh sách `skipped_existing` là các file trùng tên đã có.
3. **Lập bảng đối chiếu** trình PO, mỗi dòng: thứ đang có → chỗ tương ứng trong shipfast → đề xuất. Đề xuất mặc định:

| Đang có | Đề xuất |
|---|---|
| Decision log ở chỗ khác | Giữ nguyên chỗ cũ làm nguồn; `docs/05_decisions/README.md` trỏ tới, hoặc chuyển dần khi PO muốn. Không chép hai nơi |
| `CLAUDE.md` đã có | Giữ; thêm các mục còn thiếu từ khung (vai trò, wave, luật git cho agent, khi không chắc), PO duyệt từng mục |
| Backlog ở công cụ ngoài (issue tracker) | `BACKLOG.md` chỉ trỏ tới công cụ đó, hoặc dùng `BACKLOG.md` cho việc của agent |
| Quy trình riêng đang chạy tốt | Ghi khác biệt thành `QT-nnn`; phần tốt hơn shipfast đề nghị PO góp lại cho shipfast |
| Lệnh build/test | Điền `docs/02_build/CONTRACTS.md` §2 từ lệnh thật đang dùng |

4. PO duyệt thì gọi `scaffold_project` với `dry_run=false`, rồi gộp thủ công các file trùng theo bảng đã duyệt.
5. Đề xuất bộ bộ phận theo dự án (`docs/ORGANIZATION.md` §2.1), vùng sở hữu bám cấu trúc thư mục thật; PO duyệt thì lập bằng `create_department`. Ghi `QT-001` (đã có sẵn từ khung), `QT` lập bộ phận và các `QT` mô tả khác biệt. Bộ phận nền tảng điền `CONTRACTS.md`.
6. Mở wave kế từ việc đang làm dở (tool `open_wave`, chế độ phù hợp).
7. Gọi tool `check`, sửa tới khi sạch. Không commit khi PO chưa yêu cầu.
