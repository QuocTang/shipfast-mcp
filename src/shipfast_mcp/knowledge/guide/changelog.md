# Ghi chú phát hành

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
