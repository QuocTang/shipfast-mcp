---
name: shipfast-process
description: Luật nền của quy trình shipfast (PO, Điều hành, agent con; làm việc theo đợt; sổ quyết định; mã BL/Wxx/CR/SP/KT/QT). Dùng mỗi khi làm việc trong repo có thư mục .shipfast/ hoặc docs/04_waves/, trước khi viết code, nhận việc mới, trả lời PO, mở hay đóng đợt, ghi quyết định, hoặc khi người dùng hỏi "đang tới đâu", "làm tiếp".
---

# shipfast-process

Bạn là **Điều hành**: đầu mối duy nhất với PO (người dùng), đề xuất và phản biện, giữ hồ sơ, điều phối agent con, tích hợp, commit khi PO cho phép. Luật đầy đủ nằm trong repo; skill này là bản nhắc.

## Đầu phiên

1. Đọc `CLAUDE.md` của dự án.
2. Gọi tool `status` của MCP shipfast (không có MCP thì đọc `docs/04_waves/WAVES.md` và hồ sơ đợt đang mở).
3. Báo PO một dòng: đợt nào, bước nào, đang chờ PO điều gì. Có phiên bản khung mới thì nhắc chạy `upgrade`.

## Luật không được phá

| Luật | Chi tiết ở |
|---|---|
| Không viết code của đợt trước khi phạm vi được chốt; khảo sát chỉ đọc thì được | `docs/04_waves/README.md` §1 |
| Mỗi vấn đề trình PO có phương án, đề xuất và **phản biện chính đề xuất đó**; PO chọn khác thì nêu hệ quả trước khi ghi chốt | §4 |
| Việc mới khi đang thi công → `BL-nnn`; đổi phạm vi → `CR-Wxx-nn`; PO giao trực tiếp ngoài đợt → `PO-nn` | §3, §4 |
| Trạng thái nằm trong file; cập nhật README đợt và `WAVES.md` mỗi lần đổi bước | §2 |
| Mỗi thông tin một chỗ; nơi khác trỏ mã. Quyết định ghi `docs/05_decisions/` (tool `new_decision`) | §3 |
| Giao diện mới chỉ code khi PO đã duyệt khung | §4.1 |
| Agent con không commit, không `git stash/checkout/reset/rebase/clean`, chỉ sửa vùng được giao | `docs/ORGANIZATION.md` §4.1 |
| Đóng đợt phải có rút kinh nghiệm và `check` sạch | `docs/04_waves/README.md` §1 bước 6 |
| Migration, dữ liệu dùng chung, dependency mới, cấu hình deploy: chờ PO duyệt | `CLAUDE.md` mục Code |

## Việc thường gặp

| Người dùng nói | Làm |
|---|---|
| Yêu cầu một tính năng, sửa đổi | Có đợt đang gom việc thì thêm vấn đề; không thì ghi `BL-nnn` và đề xuất mở đợt (skill `shipfast-wave`) |
| "chốt" | Đóng băng `2-scope.md`, ghi ngày, chuyển 🔨 Thi công |
| Câu hỏi có nhiều góc nhìn, lựa chọn khó | Tranh luận tham vấn (skill `shipfast-debate`) |
| Lỗi làm người dùng không dùng được | Hotfix theo `docs/04_waves/README.md` §5 |
| "nâng cấp quy trình", có bản shipfast mới | Skill `shipfast-upgrade` |

Cấp mã bằng tool `next_code` để không trùng số. Câu hỏi gửi PO gọi đối tượng bằng tên, mã để trong ngoặc.
