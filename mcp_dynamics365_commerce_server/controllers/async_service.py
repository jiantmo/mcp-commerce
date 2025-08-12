from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class AsyncServiceController:
    """Controller for Async service API operations"""

    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="async_service_get_download_interval", description="Gets download interval.", inputSchema={"type":"object","properties":{"dataStoreName":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dataStoreName"]}),
            Tool(name="async_service_get_upload_interval", description="Gets upload interval.", inputSchema={"type":"object","properties":{"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":[]}),
            Tool(name="async_service_get_terminal_data_store_name", description="Gets data store name.", inputSchema={"type":"object","properties":{"terminalId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["terminalId"]}),
            Tool(name="async_service_get_download_link", description="Gets download link.", inputSchema={"type":"object","properties":{"dataStoreName":{"type":"string"},"downloadSessionId":{"type":"number"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dataStoreName","downloadSessionId"]}),
            Tool(name="async_service_get_download_sessions", description="Gets the download sessions.", inputSchema={"type":"object","properties":{"dataStoreName":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dataStoreName"]}),
            Tool(name="async_service_get_initial_download_sessions", description="Gets initial download sessions.", inputSchema={"type":"object","properties":{"dataStoreName":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dataStoreName"]}),
            Tool(name="async_service_get_upload_job_definitions", description="Gets upload job definitions.", inputSchema={"type":"object","properties":{"dataStoreName":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["dataStoreName"]}),
            Tool(name="async_service_update_download_session", description="Update download session status.", inputSchema={"type":"object","properties":{"downloadSession":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["downloadSession"]}),
            Tool(name="async_service_post_offline_transactions", description="Posts offline transactions.", inputSchema={"type":"object","properties":{"offlineTransactionForMPOS":{"type":"array","items":{"type":"string"}},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["offlineTransactionForMPOS"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url = arguments.get("baseUrl", get_base_url())
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/AsyncService/{name}",
            "toolName": name,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name}",
            "mockData": {"result": "Success", "name": name}
        }
