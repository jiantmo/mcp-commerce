from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class EnvironmentConfigurationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="env_config_get_configuration", description="Gets environment configuration.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]}),
            Tool(name="environment_configuration_get_extension_profile", description="Gets extension profile.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/EnvironmentConfiguration/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"config": {"version":"1.0"}}}
