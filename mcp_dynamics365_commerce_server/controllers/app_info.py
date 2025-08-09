from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class AppInfoController:
    """Controller for AppInfo-related Dynamics 365 Commerce API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(
                name="appinfo_update_application_version",
                description="Updates the POS device's current application version.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "appVersion": {"type": "string"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["appVersion"]
                }
            )
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/AppInfo/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"updated": True, "appVersion": arguments.get("appVersion")}
        }
