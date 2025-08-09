from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class EnvironmentConfigurationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="environment_configuration_get_environment_configuration", description="Gets environment configuration.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="environment_configuration_get_extension_profile", description="Gets extension profile.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/EnvironmentConfiguration/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"config": {"version":"1.0"}}}
