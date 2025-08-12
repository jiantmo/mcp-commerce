from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class PublishingController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="publishing_set_online_channel_publish_status", description="Updates Online Channel publishing status.", inputSchema={"type":"object","properties":{"publishingStatus":{"type":"number"},"publishingStatusMessage":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["publishingStatus","publishingStatusMessage"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Publishing/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"updated": True}}
