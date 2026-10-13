# CLAUDE.md — {{TEN_DU_AN}}

Hướng dẫn cho agent làm việc trong repo này. Đọc hết trước khi sửa bất cứ thứ gì.
Khung làm việc dựng từ shipfast {{PHIEN_BAN}} (quyết định `QT-001`). Nâng khung bằng tool `upgrade` của MCP shipfast, không chép tay từ nguồn khác.

## Dự án là gì

{{MO_TA}}

## Đọc gì trước khi làm

| Bước | Đọc | Để làm gì |
|---|---|---|
| 1 | `docs/05_decisions/README.md` | Mục lục quyết định. Quyết định đang hiệu lực thắng mọi tài liệu khác khi mâu thuẫn |
| 2 | `docs/GLOSSARY.md` | Từ vựng chuẩn: dùng đúng tên trong tài liệu, code, giao diện |
| 3 | `docs/04_waves/WAVES.md` | Đợt nào đang chạy, tới bước nào |
| 4 | Hồ sơ đợt đang làm `docs/04_waves/Wxx/` | Phạm vi đã chốt, nhật ký thi công |
| 5 | `docs/01_design/` | Tài liệu thiết kế liên quan việc đang làm |
| 6 | `docs/02_build/CONTRACTS.md` | Thành phần, lệnh chuẩn, hợp đồng giữa các phần |
| 7 | `docs/technical/README.md` | Quy chuẩn kỹ thuật bắt buộc khi viết và review code |
| 8 | `docs/00_analysis/` | Chỉ khi port hoặc tham khảo từ hệ cũ, dự án nguồn |

Chưa có tài liệu hoặc quyết định cho việc cần làm thì hỏi PO, không tự đặt luật.

## Vai trò

| Vai trò | Ai | Việc |
|---|---|---|
| PO | Người dùng | Quyết định thiết kế, chốt phạm vi đợt, duyệt, nghiệm thu |
| Điều hành | Phiên AI chính | Đầu mối duy nhất với PO; đề xuất và phản biện; giữ bảng đợt, backlog, sổ quyết định; điều phối agent; tích hợp; commit |
| Agent | Agent con | Thi công, khảo sát, QA theo phạm vi được giao; **không tự commit**, không đụng trạng thái git chung |

Sơ đồ tổ chức, bộ phận, team thi công, chế độ uỷ quyền: `docs/ORGANIZATION.md`.

## Làm việc theo đợt

Quy trình đầy đủ: `docs/04_waves/README.md`. Tóm tắt:

- Mỗi đợt: 📥 gom việc → 🗣️ thảo luận tới khi mọi vấn đề được chốt → ✅ PO nói **"chốt"** → 🔨 thi công liên tục → 🧹 dọn dẹp → 🧪 nghiệm thu → 🚀 phát hành, rút kinh nghiệm, đóng.
- Ba chế độ chốt: PO chốt từng vấn đề (mặc định); chốt thẳng cho đợt nhỏ đã rõ yêu cầu; uỷ quyền cho tranh luận giữa các bộ phận (`QT-nnn`).
- Điều hành **đề xuất và phản biện**, không ghi chép thụ động: mỗi vấn đề có phương án, đề xuất, rủi ro; PO chọn khác đề xuất thì nêu hệ quả trước khi ghi chốt.
- **Không viết code của đợt trước khi phạm vi được chốt.** Khảo sát chỉ đọc thì được.
- Hạng mục có giao diện chỉ vào thi công khi PO đã duyệt khung (`docs/04_waves/README.md` §4.1).
- Đang thi công mà gặp việc mới: ghi `BL-nnn`, không tự làm. Muốn đổi phạm vi: mở `CR-Wxx-nn`, chờ duyệt.
- PO giao việc trực tiếp ngoài đợt: ghi dòng `PO-nn` ở `WAVES.md` §2 trước khi làm.
- **Trạng thái nằm trong file**, không nằm trong agent hay cuộc hội thoại. Phiên mới đọc file (hoặc gọi tool `status`) là làm tiếp được.
- Mỗi thông tin chỉ sống ở một chỗ (`docs/04_waves/README.md` §3); nơi khác dẫn mã hoặc đường dẫn.

## Cấu trúc thư mục

```text
docs/README.md        mục lục tài liệu
docs/ORGANIZATION.md  vai trò, bộ phận, team thi công, uỷ quyền, ranh giới an toàn
docs/GLOSSARY.md      từ vựng chuẩn
docs/00_analysis/     phân tích hệ cũ, dự án nguồn (chỉ tham khảo)
docs/01_design/       thiết kế sản phẩm
docs/02_build/        thành phần, lệnh chuẩn, hợp đồng đang chạy
docs/03_release/      phát hành, vận hành, release notes
docs/04_waves/        quy trình đợt, bảng đợt, backlog, hồ sơ Wxx/
docs/05_decisions/    sổ quyết định (mỗi quyết định một file)
docs/technical/       quy chuẩn kỹ thuật theo stack đã chọn
reports/              trang HTML cho PO xem offline (gitignored trừ README)
tmp/                  file tạm, log, ảnh chụp, script thử (gitignored)
.shipfast/            phiên bản và bản gốc của khung, dùng khi nâng cấp (commit, không sửa tay)
```

## Quy tắc bắt buộc

**Bí mật và dữ liệu**
- Không commit secret. Chỉ commit file mẫu với giá trị giả. Thấy giá trị giống secret thật ở bất kỳ đâu thì dừng và báo PO.
- Không đọc, in hay ghi nội dung file env thật.
- Test và fixture dùng dữ liệu giả, không chép dữ liệu cá nhân thật vào repo, prompt hay log.

**Mọi thứ ở trong thư mục dự án**
- File tạm, log, ảnh chụp, script thử để trong `tmp/` của repo. Xoá trong `tmp/` chỉ theo danh sách cho phép (`docs/ORGANIZATION.md` §8.3), không xoá hàng loạt.
- Không đưa nội dung dự án lên dịch vụ ngoài khi PO chưa cho phép.
- Trang HTML cho PO xem đặt ở `reports/<wave>-<topic>/index.html`, tự chứa, chạy offline.

**Git khi nhiều agent cùng làm**
- Agent con không chạy `git stash`, `git checkout`, `git reset`, `git rebase`, `git clean` trên bản làm việc chung; không cài thêm phụ thuộc khi các agent đang thi công song song.
- Mỗi agent chỉ sửa vùng thư mục được giao (`docs/ORGANIZATION.md` §4.1).

**Quyết định**
- Quyết định mới ghi vào `docs/05_decisions/` theo `_template.md`, cập nhật mục lục. Code và tài liệu chỉ trỏ mã (`SP-nnn`, `KT-nnn`, `QT-nnn`), không chép lại nội dung.
- Quyết định Điều hành tự đặt tạm để chạy tiếp ghi trạng thái **Giả định**, trình PO duyệt khi nghiệm thu.
- Quyết định bị thay: đổi trạng thái thành "Bị thay thế bởi <mã>" ngay trong file cũ, không xoá.

## Code

Thành phần, lệnh chuẩn và cổng dev: `docs/02_build/CONTRACTS.md` §1, §2, §4.

**Definition of done** (cổng mặc định của bước nghiệm thu)
- Lint, typecheck (nếu stack có), test xanh cho mọi phần bị sửa; cổng đã **chạy thật** ít nhất một lần.
- Có test cho hành vi mới và ít nhất một case lỗi. Thay đổi chạm phân quyền có case người dùng không đủ quyền.
- Đổi hợp đồng (API, sự kiện, schema dùng chung) thì cập nhật `docs/02_build/CONTRACTS.md` và báo phần dùng nó.

**Vùng cần PO duyệt trước**
- Tạo hoặc chạy migration; ghi, xoá dữ liệu trên DB dùng chung; không kết nối DB production.
- Thêm dependency mới; dependency có phí hoặc đổi license.
- Sửa cấu hình build, deploy, CI khi phạm vi đợt không ghi.

## Phát hành

Quy trình phát hành và hotfix: `docs/03_release/README.md`. Chỉ một agent thao tác môi trường thật mỗi lúc; backup trước khi cập nhật.

## Git

- Nhánh chính `{{NHANH_CHINH}}`. Không push, không tạo PR khi PO chưa yêu cầu.
- Điều hành commit checkpoint cuối bước thi công và bước phát hành; quét secret trước khi commit.

## Ngôn ngữ

- Tài liệu (`docs/`, hồ sơ đợt, mô tả PR): tiếng Việt có dấu, ưu tiên bảng.
- Tên biến, hàm, file, bảng DB, API: tiếng Anh. Comment trong code và commit message: {{NGON_NGU_CODE}}.
- Dùng đúng từ vựng trong `docs/GLOSSARY.md`. Câu hỏi gửi PO gọi đối tượng bằng tên, mã chỉ kèm sau trong ngoặc.

## Khi không chắc

Thiết kế chưa chốt, tài liệu mâu thuẫn, hoặc việc chạm hạ tầng và dữ liệu thật thì dừng và hỏi PO.
