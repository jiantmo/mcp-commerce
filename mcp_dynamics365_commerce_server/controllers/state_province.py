from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class StateProvinceController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="state_province_get_state_provinces", description="Get states/provinces by country/region.", inputSchema={"type":"object","properties":{"countryRegionId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["countryRegionId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/StateProvince/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"states": []}}
