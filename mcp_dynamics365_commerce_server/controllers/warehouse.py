from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class WarehouseController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="warehouse_get_warehouse_by_id", description="Gets a Warehouse by identifier.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["inventLocation"]}),
            Tool(name="warehouse_search_warehouses", description="Search warehouses by text.", inputSchema={"type":"object","properties":{"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["searchText"]}),
            Tool(name="warehouse_get_locations", description="Gets warehouse locations.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["inventLocation"]}),
            Tool(name="warehouse_search_locations", description="Search warehouse locations.", inputSchema={"type":"object","properties":{"inventLocation":{"type":"string"},"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["inventLocation","searchText"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Warehouse/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
