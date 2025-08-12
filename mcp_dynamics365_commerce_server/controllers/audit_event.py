from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class AuditEventController:
    """Controller for Audit event API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="audit_event_register_audit_event", description="Performs the audit event saving operation.", inputSchema={"type":"object","properties":{"auditEvent":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["auditEvent"]}),
            Tool(name="audit_event_register_and_get_audit_event", description="Saves the audit event and returns it.", inputSchema={"type":"object","properties":{"auditEvent":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["auditEvent"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/AuditEvent/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"saved": True, "event": arguments.get("auditEvent")}
        }
