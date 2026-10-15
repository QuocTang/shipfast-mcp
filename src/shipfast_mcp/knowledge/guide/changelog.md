# Ghi chú phát hành

## 0.2.3

- Subagent bộ phận có `effort` (mức suy nghĩ mặc định) trong frontmatter và mục "Kỷ luật riêng của bộ phận"; `create_department` nhận thêm `effort`, `discipline`; `refresh_departments` giữ model, effort, kỷ luật riêng.
- `docs/ORGANIZATION.md` §5.1: bảng model và mức suy nghĩ theo loại việc; Orchestrator truyền `model`, `effort` khi gọi subagent cho việc khác mặc định của bộ phận.
- Skill `shipfast-wave`: lời giao việc lấy model và mức suy nghĩ theo bảng §5.1.

## 0.2.2

- Mẫu lời giao việc: không chép luật chung vào lời giao, vì subagent bộ phận đã có luật trong file của nó.
- `docs/ORGANIZATION.md` §5.1 và subagent bộ phận: dự án có công cụ tìm code theo symbol (language server, MCP dạng Serena) thì dùng trước; `grep` cho tài liệu, cấu hình, log.
- Tool mới `refresh_departments`: làm mới `.claude/agents/dept-*.md` theo mẫu hiện hành, giữ tên, mã, lĩnh vực, vùng sở hữu, model; skill `shipfast-upgrade` gọi tool này sau `upgrade`.

## 0.2.1

Ngân sách ngữ cảnh, rút từ phân tích mức tiêu token của các dự án dùng quy trình:

- `docs/ORGANIZATION.md` §5.1: Orchestrator không tự khảo sát hay build; mỗi bước của wave một phiên; giao subagent theo lô; việc giao vừa khoảng 60 lượt; lời giao việc ghi sẵn file cần đọc; đọc và in gọn; chọn model theo việc.
- Skill `shipfast-wave` có mẫu lời giao việc; `shipfast-process` nhắc mở phiên mới khi wave chuyển bước.
- `create_department` có tham số `model` (ghi vào frontmatter của subagent); subagent bộ phận có luật đọc theo đoạn, sửa bằng Edit, báo cáo tối đa khoảng 30 dòng.
- `status` trả thêm `session_hint`.
- Thay khẩu ngữ bằng từ trung tính trong khung tài liệu và hướng dẫn.

Subagent bộ phận đã lập bằng bản trước không tự cập nhật (file thuộc dự án); từ 0.2.2 dùng tool `refresh_departments`.

## 0.2.0

Thuật ngữ chuyên ngành giữ tiếng Anh, câu văn vẫn tiếng Việt.

| Bản 0.1.x | Từ 0.2.0 |
|---|---|
| Điều hành | Orchestrator |
| agent con | subagent |
| đợt | wave |
| Gom việc · Thảo luận · Chốt phạm vi · Thi công · Dọn dẹp · Nghiệm thu · Phát hành | Intake · Discussion · Scope lock · Build · Cleanup · Acceptance · Release |
| Tạm hoãn · Đã đóng | On hold · Closed |
| team thi công | build team |
| sổ quyết định | decision log |
| dựng khung · chạy thử · gộp ba phía | scaffold · dry run · three-way merge |
| cổng kiểm chứng · hợp đồng | quality gate · contract |
| tranh luận · uỷ quyền | debate · delegation |

Tổ chức:

- Bộ phận lập theo dự án ngay từ W01 (vấn đề W01-09) và thêm khi có lĩnh vực mới; việc thuộc lĩnh vực nào giao bộ phận đó.
- Orchestrator chỉ điều phối, không tự thi công việc tốn công (`docs/ORGANIZATION.md` §5).
- Tool mới `create_department`: hồ sơ `docs/departments/<mã>/`, subagent `.claude/agents/dept-<mã>.md`.

Nâng cấp từ 0.1.x:

- `upgrade` cập nhật khung, skill, `CLAUDE.md`; file dữ liệu của dự án (`WAVES.md`, `BACKLOG.md`, hồ sơ wave, decision log) giữ nguyên nhãn cũ.
- Tool `status`, `check`, `open_wave` đọc được cả nhãn cũ lẫn nhãn mới. Đổi nhãn trong file dữ liệu là tuỳ chọn, theo bảng trên, khi PO đồng ý.
- Khoá kết quả của tool `check` đổi tên: `dot_*` → `wave_*`.
- Dự án chưa có bộ phận: Orchestrator đề xuất bộ bộ phận theo `docs/ORGANIZATION.md` §2.1, PO duyệt, lập bằng `create_department`.

## 0.1.0

Bản đầu: khung tài liệu và quy trình, 6 skill, 8 tool, 3 prompt, nâng cấp three-way merge.
