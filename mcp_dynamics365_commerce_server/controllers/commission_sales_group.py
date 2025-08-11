from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class CommissionSalesGroupController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="commission_sales_get_groups", description="Gets commission sales groups for the channel.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="commission_sales_search_groups", description="Search commission sales groups by text.", inputSchema={"type":"object","properties":{"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["searchText"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/CommissionSalesGroup/{name}", "toolName": name, "arguments": arguments, "status": "success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"groups": [{"id":"CSG001","name":"Default"}]}}
