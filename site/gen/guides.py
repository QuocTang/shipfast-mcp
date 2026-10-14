"""Nội dung trang chi tiết theo câu hỏi của người đọc, khoá theo slug của PROCESSES.

Mỗi mục: when (khi nào dùng), human [(việc, câu mẫu gửi AI hoặc "")], ai [(AI làm, người kiểm tra)],
example (tuỳ chọn, cùng định dạng terminal(); thiếu thì dùng example của PROCESSES).
"""

GUIDES = {
    "w01-khoi-tao": {
        "when": "Dự án mới, repo trống hoặc gần trống. Thực hiện một lần, trước mọi wave khác.",
        "human": [
            ("Mô tả sản phẩm: ai dùng, giải quyết việc gì, bản đầu cần những gì.",
             "Bắt đầu dự án: app quản lý kho cho cửa hàng nhỏ, hai vai chủ cửa hàng và nhân viên."),
            ("Duyệt danh sách file khung trước khi AI ghi vào repo.", ""),
            ("Chọn stack và danh sách bộ phận trong các phương án AI trình.", "W01-02: A, còn lại theo đề xuất. Chốt."),
            ("Duyệt các việc tạo tài nguyên: database, migration, dependency có phí.", ""),
            ("Nói \"chốt\" ở Scope lock và nghiệm thu W01.", ""),
        ],
        "ai": [
            ("Dựng khung tài liệu, mở W01 với các vấn đề W01-01 tới W01-09.", "Danh sách file đúng với bản đã duyệt."),
            ("Tra tài liệu chính thức, trình 2–3 phương án stack kèm phản biện.", "Mỗi phương án có nguồn và rủi ro."),
            ("Đề xuất 3–5 bộ phận theo sản phẩm, lập hồ sơ và subagent sau khi chốt.", "Mỗi bộ phận có vùng sở hữu, không chồng nhau."),
            ("Dựng khung code bằng công cụ chính thức của stack, chạy thật mọi lệnh chuẩn.", "Lint, test, build xanh trên máy."),
        ],
    },
    "intake": {
        "when": "Có yêu cầu mới từ PO, hoặc backlog có việc cần đưa vào làm. Wave trước đã đóng hoặc không chặn việc mới.",
        "human": [
            ("Nêu yêu cầu cho Orchestrator: việc cần làm, lý do, giới hạn đã biết, mã backlog liên quan.",
             "Mở wave mới: thêm xuất báo cáo tồn kho ra Excel, lấy thêm BL-004 và BL-007 trong backlog."),
            ("Chọn chế độ chốt nếu khác mặc định: chốt thẳng cho việc nhỏ đã rõ, hoặc giao quyền cho các bộ phận.", ""),
            ("Đọc danh sách vấn đề AI trả về, bổ sung vấn đề còn thiếu.", ""),
        ],
        "ai": [
            ("Mở hồ sơ wave Wxx: thẻ wave và file thảo luận.", "Thẻ wave ghi đúng mục tiêu và chế độ chốt."),
            ("Tách yêu cầu thành các vấn đề Wxx-nn, mỗi vấn đề có bối cảnh, phương án, đề xuất và rủi ro.", "Vấn đề có lựa chọn thật thì có ít nhất hai phương án."),
            ("Giao bộ phận liên quan khảo sát chỉ đọc khi thiếu dữ kiện.", "Dữ kiện ghi ngày và nguồn, nằm trong research/."),
        ],
        "example": [
            ["user", "Mở wave mới: thêm xuất báo cáo tồn kho ra Excel, lấy thêm BL-004 và BL-007 trong backlog."],
            ["ai", "Đã mở W04, chế độ PO chốt. Ba vấn đề: W04-01 định dạng xuất, CSV hoặc XLSX, đề xuất XLSX, rủi ro là thêm thư viện. W04-02 quyền xuất, đề xuất chỉ chủ cửa hàng. W04-03 BL-007 làm trong wave này hay để sau, đề xuất để sau vì phụ thuộc W04-01. Bộ phận PLATFORM đang khảo sát thư viện xuất file."],
            ["user", "Thêm vấn đề: giới hạn số dòng mỗi lần xuất."],
            ["ai", "Đã thêm W04-04. Chương trình thảo luận gồm bốn vấn đề, sẵn sàng sang Discussion."],
        ],
    },
    "discussion": {
        "when": "Intake đã xong, PO đã nhận chương trình thảo luận. Còn vấn đề ở trạng thái Chờ.",
        "human": [
            ("Đọc từng vấn đề: đề xuất đứng đầu, sau đó là phương án khác và phản biện.", ""),
            ("Trả lời theo mã: chọn phương án, Làm, Không làm hoặc Hoãn.", "W04-01: XLSX. Đồng ý các vấn đề còn lại trừ W04-03, hoãn W04-03."),
            ("Khi chọn khác đề xuất, đọc hệ quả AI nêu rồi xác nhận lại.", ""),
        ],
        "ai": [
            ("Lấy ý kiến bộ phận liên quan trước khi trình.", "Mỗi vấn đề ghi bộ phận đã cho ý kiến."),
            ("Trình gộp nhiều vấn đề, gọi đối tượng bằng tên, mã để trong ngoặc.", "Câu hỏi đọc hiểu được mà không cần tra mã."),
            ("Nêu rủi ro và hệ quả khi PO chọn khác đề xuất; chạy debate khi vấn đề có nhiều góc nhìn.", "Chỉ ghi chốt sau khi PO xác nhận."),
            ("Ghi nhật ký từng lượt; vấn đề Hoãn trả về backlog.", "Vấn đề Hoãn có mã backlog."),
        ],
    },
    "scope-lock": {
        "when": "Discussion đã xong, không còn vấn đề ở trạng thái Chờ. Chưa có dòng code nào của wave được viết.",
        "human": [
            ("Đọc bảng tóm tắt phạm vi: hạng mục, bộ phận phụ trách, tiêu chí đo được.", ""),
            ("Duyệt khung giao diện nếu wave có màn hình mới.", ""),
            ("Nói \"chốt\" để đóng băng phạm vi.", "Chốt."),
            ("Mở phiên mới cho bước Build khi AI đề nghị.", ""),
        ],
        "ai": [
            ("Viết 2-scope.md: mỗi hạng mục có bộ phận, vùng thư mục, tiêu chí đo được.", "Tiêu chí kiểm được bằng lệnh hoặc thao tác cụ thể."),
            ("Chia build team khi chạy song song, ghi vùng được sửa và không được sửa.", "Các vùng không chồng nhau."),
            ("Ghi quyết định mới vào decision log, contract mới vào CONTRACTS.md.", "Mỗi quyết định có mã D-nnn."),
        ],
    },
    "build": {
        "when": "Scope lock đã chốt. Mở phiên mới cho bước này.",
        "human": [
            ("Yêu cầu AI bắt đầu build theo phạm vi đã chốt.", "Build W04 theo 2-scope.md."),
            ("Duyệt CR khi AI đề nghị đổi phạm vi.", "CR-W04-01: đồng ý."),
            ("Trả lời câu hỏi thiết kế chưa có trong tài liệu.", ""),
        ],
        "ai": [
            ("Orchestrator giao từng hạng mục cho subagent của bộ phận phụ trách, theo lô.", "Lời giao việc có mục tiêu, tiêu chí, vùng được sửa, lệnh kiểm."),
            ("Bộ phận build hạng mục trong vùng của mình, chạy lệnh kiểm.", "Không sửa ngoài vùng đã giao."),
            ("Ghi việc mới phát hiện vào backlog; đổi phạm vi thì mở CR-Wxx-nn.", "Không có việc ngoài phạm vi được làm khi chưa duyệt."),
            ("Chạy quality gate, quét secret, commit checkpoint.", "Quality gate xanh, đã chạy thật."),
        ],
    },
    "cleanup": {
        "when": "Build xong, quality gate xanh. Trước Acceptance.",
        "human": [
            ("Yêu cầu AI dọn theo danh sách kiểm.", "Cleanup W04."),
            ("Duyệt xoá file nằm ngoài danh sách được phép.", ""),
        ],
        "ai": [
            ("Quét chỉ đọc: mã không còn được gọi, tài liệu lệch, file tạm.", "Mỗi mục có vị trí và lý do."),
            ("Chủ vùng xoá mục trong vùng của mình, người dọn kiểm lại.", "Trong tmp/ chỉ xoá theo mẫu tên được phép."),
            ("Việc đổi hành vi chạy (route, migration, cấu hình, phụ thuộc) ghi backlog.", "Bước này không đổi hành vi của hệ thống."),
            ("Chạy lại quality gate.", "Quality gate vẫn xanh."),
        ],
    },
    "acceptance": {
        "when": "Cleanup xong. Wave cần được kiểm theo tiêu chí trước khi phát hành.",
        "human": [
            ("Yêu cầu AI nghiệm thu theo tiêu chí trong 2-scope.md.", "Acceptance W04."),
            ("Duyệt các quyết định đang ở trạng thái Giả định.", "D-014: đồng ý, chuyển Hiệu lực."),
            ("Chấp nhận hoặc từ chối ngoại lệ khi có tiêu chí chưa đạt.", ""),
        ],
        "ai": [
            ("Gọi bộ phận QA, hoặc subagent khác bộ phận đã build.", "Người kiểm không phải người đã build."),
            ("Chạy lại quality gate và kịch bản đầu cuối, ghi bằng chứng cho từng tiêu chí.", "Mỗi tiêu chí có bằng chứng: output lệnh, ảnh chụp, log."),
            ("Sửa lỗi QAxx-n rồi kiểm lại.", "Lỗi đã sửa có bằng chứng kiểm lại."),
        ],
    },
    "release": {
        "when": "Acceptance đạt hoặc PO đã chấp nhận ngoại lệ.",
        "human": [
            ("Yêu cầu AI phát hành và đóng wave.", "Release và đóng W04."),
            ("Đọc rút kinh nghiệm, đồng ý hoặc bỏ các đề xuất đổi cách làm.", ""),
            ("Chọn wave kế tiếp trong các đề xuất.", ""),
        ],
        "ai": [
            ("Phát hành theo docs/03_release/README.md: kiểm trước, backup, triển khai, kiểm sau.", "Kiểm sau triển khai đạt."),
            ("Viết rút kinh nghiệm; đổi cách làm được PO đồng ý thì ghi QT-nnn.", "Mỗi đề xuất có lý do từ sự việc trong wave."),
            ("Trả việc dở về backlog, cập nhật README wave, WAVES.md, BACKLOG.md.", "Tool check không báo lỗi cho wave."),
            ("Đề xuất wave kế tiếp từ backlog.", ""),
        ],
    },
    "hotfix": {
        "when": "Lỗi làm người dùng không dùng được sản phẩm: không vào được, mất dữ liệu, lỗi lặp lại. Không chờ wave.",
        "human": [
            ("Báo lỗi cho AI: hiện tượng, ai bị ảnh hưởng, từ lúc nào.", "Hotfix: nhân viên không đăng nhập được từ 9 giờ sáng nay."),
            ("Đồng ý sửa ngay khi AI xác nhận phạm vi lỗi.", ""),
        ],
        "ai": [
            ("Báo PO một dòng: lỗi gì, ảnh hưởng ai.", ""),
            ("Sửa nhỏ nhất có thể trên nhánh hotfix, kèm test tái hiện lỗi.", "Test tái hiện lỗi đỏ trước khi sửa, xanh sau khi sửa."),
            ("Backup, triển khai, kiểm trước và sau.", "Kiểm sau triển khai đạt."),
            ("Ghi HOTFIX-nn vào WAVES.md, commit.", ""),
        ],
    },
    "viec-po-giao": {
        "when": "Việc nhỏ, đã rõ, cần làm ngay mà không cần thảo luận. Việc lớn thì mở wave.",
        "human": [
            ("Giao việc trực tiếp cho Orchestrator.", "Việc PO: đổi nhãn nút Lưu thành Lưu phiếu ở màn hình nhập kho."),
        ],
        "ai": [
            ("Ghi dòng PO-nn trước khi làm.", ""),
            ("Làm, ghi kết quả, commit.", "Dòng PO-nn có kết quả và commit."),
            ("Đề nghị mở wave nếu việc lớn hơn dự kiến.", ""),
        ],
    },
    "to-chuc": {
        "when": "Khi lập bộ phận ở W01, khi dự án có lĩnh vực mới, hoặc khi cần biết việc nào giao cho ai.",
        "human": [
            ("Duyệt danh sách bộ phận và vùng sở hữu ở W01-09.", ""),
            ("Duyệt lập thêm bộ phận khi AI đề xuất.", "Đồng ý lập bộ phận BILLING."),
        ],
        "ai": [
            ("Đề xuất 3–5 bộ phận theo đặc thù sản phẩm, lập hồ sơ và subagent.", "Mỗi bộ phận có lĩnh vực và vùng sở hữu rõ."),
            ("Giao việc theo lĩnh vực; việc chạm nhiều lĩnh vực thì mỗi bộ phận nhận phần của mình.", "Orchestrator không tự làm việc của bộ phận."),
            ("Lập build team theo wave khi chạy song song; QA độc lập với bộ phận đã build.", ""),
        ],
    },
    "debate": {
        "when": "Vấn đề có nhiều phương án ngang nhau hoặc rủi ro cao; hoặc PO giao quyền chốt cho các bộ phận.",
        "human": [
            ("Yêu cầu debate cho vấn đề cần nhiều góc nhìn.", "Debate W04-01."),
            ("Tham vấn: đọc bảng tổng hợp rồi chốt.", ""),
            ("Delegation: giao quyền chốt; có thể lật lại phán quyết.", "W05 delegation, Chủ toạ là PLATFORM."),
        ],
        "ai": [
            ("Chọn 2–4 bên: bộ phận liên quan, thêm vai phản biện cho góc nhìn còn thiếu.", ""),
            ("R1: mỗi bên viết lập trường độc lập. R2: đọc lập trường các bên rồi phản biện.", "Mỗi lập trường có căn cứ và điều kiện để đổi ý."),
            ("R3: Orchestrator tổng hợp trình PO, hoặc Chủ toạ phán quyết theo tiêu chí.", "Bảng tổng hợp nêu điểm đồng thuận và điểm còn khác."),
        ],
    },
    "decision-log": {
        "when": "Mỗi khi có quyết định cần giữ lại: chọn phương án, đổi luật, đặt tạm khi PO chưa trả lời.",
        "human": [
            ("Chốt quyết định, chuyển Giả định thành Hiệu lực ở Acceptance.", "D-014: đồng ý."),
        ],
        "ai": [
            ("Ghi quyết định theo mẫu, cấp mã, cập nhật mục lục.", "Mã không trùng."),
            ("Quyết định bị thay: đổi trạng thái thành \"Bị thay thế bởi <mã>\" trong file cũ, không xoá.", ""),
            ("Code và tài liệu chỉ dẫn mã, không chép lại nội dung.", "Mỗi thông tin chỉ nằm ở một chỗ."),
        ],
    },
    "ngan-sach-ngu-canh": {
        "when": "Áp dụng ở mọi bước, đặc biệt khi phiên điều phối dài hoặc chi phí token tăng.",
        "human": [
            ("Mở phiên mới khi AI đề nghị lúc chuyển bước.", ""),
        ],
        "ai": [
            ("Orchestrator giao khảo sát và build cho subagent, nhận báo cáo ngắn.", "Phiên điều phối không đọc nhiều file hay viết code dài."),
            ("Giao theo lô, chờ cả lô xong rồi tổng hợp.", ""),
            ("Tìm code theo symbol, đọc file theo đoạn, in output gọn, sửa theo đoạn.", ""),
            ("Ghi hồ sơ khi chuyển bước rồi đề nghị mở phiên mới.", "Phiên mới đọc hồ sơ là tiếp tục được."),
        ],
    },
    "nang-cap": {
        "when": "Khung có phiên bản mới, dự án muốn nhận luật mới mà không mất phần đã sửa.",
        "human": [
            ("Yêu cầu nâng cấp khung.", "Nâng cấp khung shipfast."),
            ("Duyệt danh sách thay đổi: cập nhật thẳng, gộp tự động, xung đột.", ""),
            ("Chọn cách hợp nhất ở chỗ xung đột.", ""),
        ],
        "ai": [
            ("Dry run, trình danh sách thay đổi.", "Bảng wave, backlog, decision log không nằm trong danh sách."),
            ("File chưa sửa thì thay bản mới; hai bên sửa khác chỗ thì gộp ba phía.", ""),
            ("Sửa cùng chỗ: giữ file thật, đặt bản gộp có dấu xung đột để duyệt.", "Không file nào bị ghi đè khi có xung đột."),
            ("Làm mới subagent bộ phận theo mẫu mới.", "Tool check sạch."),
        ],
    },
}
