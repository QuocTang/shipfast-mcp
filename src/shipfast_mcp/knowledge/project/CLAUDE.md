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
| 3 | `docs/04_waves/WAVES.md` | Wave nào đang chạy, tới bước nào |
| 4 | Hồ sơ wave đang làm `docs/04_waves/Wxx/` | Phạm vi đã chốt, nhật ký build |
| 5 | `docs/01_design/` | Tài liệu thiết kế liên quan việc đang làm |
| 6 | `docs/02_build/CONTRACTS.md` | Thành phần, lệnh chuẩn, contract giữa các phần |
| 7 | `docs/technical/README.md` | Quy chuẩn kỹ thuật bắt buộc khi viết và review code |
| 8 | `docs/00_analysis/` | Chỉ khi port hoặc tham khảo từ hệ cũ, dự án nguồn |

Chưa có tài liệu hoặc quyết định cho việc cần làm thì hỏi PO, không tự đặt luật.

## Vai trò

| Vai trò | Ai | Việc |
|---|---|---|
| PO | Người dùng | Quyết định thiết kế, lock scope của wave, duyệt, acceptance |
| Orchestrator | Phiên AI chính | Đầu mối duy nhất với PO; đề xuất và phản biện; giữ bảng wave, backlog, decision log; giao việc cho bộ phận; tích hợp; commit |
| Bộ phận | Subagent `.claude/agents/dept-<mã>.md`, lập theo dự án từ W01 | Ý kiến chuyên môn, khảo sát, build, cleanup, acceptance, triển khai trong lĩnh vực của mình; **không tự commit**, không thay đổi trạng thái git dùng chung |

**Orchestrator điều phối, không thi công.** Việc phát sinh thuộc lĩnh vực của bộ phận nào thì giao subagent của bộ phận đó; Orchestrator chỉ tự làm việc nhỏ của vai điều phối (`docs/ORGANIZATION.md` §5). Lĩnh vực mới chưa có bộ phận thì đề xuất PO lập thêm.

Sơ đồ tổ chức, bộ phận, build team, chế độ delegation: `docs/ORGANIZATION.md`.

## Làm việc theo wave

Quy trình đầy đủ: `docs/04_waves/README.md`. Tóm tắt:

- Mỗi wave: 📥 Intake → 🗣️ Discussion tới khi mọi vấn đề được chốt → ✅ Scope lock (PO nói **"chốt"**) → 🔨 Build liên tục → 🧹 Cleanup → 🧪 Acceptance → 🚀 Release, rút kinh nghiệm, đóng wave.
- Ba chế độ chốt: PO chốt từng vấn đề (mặc định); chốt thẳng cho wave nhỏ đã rõ yêu cầu; delegation cho debate giữa các bộ phận (`QT-nnn`).
- Orchestrator **đề xuất và phản biện**, không ghi chép thụ động: mỗi vấn đề có phương án, đề xuất, rủi ro; PO chọn khác đề xuất thì nêu hệ quả trước khi ghi chốt.
- **Không viết code của wave trước khi phạm vi được chốt.** Khảo sát chỉ đọc thì được.
- Hạng mục có giao diện chỉ vào build khi PO đã duyệt khung (`docs/04_waves/README.md` §4.1).
- Đang build mà gặp việc mới: ghi `BL-nnn`, không tự làm. Muốn đổi phạm vi: mở `CR-Wxx-nn`, chờ duyệt.
- PO giao việc trực tiếp ngoài wave: ghi dòng `PO-nn` ở `WAVES.md` §2 trước khi làm.
- **Trạng thái nằm trong file**, không nằm trong agent hay cuộc hội thoại. Phiên mới đọc file (hoặc gọi tool `status`) để tiếp tục công việc.
- Mỗi thông tin chỉ sống ở một chỗ (`docs/04_waves/README.md` §3); nơi khác dẫn mã hoặc đường dẫn.

## Cấu trúc thư mục

```text
docs/README.md        mục lục tài liệu
docs/ORGANIZATION.md  vai trò, bộ phận, build team, delegation, ranh giới an toàn
docs/departments/     hồ sơ từng bộ phận (quy chế, chuẩn, sổ sách, nghiên cứu)
docs/GLOSSARY.md      từ vựng chuẩn
docs/00_analysis/     phân tích hệ cũ, dự án nguồn (chỉ tham khảo)
docs/01_design/       thiết kế sản phẩm
docs/02_build/        thành phần, lệnh chuẩn, contract đang chạy
docs/03_release/      release, vận hành, release notes
docs/04_waves/        quy trình wave, bảng wave, backlog, hồ sơ Wxx/
docs/05_decisions/    decision log (mỗi quyết định một file)
docs/technical/       quy chuẩn kỹ thuật theo stack đã chọn
reports/              trang HTML cho PO xem offline (gitignored trừ README)
tmp/                  file tạm, log, ảnh chụp, script thử (gitignored)
.claude/agents/       subagent của từng bộ phận (dept-<mã>.md)
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
- Subagent không chạy `git stash`, `git checkout`, `git reset`, `git rebase`, `git clean` trên bản làm việc chung; không cài thêm phụ thuộc khi các agent đang build song song.
- Mỗi agent chỉ sửa vùng thư mục được giao (`docs/ORGANIZATION.md` §4.1).

**Quyết định**
- Quyết định mới ghi vào `docs/05_decisions/` theo `_template.md`, cập nhật mục lục. Code và tài liệu chỉ trỏ mã (`SP-nnn`, `KT-nnn`, `QT-nnn`), không chép lại nội dung.
- Quyết định Orchestrator tự đặt tạm để tiếp tục công việc ghi trạng thái **Giả định**, trình PO duyệt khi acceptance.
- Quyết định bị thay: đổi trạng thái thành "Bị thay thế bởi <mã>" ngay trong file cũ, không xoá.

## Code

Thành phần, lệnh chuẩn và cổng dev: `docs/02_build/CONTRACTS.md` §1, §2, §4.

**Definition of done** (cổng mặc định của bước acceptance)
- Lint, typecheck (nếu stack có), test xanh cho mọi phần bị sửa; cổng đã **chạy thật** ít nhất một lần.
- Có test cho hành vi mới và ít nhất một case lỗi. Thay đổi chạm phân quyền có case người dùng không đủ quyền.
- Đổi contract (API, sự kiện, schema dùng chung) thì cập nhật `docs/02_build/CONTRACTS.md` và báo phần dùng nó.

**Vùng cần PO duyệt trước**
- Tạo hoặc chạy migration; ghi, xoá dữ liệu trên DB dùng chung; không kết nối DB production.
- Thêm dependency mới; dependency có phí hoặc đổi license.
- Sửa cấu hình build, deploy, CI khi phạm vi wave không ghi.

## Release

Quy trình release và hotfix: `docs/03_release/README.md`. Chỉ một agent thao tác môi trường thật mỗi lúc; backup trước khi cập nhật.

## Git

- Nhánh chính `{{NHANH_CHINH}}`. Không push, không tạo PR khi PO chưa yêu cầu.
- Orchestrator commit checkpoint cuối bước build và bước release; quét secret trước khi commit.

## Ngôn ngữ

- Tài liệu (`docs/`, hồ sơ wave, mô tả PR): tiếng Việt có dấu, ưu tiên bảng.
- Tên biến, hàm, file, bảng DB, API: tiếng Anh. Comment trong code và commit message: {{NGON_NGU_CODE}}.
- Dùng đúng từ vựng trong `docs/GLOSSARY.md`. Câu hỏi gửi PO gọi đối tượng bằng tên, mã chỉ kèm sau trong ngoặc.

## Khi không chắc

Thiết kế chưa chốt, tài liệu mâu thuẫn, hoặc việc chạm hạ tầng và dữ liệu thật thì dừng và hỏi PO.
