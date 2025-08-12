from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class NotificationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="notification_get_notifications", description="Gets notifications.", inputSchema={"type":"object","properties":{"subscribedOperations":{"type":"array","items":{"type":"number"}},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["subscribedOperations"]}),
            Tool(name="notification_acknowledge_notifications", description="Acknowledge notifications.", inputSchema={"type":"object","properties":{"lastPullDateTime":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["lastPullDateTime"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Notification/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"notifications": []}}
