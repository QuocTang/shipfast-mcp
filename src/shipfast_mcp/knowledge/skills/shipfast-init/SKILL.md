---
name: shipfast-init
description: Khởi tạo dự án mới theo quy trình shipfast từ một repo trống hoặc gần trống - chạy wave W01 (trao đổi, đề xuất và phản biện stack, chốt), scaffold tài liệu, dựng bộ khung code theo stack đã chốt, chạy được và acceptance. Dùng khi người dùng nói "khởi tạo dự án", "setup dự án mới", "bắt đầu dự án", gọi prompt init của MCP shipfast, hoặc repo chưa có .shipfast/ và chưa có code.
---

# shipfast-init

Đưa repo mới tới trạng thái: có khung quy trình, stack đã chốt, khung code chạy được ở local, quality gate xanh, sẵn sàng làm tính năng đầu tiên. Việc này là một wave thật: **W01 — Khởi tạo dự án**. Bạn là Orchestrator, người dùng là PO.

Không giới hạn stack. Bạn được sáng tạo trong đề xuất, nhưng mọi đề xuất phải kèm phản biện và PO chốt.

## Pha 1 — Scaffold quy trình và mở W01

1. Xác định gốc repo (`git rev-parse --show-toplevel` hoặc thư mục PO chỉ). Xem repo đang có gì; không đọc file env. Đã có code đáng kể thì chuyển sang skill `shipfast-adopt`.
2. Gọi tool `scaffold_project` với `mode="init"`, `dry_run=true`; slug tạm theo tên thư mục. Trình PO danh sách file sẽ tạo, file bỏ qua vì đã có.
3. PO đồng ý thì gọi lại với `dry_run=false`. Không có MCP: báo PO cài MCP shipfast (`read_guide start`), không chép tay khung.

## Pha 2 — Discussion W01

Theo `docs/04_waves/W01/1-discussion.md`:

1. **W01-01 trước**: nghe PO mô tả, tóm lại, hỏi làm rõ, đề xuất cắt bớt. Ghi mô tả vào `CLAUDE.md` mục "Dự án là gì", tính năng bản đầu vào `BACKLOG.md` (`BL-nnn`).
2. **W01-02 stack**: tra tài liệu chính thức hiện hành, ghi `W01/research/01-stack.md` kèm nguồn. Trình 2–3 phương án; vấn đề khó thì chạy debate tham vấn (skill `shipfast-debate`) với các vai ARCH, OPS, TRUST, USER, rồi trình bảng tổng hợp.
3. **W01-09 tổ chức**: đề xuất 3–5 bộ phận theo sản phẩm và stack (`docs/ORGANIZATION.md` §2.1), mỗi bộ phận có mã, lĩnh vực, vùng sở hữu, lý do. Chốt xong thì lập ngay bằng tool `create_department` để các bộ phận nhận việc từ phần còn lại của W01.
4. W01-03 … W01-08: hỏi gộp (AskUserQuestion khi có), mỗi câu có đề xuất đứng đầu; lấy ý kiến bộ phận liên quan khi đã lập.
5. Mỗi lượt: ghi nhật ký §3, điền cột **PO chốt**. PO chọn khác đề xuất thì nêu hệ quả trước khi ghi. Vấn đề mới thêm `W01-09…`.

Cổng: không còn vấn đề "Chờ".

## Pha 3 — Scope lock

1. Viết `W01/2-scope.md` theo `_template/2-scope.md`: hạng mục (khung code từng thành phần, cấu hình môi trường, lệnh chuẩn, chạy local), tiêu chí đo được (ví dụ: lint/test/build xanh, endpoint health trả 200, trang chủ mở được), ngoài phạm vi.
2. Ghi quyết định bằng tool `new_decision` (trạng thái Hiệu lực sau khi PO chốt): `SP-001` sản phẩm và phạm vi bản đầu; `KT-001` stack và thành phần; `KT-002` dữ liệu và dịch vụ dev; `QT-002` lập các bộ phận; thêm nếu có. Mỗi hạng mục trong `2-scope.md` ghi bộ phận phụ trách.
3. Điền `docs/02_build/CONTRACTS.md` §1 thành phần, §2 lệnh chuẩn, §4 cổng.
4. Trình bảng tóm tắt; chờ PO nói **"chốt"**. Ghi ngày vào `W01/README.md` và `WAVES.md`.

## Pha 4 — Build khung code

Giao từng hạng mục cho subagent của bộ phận phụ trách; Orchestrator theo dõi, tổng hợp, ghi `W01/3-build.md`.

1. Bộ phận nền tảng dựng khung code bằng công cụ chính thức của stack (CLI tạo dự án, template chính thức) thay vì tự viết từ đầu; ghi lệnh đã chạy.
2. Thêm tối thiểu: một endpoint hoặc màn kiểm sống, một test mẫu chạy được, cấu hình lint, file mẫu môi trường giá trị giả, quét secret.
3. Bộ phận phụ trách thêm quy chuẩn kỹ thuật ban đầu vào `docs/technical/` (ngắn, chỉ luật có lý do); mỗi bộ phận viết điều lệ `01_quy-che/01-dieu-le.md` của mình.
4. Chạy thật mọi lệnh ở `CONTRACTS.md` §2. Tạo DB, migration, dependency có phí: chờ PO duyệt.

## Pha 5 — Cleanup, acceptance, đóng

1. `W01/4-cleanup.md`: file trong `tmp/`, chỗ "(chưa điền)" còn lại cần PO điền.
2. `W01/5-acceptance.md`: subagent khác bộ phận đã build kiểm từng tiêu chí kèm lệnh và kết quả; quyết định giả định chờ PO; rút kinh nghiệm.
3. Gọi tool `check`, sửa tới khi sạch. Đóng W01 trong README wave và `WAVES.md`.
4. Đề xuất W02 từ backlog (tool `open_wave`). Không commit, không push khi PO chưa yêu cầu; khi commit thì commit cả `.shipfast/`.
