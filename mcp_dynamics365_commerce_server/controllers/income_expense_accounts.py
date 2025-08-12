from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class IncomeExpenseAccountsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="income_expense_get_accounts", description="Gets income or expense accounts.", inputSchema={"type":"object","properties":{"incomeExpenseAccountType":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["incomeExpenseAccountType"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/IncomeExpenseAccounts/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"accounts": []}}
