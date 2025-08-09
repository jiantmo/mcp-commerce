from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class TaxController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="tax_get_tax_overrides", description="Searches tax overrides.", inputSchema={"type":"object","properties":{"suggestionCriteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["suggestionCriteria"]}),
            Tool(name="tax_get_sales_tax_groups", description="Gets sales tax groups.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Tax/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"taxGroups": []}}
