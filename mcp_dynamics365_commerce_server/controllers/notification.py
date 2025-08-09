from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class NotificationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="notification_get_notifications", description="Gets notifications.", inputSchema={"type":"object","properties":{"subscribedOperations":{"type":"array","items":{"type":"number"}},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["subscribedOperations"]}),
            Tool(name="notification_acknowledge_notifications", description="Acknowledge notifications.", inputSchema={"type":"object","properties":{"lastPullDateTime":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["lastPullDateTime"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Notification/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"notifications": []}}
