# Tổ chức dự án {{TEN_DU_AN}}

> Vai trò, bộ phận, build team, vùng sở hữu, cách phối hợp, debate và delegation, ranh giới an toàn khi cleanup. Quy trình wave ở `04_waves/README.md`; luật chung cho agent ở `../CLAUDE.md`.

## 1. Sơ đồ

```text
                         PO (người dùng)
       quyết định · lock scope của wave · duyệt · acceptance
                              │
                Orchestrator (phiên AI chính)
   đề xuất · phản biện · bảng wave · backlog · decision log · điều phối · tích hợp · commit
                              │
        ┌─────────────────────┼──────────────────────┐
   Bộ phận (lập theo dự án,    Build team (lập theo     Vai phản biện (gọi khi
   sở hữu lĩnh vực, §2 §6)     wave, sở hữu vùng code, §4.1) debate tham vấn, §7.4)
```

## 2. Các bộ phận

| Bộ phận | Mã | Trạng thái | Phụ trách | Hồ sơ | Subagent |
|---|---|---|---|---|---|
| Orchestrator | — | Hoạt động từ {{NGAY}} | Điều phối, hồ sơ quy trình, tích hợp | `04_waves/`, `05_decisions/` | Phiên AI chính |

**Lập theo dự án, ngay từ W01.** Ở W01 Orchestrator đề xuất bộ bộ phận hợp với sản phẩm (vấn đề W01-09), PO duyệt, rồi lập bằng tool `create_department`. Khi dự án phát sinh một lĩnh vực mới mà không bộ phận nào phụ trách, Orchestrator đề xuất lập thêm (ghi `QT-nnn`), không tự đảm nhận lĩnh vực đó lâu dài.

**Việc thuộc lĩnh vực nào thì giao bộ phận đó.** Mỗi việc phát sinh (vấn đề cần ý kiến chuyên môn, khảo sát, hạng mục build, cleanup, acceptance, triển khai) được giao cho subagent của bộ phận phụ trách lĩnh vực đó; việc chạm nhiều lĩnh vực thì mỗi bộ phận nhận phần của mình. Không có bộ phận phù hợp thì giao bộ phận gần nhất và đề xuất lập bộ phận mới.

### 2.1. Danh mục gợi ý

Chọn theo sản phẩm, thường 3–5 bộ phận; đổi tên, gộp, tách cho hợp dự án.

| Mã | Lĩnh vực | Nên lập khi |
|---|---|---|
| PRODUCT | Nghiệp vụ, yêu cầu, phạm vi, từ vựng | Luôn có khi sản phẩm có nghiệp vụ riêng |
| UX | Giao diện, luồng, nguyên tắc thiết kế | Có giao diện người dùng |
| PLATFORM | Code chính, kiến trúc, dữ liệu, contract | Luôn có khi có code |
| DATA | Mô hình dữ liệu, báo cáo, pipeline | Dữ liệu là trọng tâm (báo cáo, phân tích, đồng bộ) |
| TRUST | Bảo mật, quyền, riêng tư, bí mật | Có dữ liệu người dùng, phân quyền, tích hợp ngoài |
| QA | Kịch bản kiểm thử, quality gate, acceptance độc lập | Sản phẩm có nhiều luồng cần kiểm lại mỗi wave |
| OPS | Triển khai, vận hành, quan sát, backup | Có môi trường thật cần giữ |
| CLEAN | Cleanup, nợ kỹ thuật, tài liệu lệch | Dự án đã qua vài wave, mã chết và tài liệu lệch tích tụ |

**QA** luôn độc lập với bộ phận đã build hạng mục đó, kể cả khi chưa lập bộ phận QA: Orchestrator gọi một subagent khác làm acceptance.

## 3. Bộ phận sở hữu gì

Bộ phận sở hữu **lĩnh vực**: quyết định chuyên môn (trình PO khi là luật sản phẩm), dữ liệu, tài liệu và chuẩn của lĩnh vực. Bộ phận là **đầu mối** của các vùng thư mục dưới đây; ai muốn đổi thì qua bộ phận đó.

| Bộ phận | Đầu mối của |
|---|---|
| Orchestrator | `docs/ORGANIZATION.md`, `docs/04_waves/`, `docs/05_decisions/`, tích hợp, release; mọi vùng chưa có đầu mối |

## 4. Phối hợp

| Cơ chế | Cách chạy |
|---|---|
| Bảng wave chung (`04_waves/WAVES.md`) | Mỗi wave ghi người chủ trì và bộ phận tham gia. Mỗi bộ phận chủ trì tối đa **một** wave đang build. Hai wave song song không sửa cùng vùng thư mục; nếu phải chạm nhau thì Orchestrator xếp thứ tự |
| Backlog chung (`04_waves/BACKLOG.md`) | Mỗi việc có cột Phụ trách. Bộ phận tự xếp ưu tiên việc của mình, Orchestrator gom thành wave để thảo luận với PO |
| Yêu cầu giữa bộ phận | Bộ phận A cần bộ phận B làm gì thì ghi một dòng backlog cho B (Nguồn: "yêu cầu từ A"), không tự sửa vùng của B. Việc nhỏ trong cùng wave ghi thành hạng mục của wave, một người sửa |
| Contract và nguồn sự thật | Quyết định: `05_decisions/`. Từ vựng: `GLOSSARY.md`. Đổi contract dùng chung thì bộ phận đầu mối ghi quyết định và báo các bộ phận dùng nó |
| Đóng wave chung | Orchestrator gộp kết quả các wave đã qua Acceptance, chạy quality gate toàn repo, commit |

### 4.1. Build team

Bộ phận sở hữu **lĩnh vực** và quyết định; build team sở hữu **vùng code** trong một wave. Một wave có thể chia nhiều team chạy song song (ví dụ CORE, SERVER, WEB, OPS, QA); team lập theo `2-scope.md`, giải tán khi wave đóng.

| Team | Được sửa | Không được sửa | Wave |
|---|---|---|---|
| (chưa có) | | | |

| Luật | Nội dung |
|---|---|
| Vùng không chồng nhau | Hai team không cùng sửa một thư mục; file dùng chung (contract, cấu hình gốc) giao một team, team khác ghi yêu cầu |
| Không thay đổi trạng thái git dùng chung | Không `git stash`, `checkout`, `reset`, `rebase`, `clean`; không cài thêm phụ thuộc khi đang có team khác chạy |
| Báo cáo | Mỗi team ghi kết quả vào `3-build.md` §1 theo mã hạng mục; không tự commit |

## 5. Vai trò của Orchestrator

Orchestrator **điều phối, không thi công**. Việc tốn công giao cho bộ phận; Orchestrator chỉ tự làm việc nhỏ của chính vai điều phối.

| Orchestrator tự làm | Giao bộ phận |
|---|---|
| Làm việc với PO: mở wave, trình vấn đề, nhận quyết định, báo kết quả | Ý kiến chuyên môn cho từng vấn đề (lập trường R1, R2) |
| Cập nhật hồ sơ quy trình: README wave, `WAVES.md`, `BACKLOG.md`, mục lục decision log | Khảo sát, đọc nhiều file, tra tài liệu ngoài |
| Tổng hợp kết quả các bộ phận, phán quyết khi delegation | Viết code, test, tài liệu chuyên môn, quy chuẩn |
| Sửa nhỏ một chỗ để nối kết quả hai bộ phận (dưới khoảng 20 dòng, không phải code nghiệp vụ) | Cleanup, acceptance, triển khai |
| Chạy quality gate cuối, quét secret, commit | Mọi việc khác thuộc vùng sở hữu của một bộ phận |

| Việc | Chi tiết |
|---|---|
| Chủ toạ (chế độ delegation) | Mở vấn đề, chạy các vòng debate, phán quyết theo §7.2, ghi quyết định vào `05_decisions/` |
| Điều phối | Giao việc theo §2, giữ bảng wave và backlog; xếp wave song song không chồng vùng; kiểm tra subagent định kỳ |
| Đề xuất và phản biện | Mỗi vấn đề trình PO có phương án, đề xuất, rủi ro của đề xuất; lấy lập trường của bộ phận liên quan, gọi thêm vai phản biện (§7.4) khi cần |
| Chạy việc | Mỗi bước build hoặc vòng duyệt là một lượt gồm subagent của các bộ phận, team liên quan. **Trạng thái nằm trong file**, không nằm trong agent |

Không còn bộ phận nào làm được và việc gấp thì Orchestrator làm, ghi "Orchestrator (thay <mã>)" trong hồ sơ wave, và đề xuất lập bộ phận ở lần trình PO kế tiếp.

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
| 1 | PO duyệt (W01-09 hoặc một vấn đề trong wave); ghi `QT-nnn` lập bộ phận: mã, lĩnh vực, vùng sở hữu |
| 2 | Tool `create_department`: tạo hồ sơ `docs/departments/<mã>/` theo khung §6.1, subagent `.claude/agents/dept-<mã>.md`, thêm dòng vào §2, §3 |
| 3 | Bộ phận viết `01_quy-che/01-dieu-le.md` và kiểm kê lĩnh vực (nghiên cứu `NC01`); chuyển việc tồn đọng trong backlog sang bộ phận |
| 4 | Cập nhật `docs/README.md` nếu cần |

## 7. Debate và chế độ delegation

Mặc định PO chốt từng vấn đề; Orchestrator lấy lập trường của các bộ phận liên quan, gọi thêm vai phản biện (§7.4) khi cần, rồi trình PO. Ở chế độ delegation, PO giao quyền chốt cho debate giữa các bộ phận, Orchestrator làm Chủ toạ.

| Bước bật | Việc |
|---|---|
| 1 | PO chốt quyết định `QT-nnn` delegation: phạm vi (mọi wave hay wave nào), việc PO giữ lại (ví dụ: tiêu tiền, cài lên máy thật, mở hệ thống ra ngoài, thao tác dự án khác), tiêu chí §7.2 đã điền |
| 2 | Cập nhật §7.2 của file này và dòng "Chế độ chốt" trong README wave |

Việc PO giữ lại mặc định, kể cả khi delegation: duyệt khung giao diện (`04_waves/README.md` §4.1), vấn đề bộ phận an toàn đẩy lên, tiêu tiền, thao tác môi trường thật, mở hệ thống ra ngoài.

### 7.1. Vòng debate

| Vòng | Ai | Việc | Đầu ra |
|---|---|---|---|
| R1 Lập trường | Mỗi bộ phận tham gia, độc lập, không đọc lập trường của bộ phận khác | Trả lời mọi vấn đề `Wxx-nn`: phương án đề xuất, lý do, rủi ro, cái giá; được đề xuất vấn đề mới | `Wxx/debate/r1-<mã>.md` (mẫu `04_waves/_template/debate-r1.md`) |
| R2 Phản biện | Mỗi bộ phận, sau khi đọc **mọi** file R1 | Đồng ý, phản đối có lý do, nhượng bộ, lập trường cuối cho từng vấn đề | `Wxx/debate/r2-<mã>.md` (mẫu `04_waves/_template/debate-r2.md`) |
| R3 Phán quyết | Chủ toạ | Đọc R1, R2; chốt từng vấn đề theo §7.2; ghi ý kiến thiểu số | Cột **PO chốt** (`Delegation: …`) trong `Wxx/1-discussion.md`, bản nháp `2-scope.md` |
| R4 Kháng nghị (nếu có) | Bộ phận thấy phán quyết gây hại nghiêm trọng cho lĩnh vực của mình | Một kháng nghị ngắn: phán quyết nào, hại gì, đề xuất sửa | `Wxx/debate/r4-<mã>.md` |
| R5 Giải quyết kháng nghị | Chủ toạ | Giữ hoặc sửa phán quyết, ghi lý do | Nhật ký `Wxx/1-discussion.md` |

### 7.2. Tiêu chí của Chủ toạ

Theo thứ tự ưu tiên khi xung đột. Điền khi bật chế độ delegation.

| # | Tiêu chí |
|---|---|
| 1 | (chưa điền; ví dụ: an toàn, riêng tư, không làm hỏng dữ liệu và máy của người dùng) |
| 2 | (chưa điền; ví dụ: trả lời đúng yêu cầu PO đã nêu) |
| 3 | (chưa điền; ví dụ: chạy được thật, kiểm chứng được bằng test tự động) |
| 4 | (chưa điền; ví dụ: đơn giản khi vận hành) |

### 7.3. Luật debate

| Luật | Nội dung |
|---|---|
| Lập trường có căn cứ | Viện dẫn dữ kiện: tài liệu chính thức, kiểm trên máy, file `Wxx/research/`. Điều chưa kiểm được ghi rõ là giả định |
| Phủ quyết | Bộ phận hoặc vai giữ an toàn, bảo mật được phủ quyết phương án có rủi ro nghiêm trọng. Chủ toạ chỉ gỡ phủ quyết khi có biện pháp giảm thiểu ghi rõ trong phán quyết |
| Không hạ thấp yêu cầu PO | Không phương án nào được bỏ một yêu cầu PO đã nêu; việc lớn không kịp trong wave thì chia wave |
| Kết luận | Mỗi vấn đề ra một trong ba: **Làm** (phương án …), **Không làm** (lý do), **Hoãn → BL-nnn** |
| PO lật lại | PO lật lại được mọi phán quyết; Orchestrator ghi nhật ký, đang build thì mở CR |

### 7.4. Vai phản biện

Vai do Orchestrator giao cho subagent (hoặc tự đóng lần lượt khi không có subagent) để nhìn vấn đề từ nhiều phía. Mỗi vai viết R1 độc lập, đọc mọi R1 rồi viết R2. Chọn 2–4 vai liên quan tới vấn đề; dự án thêm vai riêng vào bảng.

| Mã | Vai | Hỏi gì | Phủ quyết |
|---|---|---|---|
| USER | Người dùng cuối | Dùng có dễ, có đúng việc họ cần, có bị mất dữ liệu hay thói quen không | Không |
| PROD | Sản phẩm | Có trả lời đúng yêu cầu PO, phạm vi có vừa wave, cái gì nên hoãn | Không |
| ARCH | Kiến trúc | Đơn giản nhất chạy được là gì, nợ kỹ thuật, khả năng đổi sau này | Không |
| TRUST | An toàn, bảo mật, riêng tư | Dữ liệu, bí mật, quyền, rủi ro không đảo ngược | Có (§7.3) |
| OPS | Vận hành | Triển khai, quan sát, backup, quay lại bản trước, chi phí | Không |
| QA | Kiểm định | Kiểm chứng bằng cách nào, tiêu chí có đo được không | Không |
| DEVIL | Phản biện tự do | Tìm lý do mạnh nhất để không làm hoặc làm khác | Không |

Lập trường của vai là tham vấn; chỉ thành quyết định khi PO chốt (hoặc Chủ toạ chốt trong phạm vi delegation).

## 8. Ranh giới an toàn khi cleanup và triển khai

Đổi mục nào trong phần này cần PO duyệt, ghi quyết định `QT-nnn`.

### 8.1. Cách cleanup

| Luật | Nội dung |
|---|---|
| Chỉ đọc | Người dọn quét toàn repo ở chế độ chỉ đọc, lập danh sách theo vùng sở hữu và tên file; không mở nội dung file trong danh sách cấm (§8.2) |
| Chủ vùng xoá | Mỗi mục do chủ vùng xoá trong vùng của mình; người dọn kiểm lại sau khi xoá |
| Chỉ xoá mã không được gọi | Lượt dọn chỉ xoá mã không còn được gọi, tài liệu lệch, file tạm. Việc đổi hành vi chạy (route, migration, cấu hình, phụ thuộc) ghi backlog |
| Ngoại lệ `tmp/` | Được xoá trực tiếp trong `tmp/` chỉ theo danh sách cho phép (§8.3); file khác của `tmp/` đưa vào danh sách và chờ PO. Không xoá hàng loạt `tmp/` bằng một lệnh |
| `reports/` của wave đã đóng | Người dọn đề xuất, Orchestrator xoá |
| Khung thiết kế, demo | Khung của màn đã bỏ được đánh dấu "đã bỏ"; chỉ xoá khi PO đồng ý |
| Sau dọn | Mọi quality gate chạy lại ở bước 🧪 Acceptance |

### 8.2. Danh sách cấm xoá

Không xoá, không ghi đè, không đổi tên, không di chuyển, không mở nội dung các mục dưới đây khi PO chưa đồng ý.

| Đường dẫn | Loại | Lý do giữ |
|---|---|---|
| File env thật, khoá riêng (`*.key`, `*.pem`) | Bí mật | Mất thì không khôi phục được từ git |
| Migration đã áp lên DB dùng chung | Lịch sử DB | Xoá làm lệch lịch sử migration của DB thật |
| (dự án bổ sung: bản sao lưu, bản lưu cấu hình thật, bản phát hành đang chạy và bản liền trước) | | |

### 8.3. Danh sách cho phép trong `tmp/`

Mẫu tên được xoá trực tiếp, PO duyệt. Mục nào cũng không được khớp một file ở §8.2; khớp thì §8.2 thắng. Thêm mẫu mới: đề xuất ở `Wxx/4-cleanup.md` §5, PO duyệt, Orchestrator ghi vào bảng.

| Mẫu tên | Nội dung | Trạng thái duyệt |
|---|---|---|
| (chưa có) | | |

### 8.4. Ranh giới triển khai

| Việc | Ai | Ràng buộc |
|---|---|---|
| Chạy lệnh triển khai | Orchestrator | Chỉ từ trạng thái đã commit |
| Giữ bí mật | Orchestrator | Bí mật không vào log, tài liệu, kênh chat, image ngoài phần đã có quyết định |
| Kiểm trước và sau triển khai | Orchestrator, hoặc bộ phận triển khai khi đã lập | Theo `03_release/README.md` §2; ảnh chụp có dữ liệu thật chỉ lưu ở `tmp/` |
| Quay lại bản trước | Orchestrator | Theo `03_release/README.md` §3 |
