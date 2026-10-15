"""Nội dung của trang tài liệu shipfast: tổng quan và trang chi tiết từng quy trình.

Mỗi quy trình là một dict với các khoá cố định; build.py dựng thành trang `<slug>.html`.
"""

SITE = {
    "title": "shipfast",
    "headline": "Mô hình làm việc theo wave",
    "lead": "Quy trình làm dự án phần mềm cùng AI: người quyết định làm gì và duyệt kết quả, AI làm phần còn lại theo từng wave có phạm vi chốt trước và có bằng chứng kiểm tra.",
    "entries": [
        ("Tìm hiểu mô hình", "Ba vai và cách phân việc", "#mo-hinh"),
        ("Bắt đầu dự án mới", "Khởi tạo dự án (W01)", "w01-khoi-tao.html"),
        ("Áp dụng cho dự án đang chạy", "Cài shipfast-mcp, gọi prompt adopt", "ap-dung.html"),
        ("Làm một wave", "7 bước từ Intake tới Release", "#quy-trinh"),
    ],
    "repo": "https://github.com/QuocTang/shipfast-mcp",
    "pypi": "https://pypi.org/project/shipfast-mcp/",
}

ROLES = [
    ("PO", "Người dùng", "Quyết định phạm vi, chốt từng vấn đề, duyệt và nghiệm thu."),
    ("Orchestrator", "Phiên AI chính", "Đề xuất, phản biện, giữ hồ sơ, giao việc cho bộ phận, tích hợp. Điều phối, không thi công."),
    ("Bộ phận", "Subagent theo lĩnh vực", "Lập theo dự án từ W01. Nhận mọi việc thuộc lĩnh vực của mình: ý kiến chuyên môn, khảo sát, build, kiểm thử. Có model, mức suy nghĩ mặc định và kỷ luật riêng."),
]

GROUPS = [
    ("khoi-tao", "Khởi tạo", "Thực hiện một lần khi bắt đầu dự án."),
    ("wave", "Vòng đời một wave", "Mọi thay đổi code đi qua 7 bước theo thứ tự. Code chỉ được viết sau bước Scope lock."),
    ("ngoai-wave", "Ngoài wave", "Việc xử lý ngay, không chờ wave, vẫn lưu vết trong hồ sơ."),
    ("xuyen-suot", "Xuyên suốt", "Cơ chế áp dụng ở mọi bước."),
]

PO, ORC, DEPT = "PO", "Orchestrator", "Bộ phận"

PROCESSES = [
    # ---------------------------------------------------------------- Khởi tạo
    {
        "slug": "w01-khoi-tao", "brief": "Chốt sản phẩm, stack, bộ phận; dựng khung", "group": "khoi-tao", "code": "W01", "name": "Khởi tạo dự án",
        "goal": "Chốt sản phẩm, stack và tổ chức bộ phận; dựng khung tài liệu và khung code chạy được.",
        "outputs": [("CLAUDE.md, docs/", "Khung quy trình: wave, backlog, decision log, tổ chức"),
                    ("docs/04_waves/W01/", "Hồ sơ wave khởi tạo"),
                    ("SP-001, KT-001, QT-002", "Phạm vi bản đầu, stack, quyết định lập bộ phận"),
                    ("docs/departments/, .claude/agents/", "Hồ sơ và subagent của từng bộ phận")],
        "gate": "Khung code chạy được; lint, test, build xanh; mọi vấn đề W01 đã chốt.",
        "cases": [
            ("Repo đã có code đáng kể", "Không chạy W01; áp quy trình theo trang Áp dụng (dự án đang chạy)."),
            ("PO chưa chắc về stack", "Debate tham vấn với các vai kiến trúc, vận hành, an toàn; trình bảng tổng hợp."),
            ("Tạo DB, migration, dependency có phí", "Chờ PO duyệt trước khi làm."),
        ],
        "example": [
            ("user", "Bắt đầu dự án: app quản lý kho cho cửa hàng nhỏ, hai vai chủ cửa hàng và nhân viên."),
            ("ai", "W01-01: nhập xuất kho, cảnh báo sắp hết, báo cáo tồn; in hoá đơn để sau (BL-005). W01-02 stack: đề xuất A, phản biện: cần thêm runtime khi có job nền. W01-09: lập ba bộ phận PRODUCT, PLATFORM, TRUST."),
            ("user", "W01-02: A, còn lại theo đề xuất. Chốt."),
        ],
        "tools": [("scaffold_project", "Dựng khung tài liệu và skill, không ghi đè"), ("create_department", "Lập bộ phận"), ("new_decision", "Ghi SP, KT, QT")],
    },
    # ---------------------------------------------------------------- Wave
    {
        "slug": "intake", "brief": "Gom việc thành vấn đề cần chốt", "group": "wave", "code": "1", "name": "Intake",
        "goal": "Gom việc thành danh sách vấn đề cần chốt, mỗi vấn đề có phương án và đề xuất.",
        "outputs": [("Wxx/README.md", "Thẻ wave: chủ trì, chế độ chốt, mục tiêu, trạng thái"),
                    ("Wxx/1-discussion.md", "Bản đầu danh sách vấn đề Wxx-nn"),
                    ("Wxx/research/", "Dữ kiện khảo sát chỉ đọc, ghi ngày và nguồn")],
        "gate": "PO đã nhận chương trình thảo luận.",
        "cases": [
            ("Lĩnh vực mới chưa có bộ phận", "Thêm một vấn đề đề xuất lập bộ phận."),
            ("Việc nhỏ, yêu cầu đã rõ", "Chọn chế độ chốt thẳng; ghi lý do trong README wave."),
        ],
        "tools": [("open_wave", "Tạo hồ sơ wave từ mẫu, thêm dòng vào bảng wave"), ("next_code", "Cấp mã Wxx-nn không trùng")],
    },
    {
        "slug": "discussion", "brief": "Chốt từng vấn đề sau phản biện", "group": "wave", "code": "2", "name": "Discussion",
        "goal": "Mọi vấn đề của wave có kết luận Làm, Không làm hoặc Hoãn, sau khi đã được đề xuất và phản biện.",
        "outputs": [("Wxx/1-discussion.md", "Cột PO chốt điền đủ; nhật ký trao đổi"),
                    ("Wxx/debate/", "Lập trường R1, phản biện R2 khi có debate")],
        "gate": "Không còn vấn đề ở trạng thái Chờ.",
        "sections": [
            ("Ba chế độ chốt", "table", [("Chế độ", "Khi nào", "Cách chạy"),
                ("PO chốt", "Mặc định", "Orchestrator trình từng vấn đề, PO chốt"),
                ("Chốt thẳng", "Wave nhỏ, yêu cầu đã rõ", "Ghi lý do; chỉ cần bảng tổng hợp; PO duyệt phạm vi như thường"),
                ("Delegation", "PO muốn giảm số lần chốt, đã có từ hai bộ phận", "PO ghi QT-nnn: phạm vi, việc PO giữ lại, tiêu chí Chủ toạ; bộ phận debate, Chủ toạ chốt")]),
        ],
        "cases": [
            ("Cần số liệu mới quyết được", "Bộ phận khảo sát chỉ đọc, ghi research/, mang kết quả về thảo luận tiếp."),
            ("PO lật lại một kết luận", "Ghi nhật ký; nếu wave đang build thì mở CR."),
            ("Câu hỏi gửi PO dùng toàn mã", "Viết lại bằng tên đối tượng kèm trạng thái hiện tại; mã để sau trong ngoặc."),
        ],
        "example": [
            ("ai", "W02-01 đăng nhập: đề xuất A (email và mật khẩu). Phản biện: chưa có quên mật khẩu, cần gửi email. W02-02 phân quyền: đề xuất hai vai cố định; TRUST lưu ý kiểm quyền ở API, không chỉ ẩn nút."),
            ("user", "W02-01: B (đăng nhập bằng tài khoản Google). W02-02 theo đề xuất."),
            ("ai", "W02-01 chọn B: hệ quả là cửa hàng cần tài khoản Google cho nhân viên. Xác nhận chốt B?"),
            ("user", "Xác nhận."),
        ],
        "tools": [("next_code", "Cấp mã vấn đề mới khi phát sinh"), ("new_decision", "Ghi quyết định ảnh hưởng ngoài wave")],
        "related": ["debate"],
    },
    {
        "slug": "scope-lock", "brief": "Đóng băng phạm vi và tiêu chí", "group": "wave", "code": "3", "name": "Scope lock",
        "goal": "Đóng băng phạm vi: hạng mục, tiêu chí đo được, bộ phận phụ trách, quality gate.",
        "outputs": [("Wxx/2-scope.md", "Hạng mục Wxx-Pnn, tiêu chí, vùng sở hữu, quality gate, ngoài phạm vi, rủi ro"),
                    ("docs/05_decisions/", "Quyết định mới SP, KT, QT"),
                    ("docs/02_build/CONTRACTS.md", "Contract mới giữa các phần")],
        "gate": "PO nói \"chốt\" (delegation: Chủ toạ chốt và báo PO); ngày chốt ghi vào README wave và WAVES.md.",
        "cases": [
            ("Hạng mục có giao diện mới", "Chỉ vào build khi PO đã duyệt khung (trang demo hoặc file thiết kế)."),
            ("Tiêu chí không đo được", "Viết lại thành điều kiện kiểm được bằng lệnh hoặc kịch bản."),
        ],
        "tools": [("new_decision", "Ghi quyết định đi kèm phạm vi")],
    },
    {
        "slug": "build", "brief": "Bộ phận thi công tới khi gate xanh", "group": "wave", "code": "4", "name": "Build",
        "goal": "Các bộ phận thi công từng hạng mục tới khi quality gate của wave xanh.",
        "outputs": [("Wxx/3-build.md", "Trạng thái hạng mục, quyết định nhỏ Q-Wxx-nn, CR, lượt chạy, commit")],
        "gate": "Quality gate của wave xanh và đã chạy thật ít nhất một lần.",
        "sections": [
            ("Mẫu lời giao việc", "code", "Việc: Wxx-Pnn <tên hạng mục>\nTiêu chí: <tiêu chí đo được, chép từ 2-scope.md>\nVùng được sửa: <thư mục, file>\nĐọc trước: <file:đoạn cần đọc>\nKiểm: <lệnh quality gate của hạng mục>\nBáo cáo: tối đa 30 dòng"),
        ],
        "cases": [
            ("Hạng mục lớn hơn khoảng 60 lượt gọi tool", "Chia nhỏ trước khi giao."),
            ("Câu hỏi thiết kế chưa có tài liệu", "Dừng hạng mục đó, hỏi PO; các hạng mục khác vẫn chạy."),
            ("Subagent bị treo", "Chạy lại từ bước dở theo 3-build.md."),
        ],
        "example": [
            ("ai", "Giao lô 1: W04-P01 cho PLATFORM (API xuất báo cáo tồn kho), W04-P02 cho UX (nút xuất trên màn báo cáo). Chờ cả lô."),
            ("tool", "dept-platform", "W04-P01", "Xong: 4 file sửa, test 12/12 xanh"),
            ("tool", "dept-ux", "W04-P02", "Xong: 3 file sửa, typecheck sạch"),
            ("ai", "Lô 1 xong. Quality gate xanh. Ghi 3-build.md, commit checkpoint."),
        ],
        "tools": [("status", "Xem hạng mục còn lại")],
    },
    {
        "slug": "cleanup", "brief": "Dọn mã chết, tài liệu lệch", "group": "wave", "code": "5", "name": "Cleanup",
        "goal": "Dọn mã không còn được gọi, tài liệu lệch, file tạm, trong ranh giới an toàn.",
        "outputs": [("Wxx/4-cleanup.md", "Mục dọn CL-Wxx-nn, file đã xoá trong tmp/, việc chuyển backlog")],
        "gate": "Mọi mục đã xử lý hoặc có lý do và mã backlog; quality gate xanh.",
        "cases": [("Gặp file trong danh sách cấm xoá", "Không mở, không xoá; báo PO.")],
        "tools": [("check", "Hồ sơ lệch, link gãy, trạng thái lệch")],
    },
    {
        "slug": "acceptance", "brief": "Kiểm độc lập từng tiêu chí", "group": "wave", "code": "6", "name": "Acceptance",
        "goal": "Kiểm từng tiêu chí bằng bằng chứng, do người kiểm độc lập với bộ phận đã build.",
        "outputs": [("Wxx/5-acceptance.md", "Kết quả theo tiêu chí, lỗi QAxx-n, giả định chờ PO")],
        "gate": "Mọi tiêu chí đạt, hoặc PO chấp nhận ngoại lệ.",
        "cases": [("Một tiêu chí không đạt nhưng PO vẫn muốn phát hành", "Ghi ngoại lệ được PO chấp nhận, đưa phần thiếu vào backlog.")],
        "tools": [("check", "Kiểm hồ sơ trước khi trình")],
    },
    {
        "slug": "release", "brief": "Phát hành, rút kinh nghiệm, đóng wave", "group": "wave", "code": "7", "name": "Release và đóng",
        "goal": "Phát hành, rút kinh nghiệm, trả việc dở về backlog và đóng wave.",
        "outputs": [("docs/03_release/RELEASE-NOTES.md", "Ghi chú phát hành"),
                    ("Wxx/5-acceptance.md §6", "Rút kinh nghiệm: tốt, chưa tốt, đổi cách làm"),
                    ("README wave, WAVES.md", "Trạng thái Closed, phiên bản, commit")],
        "gate": "Tool check không báo lỗi cho wave này.",
        "cases": [("Chỉ một agent thao tác môi trường thật mỗi lúc", "Xếp thứ tự, không chạy song song lệnh triển khai.")],
        "tools": [("check", "Xác nhận hồ sơ sạch trước khi đóng")],
    },
    # ---------------------------------------------------------------- Ngoài wave
    {
        "slug": "hotfix", "brief": "Sửa ngay lỗi chặn người dùng", "group": "ngoai-wave", "code": "HOTFIX", "name": "Hotfix",
        "goal": "Sửa ngay lỗi làm người dùng không dùng được sản phẩm, không chờ wave.",
        "outputs": [("WAVES.md §2", "Dòng HOTFIX-nn")],
        "gate": "Kiểm sau triển khai đạt.",
        "cases": [("Lỗi không chặn người dùng", "Ghi backlog, xếp vào wave sau.")],
        "tools": [("next_code", "Cấp mã HOTFIX-nn")],
    },
    {
        "slug": "viec-po-giao", "brief": "Việc nhỏ làm ngay, vẫn ghi hồ sơ", "group": "ngoai-wave", "code": "PO-nn", "name": "Việc PO giao trực tiếp",
        "goal": "Làm việc nhỏ PO yêu cầu ngay mà vẫn để lại dấu vết trong hồ sơ.",
        "outputs": [("WAVES.md §2", "Dòng PO-nn: việc, lý do không qua wave, kết quả")],
        "gate": "Kết quả và commit đã ghi.",
        "cases": [],
        "tools": [("next_code", "Cấp mã PO-nn")],
    },
    # ---------------------------------------------------------------- Xuyên suốt
    {
        "slug": "to-chuc", "brief": "Ai quyết, ai điều phối, ai làm", "group": "xuyen-suot", "code": "ORG", "name": "Tổ chức và vai trò",
        "goal": "Ai quyết, ai điều phối, ai làm; bộ phận lập theo dự án, Orchestrator chỉ điều phối.",
        "outputs": [("docs/ORGANIZATION.md", "Bộ phận, vùng sở hữu, build team, delegation, ranh giới an toàn"),
                                   ("docs/departments/<mã>/", "Hồ sơ bộ phận: quy chế, chuẩn, sổ sách, nghiên cứu"),
                                   (".claude/agents/dept-<mã>.md", "Subagent của bộ phận")],
        "gate": "",
        "sections": [
            ("Orchestrator tự làm và việc phải giao", "table", [("Orchestrator tự làm", "Giao bộ phận"),
                ("Làm việc với PO: mở wave, trình vấn đề, báo kết quả", "Ý kiến chuyên môn cho từng vấn đề"),
                ("Cập nhật hồ sơ quy trình", "Khảo sát, đọc nhiều file, tra tài liệu ngoài"),
                ("Tổng hợp kết quả, phán quyết khi delegation", "Viết code, test, tài liệu chuyên môn"),
                ("Chạy quality gate cuối, quét secret, commit", "Cleanup, acceptance, triển khai")]),
            ("Danh mục bộ phận gợi ý", "table", [("Mã", "Lĩnh vực", "Nên lập khi"),
                ("PRODUCT", "Nghiệp vụ, yêu cầu, phạm vi", "Sản phẩm có nghiệp vụ riêng"),
                ("UX", "Giao diện, luồng, nguyên tắc thiết kế", "Có giao diện người dùng"),
                ("PLATFORM", "Code chính, kiến trúc, dữ liệu, contract", "Có code"),
                ("TRUST", "Bảo mật, quyền, riêng tư", "Có dữ liệu người dùng, phân quyền"),
                ("QA", "Kịch bản kiểm thử, acceptance độc lập", "Nhiều luồng cần kiểm lại mỗi wave"),
                ("OPS", "Triển khai, vận hành, backup", "Có môi trường thật")]),
        ],
        "cases": [("Không bộ phận nào làm được và việc gấp", "Orchestrator làm, ghi \"Orchestrator (thay <mã>)\", đề xuất lập bộ phận.")],
        "tools": [("create_department", "Lập bộ phận"), ("refresh_departments", "Làm mới subagent theo mẫu mới")],
    },
    {
        "slug": "debate", "brief": "Phản biện nhiều phía trước khi chốt", "group": "xuyen-suot", "code": "R1–R5", "name": "Debate và delegation",
        "goal": "Nhìn một vấn đề từ nhiều phía trước khi chốt; khi PO giao quyền, các bộ phận tranh luận và Chủ toạ chốt.",
        "outputs": [("Wxx/debate/r1-<mã>.md", "Lập trường độc lập"), ("Wxx/debate/r2-<mã>.md", "Phản biện sau khi đọc mọi R1")],
        "gate": "",
        "sections": [
            ("Vai phản biện", "table", [("Mã", "Hỏi gì"),
                ("USER", "Dùng có dễ, có đúng việc người dùng cần"),
                ("PROD", "Có trả lời đúng yêu cầu PO, phạm vi có vừa wave"),
                ("ARCH", "Đơn giản nhất chạy được là gì, nợ kỹ thuật"),
                ("TRUST", "Dữ liệu, bí mật, quyền, rủi ro không đảo ngược (có quyền phủ quyết)"),
                ("OPS", "Triển khai, quan sát, backup, chi phí"),
                ("QA", "Kiểm chứng bằng cách nào"),
                ("DEVIL", "Lý do mạnh nhất để không làm hoặc làm khác")]),
        ],
        "cases": [("Một phương án bỏ yêu cầu PO đã nêu", "Không được chấp nhận; việc lớn thì đề xuất chia wave.")],
        "tools": [],
    },
    {
        "slug": "decision-log", "brief": "Mỗi thông tin một chỗ, nơi khác dẫn mã", "group": "xuyen-suot", "code": "SP · KT · QT", "name": "Decision log và hệ mã",
        "goal": "Mỗi thông tin chỉ sống ở một chỗ; nơi khác dẫn mã.",
        "outputs": [("docs/05_decisions/", "Mỗi quyết định một file, README là mục lục"),
                                   ("docs/04_waves/BACKLOG.md", "Việc chưa xếp wave"),
                                   ("docs/04_waves/WAVES.md", "Bảng wave, việc ngoài wave")],
        "gate": "",
        "sections": [
            ("Hệ mã", "table", [("Mã", "Là gì", "Ghi ở"),
                ("BL-nnn", "Việc chưa xếp wave", "BACKLOG.md"),
                ("Wxx-nn", "Vấn đề trong wave", "Wxx/1-discussion.md"),
                ("Wxx-Pnn", "Hạng mục build", "Wxx/2-scope.md"),
                ("CR-Wxx-nn", "Đổi phạm vi khi đang build", "Wxx/3-build.md"),
                ("QAxx-n", "Lỗi tìm thấy khi acceptance", "Wxx/5-acceptance.md"),
                ("SP / KT / QT-nnn", "Quyết định sản phẩm / kỹ thuật / quy trình", "docs/05_decisions/"),
                ("PO-nn, OPS-nn, HOTFIX-nn", "Việc ngoài wave", "WAVES.md §2")]),
        ],
        "cases": [],
        "tools": [("new_decision", "Ghi quyết định, cập nhật mục lục"), ("next_code", "Cấp mã không trùng")],
    },
    {
        "slug": "ngan-sach-ngu-canh", "brief": "Giữ phiên điều phối gọn, việc nặng giao đi", "group": "xuyen-suot", "code": "§5.1", "name": "Ngân sách ngữ cảnh",
        "goal": "Giữ chi phí token thấp: phiên điều phối gọn, việc nặng giao subagent.",
        "outputs": [], "gate": "",
        "cases": [("Phiên điều phối kéo dài nhiều giờ, ngữ cảnh hàng trăm nghìn token", "Cập nhật hồ sơ, mở phiên mới, gọi status để tiếp tục.")],
        "tools": [("status", "Trả kèm gợi ý mở phiên mới khi chuyển bước")],
    },
    {
        "slug": "nang-cap", "brief": "Nhận luật mới, giữ phần dự án đã sửa", "group": "xuyen-suot", "code": "UPGRADE", "name": "Nâng cấp khung",
        "goal": "Đưa luật mới của khung vào dự án mà không mất phần dự án đã sửa.",
        "outputs": [(".shipfast/", "Phiên bản và bản gốc của khung, commit cùng dự án")],
        "gate": "check sạch.",
        "cases": [],
        "tools": [("upgrade", "Three-way merge"), ("refresh_departments", "Làm mới subagent bộ phận")],
    },
]

APPLY = {
    "slug": "ap-dung",
    "name": "Dùng shipfast-mcp",
    "lead": "shipfast-mcp là MCP server dựng bộ khung tài liệu vào dự án, cấp mã, kiểm hồ sơ và nâng cấp khung bằng three-way merge.",
    "mcp": [
        ("Claude Code (plugin)", "/plugin install shipfast --marketplace QuocTang/shipfast-mcp"),
        ("Claude Code (MCP)", "claude mcp add shipfast -- uvx shipfast-mcp"),
        ("Client MCP khác", "uvx shipfast-mcp"),
    ],
    "prompts": "Sau khi cài: repo mới gọi prompt init, dự án đang có code gọi adopt, khung có bản mới gọi upgrade.",
    "prompt_table": [
        ("init", "Repo mới: dựng khung và chạy W01, AI đề xuất và phản biện stack, PO chốt"),
        ("adopt", "Dự án đang có code: dựng khung, giữ tài liệu và quyết định sẵn có"),
        ("upgrade", "Khung có bản mới: dry run, gộp ba phía, trình chỗ xung đột"),
    ],
    "tools": [
        ("scaffold_project", "Dựng khung tài liệu, có dry run"),
        ("upgrade", "Nâng cấp khung bằng three-way merge"),
        ("status", "Trạng thái: bảng wave, wave đang mở, vấn đề chờ PO, backlog, quyết định giả định"),
        ("check", "Kiểm hồ sơ: biến khung còn sót, liên kết hỏng, wave đóng thiếu rút kinh nghiệm, bảng wave lệch"),
        ("open_wave", "Mở hồ sơ wave mới"),
        ("new_decision", "Ghi quyết định mới theo mẫu"),
        ("next_code", "Cấp mã không trùng"),
        ("create_department", "Lập bộ phận và subagent"),
        ("refresh_departments", "Làm mới subagent bộ phận theo mẫu mới"),
        ("read_guide", "Đọc tài liệu hướng dẫn"),
    ],
}
