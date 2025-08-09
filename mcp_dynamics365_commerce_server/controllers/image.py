from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool

class ImageController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="image_get_image_blob", description="Gets image blob by image identifier.", inputSchema={"type":"object","properties":{"imageId":{"type":"number"},"baseUrl":{"type":"string","default":"https://your-commerce-site.com"}},"required":["imageId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl","https://your-commerce-site.com")
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Image/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"imageId": arguments.get("imageId"), "contentType": "image/jpeg"}}
