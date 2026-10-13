# W01 — Discussion

> Trạng thái: 🗣️ Discussion. PO trả lời theo mã (ví dụ "W01-03: A"). Cột **PO chốt**: `Chờ` → `Làm (phương án …)` / `Không làm` / `Hoãn → BL-nnn`. Thứ tự gợi ý: W01-01 trước, W01-02 sau khi đã rõ sản phẩm; các vấn đề còn lại hỏi gộp.

## 1. Tổng hợp

| Mã | Vấn đề | Nguồn | Đề xuất | PO chốt |
|---|---|---|---|---|
| W01-01 | Sản phẩm làm gì, cho ai, bản đầu tiên cần gì | mới | Orchestrator tóm tắt sau khi nghe PO | Chờ |
| W01-02 | Stack và thành phần | mới | Orchestrator đề xuất 2–3 phương án, phản biện, PO chọn | Chờ |
| W01-03 | Tên dự án (slug) và tên hiển thị | mới | Slug = tên thư mục repo | Chờ |
| W01-04 | Dữ liệu và dịch vụ khi dev | mới | Theo stack đã chọn ở W01-02 | Chờ |
| W01-05 | Lệnh chuẩn và quality gate | mới | Lint, typecheck, test, build, quét secret | Chờ |
| W01-06 | Bí mật và cấu hình môi trường | mới | File mẫu commit, file thật gitignore | Chờ |
| W01-07 | Git | mới | Nhánh chính theo repo, chưa push | Chờ |
| W01-08 | Chế độ chốt từ W02 | mới | PO chốt, lấy ý kiến bộ phận và vai phản biện khi cần | Chờ |
| W01-09 | Tổ chức bộ phận | mới | Orchestrator đề xuất 3–5 bộ phận theo sản phẩm | Chờ |

## 2. Chi tiết từng vấn đề

### W01-01 — Sản phẩm

| Mục | Nội dung |
|---|---|
| Bối cảnh | Cần mô tả một hai câu cho `CLAUDE.md` mục "Dự án là gì" và danh sách tính năng bản đầu để xếp backlog |
| Câu hỏi | Sản phẩm giải quyết việc gì? Ai dùng, bao nhiêu vai? Bản đầu cần làm được gì, cái gì chưa cần? Có hệ cũ hay dự án nguồn cần phân tích (`docs/00_analysis/`)? Ràng buộc về hạn, chi phí, nơi chạy? |
| Đề xuất | Orchestrator tóm thành mô tả + danh sách `BL-nnn`, nêu những điểm còn mơ hồ, PO duyệt |
| Phản biện đề xuất | Phạm vi bản đầu thường mở rộng quá mức; Orchestrator chủ động đề xuất cắt những gì chưa cần để kiểm giả thuyết chính |
| Công ước lượng | S |
| PO chốt | Chờ |

### W01-02 — Stack và thành phần

| Mục | Nội dung |
|---|---|
| Bối cảnh | Chưa có stack định sẵn. Chọn theo sản phẩm ở W01-01, kỹ năng của đội, nơi triển khai, hệ sinh thái sẵn có |
| Cách trình | 2–3 phương án, mỗi phương án: thành phần (thư mục, công nghệ, phiên bản ổn định hiện hành đã tra), lý do hợp, cái giá, rủi ro. Gọi vai phản biện ARCH, OPS, TRUST (`../../ORGANIZATION.md` §7.4) khi các phương án ngang nhau |
| Tra cứu | Phiên bản và cách scaffold lấy từ tài liệu chính thức hiện hành, ghi nguồn trong `research/` |
| Đề xuất | (Orchestrator điền sau W01-01) |
| Phản biện đề xuất | (Orchestrator điền: điểm yếu của phương án đề xuất, khi nào nên đổi) |
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
| Đề xuất | (Orchestrator điền theo stack ở W01-02; ưu tiên chạy hoàn toàn trên máy dev nếu không có ràng buộc khác) |
| Lưu ý | Tạo DB, chạy migration, ghi dữ liệu dùng chung chỉ khi PO duyệt |
| PO chốt | Chờ |

### W01-05 — Lệnh chuẩn và quality gate

| Mục | Nội dung |
|---|---|
| Bối cảnh | Definition of done của mọi wave dựa vào các lệnh này (`../../../CLAUDE.md` mục Code) |
| Đề xuất | Một lệnh cho mỗi việc: cài đặt, lint, typecheck, test, build, chạy local, quét secret; ghi `docs/02_build/CONTRACTS.md` §2 |
| Phản biện đề xuất | Cổng chưa chạy thật lần nào thì vô nghĩa; acceptance W01 phải chạy đủ |
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
| Phương án A | PO chốt từng vấn đề; Orchestrator gọi vai phản biện tham vấn khi vấn đề có nhiều góc nhìn; wave nhỏ chốt thẳng |
| Phương án B | Delegation: ghi `QT-nnn` (phạm vi, việc PO giữ lại, tiêu chí Chủ toạ); các bộ phận lập ở W01-09 debate, Chủ toạ chốt |
| Đề xuất | A; chuyển B khi PO muốn giảm số lần chốt |
| PO chốt | Chờ |

### W01-09 — Tổ chức bộ phận

| Mục | Nội dung |
|---|---|
| Bối cảnh | Orchestrator chỉ điều phối; việc chuyên môn giao cho bộ phận (`../../ORGANIZATION.md` §2, §5). Bộ phận lập ngay ở W01 để W01 và các wave sau có người nhận việc |
| Cách trình | Sau W01-01 và W01-02: bảng 3–5 bộ phận chọn từ danh mục gợi ý (`../../ORGANIZATION.md` §2.1) hoặc đặt riêng, mỗi dòng: mã, lĩnh vực, vùng sở hữu (thư mục), vì sao cần với sản phẩm này |
| Đề xuất | (Orchestrator điền theo sản phẩm và stack đã chốt) |
| Phản biện đề xuất | Quá nhiều bộ phận thì tốn lượt điều phối; quá ít thì một bộ phận phụ trách quá nhiều lĩnh vực, ý kiến chuyên môn mỏng |
| Đầu ra khi chốt | `QT-nnn` lập bộ phận; tool `create_department` cho từng bộ phận |
| PO chốt | Chờ |

## 3. Nhật ký trao đổi

| Ngày | Ai / vòng | Nội dung |
|---|---|---|
