# shipfast-mcp

<!-- mcp-name: io.github.QuocTang/shipfast-mcp -->

MCP server phân phối **quy trình làm việc theo đợt giữa người (PO) và AI**: AI làm Điều hành, đề xuất và phản biện, PO chốt; agent con thi công; mọi trạng thái nằm trong file. Dùng được cho mọi stack.

Cài MCP là có quy trình. Không cần clone repo mẫu, không phải so sánh tay khi nâng cấp: tool `upgrade` tự gộp ba phía giữa bản khung cũ, bản dự án đã sửa và bản khung mới.

## Cài

Cần [uv](https://docs.astral.sh/uv/).

| Công cụ | Lệnh |
|---|---|
| Claude Code (plugin) | `/plugin install shipfast --marketplace QuocTang/shipfast-mcp` |
| Claude Code (MCP) | `claude mcp add shipfast -- uvx shipfast-mcp` |
| Client MCP khác | Server stdio: `uvx shipfast-mcp` |

```json
{ "mcpServers": { "shipfast": { "command": "uvx", "args": ["shipfast-mcp"] } } }
```

## Dùng

| Tình huống | Gọi |
|---|---|
| Repo mới | Prompt `init`: đợt W01, AI đề xuất và phản biện stack, PO chốt, dựng khung và code chạy được |
| Dự án đang chạy | Prompt `adopt`: khảo sát, bảng đối chiếu, thêm khung không phá tài liệu cũ |
| Có bản shipfast mới | Prompt `upgrade` |

## Thành phần

| Loại | Tên | Việc |
|---|---|---|
| Tool | `scaffold_project` | Dựng `CLAUDE.md`, `docs/` (đợt, backlog, sổ quyết định, tổ chức), skill `.claude/skills/shipfast-*`; chạy thử trước, không ghi đè |
| Tool | `upgrade` | Nâng khung, gộp ba phía; xung đột để ở `.shipfast/pending/`, file thật giữ nguyên |
| Tool | `status`, `check` | Đang tới đâu, chờ PO điều gì; hồ sơ có lệch không |
| Tool | `open_wave`, `new_decision`, `next_code` | Mở đợt, ghi quyết định, cấp mã không trùng |
| Tool | `read_guide` | Tài liệu cho người |
| Prompt | `init`, `adopt`, `upgrade` | Điểm vào |
| Resource | `skill://shipfast-*/SKILL.md`, `shipfast://guide/*` | Skill và hướng dẫn |

## Hướng dẫn

| Bài | File |
|---|---|
| Bắt đầu từ đâu | [`start.md`](src/shipfast_mcp/knowledge/guide/start.md) |
| Tổ chức ra sao | [`organization.md`](src/shipfast_mcp/knowledge/guide/organization.md) |
| Ý nghĩa và mục đích | [`purpose.md`](src/shipfast_mcp/knowledge/guide/purpose.md) |
| Phát triển tiếp và nâng cấp | [`evolve.md`](src/shipfast_mcp/knowledge/guide/evolve.md) |

## Phát triển

```bash
uv sync
uv run pytest
uv run shipfast-mcp          # chạy server stdio
```

Kho tri thức ở `src/shipfast_mcp/knowledge/`: `project/` (khung dựng vào dự án), `skills/`, `guide/`. Quyết định thiết kế: [`docs/decisions/README.md`](docs/decisions/README.md).

## License

MIT
