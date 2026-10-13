import pytest

from shipfast_mcp import project as proj


def test_status_fresh_project(project):
    s = proj.status(str(project))
    assert s["shipfast_installed"] == s["shipfast_available"]
    assert s["open_waves"][0]["wave"] == "W01"
    assert "W01-01" in s["open_waves"][0]["issues_waiting_po"]


def test_status_without_scaffold(tmp_path):
    assert "init" in proj.status(str(tmp_path))["hint"]


def test_next_code_global_and_wave(project):
    assert proj.next_code(str(project), "QT")["code"] == "QT-002"
    assert proj.next_code(str(project), "BL")["code"] == "BL-001"
    assert proj.next_code(str(project), "W")["code"] == "W02"
    assert proj.next_code(str(project), "ISSUE", "W01")["code"] == "W01-09"
    assert proj.next_code(str(project), "CR", "1")["code"] == "CR-W01-01"
    assert proj.next_code(str(project), "QA", "W01")["code"] == "QA01-1"
    with pytest.raises(ValueError):
        proj.next_code(str(project), "P")


def test_open_wave(project):
    r = proj.open_wave(str(project), "Đăng nhập", "Người dùng đăng nhập được", mode="direct")
    assert r["wave"] == "W02"
    readme = (project / "docs/04_waves/W02/README.md").read_text()
    assert "Đăng nhập" in readme and "Chốt thẳng" in readme and "Wxx" not in readme
    assert not (project / "docs/04_waves/W02/debate").exists()
    assert "| W02 |" in (project / "docs/04_waves/WAVES.md").read_text()
    assert proj.check(str(project))["ok"]


def test_open_wave_delegated_has_debate(project):
    r = proj.open_wave(str(project), "Lớn", "Mục tiêu", mode="delegated")
    assert (project / f"docs/04_waves/{r['wave']}/debate/r1-_mau.md").exists()


def test_new_decision(project):
    r = proj.new_decision(str(project), "KT", "Chọn stack", "Stack Choice", decision="Dùng X.", status="Hiệu lực")
    assert r["code"] == "KT-001"
    text = (project / r["file"]).read_text()
    assert "Chọn stack" in text and "Dùng X." in text and "| Trạng thái | Hiệu lực |" in text
    assert "[KT-001](KT-001-stack-choice.md)" in (project / "docs/05_decisions/README.md").read_text()
    assert proj.new_decision(str(project), "KT", "Khác", "other")["code"] == "KT-002"
    assert proj.status(str(project))["decisions_assumed"] == ["[KT-002](KT-002-other.md)"]


def test_check_detects_problems(project):
    (project / "docs/01_design/README.md").write_text("[gãy](khong-co.md) {{SLUG}}\n")
    (project / "docs/05_decisions/SP-009-orphan.md").write_text("# SP-009\n")
    readme = project / "docs/04_waves/W01/README.md"
    readme.write_text(readme.read_text().replace("🗣️ Thảo luận", "🚀 Đã đóng"))
    issues = proj.check(str(project))["issues"]
    assert issues["link_gay"] and issues["bien_khung_con_sot"]
    assert issues["quyet_dinh_thieu_muc_luc"] == ["SP-009"]
    assert "W01" in issues["dong_dot_thieu_rut_kinh_nghiem"]
    assert issues["dong_dot_con_cho"]
