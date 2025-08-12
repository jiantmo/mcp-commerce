from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class CardTypeController:
    """Controller for Card type API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="card_type_get_card_types", description="Returns the list of card types.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]}),
            Tool(name="card_type_get_supported_payment_card_types", description="Returns supported payment cards.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/CardType/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"cardTypes": ["Visa","MasterCard"]}
        }
