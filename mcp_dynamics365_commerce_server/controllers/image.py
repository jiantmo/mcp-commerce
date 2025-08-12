from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class ImageController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="image_get_image_blob", description="Gets image blob by image identifier.", inputSchema={"type":"object","properties":{"imageId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["imageId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/Image/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"imageId": arguments.get("imageId"), "contentType": "image/jpeg"}}
