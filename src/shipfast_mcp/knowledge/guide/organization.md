# Tổ chức ra sao

## Vai trò

| Vai | Ai | Làm gì | Không làm gì |
|---|---|---|---|
| PO | Người (bạn) | Quyết định, lock scope, duyệt, acceptance | Không phải viết tài liệu quy trình |
| Orchestrator | Phiên AI chính | Điều phối: đề xuất, phản biện, giữ hồ sơ, giao việc cho bộ phận, tích hợp, commit khi được phép | Không tự thi công việc tốn công; không tự quyết thay PO ngoài phạm vi delegation |
| Bộ phận | Subagent `dept-<mã>` theo lĩnh vực, lập theo dự án từ W01, thêm khi cần | Nhận mọi việc thuộc lĩnh vực của mình: ý kiến chuyên môn, khảo sát, build, cleanup, kiểm thử; giữ chuẩn và sổ sách | Không commit, không thay đổi trạng thái git dùng chung, không sửa vùng của bộ phận khác |
| Build team | Nhóm agent theo vùng code trong một wave | Build song song không chồng vùng | Giải tán khi wave đóng |
| Vai phản biện | Góc nhìn AI đóng khi debate | Người dùng, sản phẩm, kiến trúc, an toàn, vận hành, QA, phản biện tự do | Chỉ tham vấn, không quyết |

## Wave

Mọi việc có code đi qua một wave 7 bước: 📥 Intake → 🗣️ Discussion → ✅ Scope lock → 🔨 Build → 🧹 Cleanup → 🧪 Acceptance → 🚀 Release và đóng wave. Trừ hai ngoại lệ: hotfix (lỗi chặn người dùng) và việc PO giao trực tiếp (`PO-nn`, ghi lại trước khi làm).

Ba chế độ chốt: PO chốt từng vấn đề (mặc định), chốt thẳng cho wave nhỏ đã rõ, delegation cho debate giữa các bộ phận.

## Thư mục

```text
CLAUDE.md             luật cho AI
docs/
  ORGANIZATION.md     vai trò, bộ phận, team, delegation, ranh giới an toàn
  GLOSSARY.md         từ vựng chuẩn
  00_analysis/        phân tích hệ cũ, dự án nguồn
  01_design/          thiết kế sản phẩm
  02_build/           thành phần, lệnh chuẩn, contract (CONTRACTS.md)
  03_release/         release, vận hành
  04_waves/           quy trình wave, bảng wave, backlog, hồ sơ Wxx/
  05_decisions/       decision log SP/KT/QT
  technical/          quy chuẩn kỹ thuật của stack
.claude/skills/       skill shipfast-* (quản lý bởi shipfast, nâng cấp được)
.shipfast/            phiên bản và bản gốc của khung (commit, không sửa tay)
reports/              trang HTML cho PO xem offline
tmp/                  file tạm (gitignored)
```

## Hệ mã

| Mã | Là gì |
|---|---|
| `BL-012` | Việc trong backlog |
| `W03` | Wave thứ 3 |
| `W03-04` | Vấn đề thứ 4 cần chốt trong wave 3 |
| `W03-P02` | Hạng mục build thứ 2 của wave 3 |
| `CR-W03-01` | Yêu cầu đổi phạm vi khi đang build |
| `SP-002` / `KT-005` / `QT-003` | Quyết định sản phẩm / kỹ thuật / quy trình |
| `PO-04`, `OPS-02`, `HOTFIX-01` | Việc ngoài wave |

Mỗi thông tin chỉ sống ở một chỗ; nơi khác trỏ mã.
