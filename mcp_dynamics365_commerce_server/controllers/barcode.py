"""
Barcode Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. barcode_get_barcode_by_id - Gets barcode by identifier

This controller handles barcode-related operations including barcode retrieval and validation.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class BarcodeController:
    """Controller for Barcode-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of barcode-related tools"""
        return [
            Tool(
                name="barcode_get_barcode_by_id",
                description="Gets barcode by identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "barcodeId": {
                            "type": "string",
                            "description": "Barcode identifier to retrieve"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["barcodeId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle barcode tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "barcode_get_barcode_by_id":
            barcode_id = arguments.get("barcodeId", "123456789012")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Barcodes/{barcode_id}",
                "barcodeId": barcode_id,
                "barcode": {
                    "barcodeId": barcode_id,
                    "productId": f"PROD_{random.randint(1000, 9999)}",
                    "productName": "Sample Product",
                    "variantId": f"VAR_{random.randint(100, 999)}",
                    "unitId": "ea",
                    "barcodeType": "EAN13",
                    "isActive": True,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z",
                    "price": round(random.uniform(5.0, 200.0), 2),
                    "currency": "USD",
                    "inventoryStatus": "InStock",
                    "quantity": random.randint(1, 100),
                    "category": "Electronics",
                    "brand": "Sample Brand",
                    "description": "Product retrieved by barcode scan",
                    "dimensions": {
                        "length": 10.5,
                        "width": 7.2,
                        "height": 3.1,
                        "weight": 0.8
                    },
                    "attributes": {
                        "color": "Black",
                        "size": "Medium",
                        "material": "Plastic"
                    }
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "Barcode",
                    "description": "Gets barcode by identifier"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown barcode tool: {name}"}