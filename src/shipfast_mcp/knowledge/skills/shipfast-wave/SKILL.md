---
name: shipfast-wave
description: Chạy một wave shipfast từ intake tới đóng - mở wave, thảo luận và chốt với PO, viết phạm vi, giao việc cho các bộ phận, cleanup, acceptance, release, rút kinh nghiệm. Dùng khi người dùng muốn làm tính năng hoặc nhóm việc mới, nói "mở wave", "W0x", "chốt", "acceptance", "đóng wave", hoặc khi wave đang mở cần đi tiếp bước sau.
---

# shipfast-wave

Quy trình gốc: `docs/04_waves/README.md` của dự án. Skill này là cách chạy từng bước.

## 0. Intake

1. Gọi `status`. Intake từ yêu cầu PO, `BACKLOG.md`, phản hồi.
2. Chọn chế độ chốt: **PO chốt** (mặc định); **chốt thẳng** khi wave nhỏ và yêu cầu đã rõ (ghi lý do); **delegation** chỉ khi đã có `QT` delegation.
3. Tool `open_wave` (tiêu đề, mục tiêu một câu, chế độ). Viết bản đầu `1-discussion.md`: mỗi vấn đề `Wxx-nn` có bối cảnh, phương án, đề xuất, phản biện đề xuất, ước lượng.
4. Mỗi vấn đề ghi bộ phận liên quan. Cần dữ kiện thì giao bộ phận đó khảo sát chỉ đọc, ghi `research/nn-<chủ đề>.md` kèm ngày và nguồn. Lĩnh vực chưa có bộ phận thì thêm một vấn đề đề xuất lập bộ phận.

## 1. Discussion

- Hỏi gộp, mỗi câu có đề xuất đứng đầu, gọi đối tượng bằng tên.
- PO chọn khác đề xuất: nêu rủi ro, hệ quả; chỉ ghi khi PO xác nhận.
- Lấy ý kiến bộ phận liên quan trước khi trình; vấn đề có nhiều góc nhìn thì debate tham vấn (skill `shipfast-debate`).
- Ghi nhật ký §3 mỗi lượt. Cổng: không còn "Chờ".

## 2. Scope lock

1. Chép `_template/2-scope.md`. Hạng mục `Wxx-Pnn` có bộ phận phụ trách, vùng thư mục, tiêu chí đo được. Quality gate lấy từ `CONTRACTS.md` §2.
2. Chia team khi chạy song song: ghi bảng `docs/ORGANIZATION.md` §4.1 (được sửa / không được sửa).
3. Quyết định mới: tool `new_decision`. Contract mới: `CONTRACTS.md` §3.
4. Trình tóm tắt, chờ **"chốt"**. Ghi ngày vào README wave và `WAVES.md`, chuyển 🔨.

Sau khi chốt và ghi hồ sơ, đề nghị PO mở phiên mới cho bước Build.

## 3. Build

1. Chép `_template/3-build.md`. Giao từng hạng mục cho subagent `dept-<mã>` của bộ phận phụ trách; Orchestrator không tự build hạng mục. Giao các hạng mục độc lập trong cùng một lượt, chờ cả lô xong rồi tổng hợp. Hạng mục lớn hơn khoảng 60 lượt gọi tool thì chia nhỏ. Lời giao việc theo mẫu:

   ```text
   Việc: Wxx-Pnn <tên hạng mục>
   Tiêu chí: <tiêu chí đo được, chép từ 2-scope.md>
   Vùng được sửa: <thư mục, file>
   Đọc trước: <file:đoạn cần đọc>; không khảo sát ngoài danh sách này trừ khi thiếu thông tin
   Kiểm: <lệnh quality gate của hạng mục>
   Báo cáo: tối đa 30 dòng gồm việc đã làm, file đã sửa, lệnh kiểm và kết quả, giả định, việc phát sinh
   ```

   Không chép luật chung (đọc theo đoạn, báo cáo ngắn…) vào lời giao việc: subagent bộ phận đã có luật đó trong `.claude/agents/dept-<mã>.md`. Lời giao chỉ ghi phần riêng của việc.

   Model và mức suy nghĩ lấy theo mặc định của bộ phận. Việc cần khác mặc định thì truyền `model`, `effort` khi gọi subagent theo bảng "Model và mức suy nghĩ theo việc" ở `docs/ORGANIZATION.md` §5.1, không ghi vào lời giao việc.

   Mỗi lần giao gồm: mã hạng mục, tiêu chí, vùng được sửa, luật "không commit, không stash/checkout/reset, không cài phụ thuộc khi chạy song song".
2. Kiểm subagent định kỳ; cập nhật §1 trạng thái, §3 lượt chạy.
3. Việc mới → `BL-nnn`. Đổi phạm vi → `CR-Wxx-nn` chờ duyệt. Quyết định nhỏ → `Q-Wxx-nn`.
4. Cổng: chạy thật toàn bộ quality gate, xanh. Orchestrator commit checkpoint khi PO cho phép.

Sau khi Build xong và hồ sơ đã cập nhật, đề nghị PO mở phiên mới cho bước Cleanup và Acceptance.

## 4. Cleanup

Chép `_template/4-cleanup.md`. Bộ phận cleanup (hoặc subagent được giao) quét chỉ đọc theo danh sách kiểm; chủ vùng xoá; `tmp/` chỉ xoá theo danh sách cho phép (`ORGANIZATION.md` §8). Gọi `check` (mục 13). Quality gate chạy lại.

## 5. Acceptance

Chép `_template/5-acceptance.md`. Gọi bộ phận QA, hoặc một subagent **khác** bộ phận đã build: chạy lại cổng, kịch bản đầu cuối, so từng tiêu chí, ghi bằng chứng. Lỗi `QAxx-n` sửa rồi kiểm lại. Trình PO các quyết định "Giả định".

## 6. Release và đóng

1. Release theo `docs/03_release/README.md` khi wave có release; ghi `RELEASE-NOTES.md`.
2. **Rút kinh nghiệm** `5-acceptance.md` §6: tốt, chưa tốt, đổi cách làm. Đổi cách làm PO đồng ý → `QT-nnn` hoặc sửa quy chuẩn.
3. Việc dở → backlog. Cập nhật README wave (Closed, ngày, phiên bản, commit), `WAVES.md`, `BACKLOG.md` §2.
4. Gọi `check` tới khi không còn lỗi của wave này. Đề xuất wave kế.
