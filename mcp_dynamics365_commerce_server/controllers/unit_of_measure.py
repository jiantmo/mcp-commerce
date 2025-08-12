from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class UnitOfMeasureController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="unit_of_measure_get_units_of_measure", description="Get all units of measure supported by the store.", inputSchema={"type":"object","properties":{"queryResultSettings":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/UnitOfMeasure/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"units": []}}
