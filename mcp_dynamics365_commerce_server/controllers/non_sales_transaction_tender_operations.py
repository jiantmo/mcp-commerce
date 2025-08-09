from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class NonSalesTransactionTenderOperationsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="non_sales_transaction_tender_operations_get_non_sales_transactions", description="Gets non-sales transactions.", inputSchema={"type":"object","properties":{"shiftId":{"type":"string"},"shiftTerminalId":{"type":"string"},"nonSalesTenderTypeValue":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["shiftId","shiftTerminalId","nonSalesTenderTypeValue"]}),
            Tool(name="non_sales_transaction_tender_operations_create_non_sales_transaction", description="Creates non-sales transaction.", inputSchema={"type":"object","properties":{"nonSalesTransaction":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["nonSalesTransaction"]}),
            Tool(name="non_sales_transaction_tender_operations_get_affiliations", description="Gets affiliations.", inputSchema={"type":"object","properties":{"queryResultSettings":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/NonSalesTransactionTenderOperations/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
