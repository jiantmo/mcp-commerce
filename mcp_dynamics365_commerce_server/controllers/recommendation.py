from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class RecommendationController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="recommendation_get", description="Gets the list of recommendations.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":[]}),
            Tool(name="recommendation_get_elements", description="Gets recommended elements by list and criteria.", inputSchema={"type":"object","properties":{"listId":{"type":"string"},"criteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["listId","criteria"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Recommendation/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"recommendations": []}}
