from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class WarehouseController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="warehouse_get_warehouse_by_id", description="Gets a Warehouse by identifier.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["inventLocation"]}),
            Tool(name="warehouse_search_warehouses", description="Search warehouses by text.", inputSchema={"type":"object","properties":{"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["searchText"]}),
            Tool(name="warehouse_get_locations", description="Gets warehouse locations.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["inventLocation"]}),
            Tool(name="warehouse_search_locations", description="Search warehouse locations.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["inventLocation","searchText"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Warehouse/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
