from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class CategoriesController:
    """Controller for Categories API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="categories_get_categories", description="Gets categories by OData query.", inputSchema={"type":"object","properties":{"channelId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["channelId"]}),
            Tool(name="categories_get_children", description="Gets subcategories by channel and category id.", inputSchema={"type":"object","properties":{"channelId":{"type":"number"},"categoryId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["channelId","categoryId"]}),
            Tool(name="categories_get_attributes", description="Gets categories' attributes.", inputSchema={"type":"object","properties":{"categoryId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["categoryId"]}),
            Tool(name="categories_get_all", description="Gets full list of categories.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/Categories/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"result": "Success", "name": name}
        }
