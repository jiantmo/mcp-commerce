from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class TransferOrderController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="transfer_order_get", description="Gets open transfer orders for the store.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="transfer_order_commit", description="Commits a transfer order.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="transfer_order_get_transfer_order_journals", description="Gets transfer order journals.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="transfer_order_get_transfer_order_lines", description="Gets transfer order lines.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="transfer_order_create_transfer_order_lines", description="Creates transfer order lines.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"transferOrderLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId","transferOrderLines"]}),
            Tool(name="transfer_order_update_transfer_order_lines", description="Updates transfer order lines.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"transferOrderLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId","transferOrderLines"]}),
            Tool(name="transfer_order_delete_transfer_order_lines", description="Deletes transfer order lines.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"transferOrderLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId","transferOrderLines"]}),
            Tool(name="transfer_order_get_transfer_order_comments", description="Gets transfer order comments.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="transfer_order_add_transfer_order_comment", description="Adds transfer order comment.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"commentedBy":{"type":"string"},"comment":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId","commentedBy","comment"]}),
            Tool(name="transfer_order_get_transfer_packing_slip", description="Gets packing slip for transfer order journal.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"voucherId":{"type":"string"},"criteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId","voucherId","criteria"]}),
            Tool(name="transfer_order_patch_entity", description="Saves transfer order to local DB.", inputSchema={"type":"object","properties":{"entity":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["entity"]}),
            Tool(name="transfer_order_get_entity_by_key", description="Gets transfer order by id.", inputSchema={"type":"object","properties":{"orderId":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["orderId"]}),
            Tool(name="transfer_order_delete_entity", description="Deletes specified transfer order.", inputSchema={"type":"object","properties":{"entity":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["entity"]}),
            Tool(name="transfer_order_create_entity", description="Creates transfer order.", inputSchema={"type":"object","properties":{"entity":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["entity"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/TransferOrder/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
