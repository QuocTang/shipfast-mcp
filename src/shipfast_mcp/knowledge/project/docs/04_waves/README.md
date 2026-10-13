# Quy trình làm việc theo wave

> Áp dụng từ {{NGAY}} (`QT-001`). Vai trò: **PO** = người dùng (quyết định). **Orchestrator** = phiên AI chính (intake, đề xuất, phản biện, điều phối, tích hợp, commit). **Agent** = subagent (build, khảo sát, cleanup, QA).

## 1. Vòng đời một wave

Mỗi wave đi qua 7 bước theo thứ tự. **Không viết code trước bước 3**, trừ khảo sát chỉ đọc và hotfix (§5). Hạng mục có giao diện còn phải qua cổng thiết kế (§4.1).

| Bước | Trạng thái | Ai làm | Việc | Đầu ra | Cổng để sang bước sau |
|---|---|---|---|---|---|
| 0 | 📥 Intake | Orchestrator | Lấy việc từ yêu cầu PO, `BACKLOG.md`, phản hồi người dùng, giới hạn đã biết. Mỗi vấn đề kèm bối cảnh, phương án, đề xuất. Dữ kiện cần kiểm thì cho agent khảo sát chỉ đọc, ghi vào `Wxx/research/`. Chọn chế độ chốt (§4.2) | `Wxx/README.md`, `Wxx/1-discussion.md` bản đầu | PO đã nhận chương trình |
| 1 | 🗣️ Discussion | PO ↔ Orchestrator; hoặc các bộ phận debate (§4.3) | Trao đổi từng vấn đề, nhiều lượt nếu cần. Orchestrator phản biện cả đề xuất của mình lẫn lựa chọn của PO | Cột **PO chốt** của mọi vấn đề là Làm, Không làm hoặc Hoãn. Hoãn thì trả về backlog | Không còn vấn đề "Chờ" |
| 2 | ✅ Scope lock | Orchestrator viết, PO duyệt | Viết `2-scope.md`: hạng mục `Wxx-Pnn`, tiêu chí acceptance đo được, vùng sở hữu, quality gate, rủi ro. Ghi quyết định mới vào `../05_decisions/`, contract vào `../02_build/CONTRACTS.md` | Phạm vi được duyệt | PO nói **"chốt"** (delegation: Chủ toạ chốt và báo PO). Ghi ngày chốt vào README wave và `WAVES.md` |
| 3 | 🔨 Build | Agent hoặc team (`../ORGANIZATION.md` §4.1) | Chạy liên tục tới khi xong, song song theo vùng sở hữu khi được. Orchestrator kiểm tra agent định kỳ, ghi `3-build.md`. Việc ngoài phạm vi vào backlog; đổi phạm vi qua CR (§4) | Mọi hạng mục xong | Quality gate của wave xanh, đã **chạy thật** ít nhất một lần |
| 4 | 🧹 Cleanup | Agent cleanup + chủ vùng | Quét chỉ đọc theo danh sách kiểm của `4-cleanup.md`; chủ vùng xoá mục trong vùng mình. Chỉ xoá mã không được gọi, tài liệu lệch, file tạm; việc đổi hành vi chạy ghi backlog. Ranh giới: `../ORGANIZATION.md` §8 | `4-cleanup.md` | Mọi mục đã xử lý hoặc có lý do và mã backlog; quality gate xanh |
| 5 | 🧪 Acceptance | Agent QA độc lập + Orchestrator | Chạy lại toàn bộ quality gate trên mã đã dọn, kịch bản đầu cuối, so với từng tiêu chí; lỗi `QAxx-n` được sửa rồi kiểm lại; trình các quyết định "Giả định" | `5-acceptance.md` §1–§4 | Mọi tiêu chí đạt, hoặc PO chấp nhận ngoại lệ |
| 6 | 🚀 Release và đóng | Orchestrator (+ bộ phận triển khai khi đã lập) | Release theo `../03_release/README.md`, commit, **rút kinh nghiệm** (`5-acceptance.md` §6, bắt buộc), trả việc dở về backlog, cập nhật mọi trạng thái | README wave **Closed**; `WAVES.md` cập nhật | Tool `check` không báo lỗi cho wave này |

Mỗi wave có một **người chủ trì**: Orchestrator, hoặc một bộ phận khi đã lập. Mỗi bộ phận chủ trì tối đa **một** wave ở bước 3–6 cùng lúc; hai wave song song không sửa cùng vùng thư mục. Được mở discussion cho wave kế (bước 0–2) khi wave trước đang build.

**QA** không phải bộ phận: là vai trò kiểm định do Orchestrator gọi ở bước 5, độc lập với agent đã build.

## 2. Hồ sơ mỗi wave

Mỗi wave có một thư mục `Wxx/` (hai chữ số). Mẫu ở `_template/`. Tiền tố số của file trùng số bước tạo ra file đó. Mở wave bằng tool `open_wave` hoặc chép `_template/` thủ công.

| File | Tạo ở bước | Nội dung | Ai cập nhật |
|---|---|---|---|
| `README.md` | 0 | Thẻ wave: chủ trì, chế độ chốt, mục tiêu, trạng thái, ngày các mốc, phiên bản, commit | Orchestrator, mỗi lần đổi bước |
| `1-discussion.md` | 0 | Vấn đề `Wxx-nn`: bối cảnh, dữ kiện, phương án, đề xuất, phản biện, **PO chốt**; nhật ký trao đổi | Orchestrator theo từng lượt |
| `research/` | 0–1 | Dữ kiện, khảo sát chỉ đọc; mỗi file ghi ngày và nguồn | Agent khảo sát |
| `debate/` | 1 | Lập trường các vai hoặc bộ phận: `r1-<mã>.md`, `r2-<mã>.md`, `r4-<mã>.md`. Giữ lại sau khi đóng wave | Đại diện vai, bộ phận |
| `2-scope.md` | 2 | Hạng mục, tiêu chí acceptance, vùng sở hữu, quality gate, ngoài phạm vi, rủi ro | Orchestrator; đóng băng sau khi chốt, chỉ đổi qua CR |
| `3-build.md` | 3 | Trạng thái hạng mục, quyết định trong build, lượt chạy, CR, commit | Orchestrator |
| `4-cleanup.md` | 4 | Kiểm ranh giới an toàn, danh sách kiểm, mục dọn theo vùng, việc chuyển backlog | Agent cleanup, chủ vùng |
| `5-acceptance.md` | 5–6 | Kết quả theo tiêu chí, quality gate, lỗi, release, rút kinh nghiệm, việc chuyển wave sau | QA, Orchestrator |

Wave chốt thẳng (§4.2) vẫn có `README.md`, `2-scope.md`, `3-build.md`, `5-acceptance.md`; `1-discussion.md` chỉ cần bảng tổng hợp và lý do chốt thẳng.

## 3. Mã và nơi ghi

| Loại | Mã | Ghi ở đâu |
|---|---|---|
| Việc chưa xếp wave | `BL-nnn` | `BACKLOG.md` |
| Phản hồi của người dùng | `FB-nnn` | `BACKLOG.md`, cột Nguồn |
| Vấn đề trong một wave | `Wxx-nn` | `Wxx/1-discussion.md`, sau đó `2-scope.md` |
| Hạng mục build | `Wxx-Pnn` | `Wxx/2-scope.md`, `3-build.md` |
| Quyết định nhỏ trong build | `Q-Wxx-nn` | `Wxx/3-build.md` §2; ảnh hưởng ngoài wave thì ghi `../05_decisions/` |
| Yêu cầu đổi phạm vi khi đang build | `CR-Wxx-nn` | `Wxx/3-build.md` §4 |
| Mục cleanup | `CL-Wxx-nn` | `Wxx/4-cleanup.md` |
| Lỗi tìm thấy khi acceptance | `QAxx-n` | `Wxx/5-acceptance.md` |
| Quyết định sản phẩm, nghiệp vụ | `SP-nnn` | `../05_decisions/` |
| Quyết định kỹ thuật | `KT-nnn` | `../05_decisions/` |
| Quyết định quy trình, cách làm việc | `QT-nnn` | `../05_decisions/` |
| Việc PO giao trực tiếp ngoài wave | `PO-nn` | `WAVES.md` §2 |
| Vận hành, hotfix | `OPS-nn`, `HOTFIX-nn` | `WAVES.md` §2 |
| Từ vựng chuẩn | — | `../GLOSSARY.md` |
| Phân tích hệ cũ, dự án nguồn | `nn` | `../00_analysis/` |
| Thành phần, lệnh, contract giữa các phần | — | `../02_build/CONTRACTS.md` |

Mỗi thông tin chỉ sống ở **một** chỗ; nơi khác chỉ dẫn mã hoặc đường dẫn. Tool `next_code` cấp mã kế tiếp để tránh trùng số.

## 4. Luật ở bước Discussion và Build

| Tình huống | Làm gì |
|---|---|
| Trình một vấn đề | Bối cảnh, ít nhất hai phương án khi có lựa chọn thật, đề xuất của Orchestrator, rủi ro của chính đề xuất đó |
| PO trả lời | Theo mã: "W02-03: A", "đồng ý đề xuất trừ W02-05", "W02-07 hoãn". Orchestrator ghi nhật ký và điền cột PO chốt |
| PO chọn khác đề xuất hoặc yêu cầu mơ hồ | Orchestrator nêu rủi ro, hệ quả, câu hỏi làm rõ cụ thể; chỉ ghi chốt khi PO xác nhận |
| Câu hỏi gửi PO | Gọi đối tượng bằng tên, kèm trạng thái hiện tại; mã chỉ kèm sau trong ngoặc |
| Vấn đề cần số liệu mới quyết được | Agent khảo sát chỉ đọc, ghi `Wxx/research/`, mang kết quả về discussion tiếp |
| PO lật lại một kết luận | Ghi nhật ký `1-discussion.md`; đang build thì mở CR |
| Đang build mà phát hiện việc mới | Ghi backlog (`BL-nnn`), không tự làm |
| Đang build mà cần đổi phạm vi hoặc tiêu chí | Mở `CR-Wxx-nn`: lý do, ảnh hưởng, đề xuất. Duyệt mới làm |
| PO giao việc trực tiếp ngoài wave | Ghi `PO-nn` ở `WAVES.md` §2 (việc, lý do không qua wave), làm, ghi kết quả và commit; việc lớn thì đề nghị mở wave |
| Câu hỏi thiết kế chưa có tài liệu | Dừng hạng mục đó, hỏi PO; các hạng mục khác vẫn chạy |
| Quality gate chưa từng chạy được | Không chuyển wave sang bước sau |
| Agent bị treo hoặc chết | Orchestrator kiểm tra định kỳ, chạy lại từ bước dở theo `3-build.md` |
| Commit | Agent không tự commit. Orchestrator commit checkpoint cuối bước 3 và bước 6, quét secret trước |

### 4.1. Cổng thiết kế trước code giao diện

| Luật | Nội dung |
|---|---|
| Cổng | Hạng mục có giao diện mới hoặc đổi bố cục chỉ vào build khi PO đã duyệt khung: trang demo tĩnh trong `reports/`, file thiết kế, hoặc ảnh phác |
| Khung bắt buộc | Góc nhìn của từng vai người dùng bị ảnh hưởng; trạng thái rỗng, đang tải, lỗi của từng màn hay khối mới |
| Phần không có giao diện | API, contract, dữ liệu của cùng hạng mục làm ngay sau lock scope |
| Rút nguyên tắc | Góp ý giao diện của PO trong wave rút thành nguyên tắc trong `../technical/` ở bước 🧹 |
| Dữ liệu mẫu | Giả hoàn toàn: không tên, email, số điện thoại người thật |

### 4.2. Chế độ chốt

| Chế độ | Khi nào | Cách chạy |
|---|---|---|
| **PO chốt** (mặc định) | Mọi wave | Orchestrator trình từng vấn đề, PO chốt |
| **Chốt thẳng** | Wave nhỏ, yêu cầu PO đã rõ, không có lựa chọn thiết kế đáng kể | Ghi lý do trong README wave; `1-discussion.md` chỉ có bảng tổng hợp; PO duyệt `2-scope.md` như thường |
| **Delegation** | PO muốn giảm số lần chốt và đã có ít nhất hai bộ phận | PO ghi `QT-nnn`: phạm vi, việc PO giữ lại, tiêu chí Chủ toạ (`../ORGANIZATION.md` §7). Các bộ phận debate, Chủ toạ chốt |

### 4.3. Debate

Debate dùng được ở mọi chế độ:

- **Tham vấn** (PO chốt): khi một vấn đề có nhiều góc nhìn, Orchestrator cho các **vai phản biện** viết lập trường độc lập rồi phản biện nhau, sau đó trình PO bảng tổng hợp. Vai phản biện không cần là bộ phận đã lập (danh mục vai: `../ORGANIZATION.md` §7.4). PO vẫn chốt.
- **Delegation**: bộ phận đã lập debate, Chủ toạ phán quyết.

| Vòng | Ai | Đầu ra |
|---|---|---|
| R1 Lập trường | Mỗi vai hoặc bộ phận, độc lập, không đọc lập trường của bên khác | `Wxx/debate/r1-<mã>.md` |
| R2 Phản biện | Mỗi bên, sau khi đọc **mọi** file R1 | `Wxx/debate/r2-<mã>.md` |
| R3 Kết luận | Tham vấn: Orchestrator tổng hợp trình PO. Delegation: Chủ toạ phán quyết theo `../ORGANIZATION.md` §7.2 | Cột **PO chốt** (delegation ghi `Delegation: …`), ý kiến thiểu số |
| R4 Kháng nghị (delegation) | Bộ phận thấy phán quyết gây hại nghiêm trọng cho lĩnh vực của mình | `Wxx/debate/r4-<mã>.md` |
| R5 Giải quyết kháng nghị | Chủ toạ | Nhật ký `1-discussion.md` |

Chỉ điền những bảng thật sự dùng; bảng tổng hợp §1 của `1-discussion.md` luôn phải đủ. PO lật lại được mọi phán quyết. Việc ngoài phạm vi delegation vẫn dừng và hỏi PO.

## 5. Hotfix (ngoài wave)

Lỗi làm người dùng **không dùng được** sản phẩm (không vào được, mất dữ liệu, crash lặp lại) thì sửa ngay, không chờ wave.

| Bước | Việc |
|---|---|
| 1 | Báo PO một dòng: lỗi gì, ảnh hưởng ai |
| 2 | Sửa nhỏ nhất có thể trên nhánh hotfix, kèm test tái hiện lỗi |
| 3 | Backup, triển khai, kiểm trước và sau theo `../03_release/README.md` |
| 4 | Ghi dòng `HOTFIX-nn` vào `WAVES.md` §2, commit |

Lỗi không chặn người dùng thì ghi backlog, xếp vào wave sau.

## 6. Bắt đầu nhanh

| Muốn biết | Mở |
|---|---|
| Wave nào đang chạy, tới bước nào | `WAVES.md` hoặc tool `status` |
| Wave này cần PO trả lời gì | `Wxx/1-discussion.md`, các dòng "Chờ" |
| Wave này làm gì, khi nào tính là xong | `Wxx/2-scope.md` |
| Việc đang chờ xếp wave | `BACKLOG.md` |
| Hồ sơ có lệch không | Tool `check` |
