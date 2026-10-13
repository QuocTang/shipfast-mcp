"""shipfast-mcp: quy trình làm việc PO, Điều hành, agent con, phân phối qua MCP."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("shipfast-mcp")
except PackageNotFoundError:
    __version__ = "0.0.0"
