import asyncio

from fastmcp import Client

from shipfast_mcp.server import mcp


def test_server_exposes_tools_prompts_resources(tmp_path):
    async def run():
        async with Client(mcp) as client:
            tools = {t.name for t in await client.list_tools()}
            assert {"scaffold_project", "upgrade", "status", "next_code", "open_wave", "new_decision", "check", "read_guide"} <= tools
            prompts = {p.name for p in await client.list_prompts()}
            assert {"init", "adopt", "upgrade"} <= prompts
            uris = {str(r.uri) for r in await client.list_resources()}
            assert "skill://shipfast-process/SKILL.md" in uris
            assert "shipfast://guide/start" in uris
            guide = await client.call_tool("read_guide", {"topic": "start"})
            assert "Bắt đầu từ đâu" in guide.content[0].text
            result = await client.call_tool(
                "scaffold_project", {"project_dir": str(tmp_path), "name": "x-app", "display_name": "X", "dry_run": False}
            )
            assert "CLAUDE.md" in result.structured_content["created"]
            prompt = await client.get_prompt("init", {"project_dir": str(tmp_path)})
            assert "W01" in prompt.messages[0].content.text

    asyncio.run(run())
