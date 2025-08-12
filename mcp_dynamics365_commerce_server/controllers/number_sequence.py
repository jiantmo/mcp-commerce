from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class NumberSequenceController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="number_sequence_get_latest_number_sequence", description="Gets the next number sequence for the current terminal.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/NumberSequence/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"sequence": f"SEQ-{datetime.now().strftime('%Y%m%d%H%M%S')}"}}
