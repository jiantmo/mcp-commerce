from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class TenderDropAndDeclareOperationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="tender_drop_create_transaction", description="Performs saving tender drop and declare store operations.", inputSchema={"type":"object","properties":{"dropAndDeclareTransaction":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dropAndDeclareTransaction"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/TenderDropAndDeclareOperation/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"saved": True}}
