# 🚢 shipfast-mcp

<!-- mcp-name: io.github.QuocTang/shipfast-mcp -->

**Quy trình làm việc theo wave giữa PO và AI, đóng gói thành MCP server.** AI làm Orchestrator: điều phối, đề xuất, phản biện; việc chuyên môn giao cho các bộ phận lập theo dự án, mỗi bộ phận là một subagent. Người làm PO: chốt và nghiệm thu. Dùng được cho mọi stack.

[![CI](https://github.com/QuocTang/shipfast-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/QuocTang/shipfast-mcp/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/shipfast-mcp.svg)](https://pypi.org/project/shipfast-mcp/)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-2026--07--28-8A2BE2.svg)](https://modelcontextprotocol.io/specification/2026-07-28)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Trang giới thiệu:** https://quoctang.github.io/shipfast-mcp/

> A Model Context Protocol server that ships a wave-based PO ↔ AI working process (propose, critique, decide, build, verify) to any stack, with three-way-merge upgrades so projects never diff against a template repo by hand.

## Table of Contents

- [🚀 Quick Start](#quick-start)
- [🛠️ Installation](#installation)
- [📦 Features](#features)
- [🤝 How to Contribute](#how-to-contribute)
- [💬 Community & Support](#community--support)
- [👥 Repo Contributors](#repo-contributors)
- [⚖️ License](#license)
- [🌟 Star History](#star-history)

---

## Quick Start

Cần [uv](https://docs.astral.sh/uv/). Trong Claude Code:

```text
/plugin install shipfast --marketplace QuocTang/shipfast-mcp
```

Mở repo cần làm, gọi điểm vào phù hợp:

| Tình huống | Gọi | Kết quả |
|---|---|---|
| Repo mới, chưa có code | `/mcp__shipfast__init` | Wave W01: AI hỏi về sản phẩm, đề xuất và phản biện 2–3 phương án stack, PO chốt; scaffold tài liệu, khung code chạy được, acceptance |
| Dự án đang chạy | `/mcp__shipfast__adopt` | AI khảo sát cái đang có, lập bảng đối chiếu; khung được thêm mà không phá tài liệu, quyết định sẵn có |
| Đã dùng shipfast | Hỏi "đang tới đâu" | Skill trong dự án tự kích hoạt, AI gọi `status` và làm tiếp |

Sau đó làm việc như với một trưởng nhóm: nêu yêu cầu, trả lời theo mã ("W02-03: A"), nói **"chốt"** khi đồng ý phạm vi.

## Installation

| Công cụ | Cách cài |
|---|---|
| Claude Code (plugin) | `/plugin install shipfast --marketplace QuocTang/shipfast-mcp` |
| Claude Code (MCP) | `claude mcp add shipfast -- uvx shipfast-mcp` |
| Cursor, VS Code, Codex và client MCP khác | Server stdio, lệnh `uvx`, tham số `shipfast-mcp` |

Cấu hình dạng JSON cho client đọc `mcpServers`:

```json
{
  "mcpServers": {
    "shipfast": { "command": "uvx", "args": ["shipfast-mcp"] }
  }
}
```

Ghim phiên bản: `uvx shipfast-mcp@0.2.0`.

## Features

### Vấn đề và cách giải

| Khi làm việc với AI không có quy trình | shipfast |
|---|---|
| AI viết code khi chưa hiểu đúng yêu cầu | 🛑 Không code trước khi PO lock scope |
| AI chiều theo mọi yêu cầu | 🥊 Orchestrator phản biện cả đề xuất của mình; 7 vai phản biện debate độc lập rồi phản biện chéo |
| Một phiên AI ôm mọi việc, ý kiến chuyên môn mỏng | 🏢 Bộ phận lập theo dự án từ W01 (PRODUCT, PLATFORM, TRUST…); việc thuộc lĩnh vực nào giao bộ phận đó, Orchestrator chỉ điều phối |
| Quyết định rải rác trong chat và comment | 📒 Decision log một chỗ (`SP`, `KT`, `QT`), code chỉ trỏ mã |
| Phiên mới quên bối cảnh | 💾 Trạng thái nằm trong file; tool `status` cho biết đang tới đâu |
| Phạm vi phình dần | 📥 Việc mới vào backlog, đổi phạm vi qua CR |
| "Xong" nhưng chưa chạy thật | ✅ Quality gate phải chạy thật; QA độc lập acceptance |
| Chép template rồi lệch dần, cập nhật phải so tay với repo gốc | 🔀 Nâng cấp three-way merge tự động, không cần repo gốc |

### Vòng đời một wave

```text
📥 Intake → 🗣️ Discussion → ✅ Scope lock → 🔨 Build → 🧹 Cleanup → 🧪 Acceptance → 🚀 Release, rút kinh nghiệm, đóng
```

| Chế độ chốt | Khi nào |
|---|---|
| PO chốt | Mặc định |
| Chốt thẳng | Wave nhỏ, yêu cầu đã rõ |
| Delegation | Đã có từ hai bộ phận; Chủ toạ phán quyết theo tiêu chí PO đặt |

### Thành phần MCP

| Loại | Tên | Việc |
|---|---|---|
| 🔧 Tool | `scaffold_project` | Dựng `CLAUDE.md`, `docs/` (wave, backlog, decision log, tổ chức) và skill `.claude/skills/shipfast-*`; dry run trước, không ghi đè |
| 🔧 Tool | `upgrade` | Nâng khung lên phiên bản mới bằng three-way merge |
| 🔧 Tool | `status`, `check` | Wave nào đang chạy, chờ PO điều gì; hồ sơ có lệch không |
| 🔧 Tool | `create_department` | Lập bộ phận theo dự án: hồ sơ `docs/departments/<mã>/`, subagent `.claude/agents/dept-<mã>.md` |
| 🔧 Tool | `open_wave`, `new_decision`, `next_code` | Mở wave, ghi quyết định, cấp mã không trùng |
| 🔧 Tool | `read_guide` | Tài liệu hướng dẫn cho người |
| 💬 Prompt | `init`, `adopt`, `upgrade` | Điểm vào |
| 📚 Resource | `skill://shipfast-*/SKILL.md` | 6 skill: luật nền, khởi tạo, áp dụng, chạy wave, debate, nâng cấp |
| 📚 Resource | `shipfast://guide/*` | Bắt đầu, tổ chức, ý nghĩa, phát triển và nâng cấp |

### Nâng cấp không cần repo gốc

Dự án giữ `.shipfast/manifest.json` và `.shipfast/base/` (bản khung lần trước). `upgrade` so ba bản: bản gốc, bản dự án, bản mới.

| Trường hợp | Kết quả |
|---|---|
| Dự án chưa sửa file | Thay bằng bản mới |
| Hai bên sửa khác chỗ | Gộp tự động |
| Hai bên sửa cùng chỗ | File thật giữ nguyên; bản gộp có dấu xung đột ở `.shipfast/pending/` để duyệt |
| Bảng wave, backlog, decision log | Không bao giờ bị đụng |

### Hướng dẫn

| Bài | File |
|---|---|
| Bắt đầu từ đâu | [`start.md`](src/shipfast_mcp/knowledge/guide/start.md) |
| Tổ chức ra sao | [`organization.md`](src/shipfast_mcp/knowledge/guide/organization.md) |
| Ý nghĩa và mục đích | [`purpose.md`](src/shipfast_mcp/knowledge/guide/purpose.md) |
| Phát triển tiếp và nâng cấp | [`evolve.md`](src/shipfast_mcp/knowledge/guide/evolve.md) |

## How to Contribute

Đóng góp được hoan nghênh, nhất là cách làm đã chạy thật ở dự án của bạn và dùng được cho mọi stack.

1. **Fork** repository.
2. **Tạo nhánh mới** cho thay đổi.
3. **Gửi Pull Request**: mô tả vấn đề gặp phải, cách làm, bằng chứng từ dự án thật.

Phát triển tại máy:

```bash
uv sync
uv run pytest
uv run shipfast-mcp
```

Kho tri thức nằm ở `src/shipfast_mcp/knowledge/`: `project/` (khung dựng vào dự án), `skills/`, `guide/`. Quyết định thiết kế: [`docs/decisions/README.md`](docs/decisions/README.md).

## Community & Support

- Báo lỗi, đề xuất: [GitHub Issues](https://github.com/QuocTang/shipfast-mcp/issues).
- Nếu repository giúp bạn tiết kiệm thời gian, hãy để lại một ⭐.

## Repo Contributors

<a href="https://github.com/QuocTang/shipfast-mcp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=QuocTang/shipfast-mcp" alt="Repository contributors" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

## License

MIT License. See [LICENSE](LICENSE) for details.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=QuocTang/shipfast-mcp&type=Date)](https://star-history.com/#QuocTang/shipfast-mcp&Date)
