from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class CatalogsController:
    """Controller for Catalogs API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="catalogs_get_catalogs", description="Gets catalogs by OData query.", inputSchema={"type":"object","properties":{"channelId":{"type":"number"},"activeOnly":{"type":"boolean"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["channelId","activeOnly"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/Catalogs/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"catalogs": [], "channelId": arguments.get("channelId")}
        }
