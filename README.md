<p align="center"><img src="https://raw.githubusercontent.com/QuocTang/shipfast-mcp/main/assets/logo.svg" width="72" height="72" alt="shipfast" /></p>

<h1 align="center">shipfast-mcp</h1>

<!-- mcp-name: io.github.QuocTang/shipfast-mcp -->

<p align="center"><b>Quy trình làm việc giữa PO và AI, đóng gói thành MCP server.</b><br />PO quyết định phạm vi và nghiệm thu. Orchestrator điều phối, đề xuất và phản biện. Việc chuyên môn do các bộ phận lập theo dự án đảm nhận, mỗi bộ phận là một subagent.</p>

<p align="center">
  <a href="https://github.com/QuocTang/shipfast-mcp/actions/workflows/ci.yml"><img src="https://github.com/QuocTang/shipfast-mcp/actions/workflows/ci.yml/badge.svg" alt="CI" /></a>
  <a href="https://pypi.org/project/shipfast-mcp/"><img src="https://img.shields.io/pypi/v/shipfast-mcp.svg" alt="PyPI" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.12%2B-blue.svg" alt="Python" /></a>
  <a href="https://modelcontextprotocol.io/specification/2026-07-28"><img src="https://img.shields.io/badge/MCP-2026--07--28-8A2BE2.svg" alt="MCP" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
</p>

<p align="center"><a href="https://quoctang.github.io/shipfast-mcp/">Trang giới thiệu</a> · <a href="https://pypi.org/project/shipfast-mcp/">PyPI</a> · <a href="https://github.com/QuocTang/shipfast-mcp/blob/main/src/shipfast_mcp/knowledge/guide/start.md">Tài liệu</a> · <a href="https://github.com/QuocTang/shipfast-mcp/blob/main/src/shipfast_mcp/knowledge/guide/changelog.md">Ghi chú phát hành</a></p>

> A Model Context Protocol server that brings a wave-based working process between a product owner and AI agents to any stack: an orchestrator that coordinates and critiques, project-specific departments as subagents, a single decision log, verified quality gates, and three-way-merge upgrades.

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

Cần [uv](https://docs.astral.sh/uv/).

| # | Bước | Lệnh |
|---|---|---|
| 1 | Cài uv | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| 2 | Thêm shipfast vào Claude Code | `/plugin install shipfast --marketplace QuocTang/shipfast-mcp` |
| 3 | Gọi prompt init (repo mới) hoặc adopt (dự án đang có code) | `/mcp__shipfast__init` |
| 4 | Trả lời theo mã vấn đề | `W01-02: A`; nói **"chốt"** khi đồng ý phạm vi |
| 5 | Nâng cấp khi có bản mới | `/mcp__shipfast__upgrade` |

Một phiên `init` trong Claude Code (rút gọn):

```text
> /mcp__shipfast__init

● shipfast - scaffold_project (MCP)(mode: "init", dry_run: true)
  └ 34 file sẽ tạo, 0 file trùng

● Đã mở wave W01. Sản phẩm làm gì, cho ai dùng?

> App quản lý kho cho cửa hàng nhỏ, hai vai: chủ cửa hàng và nhân viên.

● W01-01: nhập xuất kho, cảnh báo sắp hết, báo cáo tồn; in hoá đơn và đa chi
  nhánh để sau (BL-005, BL-006). W01-02 stack: đề xuất A (Next.js + Postgres).
  Phản biện: cần thêm runtime khi có job nền. W01-09: lập ba bộ phận PRODUCT,
  PLATFORM, TRUST.

> W01-02: A, còn lại theo đề xuất. Chốt.

● shipfast - create_department (MCP)(code: "PLATFORM")
  └ docs/departments/platform/, .claude/agents/dept-platform.md
```

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

### Vòng đời một wave

```text
📥 Intake → 🗣️ Discussion → ✅ Scope lock → 🔨 Build → 🧹 Cleanup → 🧪 Acceptance → 🚀 Release
```

| Bước | Việc |
|---|---|
| Intake | Gom việc, mỗi vấn đề kèm phương án |
| Discussion | Orchestrator đề xuất và phản biện, lấy ý kiến bộ phận; PO chốt |
| Scope lock | PO nói "chốt"; phạm vi đóng băng, đổi qua CR |
| Build | Bộ phận phụ trách build theo hạng mục |
| Cleanup | Dọn mã chết, tài liệu lệch |
| Acceptance | QA độc lập với bộ phận đã build; quality gate chạy thật |
| Release | Phát hành, rút kinh nghiệm, đóng wave |

| Chế độ chốt | Khi nào |
|---|---|
| PO chốt | Mặc định |
| Chốt thẳng | Wave nhỏ, yêu cầu đã rõ |
| Delegation | PO giao quyền chốt cho debate giữa các bộ phận; Orchestrator làm Chủ toạ |

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

### Nâng cấp khung

Dự án giữ `.shipfast/manifest.json` và `.shipfast/base/` (bản khung lần trước). `upgrade` so ba bản: bản gốc, bản dự án, bản mới.

| Trường hợp | Kết quả |
|---|---|
| Dự án chưa sửa file | Thay bằng bản mới |
| Hai bên sửa khác chỗ | Gộp tự động |
| Hai bên sửa cùng chỗ | File thật giữ nguyên; bản gộp có dấu xung đột ở `.shipfast/pending/` để duyệt |
| Bảng wave, backlog, decision log | Giữ nguyên |

### Hướng dẫn

| Bài | File |
|---|---|
| Bắt đầu từ đâu | [`start.md`](src/shipfast_mcp/knowledge/guide/start.md) |
| Tổ chức ra sao | [`organization.md`](src/shipfast_mcp/knowledge/guide/organization.md) |
| Ý nghĩa và mục đích | [`purpose.md`](src/shipfast_mcp/knowledge/guide/purpose.md) |
| Phát triển tiếp và nâng cấp | [`evolve.md`](src/shipfast_mcp/knowledge/guide/evolve.md) |
| Ghi chú phát hành | [`changelog.md`](src/shipfast_mcp/knowledge/guide/changelog.md) |

## How to Contribute

Đóng góp nên là cách làm đã chạy ở dự án thật và dùng được cho mọi stack.

1. **Fork** repository.
2. **Tạo nhánh mới** cho thay đổi.
3. **Gửi Pull Request**: mô tả vấn đề gặp phải, cách làm, bằng chứng từ dự án thật.

Phát triển tại máy:

```bash
uv sync
uv run pytest
uv run shipfast-mcp
```

Kho tri thức nằm ở `src/shipfast_mcp/knowledge/`: `project/` (khung dựng vào dự án), `department/` (hồ sơ và subagent bộ phận), `skills/`, `guide/`. Landing page ở `site/` (`site/README.md`). Quyết định thiết kế: [`docs/decisions/README.md`](docs/decisions/README.md).

## Community & Support

- Báo lỗi, đề xuất: [GitHub Issues](https://github.com/QuocTang/shipfast-mcp/issues).
- Gắn sao (⭐) repository để theo dõi các bản phát hành mới.

## Repo Contributors

<a href="https://github.com/QuocTang/shipfast-mcp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=QuocTang/shipfast-mcp" alt="Repository contributors" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

## License

MIT License. See [LICENSE](LICENSE) for details.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=QuocTang/shipfast-mcp&type=Date)](https://star-history.com/#QuocTang/shipfast-mcp&Date)
