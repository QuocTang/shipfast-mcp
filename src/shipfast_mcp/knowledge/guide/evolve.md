# Phát triển tiếp và nâng cấp

## Trong một dự án

| Muốn | Làm |
|---|---|
| Đổi cách làm việc của dự án | Ghi `QT-nnn` (tool `new_decision`), sửa tài liệu tương ứng; PO chốt |
| Thêm quy chuẩn kỹ thuật | Thêm file vào `docs/technical/`, ghi vào mục lục của thư mục |
| Thêm bộ phận | Lĩnh vực mới không bộ phận nào phụ trách: PO duyệt, tool `create_department` (`docs/ORGANIZATION.md` §6) |
| Chạy song song nhiều agent | Chia team theo vùng thư mục (`docs/ORGANIZATION.md` §4.1) trong `2-scope.md` |
| Giảm số lần phải chốt | Delegation (`docs/ORGANIZATION.md` §7) |
| Thêm vai phản biện riêng | Thêm dòng vào `docs/ORGANIZATION.md` §7.4 |

Sửa thoải mái các file khung trong dự án; khi nâng cấp, phần đã sửa được giữ và gộp với thay đổi mới.

## Nâng cấp khung lên phiên bản shipfast mới

1. `uvx` tự lấy bản mới nhất khi khởi động MCP (ghim phiên bản bằng `uvx shipfast-mcp@0.2.1` nếu cần).
2. Tool `status` báo có bản mới. Gọi prompt `upgrade` hoặc nói "nâng cấp quy trình".
3. Tool `upgrade` dry run trước, phân loại từng file:
   - dự án chưa sửa → thay bằng bản mới;
   - cả hai cùng sửa nhưng khác chỗ → gộp tự động;
   - sửa cùng chỗ → bản gộp có đánh dấu xung đột ở `.shipfast/pending/`, file thật giữ nguyên, AI đề xuất cách hợp nhất để bạn duyệt;
   - file dữ liệu của dự án (bảng wave, backlog, decision log, thiết kế) không bị thay đổi.
4. Commit cả `.shipfast/` để người khác trong nhóm nâng cấp từ cùng một bản gốc.

## Góp lại cho shipfast

Cách làm nào chạy tốt ở dự án của bạn và dùng được cho mọi stack thì mở issue hoặc pull request ở repo shipfast-mcp: mô tả vấn đề gặp phải, cách làm, bằng chứng từ dự án thật. Bản release mới đến với mọi dự án qua `upgrade`.
