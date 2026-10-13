# Ý nghĩa và mục đích

## Vấn đề shipfast giải quyết

| Khi làm việc với AI không có quy trình | shipfast làm gì |
|---|---|
| AI viết code ngay khi chưa hiểu đúng yêu cầu | Không code trước khi PO chốt phạm vi |
| AI chiều theo mọi yêu cầu, không ai chỉ ra rủi ro | Điều hành bắt buộc phản biện cả đề xuất của mình; vai phản biện cho nhiều góc nhìn |
| Quyết định nằm rải rác trong chat, comment, tin nhắn | Sổ quyết định một chỗ, code chỉ trỏ mã |
| Phiên mới quên hết bối cảnh | Trạng thái nằm trong file; `status` cho biết đang tới đâu |
| Phạm vi phình dần trong lúc làm | Việc mới vào backlog, đổi phạm vi qua CR |
| "Xong" nhưng chưa chạy thật | Cổng kiểm chứng phải chạy thật; QA độc lập nghiệm thu |
| Rác tích tụ sau mỗi đợt | Bước dọn dẹp có ranh giới an toàn |
| Mỗi dự án chép mẫu rồi lệch dần, cập nhật phải so tay với repo gốc | Khung phân phối qua MCP, nâng cấp gộp ba phía tự động |

## Nguyên lý

1. **Người quyết, AI đề xuất và phản biện.** AI được sáng tạo trong phương án, không được tự quyết điều thuộc về PO.
2. **Trạng thái nằm trong file.** Không phụ thuộc trí nhớ của phiên hay của agent.
3. **Mỗi thông tin một chỗ.** Chép lại là bắt đầu lệch.
4. **Cổng phải chạy thật.** Tiêu chí đo được, bằng chứng ghi lại.
5. **Lập tổ chức khi có việc.** Bộ phận, team, uỷ quyền chỉ dùng khi dự án thật sự cần.
6. **Không giới hạn stack.** Quy trình không gắn công nghệ; stack là một quyết định của từng dự án.

## Nguồn gốc

Quy trình rút từ các dự án thật làm việc với AI theo đợt. Những cách làm tốt (chốt thẳng cho đợt nhỏ, tách team khỏi bộ phận, rút kinh nghiệm bắt buộc, cấm agent đụng trạng thái git chung) được đưa vào khung chung sau khi đã chạy thật.
