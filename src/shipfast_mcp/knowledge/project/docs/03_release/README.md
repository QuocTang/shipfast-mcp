# Release và vận hành

> Bước 6 của wave và hotfix (`../04_waves/README.md` §1, §5) theo file này. Ranh giới triển khai: `../ORGANIZATION.md` §8.4.

## 1. Môi trường

| Môi trường | Địa chỉ | Cách truy cập | Ghi chú |
|---|---|---|---|
| (chưa điền) | | | |

## 2. Các bước release

| # | Việc |
|---|---|
| 1 | Orchestrator commit bản đã qua acceptance (chỉ file của wave) |
| 2 | Kiểm trước triển khai: (chưa điền danh sách kiểm; ví dụ quality gate xanh trên commit sẽ triển khai, không còn thay đổi chưa commit, phiên bản đã tăng, migration mới chỉ thêm) |
| 3 | Backup dữ liệu, giữ bản đang chạy để quay lại |
| 4 | Build và triển khai: (chưa điền lệnh) |
| 5 | Kiểm sau triển khai: (chưa điền lệnh hoặc danh sách kiểm; ví dụ health trả 200, phiên bản đúng, màn chính mở được); xem log vài phút |
| 6 | Ghi `RELEASE-NOTES.md` (không lặp mục, phiên bản khớp tag); gắn tag phiên bản |

Chỉ một agent thao tác môi trường thật mỗi lúc.

## 3. Quay lại bản trước

(chưa điền lệnh)

## 4. Tài liệu

| File | Nội dung |
|---|---|
| [`RELEASE-NOTES.md`](RELEASE-NOTES.md) | Ghi chú từng bản release |
| [`OPERATIONS.md`](OPERATIONS.md) | Vận hành hằng ngày: khởi động, log, backup, sự cố thường gặp |
