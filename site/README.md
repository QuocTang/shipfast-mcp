# Site tài liệu shipfast

Trang tài liệu về mô hình làm việc shipfast, đăng tại https://quoctang.github.io/shipfast-mcp/ bằng workflow `.github/workflows/pages.yml`.

| Lệnh | Việc |
|---|---|
| `npm ci` | Cài Tailwind CLI, font Inter và JetBrains Mono |
| `npm run gen` | Sinh các trang HTML trong `src/` từ `gen/content.py` |
| `npm run build` | Dựng `dist/`: chép HTML, JS, favicon, font; biên dịch `src/style.css` |
| `npm run preview` | Dựng rồi chạy ở http://localhost:4173 |

| File | Nội dung |
|---|---|
| `gen/content.py` | Nội dung: tổng quan, từng quy trình, trang Áp dụng. Sửa nội dung ở đây |
| `gen/guides.py` | Nội dung trang chi tiết theo câu hỏi của người đọc: khi nào dùng, việc của người kèm câu mẫu, việc của AI kèm điểm cần kiểm tra, ví dụ |
| `gen/build.py` | Khung trang: tổng quan, trang chi tiết quy trình, trang Áp dụng |
| `gen/header.html`, `gen/waves.html` | Header và dải sóng có cá ở đầu trang tổng quan |
| `src/*.html` | Trang đã sinh (commit cùng repo); không sửa tay |
| `src/style.css` | Token màu, font, chuyển động; nguồn của Tailwind |
| `src/app.js` | Hiện dần khi cuộn tới, nút chép lệnh |

Mỗi quy trình trong `gen/content.py` có các khoá: `slug`, `brief`, `group`, `code`, `name`, `goal`, `outputs`, `gate`, `cases`, tuỳ chọn `sections`, `example`, `tools`. Mỗi `slug` cần một mục cùng tên trong `GUIDES` của `gen/guides.py`. Thêm quy trình thì thêm cả hai, chạy `npm run gen`.
