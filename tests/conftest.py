import pytest

from shipfast_mcp import scaffold


@pytest.fixture
def project(tmp_path):
    """Repo trống đã scaffold shipfast ở chế độ init."""
    scaffold.scaffold(str(tmp_path), "demo-app", "Demo App", "Ứng dụng thử.", dry_run=False)
    return tmp_path
