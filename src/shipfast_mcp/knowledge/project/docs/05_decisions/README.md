# Sổ quyết định

> Nơi duy nhất ghi quyết định của dự án. Mỗi quyết định một file; file này là mục lục. Code và tài liệu chỉ trỏ mã, không chép lại nội dung. Tạo nhanh bằng tool `new_decision`.

## 1. Quy ước

| Mục | Nội dung |
|---|---|
| Loại và mã | `SP-nnn` sản phẩm, nghiệp vụ · `KT-nnn` kỹ thuật · `QT-nnn` quy trình, cách làm việc. Số tăng dần theo từng loại, không đánh lại, không dùng lại |
| Tên file | `<mã>-<short-name>.md`, tên ngắn tiếng Anh, chữ thường, gạch nối. Ví dụ `KT-003-cookie-session-auth.md` |
| Mẫu | [`_template.md`](_template.md) |
| Trạng thái | **Giả định** (Điều hành đặt tạm, chờ PO) · **Hiệu lực** (PO chốt) · **Bị thay thế bởi <mã>** · **Huỷ** |
| Sửa đổi | Không sửa nội dung quyết định đã hiệu lực. Đổi thì tạo quyết định mới ghi "Thay thế cho", và đổi trạng thái bản cũ ngay trong file cũ lẫn mục lục |
| Định danh không đổi | Tên kỹ thuật đã phát hành (tên package, bảng DB, khoá cấu hình, tiền tố route) muốn giữ nguyên khi đổi tên sản phẩm thì ghi thành một quyết định `KT` liệt kê từng tên |
| Thứ tự ưu tiên | Quyết định hiệu lực > tài liệu thiết kế > ghi chú khác. Mâu thuẫn mới thì báo PO |

## 2. Mục lục

| Mã | Tên | Trạng thái | Ngày | Đợt | Thay thế cho |
|---|---|---|---|---|---|
| [QT-001](QT-001-adopt-shipfast.md) | Áp dụng quy trình shipfast | Hiệu lực | {{NGAY}} | — | — |
