import json
import re

import pytest

from shipfast_mcp import __version__, scaffold, templates


def test_dry_run_writes_nothing(tmp_path):
    report = scaffold.scaffold(str(tmp_path), "demo-app", "Demo App")
    assert report["dry_run"] is True
    assert "CLAUDE.md" in report["created"]
    assert list(tmp_path.iterdir()) == []


def test_init_creates_framework_and_state(project):
    claude = (project / "CLAUDE.md").read_text()
    assert "Demo App" in claude and "Ứng dụng thử." in claude
    assert (project / "docs/04_waves/W01/1-discussion.md").exists()
    assert (project / ".claude/skills/shipfast-process/SKILL.md").exists()
    manifest = json.loads((project / ".shipfast/manifest.json").read_text())
    assert manifest["version"] == __version__
    assert manifest["files"]["docs/04_waves/WAVES.md"] == "seed"
    assert (project / ".shipfast/base/CLAUDE.md").exists()
    assert not (project / ".shipfast/base/docs/04_waves/WAVES.md").exists()
    assert "tmp/" in (project / ".gitignore").read_text()


def test_no_leftover_placeholders_or_broken_links(project):
    for path in project.rglob("*.md"):
        if ".shipfast" in path.parts:
            continue
        text = path.read_text()
        assert not re.search(r"\{\{[A-Z_]+\}\}", text), path
    from shipfast_mcp import project as proj

    result = proj.check(str(project))
    assert result["ok"], result


def test_adopt_skips_w01_and_existing_files(tmp_path):
    (tmp_path / "CLAUDE.md").write_text("riêng của dự án\n")
    report = scaffold.scaffold(str(tmp_path), "old-app", "Old App", mode="adopt", dry_run=False)
    assert "CLAUDE.md" in report["skipped_existing"]
    assert (tmp_path / "CLAUDE.md").read_text() == "riêng của dự án\n"
    assert not (tmp_path / "docs/04_waves/W01").exists()


def test_scaffold_twice_refused(project):
    with pytest.raises(ValueError, match="upgrade"):
        scaffold.scaffold(str(project), "demo-app", "Demo App")


@pytest.mark.parametrize("bad", ["Demo", "1app", "demo_app", ""])
def test_invalid_slug(tmp_path, bad):
    with pytest.raises(ValueError):
        scaffold.scaffold(str(tmp_path), bad, "x")


def test_relative_path_refused():
    with pytest.raises(ValueError, match="tuyệt đối"):
        scaffold.scaffold("relative/dir", "demo-app", "Demo App")


def _new_template(monkeypatch, tmp_path, rel, mutate):
    """Giả lập phiên bản khung mới: chép kho tri thức, sửa một file bằng mutate."""
    import shutil

    knowledge = tmp_path / "knowledge"
    shutil.copytree(templates.KNOWLEDGE, knowledge)
    target = knowledge / "project" / rel
    target.write_text(mutate(target.read_text()))
    monkeypatch.setattr(templates, "PROJECT_TEMPLATE", knowledge / "project")
    monkeypatch.setattr(templates, "SKILLS", knowledge / "skills")


def test_upgrade_noop_when_same_version(project):
    report = scaffold.upgrade(str(project))
    assert not report.get("updated") and not report.get("conflicts") and not report.get("created")


def test_upgrade_fast_forward_untouched_file(project, monkeypatch, tmp_path_factory):
    _new_template(monkeypatch, tmp_path_factory.mktemp("k"), "docs/04_waves/README.md", lambda t: t + "\nLuật mới.\n")
    report = scaffold.upgrade(str(project), dry_run=False)
    assert "docs/04_waves/README.md" in report["updated"]
    assert (project / "docs/04_waves/README.md").read_text().endswith("Luật mới.\n")


def test_upgrade_merges_both_sides(project, monkeypatch, tmp_path_factory):
    claude = project / "CLAUDE.md"
    claude.write_text(claude.read_text().replace("## Khi không chắc", "## Luật riêng\n\nChỉ của dự án.\n\n## Khi không chắc"))
    _new_template(
        monkeypatch,
        tmp_path_factory.mktemp("k"),
        "CLAUDE.md",
        lambda t: t.replace("## Vai trò\n", "## Vai trò\n\nDòng mới của khung.\n"),
    )
    report = scaffold.upgrade(str(project), dry_run=False)
    assert "CLAUDE.md" in report["merged"]
    text = claude.read_text()
    assert "Chỉ của dự án." in text and "Dòng mới của khung." in text


def test_upgrade_conflict_keeps_project_file(project, monkeypatch, tmp_path_factory):
    claude = project / "CLAUDE.md"
    original_line = "Chưa có tài liệu hoặc quyết định cho việc cần làm thì hỏi PO, không tự đặt luật."
    claude.write_text(claude.read_text().replace(original_line, "Phiên bản của dự án."))
    before = claude.read_text()
    _new_template(monkeypatch, tmp_path_factory.mktemp("k"), "CLAUDE.md", lambda t: t.replace(original_line, "Phiên bản của khung."))
    report = scaffold.upgrade(str(project), dry_run=False)
    assert report["conflicts"] == ["CLAUDE.md"]
    assert claude.read_text() == before
    pending = (project / ".shipfast/pending/CLAUDE.md").read_text()
    assert "<<<<<<< du-an" in pending and "shipfast-moi" in pending

    claude.write_text(before.replace("Phiên bản của dự án.", "Phiên bản của khung."))
    report = scaffold.upgrade(str(project), dry_run=False)
    assert not report.get("conflicts")
    assert not (project / ".shipfast/pending").exists()


def test_upgrade_never_touches_seed(project, monkeypatch, tmp_path_factory):
    waves = project / "docs/04_waves/WAVES.md"
    waves.write_text("dữ liệu của dự án\n")
    _new_template(monkeypatch, tmp_path_factory.mktemp("k"), "docs/04_waves/WAVES.md", lambda t: t + "khung đổi\n")
    scaffold.upgrade(str(project), dry_run=False)
    assert waves.read_text() == "dữ liệu của dự án\n"


def test_upgrade_respects_deleted_and_adds_new(project, monkeypatch, tmp_path_factory):
    (project / "reports/README.md").unlink()
    k = tmp_path_factory.mktemp("k")
    _new_template(monkeypatch, k, "docs/README.md", lambda t: t)
    (templates.PROJECT_TEMPLATE / "docs/NEW.md").write_text("# Mới\n")
    report = scaffold.upgrade(str(project), dry_run=False)
    assert not (project / "reports/README.md").exists()
    assert "docs/NEW.md" in report["created"]


def test_upgrade_requires_scaffold(tmp_path):
    with pytest.raises(ValueError, match="scaffold"):
        scaffold.upgrade(str(tmp_path))
