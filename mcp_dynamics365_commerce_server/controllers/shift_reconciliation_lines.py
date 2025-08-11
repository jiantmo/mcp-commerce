from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class ShiftReconciliationLinesController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="shift_recon_get_lines", description="Gets shift reconciliation lines.", inputSchema={"type":"object","properties":{"shiftReconciliationLineRetrievalCriteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["shiftReconciliationLineRetrievalCriteria"]}),
            Tool(name="shift_reconciliation_lines_reconcile_lines", description="Reconciles the lines.", inputSchema={"type":"object","properties":{"lines":{"type":"array"},"description":{"type":"string"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["lines"]}),
            Tool(name="shift_reconciliation_lines_undo_reconciliation", description="Undo reconciliation for groups in passed lines.", inputSchema={"type":"object","properties":{"lines":{"type":"array"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["lines"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/ShiftReconciliationLines/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
