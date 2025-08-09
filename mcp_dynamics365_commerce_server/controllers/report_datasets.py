from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class ReportDatasetsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="report_datasets_search_report_data_set", description="Searches report datasets.", inputSchema={"type":"object","properties":{"receiptTransactionType":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="report_datasets_get_report_data_set_by_id", description="Gets report dataset by id.", inputSchema={"type":"object","properties":{"salesOrderToPrint":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["salesOrderToPrint"]}),
            Tool(name="report_datasets_get_srs_report_data_set", description="Gets SSRS report dataset.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/ReportDatasets/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"dataset": {}}}
