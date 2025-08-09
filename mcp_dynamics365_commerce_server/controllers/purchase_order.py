from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class PurchaseOrderController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="purchase_order_get", description="Gets open purchase orders for the store.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="purchase_order_commit", description="Commits a purchase order.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="purchase_order_patch_entity", description="Saves a purchase order to local database.", inputSchema={"type":"object","properties":{"entity":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["entity"]}),
            Tool(name="purchase_order_get_entity_by_key", description="Get a purchase order by id.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/PurchaseOrder/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
