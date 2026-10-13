---
name: shipfast-upgrade
description: Nâng khung quy trình shipfast của dự án lên phiên bản mới mà không cần repo gốc hay so sánh tay - tool upgrade tự three-way merge, Orchestrator trình PO các thay đổi và giải quyết xung đột. Dùng khi người dùng nói "nâng cấp quy trình", "cập nhật shipfast", "update template", hoặc tool status báo có phiên bản khung mới.
---

# shipfast-upgrade

Dự án giữ `.shipfast/manifest.json` (phiên bản, biến) và `.shipfast/base/` (bản khung lần trước). Tool `upgrade` dùng ba bản: bản gốc lần trước, bản dự án hiện tại, bản khung mới.

## Bước

1. Gọi `status`: xác nhận phiên bản đang cài và phiên bản có sẵn. Cây làm việc nên sạch (`git status`) để dễ xem lại thay đổi.
2. Gọi `upgrade` với `dry_run=true`. Đọc báo cáo:

| Nhóm | Nghĩa | Việc |
|---|---|---|
| `created` | File khung mới | Liệt kê cho PO |
| `updated` | Dự án chưa sửa file này, thay bằng bản mới | Liệt kê |
| `merged` | Cả hai bên đã sửa, gộp tự động không xung đột | Liệt kê, nhắc PO xem diff sau khi ghi |
| `conflicts` | Cả hai bên sửa cùng chỗ | Sẽ cần quyết |
| `kept` | Khung không đổi, hoặc dự án đã xoá file | Không làm gì |
| `skipped_existing` | File trùng tên do dự án tự tạo, không thuộc khung | Không làm gì |

3. Trình PO bảng tóm tắt (gọi file bằng tên tài liệu, ví dụ "Quy trình wave (`docs/04_waves/README.md`)"). PO đồng ý thì gọi `upgrade` với `dry_run=false`.
4. Xung đột: mở `.shipfast/pending/<file>`, giữa `<<<<<<< du-an` và `>>>>>>> shipfast-moi` là hai phiên bản. Đề xuất bản hợp nhất cho từng chỗ (giữ phần riêng của dự án, lấy luật mới của khung), PO duyệt, ghi vào file thật, rồi gọi `upgrade` (`dry_run=false`) lần nữa tới khi không còn xung đột.
5. Đọc ghi chú phát hành (tool `read_guide`, bài `changelog`) cho các bản nằm giữa bản cũ và bản mới. Bản mới đổi thuật ngữ hoặc nhãn thì liệt kê các file dữ liệu còn nhãn cũ (`WAVES.md`, `BACKLOG.md`, hồ sơ wave, decision log) và đề xuất PO đổi theo bảng trong ghi chú; tool vẫn đọc được nhãn cũ nên việc này không bắt buộc.
6. Đọc phần khác biệt của skill trong `.claude/skills/shipfast-*` và `docs/04_waves/README.md` (`git diff`), tóm tắt cho PO luật mới nào có hiệu lực.
7. Gọi `check`. Ghi một dòng `OPS-nn` vào `WAVES.md` §2: "Nâng shipfast từ <cũ> lên <mới>". Commit cả `.shipfast/` khi PO yêu cầu.
