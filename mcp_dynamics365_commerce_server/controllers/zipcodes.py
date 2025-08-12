from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class ZipcodesController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="zipcodes_get_zip_codes", description="Get zip codes filtered by location.", inputSchema={"type":"object","properties":{"countryRegionId":{"type":"string"},"stateProvinceId":{"type":"string"},"countyId":{"type":"string"},"cityName":{"type":"string"},"district":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["countryRegionId","stateProvinceId","countyId","cityName","district"]}),
            Tool(name="zipcodes_get_address_from_zip_code", description="Get addresses associated with zip code.", inputSchema={"type":"object","properties":{"countryRegionId":{"type":"string"},"zipPostalCode":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["countryRegionId","zipPostalCode"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Zipcodes/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"zipCodes": []}}
