# Wxx — Cleanup

> Bước 🧹 của vòng đời wave (`../README.md` §1), sau 🔨 Build, trước 🧪 Acceptance. Ranh giới an toàn: `../../ORGANIZATION.md` §8.

| Mục | Giá trị |
|---|---|
| Phụ trách | Orchestrator / <mã bộ phận cleanup> |
| Bắt đầu | YYYY-MM-DD |
| Kết thúc | — |
| Trạng thái | 🧹 Đang quét / Chờ chủ vùng / Xong |

## 1. Kiểm ranh giới an toàn

| Kiểm | Kết quả |
|---|---|
| Không xoá, ghi đè, đổi tên, di chuyển hay mở nội dung mục nào trong danh sách cấm `../../ORGANIZATION.md` §8.2 | ✔ / ✘ |
| Không xoá hàng loạt `tmp/` bằng một lệnh | ✔ / ✘ |
| File xoá trong `tmp/` đều khớp mẫu tên ở `../../ORGANIZATION.md` §8.3 | ✔ / ✘ |
| Không xoá trực tiếp ngoài `tmp/`; mục ở vùng khác do chủ vùng xoá | ✔ / ✘ |
| Không thêm mục bỏ qua của công cụ quét secret rộng hơn mục hiện có | ✔ / ✘ |
| Không đưa ảnh chụp, dữ liệu thật vào `reports/`, file thiết kế, hồ sơ wave hay commit | ✔ / ✘ |

## 2. Danh sách kiểm

Mỗi dòng ghi kết quả quét: "Không có" hoặc mã mục `CL-Wxx-nn` ở §3. Dự án thêm dòng riêng theo công nghệ của mình.

| # | Mục kiểm | Cách kiểm | Chủ vùng | Kết quả |
|---|---|---|---|---|
| 1 | Export, hàm, component, hook, kiểu không còn nơi gọi | Dò nơi nhập theo tên (`rg`) hoặc công cụ đã ghim bằng quyết định `KT` | Chủ vùng code | |
| 2 | Route, màn, đường chuyển hướng cũ hết hạn | Rà cấu hình route và menu | Chủ vùng giao diện | |
| 3 | Khoá chuỗi hiển thị, lớp CSS, biến theme không còn dùng | Dò tên khoá, lớp, biến trong mã nguồn | Chủ vùng giao diện | |
| 4 | Hằng giá trị trùng giữa các phần (contract, cấu hình, server) | Dò tên hằng và giá trị | Chủ vùng contract | |
| 5 | Test chết hoặc bị bỏ qua (`skip`, `todo`) không có lý do | Dò `.skip`, `.todo`, `xit`, `xdescribe` | Chủ vùng của test | |
| 6 | Test và bộ chọn e2e của màn đã bỏ | Đối chiếu kịch bản với route hiện có | Chủ vùng test | |
| 7 | Tài liệu lệch mã: `../../02_build/CONTRACTS.md`, tài liệu thiết kế, release notes (mục lặp, phiên bản sai) | Đối chiếu với mã và lịch sử release | Người giữ tài liệu | |
| 8 | Góp ý giao diện của PO trong wave đã rút thành nguyên tắc | Mục mới có trong `../../technical/` | Chủ vùng giao diện | |
| 9 | Khung thiết kế, demo của màn đã bỏ | Đánh dấu "đã bỏ"; chỉ xoá khi PO đồng ý | Chủ vùng giao diện | |
| 10 | Mục bỏ qua của công cụ quét secret còn đúng không | Quét lại đạt; mục thừa đề xuất gỡ | Người giữ bảo mật | |
| 11 | Ảnh chụp, trang thử trong `tmp/` và `reports/` của wave đã đóng | Chỉ theo danh sách cho phép; `reports/` do Orchestrator xoá | Orchestrator | |
| 12 | File khác trong `tmp/` không khớp danh sách cho phép | Chỉ liệt kê tên; chờ PO | PO | |
| 13 | Trạng thái hồ sơ lệch thực tế (README wave, `WAVES.md`, `3-build.md`, mục lục quyết định) | Tool `check` | Orchestrator | |

## 3. Mục dọn

| Mã | Vùng | Mục | Bằng chứng | Đề xuất | Người xoá | Trạng thái |
|---|---|---|---|---|---|---|
| CL-Wxx-01 | | | | Xoá / Giữ (lý do) / Backlog | | ⏳ Chờ / ✔ Đã xoá / ↩ Giữ / → BL-nnn |

## 4. File đã xoá trong `tmp/`

| Mẫu tên (`../../ORGANIZATION.md` §8.3) | Số file | Ghi chú |
|---|---|---|

## 5. Đề xuất mẫu tên mới cho danh sách cho phép

| Mẫu tên | Lý do | PO duyệt |
|---|---|---|

## 6. Việc chuyển backlog

| Việc | Phụ trách | Mã |
|---|---|---|

## 7. Kết luận

| Mục | Giá trị |
|---|---|
| Số mục | |
| Đã xử lý | |
| Giữ có lý do | |
| Chuyển backlog | |
| Quality gate sau dọn | ✔ / ✘ |
| Sang 🧪 Acceptance | YYYY-MM-DD |
