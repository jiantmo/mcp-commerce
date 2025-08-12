from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class SalesOrdersFulfillmentController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="sales_orders_fulfillment_ship_fulfillment_lines", description="Ship the fulfillment lines.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_accept_fulfillment_lines", description="Accepts the fulfillment lines.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_pick_fulfillment_lines", description="Updates status to Picking.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_mark_as_picked", description="Updates status to Picked.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_pack_fulfillment_lines", description="Updates status to Packed or Partially Packed.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="fulfillment_mark_lines_as_packed", description="Marks lines as Packed.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_get_fulfillment_lines", description="Gets fulfillment lines.", inputSchema={"type":"object","properties":{"criteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["criteria"]}),
            Tool(name="fulfillment_get_packing_slips", description="Gets packing slips.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]}),
            Tool(name="fulfillment_get_packing_slips_by_id", description="Gets packing slips by id and sales id.", inputSchema={"type":"object","properties":{"salesId":{"type":"string"},"packingSlipId":{"type":"string"},"hardwareProfileId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["salesId","packingSlipId","hardwareProfileId"]}),
            Tool(name="fulfillment_get_picking_lists", description="Gets picking lists.", inputSchema={"type":"object","properties":{"pickingListFulfillmentLines":{"type":"array"},"hardwareProfileId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["pickingListFulfillmentLines","hardwareProfileId"]}),
            Tool(name="sales_orders_fulfillment_reject_fulfillment_lines", description="Rejects fulfillment lines.", inputSchema={"type":"object","properties":{"fulfillmentLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["fulfillmentLines"]}),
            Tool(name="sales_orders_fulfillment_get_packing_slips_data", description="Gets list of packing slip data by sales id.", inputSchema={"type":"object","properties":{"salesId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["salesId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/SalesOrdersFulfillment/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
