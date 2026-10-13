---
name: shipfast-debate
description: Tổ chức debate nhiều vai trong quy trình shipfast - AI đóng các vai phản biện (người dùng, sản phẩm, kiến trúc, an toàn, vận hành, QA, phản biện tự do) hoặc các bộ phận đã lập, viết lập trường độc lập R1, phản biện chéo R2, rồi tổng hợp cho PO hoặc Chủ toạ phán quyết. Dùng khi một vấn đề có nhiều phương án ngang nhau, rủi ro cao, PO muốn "phản biện", "debate", "xem các góc nhìn", hoặc wave chạy chế độ delegation.
---

# shipfast-debate

Cơ chế gốc: `docs/04_waves/README.md` §4.3 và `docs/ORGANIZATION.md` §7.

## Chọn kiểu

| Kiểu | Khi nào | Ai kết luận |
|---|---|---|
| Tham vấn | Mặc định; PO vẫn chốt | PO, sau khi đọc bảng tổng hợp |
| Delegation | Có `QT` delegation và ít nhất hai bộ phận | Chủ toạ (Orchestrator) theo tiêu chí `ORGANIZATION.md` §7.2 |

## Chọn vai

Lấy 2–4 vai trong `ORGANIZATION.md` §7.4 (hoặc bộ phận đã lập) liên quan tới vấn đề. Luôn có ít nhất một vai có lợi ích ngược nhau (ví dụ PROD với ARCH, USER với TRUST). Vấn đề chạm dữ liệu, bí mật, quyền thì bắt buộc có TRUST.

## Chạy

1. **R1, độc lập.** Mỗi vai một subagent (chạy song song) hoặc bạn đóng lần lượt mà không đọc lại R1 của vai khác. Mỗi vai nhận: danh sách vấn đề `Wxx-nn` kèm bối cảnh, mô tả vai (§7.4), mẫu `_template/debate-r1.md`. Yêu cầu: lập trường có căn cứ (tài liệu chính thức, kiểm trên máy, `research/`), điều chưa kiểm ghi là giả định, nêu điều kiện để đổi ý. Lưu `Wxx/debate/r1-<MÃ>.md`.
2. **R2, phản biện.** Mỗi vai đọc **mọi** R1, viết theo `_template/debate-r2.md`: đồng ý, phản đối có lý do, nhượng bộ, lập trường cuối, điều không chấp nhận được. Lưu `r2-<MÃ>.md`.
3. **R3, kết luận.**
   - Tham vấn: bảng cho PO, mỗi vấn đề: các lập trường cuối, điểm đồng thuận, điểm vênh, đề xuất của Orchestrator, ý kiến thiểu số. Gọi đối tượng bằng tên.
   - Delegation: phán quyết theo §7.2, ghi cột PO chốt `Delegation: …`, ý kiến thiểu số; báo PO.
4. **R4–R5** (chỉ delegation): bộ phận kháng nghị ngắn; Chủ toạ giữ hoặc sửa, ghi nhật ký.

## Luật

- Không vai nào được bỏ một yêu cầu PO đã nêu; việc lớn thì đề xuất chia wave.
- Kết luận mỗi vấn đề là Làm (phương án …), Không làm (lý do), hoặc Hoãn → `BL-nnn`.
- TRUST phủ quyết được phương án rủi ro nghiêm trọng; chỉ gỡ khi có biện pháp giảm thiểu ghi rõ.
- Giữ file `debate/` sau khi đóng wave. Chỉ điền bảng thật sự dùng; bảng tổng hợp phải đủ.
