---
name: shipfast-wave
description: Chạy một đợt (wave) shipfast từ gom việc tới đóng - mở đợt, thảo luận và chốt với PO, viết phạm vi, điều phối thi công bằng agent con hoặc team, dọn dẹp, nghiệm thu, phát hành, rút kinh nghiệm. Dùng khi người dùng muốn làm tính năng hoặc nhóm việc mới, nói "mở đợt", "W0x", "chốt", "nghiệm thu", "đóng đợt", hoặc khi đợt đang mở cần đi tiếp bước sau.
---

# shipfast-wave

Quy trình gốc: `docs/04_waves/README.md` của dự án. Skill này là cách chạy từng bước.

## 0. Gom việc

1. Gọi `status`. Gom việc từ yêu cầu PO, `BACKLOG.md`, phản hồi.
2. Chọn chế độ chốt: **PO chốt** (mặc định); **chốt thẳng** khi đợt nhỏ và yêu cầu đã rõ (ghi lý do); **uỷ quyền** chỉ khi đã có `QT` uỷ quyền.
3. Tool `open_wave` (tiêu đề, mục tiêu một câu, chế độ). Viết bản đầu `1-discussion.md`: mỗi vấn đề `Wxx-nn` có bối cảnh, phương án, đề xuất, phản biện đề xuất, ước lượng.
4. Cần dữ kiện thì giao agent con khảo sát chỉ đọc, ghi `research/nn-<chủ đề>.md` kèm ngày và nguồn.

## 1. Thảo luận

- Hỏi gộp, mỗi câu có đề xuất đứng đầu, gọi đối tượng bằng tên.
- PO chọn khác đề xuất: nêu rủi ro, hệ quả; chỉ ghi khi PO xác nhận.
- Vấn đề có nhiều góc nhìn: tranh luận tham vấn (skill `shipfast-debate`).
- Ghi nhật ký §3 mỗi lượt. Cổng: không còn "Chờ".

## 2. Chốt phạm vi

1. Chép `_template/2-scope.md`. Hạng mục `Wxx-Pnn` có phụ trách (agent, team), vùng thư mục, tiêu chí đo được. Cổng kiểm chứng lấy từ `CONTRACTS.md` §2.
2. Chia team khi chạy song song: ghi bảng `docs/ORGANIZATION.md` §4.1 (được sửa / không được sửa).
3. Quyết định mới: tool `new_decision`. Hợp đồng mới: `CONTRACTS.md` §3.
4. Trình tóm tắt, chờ **"chốt"**. Ghi ngày vào README đợt và `WAVES.md`, chuyển 🔨.

## 3. Thi công

1. Chép `_template/3-build.md`. Giao agent con theo hạng mục, mỗi agent nhận: mã hạng mục, tiêu chí, vùng được sửa, luật "không commit, không stash/checkout/reset, không cài phụ thuộc khi chạy song song".
2. Kiểm agent định kỳ; cập nhật §1 trạng thái, §3 lượt chạy.
3. Việc mới → `BL-nnn`. Đổi phạm vi → `CR-Wxx-nn` chờ duyệt. Quyết định nhỏ → `Q-Wxx-nn`.
4. Cổng: chạy thật toàn bộ cổng kiểm chứng, xanh. Điều hành commit checkpoint khi PO cho phép.

## 4. Dọn dẹp

Chép `_template/4-cleanup.md`. Agent dọn quét chỉ đọc theo danh sách kiểm; chủ vùng xoá; `tmp/` chỉ xoá theo danh sách cho phép (`ORGANIZATION.md` §8). Gọi `check` (mục 13). Cổng kiểm chứng chạy lại.

## 5. Nghiệm thu

Chép `_template/5-acceptance.md`. Gọi một agent QA **khác** agent đã thi công: chạy lại cổng, kịch bản đầu cuối, so từng tiêu chí, ghi bằng chứng. Lỗi `QAxx-n` sửa rồi kiểm lại. Trình PO các quyết định "Giả định".

## 6. Phát hành và đóng

1. Phát hành theo `docs/03_release/README.md` khi đợt có phát hành; ghi `RELEASE-NOTES.md`.
2. **Rút kinh nghiệm** `5-acceptance.md` §6: tốt, chưa tốt, đổi cách làm. Đổi cách làm PO đồng ý → `QT-nnn` hoặc sửa quy chuẩn.
3. Việc dở → backlog. Cập nhật README đợt (Đã đóng, ngày, phiên bản, commit), `WAVES.md`, `BACKLOG.md` §2.
4. Gọi `check` tới khi không còn lỗi của đợt này. Đề xuất đợt kế.
