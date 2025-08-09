from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class StoreSafeController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="store_safe_get_store_safes", description="Gets store safe list.", inputSchema={"type":"object","properties":{"settings":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/StoreSafe/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"storeSafes": []}}
