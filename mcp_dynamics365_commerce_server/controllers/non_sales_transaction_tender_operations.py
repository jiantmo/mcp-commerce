from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class NonSalesTransactionTenderOperationsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="non_sales_tender_get_transactions", description="Gets non-sales transactions.", inputSchema={"type":"object","properties":{"shiftId":{"type":"string"},"shiftTerminalId":{"type":"string"},"nonSalesTenderTypeValue":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["shiftId","shiftTerminalId","nonSalesTenderTypeValue"]}),
            Tool(name="non_sales_tender_create_transaction", description="Creates non-sales transaction.", inputSchema={"type":"object","properties":{"nonSalesTransaction":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["nonSalesTransaction"]}),
            Tool(name="non_sales_tender_get_affiliations", description="Gets affiliations.", inputSchema={"type":"object","properties":{"queryResultSettings":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/NonSalesTransactionTenderOperations/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
