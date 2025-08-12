from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class LocalizedStringController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="localized_string_get_localized_strings", description="Gets all localized strings filtered by language and text id.", inputSchema={"type":"object","properties":{"languageId":{"type":"string"},"textId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["languageId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/LocalizedString/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"strings": []}}
