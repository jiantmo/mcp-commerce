from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class AttributeController:
    """Controller for Attribute-related API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="attribute_get_attribute_definitions", description="Gets the attribute definitions by an attribute group identifier.", inputSchema={"type":"object","properties":{"attributeDefinitionCriteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["attributeDefinitionCriteria"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/Attribute/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"definitions": [], "criteria": arguments.get("attributeDefinitionCriteria")}
        }
