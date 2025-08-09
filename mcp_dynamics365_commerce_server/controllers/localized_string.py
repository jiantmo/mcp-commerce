from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class LocalizedStringController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="localized_string_get_localized_strings", description="Gets all localized strings filtered by language and text id.", inputSchema={"type":"object","properties":{"languageId":{"type":"string"},"textId":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["languageId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/LocalizedString/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"strings": []}}
