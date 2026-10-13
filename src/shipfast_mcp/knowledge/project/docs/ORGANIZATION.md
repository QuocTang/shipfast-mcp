# Tổ chức dự án {{TEN_DU_AN}}

> Vai trò, bộ phận, team thi công, vùng sở hữu, cách phối hợp, tranh luận và uỷ quyền, ranh giới an toàn khi dọn dẹp. Quy trình đợt ở `04_waves/README.md`; luật chung cho agent ở `../CLAUDE.md`.

## 1. Sơ đồ

```text
                         PO (người dùng)
       quyết định · chốt phạm vi đợt · duyệt · nghiệm thu
                              │
                Điều hành (phiên AI chính)
   đề xuất · phản biện · bảng đợt · backlog · sổ quyết định · điều phối · tích hợp · commit
                              │
        ┌─────────────────────┼──────────────────────┐
   Bộ phận (lập khi có việc,   Team thi công (lập theo     Vai phản biện (gọi khi
   sở hữu lĩnh vực, §2 §6)     đợt, sở hữu vùng code, §4.1) tranh luận tham vấn, §7.4)
```

## 2. Các bộ phận

| Bộ phận | Mã | Trạng thái | Phụ trách | Hồ sơ |
|---|---|---|---|---|
| Điều hành | — | Hoạt động từ {{NGAY}} | Toàn bộ việc khi chưa có bộ phận đầu mối | `04_waves/`, `05_decisions/` |

**Thành lập khi có việc.** Một bộ phận chỉ được lập khi có đợt đầu tiên do nó chủ trì. Trước đó Điều hành gánh việc của lĩnh vực đó và ghi "Điều hành (thay <mã>)" trong hồ sơ đợt. Dấu hiệu nên lập: một lĩnh vực có dòng việc riêng liên tục qua nhiều đợt, có chuẩn và sổ sách riêng, hoặc cần chạy song song với lĩnh vực khác.

Việc dọn dẹp (bước 🧹) và triển khai (bước 🚀) do Điều hành gánh tới khi lập bộ phận riêng; khi lập thì bộ phận dọn dẹp giữ danh sách kiểm và báo cáo `Wxx/4-cleanup.md`, bộ phận triển khai giữ danh sách kiểm trước và sau triển khai, release notes.

**QA** không phải bộ phận: là vai trò kiểm định do Điều hành gọi ở bước nghiệm thu, độc lập với agent đã thi công.

## 3. Bộ phận sở hữu gì

Bộ phận sở hữu **lĩnh vực**: quyết định chuyên môn (trình PO khi là luật sản phẩm), dữ liệu, tài liệu và chuẩn của lĩnh vực. Bộ phận là **đầu mối** của các vùng thư mục dưới đây; ai muốn đổi thì qua bộ phận đó.

| Bộ phận | Đầu mối của |
|---|---|
| Điều hành | `docs/ORGANIZATION.md`, `docs/04_waves/`, `docs/05_decisions/`, tích hợp, phát hành; mọi vùng chưa có đầu mối |

## 4. Phối hợp

| Cơ chế | Cách chạy |
|---|---|
| Bảng đợt chung (`04_waves/WAVES.md`) | Mỗi đợt ghi người chủ trì và bộ phận tham gia. Mỗi bộ phận chủ trì tối đa **một** đợt đang thi công. Hai đợt song song không sửa cùng vùng thư mục; nếu phải chạm nhau thì Điều hành xếp thứ tự |
| Backlog chung (`04_waves/BACKLOG.md`) | Mỗi việc có cột Phụ trách. Bộ phận tự xếp ưu tiên việc của mình, Điều hành gom thành đợt để thảo luận với PO |
| Yêu cầu giữa bộ phận | Bộ phận A cần bộ phận B làm gì thì ghi một dòng backlog cho B (Nguồn: "yêu cầu từ A"), không tự sửa vùng của B. Việc nhỏ trong cùng đợt ghi thành hạng mục của đợt, một người sửa |
| Hợp đồng và nguồn sự thật | Quyết định: `05_decisions/`. Từ vựng: `GLOSSARY.md`. Đổi hợp đồng dùng chung thì bộ phận đầu mối ghi quyết định và báo các bộ phận dùng nó |
| Đóng đợt chung | Điều hành gộp kết quả các đợt đã nghiệm thu, chạy cổng kiểm chứng toàn repo, commit |

### 4.1. Team thi công

Bộ phận sở hữu **lĩnh vực** và quyết định; team thi công sở hữu **vùng code** trong một đợt. Một đợt có thể chia nhiều team chạy song song (ví dụ CORE, SERVER, WEB, OPS, QA); team lập theo `2-scope.md`, giải tán khi đợt đóng.

| Team | Được sửa | Không được sửa | Đợt |
|---|---|---|---|
| (chưa có) | | | |

| Luật | Nội dung |
|---|---|
| Vùng không chồng nhau | Hai team không cùng sửa một thư mục; file dùng chung (hợp đồng, cấu hình gốc) giao một team, team khác ghi yêu cầu |
| Không đụng trạng thái chung | Không `git stash`, `checkout`, `reset`, `rebase`, `clean`; không cài thêm phụ thuộc khi đang có team khác chạy |
| Báo cáo | Mỗi team ghi kết quả vào `3-build.md` §1 theo mã hạng mục; không tự commit |

## 5. Vai trò của Điều hành

| Việc | Chi tiết |
|---|---|
| Làm việc với PO | Đầu mối duy nhất: mở đợt, thảo luận, nhận quyết định, báo kết quả |
| Chủ toạ (chế độ uỷ quyền) | Mở vấn đề, chạy các vòng tranh luận, phán quyết theo §7.2, ghi quyết định vào `05_decisions/` |
| Điều phối | Giữ bảng đợt và backlog; xếp đợt song song không chồng vùng; kiểm tra agent đang chạy định kỳ |
| Đề xuất và phản biện | Mỗi vấn đề trình PO có phương án, đề xuất, rủi ro của đề xuất; gọi vai phản biện (§7.4) khi vấn đề có nhiều góc nhìn |
| Chạy việc | Mỗi bước thi công hoặc vòng duyệt là một lượt gồm agent của các team, bộ phận liên quan. **Trạng thái nằm trong file**, không nằm trong agent |
| Chất lượng và phát hành | Tích hợp, chạy cổng kiểm chứng, quét secret, commit; giữ bí mật và chạy lệnh triển khai |

## 6. Khi lập một bộ phận mới

### 6.1 Khung hồ sơ chuẩn

Mọi bộ phận dùng cùng khung:

| Thư mục / file | Loại | Có hiệu lực? | Mã tài liệu |
|---|---|---|---|
| `README.md` | Cổng vào: bộ phận làm gì, danh mục tài liệu có mã và trạng thái, đọc gì trước, quy ước | — | — |
| `01_quy-che/` | Quy chế: điều lệ, quy trình, luật riêng của lĩnh vực, nhật ký thay đổi | Có; chỉ sửa khi PO chốt, ghi nhật ký | `QC-nn` |
| `02_chuan/` | Chuẩn kỹ thuật, chuyên môn của lĩnh vực | Có | `CH-nn` |
| `03_so-sach/` | Sổ sách: dữ liệu sống của lĩnh vực | Phản ánh hiện trạng | `SS-nn` |
| `04_nghien-cuu/` | Nghiên cứu: khảo sát, phân tích, đề xuất, có ngày; `README.md` là sổ đăng ký | Không, chỉ tham khảo | `NCnn` |

Luật chung: không trích luật trực tiếp từ nghiên cứu. PO chốt → chép phần có hiệu lực vào quy chế hoặc chuẩn → ghi nhật ký → đổi trạng thái nghiên cứu. Quyết định ảnh hưởng ngoài bộ phận vẫn ghi ở `05_decisions/`.

### 6.2 Các bước lập

| Bước | Việc |
|---|---|
| 1 | Ghi quyết định `QT-nnn` lập bộ phận: mã, lĩnh vực, vùng sở hữu |
| 2 | Tạo thư mục hồ sơ của bộ phận trong `docs/` theo khung §6.1, viết `README.md` và `01_quy-che/01-dieu-le.md` |
| 3 | Kiểm kê lĩnh vực: đang có gì, chất lượng, việc tồn đọng (thành nghiên cứu `NC01`); chuyển việc tồn đọng trong backlog sang bộ phận mới |
| 4 | Cập nhật §2, §3 của file này, `docs/README.md`, phần cấu trúc thư mục trong `CLAUDE.md` |
| 5 | Mở đợt đầu tiên do bộ phận chủ trì |

## 7. Tranh luận và chế độ uỷ quyền

Mặc định PO chốt từng vấn đề; Điều hành có thể gọi vai phản biện (§7.4) để tham vấn trước khi trình PO. PO có thể uỷ quyền chốt cho tranh luận giữa các bộ phận, Điều hành làm Chủ toạ. Uỷ quyền cần ít nhất hai bộ phận đã lập.

| Bước bật | Việc |
|---|---|
| 1 | PO chốt quyết định `QT-nnn` uỷ quyền: phạm vi (mọi đợt hay đợt nào), việc PO giữ lại (ví dụ: tiêu tiền, cài lên máy thật, mở hệ thống ra ngoài, thao tác dự án khác), tiêu chí §7.2 đã điền |
| 2 | Cập nhật §7.2 của file này và dòng "Chế độ chốt" trong README đợt |

Việc PO giữ lại mặc định, kể cả khi uỷ quyền: duyệt khung giao diện (`04_waves/README.md` §4.1), vấn đề bộ phận an toàn đẩy lên, tiêu tiền, thao tác môi trường thật, mở hệ thống ra ngoài.

### 7.1. Vòng tranh luận

| Vòng | Ai | Việc | Đầu ra |
|---|---|---|---|
| R1 Lập trường | Mỗi bộ phận tham gia, độc lập, không đọc lập trường của bộ phận khác | Trả lời mọi vấn đề `Wxx-nn`: phương án đề xuất, lý do, rủi ro, cái giá; được đề xuất vấn đề mới | `Wxx/debate/r1-<mã>.md` (mẫu `04_waves/_template/debate-r1.md`) |
| R2 Phản biện | Mỗi bộ phận, sau khi đọc **mọi** file R1 | Đồng ý, phản đối có lý do, nhượng bộ, lập trường cuối cho từng vấn đề | `Wxx/debate/r2-<mã>.md` (mẫu `04_waves/_template/debate-r2.md`) |
| R3 Phán quyết | Chủ toạ | Đọc R1, R2; chốt từng vấn đề theo §7.2; ghi ý kiến thiểu số | Cột **PO chốt** (`Uỷ quyền: …`) trong `Wxx/1-discussion.md`, bản nháp `2-scope.md` |
| R4 Kháng nghị (nếu có) | Bộ phận thấy phán quyết gây hại nghiêm trọng cho lĩnh vực của mình | Một kháng nghị ngắn: phán quyết nào, hại gì, đề xuất sửa | `Wxx/debate/r4-<mã>.md` |
| R5 Giải quyết kháng nghị | Chủ toạ | Giữ hoặc sửa phán quyết, ghi lý do | Nhật ký `Wxx/1-discussion.md` |

### 7.2. Tiêu chí của Chủ toạ

Theo thứ tự ưu tiên khi xung đột. Điền khi bật chế độ uỷ quyền.

| # | Tiêu chí |
|---|---|
| 1 | (chưa điền; ví dụ: an toàn, riêng tư, không làm hỏng dữ liệu và máy của người dùng) |
| 2 | (chưa điền; ví dụ: trả lời đúng yêu cầu PO đã nêu) |
| 3 | (chưa điền; ví dụ: chạy được thật, kiểm chứng được bằng test tự động) |
| 4 | (chưa điền; ví dụ: đơn giản khi vận hành) |

### 7.3. Luật tranh luận

| Luật | Nội dung |
|---|---|
| Lập trường có căn cứ | Viện dẫn dữ kiện: tài liệu chính thức, kiểm trên máy, file `Wxx/research/`. Điều chưa kiểm được ghi rõ là giả định |
| Phủ quyết | Bộ phận hoặc vai giữ an toàn, bảo mật được phủ quyết phương án có rủi ro nghiêm trọng. Chủ toạ chỉ gỡ phủ quyết khi có biện pháp giảm thiểu ghi rõ trong phán quyết |
| Không hạ thấp yêu cầu PO | Không phương án nào được bỏ một yêu cầu PO đã nêu; việc lớn không kịp trong đợt thì chia đợt |
| Kết luận | Mỗi vấn đề ra một trong ba: **Làm** (phương án …), **Không làm** (lý do), **Hoãn → BL-nnn** |
| PO lật lại | PO lật lại được mọi phán quyết; Điều hành ghi nhật ký, đang thi công thì mở CR |

### 7.4. Vai phản biện

Vai do Điều hành giao cho agent con (hoặc tự đóng lần lượt khi không có agent con) để nhìn vấn đề từ nhiều phía. Mỗi vai viết R1 độc lập, đọc mọi R1 rồi viết R2. Chọn 2–4 vai liên quan tới vấn đề; dự án thêm vai riêng vào bảng.

| Mã | Vai | Hỏi gì | Phủ quyết |
|---|---|---|---|
| USER | Người dùng cuối | Dùng có dễ, có đúng việc họ cần, có bị mất dữ liệu hay thói quen không | Không |
| PROD | Sản phẩm | Có trả lời đúng yêu cầu PO, phạm vi có vừa đợt, cái gì nên hoãn | Không |
| ARCH | Kiến trúc | Đơn giản nhất chạy được là gì, nợ kỹ thuật, khả năng đổi sau này | Không |
| TRUST | An toàn, bảo mật, riêng tư | Dữ liệu, bí mật, quyền, rủi ro không đảo ngược | Có (§7.3) |
| OPS | Vận hành | Triển khai, quan sát, backup, quay lại bản trước, chi phí | Không |
| QA | Kiểm định | Kiểm chứng bằng cách nào, tiêu chí có đo được không | Không |
| DEVIL | Phản biện tự do | Tìm lý do mạnh nhất để không làm hoặc làm khác | Không |

Lập trường của vai là tham vấn; chỉ thành quyết định khi PO chốt (hoặc Chủ toạ chốt trong phạm vi uỷ quyền).

## 8. Ranh giới an toàn khi dọn dẹp và triển khai

Đổi mục nào trong phần này cần PO duyệt, ghi quyết định `QT-nnn`.

### 8.1. Cách dọn dẹp

| Luật | Nội dung |
|---|---|
| Chỉ đọc | Người dọn quét toàn repo ở chế độ chỉ đọc, lập danh sách theo vùng sở hữu và tên file; không mở nội dung file trong danh sách cấm (§8.2) |
| Chủ vùng xoá | Mỗi mục do chủ vùng xoá trong vùng của mình; người dọn kiểm lại sau khi xoá |
| Chỉ xoá mã không được gọi | Lượt dọn chỉ xoá mã không còn được gọi, tài liệu lệch, file tạm. Việc đổi hành vi chạy (route, migration, cấu hình, phụ thuộc) ghi backlog |
| Ngoại lệ `tmp/` | Được xoá trực tiếp trong `tmp/` chỉ theo danh sách cho phép (§8.3); file khác của `tmp/` đưa vào danh sách và chờ PO. Không xoá hàng loạt `tmp/` bằng một lệnh |
| `reports/` của đợt đã đóng | Người dọn đề xuất, Điều hành xoá |
| Khung thiết kế, demo | Khung của màn đã bỏ được đánh dấu "đã bỏ"; chỉ xoá khi PO đồng ý |
| Sau dọn | Mọi cổng kiểm chứng chạy lại ở bước 🧪 Nghiệm thu |

### 8.2. Danh sách cấm xoá

Không xoá, không ghi đè, không đổi tên, không di chuyển, không mở nội dung các mục dưới đây khi PO chưa đồng ý.

| Đường dẫn | Loại | Lý do giữ |
|---|---|---|
| File env thật, khoá riêng (`*.key`, `*.pem`) | Bí mật | Mất thì không khôi phục được từ git |
| Migration đã áp lên DB dùng chung | Lịch sử DB | Xoá làm lệch lịch sử migration của DB thật |
| (dự án bổ sung: bản sao lưu, bản lưu cấu hình thật, bản phát hành đang chạy và bản liền trước) | | |

### 8.3. Danh sách cho phép trong `tmp/`

Mẫu tên được xoá trực tiếp, PO duyệt. Mục nào cũng không được khớp một file ở §8.2; khớp thì §8.2 thắng. Thêm mẫu mới: đề xuất ở `Wxx/4-cleanup.md` §5, PO duyệt, Điều hành ghi vào bảng.

| Mẫu tên | Nội dung | Trạng thái duyệt |
|---|---|---|
| (chưa có) | | |

### 8.4. Ranh giới triển khai

| Việc | Ai | Ràng buộc |
|---|---|---|
| Chạy lệnh triển khai | Điều hành | Chỉ từ trạng thái đã commit |
| Giữ bí mật | Điều hành | Bí mật không vào log, tài liệu, kênh chat, image ngoài phần đã có quyết định |
| Kiểm trước và sau triển khai | Điều hành, hoặc bộ phận triển khai khi đã lập | Theo `03_release/README.md` §2; ảnh chụp có dữ liệu thật chỉ lưu ở `tmp/` |
| Quay lại bản trước | Điều hành | Theo `03_release/README.md` §3 |
