# W01 — Thảo luận

> Trạng thái: 🗣️ Thảo luận. PO trả lời theo mã (ví dụ "W01-03: A"). Cột **PO chốt**: `Chờ` → `Làm (phương án …)` / `Không làm` / `Hoãn → BL-nnn`. Thứ tự gợi ý: W01-01 trước, W01-02 sau khi đã rõ sản phẩm; các vấn đề còn lại hỏi gộp.

## 1. Tổng hợp

| Mã | Vấn đề | Nguồn | Đề xuất | PO chốt |
|---|---|---|---|---|
| W01-01 | Sản phẩm làm gì, cho ai, bản đầu tiên cần gì | mới | Điều hành tóm tắt sau khi nghe PO | Chờ |
| W01-02 | Stack và thành phần | mới | Điều hành đề xuất 2–3 phương án, phản biện, PO chọn | Chờ |
| W01-03 | Tên dự án (slug) và tên hiển thị | mới | Slug = tên thư mục repo | Chờ |
| W01-04 | Dữ liệu và dịch vụ khi dev | mới | Theo stack đã chọn ở W01-02 | Chờ |
| W01-05 | Lệnh chuẩn và cổng kiểm chứng | mới | Lint, typecheck, test, build, quét secret | Chờ |
| W01-06 | Bí mật và cấu hình môi trường | mới | File mẫu commit, file thật gitignore | Chờ |
| W01-07 | Git | mới | Nhánh chính theo repo, chưa push | Chờ |
| W01-08 | Chế độ chốt từ W02 | mới | PO chốt, tham vấn vai phản biện khi cần | Chờ |

## 2. Chi tiết từng vấn đề

### W01-01 — Sản phẩm

| Mục | Nội dung |
|---|---|
| Bối cảnh | Cần mô tả một hai câu cho `CLAUDE.md` mục "Dự án là gì" và danh sách tính năng bản đầu để xếp backlog |
| Câu hỏi | Sản phẩm giải quyết việc gì? Ai dùng, mấy vai? Bản đầu cần làm được gì, cái gì chưa cần? Có hệ cũ hay dự án nguồn cần phân tích (`docs/00_analysis/`)? Ràng buộc về hạn, chi phí, nơi chạy? |
| Đề xuất | Điều hành tóm thành mô tả + danh sách `BL-nnn`, nêu những điểm còn mơ hồ, PO duyệt |
| Phản biện đề xuất | Bản đầu hay bị phình; Điều hành chủ động đề xuất cắt những gì chưa cần để kiểm giả thuyết chính |
| Công ước lượng | S |
| PO chốt | Chờ |

### W01-02 — Stack và thành phần

| Mục | Nội dung |
|---|---|
| Bối cảnh | Chưa có stack định sẵn. Chọn theo sản phẩm ở W01-01, kỹ năng của đội, nơi triển khai, hệ sinh thái sẵn có |
| Cách trình | 2–3 phương án, mỗi phương án: thành phần (thư mục, công nghệ, phiên bản ổn định hiện hành đã tra), lý do hợp, cái giá, rủi ro. Gọi vai phản biện ARCH, OPS, TRUST (`../../ORGANIZATION.md` §7.4) khi các phương án ngang nhau |
| Tra cứu | Phiên bản và cách dựng khung lấy từ tài liệu chính thức hiện hành, ghi nguồn trong `research/` |
| Đề xuất | (Điều hành điền sau W01-01) |
| Phản biện đề xuất | (Điều hành điền: điểm yếu của phương án đề xuất, khi nào nên đổi) |
| Đầu ra khi chốt | `KT-001` stack và thành phần; `docs/02_build/CONTRACTS.md` §1 |
| Công ước lượng | M |
| PO chốt | Chờ |

### W01-03 — Tên dự án

| Mục | Nội dung |
|---|---|
| Ràng buộc | Slug chữ thường không dấu, nối gạch ngang, bắt đầu bằng chữ cái; dùng cho tên package, image, tiền tố route, DB |
| Đề xuất | Slug = tên thư mục repo; tên hiển thị do PO đặt |
| PO chốt | Chờ |

### W01-04 — Dữ liệu và dịch vụ khi dev

| Mục | Nội dung |
|---|---|
| Câu hỏi | Cần lưu dữ liệu gì? DB nào, chạy ở đâu khi dev (máy local, container, server dùng chung)? Dịch vụ phụ (cache, hàng đợi, lưu file)? Cổng local? Đăng nhập khi dev dùng thật hay giả? |
| Đề xuất | (Điều hành điền theo stack ở W01-02; ưu tiên chạy hoàn toàn trên máy dev nếu không có ràng buộc khác) |
| Lưu ý | Tạo DB, chạy migration, ghi dữ liệu dùng chung chỉ khi PO duyệt |
| PO chốt | Chờ |

### W01-05 — Lệnh chuẩn và cổng kiểm chứng

| Mục | Nội dung |
|---|---|
| Bối cảnh | Definition of done của mọi đợt dựa vào các lệnh này (`../../../CLAUDE.md` mục Code) |
| Đề xuất | Một lệnh cho mỗi việc: cài đặt, lint, typecheck, test, build, chạy local, quét secret; ghi `docs/02_build/CONTRACTS.md` §2 |
| Phản biện đề xuất | Cổng chưa chạy thật lần nào thì vô nghĩa; nghiệm thu W01 phải chạy đủ |
| PO chốt | Chờ |

### W01-06 — Bí mật và cấu hình môi trường

| Mục | Nội dung |
|---|---|
| Phương án A | File mẫu (`.env.example` hoặc tương đương) giá trị giả được commit; file thật gitignore |
| Phương án B | Bí mật lấy từ trình quản lý bí mật hoặc biến môi trường của nền tảng triển khai |
| Đề xuất | A khi dev, B khi triển khai thật |
| PO chốt | Chờ |

### W01-07 — Git

| Mục | Nội dung |
|---|---|
| Đề xuất | Giữ nhánh chính và remote hiện có; quy ước tên nhánh và commit theo luật của PO nếu có; commit khung khi PO yêu cầu, không push tự động |
| PO chốt | Chờ |

### W01-08 — Chế độ chốt từ W02

| Mục | Nội dung |
|---|---|
| Phương án A | PO chốt từng vấn đề; Điều hành gọi vai phản biện tham vấn khi vấn đề có nhiều góc nhìn; đợt nhỏ chốt thẳng |
| Phương án B | Uỷ quyền: ghi `QT-002` (phạm vi, việc PO giữ lại, tiêu chí Chủ toạ); cần lập ít nhất hai bộ phận |
| Đề xuất | A; chuyển B khi đã có bộ phận và PO muốn giảm số lần chốt |
| PO chốt | Chờ |

## 3. Nhật ký trao đổi

| Ngày | Ai / vòng | Nội dung |
|---|---|---|
