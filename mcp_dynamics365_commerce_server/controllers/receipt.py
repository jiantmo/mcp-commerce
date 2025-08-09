from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class ReceiptController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="receipt_get_receipt_masks", description="Gets the receipt masks.", inputSchema={"type":"object","properties":{"receiptTransactionType":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="receipt_validate_print_receipt_copy_allowed", description="Validates if receipt copy printing is allowed.", inputSchema={"type":"object","properties":{"salesOrderToPrint":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["salesOrderToPrint"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Receipt/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"valid": True}}
