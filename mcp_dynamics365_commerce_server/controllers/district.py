from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class DistrictController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="district_get_districts", description="Get districts filtered by location.", inputSchema={"type":"object","properties":{"countryRegionId":{"type":"string"},"stateProvinceId":{"type":"string"},"countyId":{"type":"string"},"cityName":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["countryRegionId","stateProvinceId","countyId","cityName"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/District/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"districts": [{"name":"Central"},{"name":"North"}]}}
