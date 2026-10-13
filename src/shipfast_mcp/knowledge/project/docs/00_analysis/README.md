# Phân tích đầu vào

> Báo cáo phân tích những gì dự án kế thừa hoặc tham khảo: hệ cũ, dự án nguồn lấy code, sản phẩm tương tự. Báo cáo mô tả **nguồn**, không đặt luật cho dự án này; luật lấy từ `../05_decisions/` và `../01_design/`.

## 1. Quy ước

| Mục | Nội dung |
|---|---|
| Tên file | `nn-<topic>.md` (tiếng Anh), số tăng dần, không đánh lại số |
| Đầu mỗi báo cáo | Nguồn (đường dẫn, phiên bản hoặc commit), ngày phân tích, phạm vi, người phân tích |
| Nội dung nên có | Tóm tắt nhanh; nguồn có gì; lấy được gì (chép nguyên / viết lại / chỉ tham khảo); **không mang sang** và lý do; danh sách file đã chép sang `_legacy/` |
| Nguồn là hệ thật | Chỉ đọc. Không chạy script, seed, tool của nguồn; không đọc env, mật khẩu, cookie; chỉ ghi tên biến |
| Bản sao tham chiếu | File cần giữ để đối chiếu khi port thì chép vào `_legacy/<topic>/` ở gốc repo, giữ đường dẫn tương đối, kèm `MANIFEST.txt`. `_legacy/` chỉ đọc: không sửa, không build, không import từ code mới |
| Từ phân tích sang luật | PO chốt việc lấy hay bỏ → ghi quyết định ở `../05_decisions/` → báo cáo chỉ trỏ mã |
| Lỗi thời | Nguồn đổi nhiều hoặc đã port xong thì đổi trạng thái, không xoá |

## 2. Sổ đăng ký

| Mã | Báo cáo | Nguồn | Ngày | Kết luận chính | Bản sao `_legacy/` | Trạng thái |
|---|---|---|---|---|---|---|
