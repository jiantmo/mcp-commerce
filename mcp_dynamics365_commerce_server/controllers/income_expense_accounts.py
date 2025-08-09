from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class IncomeExpenseAccountsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="income_expense_accounts_get_income_expense_accounts", description="Gets income or expense accounts.", inputSchema={"type":"object","properties":{"incomeExpenseAccountType":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["incomeExpenseAccountType"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/IncomeExpenseAccounts/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"accounts": []}}
