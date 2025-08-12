from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class HardwareProfilesController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="hardware_profiles_get_hardware_profile_by_id", description="Gets hardware profile by id.", inputSchema={"type":"object","properties":{"hardwareProfileId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["hardwareProfileId"]}),
            Tool(name="hardware_profiles_get_hardware_station_profiles", description="Gets collection of hardware station profiles.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/HardwareProfiles/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
