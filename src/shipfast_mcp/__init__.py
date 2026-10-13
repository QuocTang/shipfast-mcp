"""shipfast-mcp: quy trình làm việc PO, Orchestrator, subagent, phân phối qua MCP."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("shipfast-mcp")
except PackageNotFoundError:
    __version__ = "0.0.0"
