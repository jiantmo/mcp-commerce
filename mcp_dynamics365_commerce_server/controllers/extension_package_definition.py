from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class ExtensionPackageDefinitionController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="extension_package_definition_get_extension_package_definitions", description="Gets configured extension package definitions.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/ExtensionPackageDefinition/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"packages": []}}
