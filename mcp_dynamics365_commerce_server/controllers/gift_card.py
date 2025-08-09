from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class GiftCardController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="gift_card_get_gift_card_inquiry", description="Get gift card with additional info by id.", inputSchema={"type":"object","properties":{"giftCardId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["giftCardId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/GiftCard/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"giftCardId": arguments.get("giftCardId"), "balance": 100.0}}
