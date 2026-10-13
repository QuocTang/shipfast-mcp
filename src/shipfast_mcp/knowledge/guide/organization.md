# Tổ chức ra sao

## Vai trò

| Vai | Ai | Làm gì | Không làm gì |
|---|---|---|---|
| PO | Người (bạn) | Quyết định, chốt phạm vi, duyệt, nghiệm thu | Không phải viết tài liệu quy trình |
| Điều hành | Phiên AI chính | Đề xuất, phản biện, giữ hồ sơ, điều phối agent, tích hợp, commit khi được phép | Không tự quyết thay PO ngoài phạm vi uỷ quyền |
| Agent con | AI do Điều hành giao việc | Thi công, khảo sát, dọn dẹp, QA trong vùng được giao | Không commit, không đụng trạng thái git chung |
| Bộ phận | Nhóm agent theo lĩnh vực, lập khi có việc | Giữ chuẩn và sổ sách của lĩnh vực, tranh luận khi uỷ quyền | Không lập trước khi có đợt do nó chủ trì |
| Team thi công | Nhóm agent theo vùng code trong một đợt | Thi công song song không chồng vùng | Giải tán khi đợt đóng |
| Vai phản biện | Góc nhìn AI đóng khi tranh luận | Người dùng, sản phẩm, kiến trúc, an toàn, vận hành, QA, phản biện tự do | Chỉ tham vấn, không quyết |

## Đợt (wave)

Mọi việc có code đi qua một đợt 7 bước: 📥 gom việc → 🗣️ thảo luận → ✅ chốt → 🔨 thi công → 🧹 dọn dẹp → 🧪 nghiệm thu → 🚀 phát hành và đóng. Trừ hai ngoại lệ: hotfix (lỗi chặn người dùng) và việc PO giao trực tiếp (`PO-nn`, ghi lại trước khi làm).

Ba chế độ chốt: PO chốt từng vấn đề (mặc định), chốt thẳng cho đợt nhỏ đã rõ, uỷ quyền cho tranh luận giữa các bộ phận.

## Thư mục

```text
CLAUDE.md             luật cho AI
docs/
  ORGANIZATION.md     vai trò, bộ phận, team, uỷ quyền, ranh giới an toàn
  GLOSSARY.md         từ vựng chuẩn
  00_analysis/        phân tích hệ cũ, dự án nguồn
  01_design/          thiết kế sản phẩm
  02_build/           thành phần, lệnh chuẩn, hợp đồng (CONTRACTS.md)
  03_release/         phát hành, vận hành
  04_waves/           quy trình đợt, bảng đợt, backlog, hồ sơ Wxx/
  05_decisions/       sổ quyết định SP/KT/QT
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
| `W03` | Đợt thứ 3 |
| `W03-04` | Vấn đề thứ 4 cần chốt trong đợt 3 |
| `W03-P02` | Hạng mục thi công thứ 2 của đợt 3 |
| `CR-W03-01` | Yêu cầu đổi phạm vi khi đang thi công |
| `SP-002` / `KT-005` / `QT-003` | Quyết định sản phẩm / kỹ thuật / quy trình |
| `PO-04`, `OPS-02`, `HOTFIX-01` | Việc ngoài đợt |

Mỗi thông tin chỉ sống ở một chỗ; nơi khác trỏ mã.
