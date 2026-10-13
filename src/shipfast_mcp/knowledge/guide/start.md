# Bắt đầu từ đâu

shipfast là một quy trình làm việc giữa người (PO) và AI, đóng gói thành một MCP server. Cài MCP vào công cụ AI đang dùng là có quy trình; không cần clone repo mẫu, không cần so sánh tay.

## 1. Cài

Cần [uv](https://docs.astral.sh/uv/) (để có lệnh `uvx`).

| Công cụ | Cách cài |
|---|---|
| Claude Code (plugin) | `/plugin install shipfast --marketplace QuocTang/shipfast-mcp` |
| Claude Code (MCP) | `claude mcp add shipfast -- uvx shipfast-mcp` |
| Cursor, VS Code, Codex và client MCP khác | Khai server stdio: lệnh `uvx`, tham số `["shipfast-mcp"]` |

Ví dụ `.mcp.json` hoặc cấu hình tương đương:

```json
{
  "mcpServers": {
    "shipfast": { "command": "uvx", "args": ["shipfast-mcp"] }
  }
}
```

## 2. Chọn điểm vào

| Tình huống | Gọi | Kết quả |
|---|---|---|
| Repo mới, chưa có code | Prompt `init` | Đợt W01: AI hỏi về sản phẩm, đề xuất và phản biện stack, bạn chốt; dựng khung tài liệu, khung code, chạy được, nghiệm thu |
| Dự án đang chạy | Prompt `adopt` | AI khảo sát cái đang có, lập bảng đối chiếu, bạn duyệt; khung được thêm mà không phá tài liệu cũ |
| Dự án đã dùng shipfast | Không cần gọi gì | Skill trong `.claude/skills/` tự kích hoạt; hỏi "đang tới đâu" để AI gọi `status` |

Trong Claude Code, prompt MCP hiện dưới dạng lệnh `/mcp__shipfast__init`, `/mcp__shipfast__adopt`.

## 3. Đọc gì trong ngày đầu

| Thứ tự | File | Vì sao |
|---|---|---|
| 1 | `CLAUDE.md` | Luật cho AI, cũng là tóm tắt cho người |
| 2 | `docs/04_waves/README.md` | Vòng đời đợt, hệ mã, luật khi thảo luận và thi công |
| 3 | `docs/04_waves/WAVES.md` | Đợt nào đang chạy |
| 4 | `docs/05_decisions/README.md` | Đã quyết những gì |
| 5 | `docs/ORGANIZATION.md` | Ai làm gì, khi nào lập bộ phận, team, vai phản biện |

## 4. Làm việc hằng ngày

- Muốn làm gì thì nói với AI như với một trưởng nhóm: AI ghi thành vấn đề, đề xuất, phản biện, rồi hỏi bạn chốt.
- Trả lời theo mã cho nhanh: "W02-03: A", "đồng ý trừ W02-05".
- Nói **"chốt"** khi đồng ý phạm vi; từ đó AI thi công liên tục tới nghiệm thu.
- Hỏi "đang tới đâu" bất cứ lúc nào; phiên mới vẫn làm tiếp được vì mọi trạng thái nằm trong file.
