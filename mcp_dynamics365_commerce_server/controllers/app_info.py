from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

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
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["appVersion"]
                }
            )
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/AppInfo/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"updated": True, "appVersion": arguments.get("appVersion")}
        }
