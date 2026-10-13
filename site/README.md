# Landing page

Trang giới thiệu shipfast, đăng tại https://quoctang.github.io/shipfast-mcp/ bằng workflow `.github/workflows/pages.yml`.

| Lệnh | Việc |
|---|---|
| `npm ci` | Cài Tailwind CLI và font Inter |
| `npm run build` | Dựng `dist/`: chép HTML, JS, favicon, font; biên dịch `src/style.css` |
| `npm run preview` | Dựng rồi chạy ở http://localhost:4173 |

| File | Nội dung |
|---|---|
| `src/index.html` | Toàn bộ nội dung trang, HTML tĩnh |
| `src/style.css` | Token màu, font, chuyển động; nguồn của Tailwind |
| `src/app.js` | Hiện dần khi cuộn tới, tab ví dụ, nút chép lệnh |
| `src/favicon.svg` | Logo trên nền màu nhấn |

Màu nhấn đổi ở `--primary` trong `src/style.css`; logo ở `src/favicon.svg` và các chỗ dùng dấu trong `src/index.html` (đầu trang, chân trang, ảnh đại diện Orchestrator trong ví dụ). Chuyển động tắt khi hệ điều hành bật giảm chuyển động.
