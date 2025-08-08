"""
Suspended Cart Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. suspended_cart_get_all_suspended_carts - Gets all suspended carts

This controller handles suspended cart operations including retrieval and management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
from mcp.types import Tool

class SuspendedCartController:
    """Controller for Suspended Cart-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of suspended cart-related tools"""
        return [
            Tool(
                name="suspended_cart_get_all_suspended_carts",
                description="Gets all suspended carts",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "queryResultSettings": {
                            "type": "object",
                            "description": "Query result settings for paging and sorting",
                            "properties": {
                                "paging": {
                                    "type": "object",
                                    "properties": {
                                        "skip": {"type": "number", "description": "Number of records to skip", "default": 0},
                                        "top": {"type": "number", "description": "Number of records to take", "default": 50}
                                    }
                                },
                                "sorting": {
                                    "type": "object",
                                    "properties": {
                                        "columns": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "columnName": {"type": "string"},
                                                    "isDescending": {"type": "boolean", "default": False}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": []
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle suspended cart tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "suspended_cart_get_all_suspended_carts":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock suspended carts data
            all_suspended_carts = [
                {
                    "suspendedCartId": "SUSP001",
                    "cartId": "CART001",
                    "customerId": "CUST001",
                    "customerName": "John Doe",
                    "employeeId": "EMP001",
                    "employeeName": "Store Associate",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "terminalId": "TERM001",
                    "suspendedDate": (datetime.now() - timedelta(hours=2)).isoformat() + "Z",
                    "suspendedReason": "Customer will return later",
                    "totalAmount": 125.99,
                    "currency": "USD",
                    "itemCount": 3,
                    "status": "Suspended",
                    "expiryDate": (datetime.now() + timedelta(days=7)).isoformat() + "Z",
                    "canResume": True,
                    "cartLines": [
                        {
                            "lineId": "LINE001",
                            "productId": "PROD001",
                            "productName": "Wireless Headphones",
                            "quantity": 1,
                            "unitPrice": 99.99,
                            "totalPrice": 99.99
                        },
                        {
                            "lineId": "LINE002", 
                            "productId": "PROD002",
                            "productName": "Phone Case",
                            "quantity": 2,
                            "unitPrice": 13.00,
                            "totalPrice": 26.00
                        }
                    ]
                },
                {
                    "suspendedCartId": "SUSP002",
                    "cartId": "CART002", 
                    "customerId": "CUST002",
                    "customerName": "Jane Smith",
                    "employeeId": "EMP002",
                    "employeeName": "Store Manager",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "terminalId": "TERM002",
                    "suspendedDate": (datetime.now() - timedelta(days=1)).isoformat() + "Z",
                    "suspendedReason": "Lunch break",
                    "totalAmount": 89.50,
                    "currency": "USD",
                    "itemCount": 2,
                    "status": "Suspended",
                    "expiryDate": (datetime.now() + timedelta(days=6)).isoformat() + "Z",
                    "canResume": True,
                    "cartLines": [
                        {
                            "lineId": "LINE003",
                            "productId": "PROD003",
                            "productName": "Bluetooth Speaker",
                            "quantity": 1,
                            "unitPrice": 89.50,
                            "totalPrice": 89.50
                        }
                    ]
                }
            ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "suspendedDate")
                is_descending = sort_column.get("isDescending", True)  # Default to newest first
                
                if column_name in ["suspendedDate", "expiryDate"]:
                    all_suspended_carts.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["totalAmount"]:
                    all_suspended_carts.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["customerName", "employeeName"]:
                    all_suspended_carts.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_carts = all_suspended_carts[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/SuspendedCarts",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_suspended_carts),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_suspended_carts),
                    "hasPreviousPage": skip > 0,
                    "results": paged_carts
                },
                "suspendedCarts": paged_carts,
                "totalCount": len(all_suspended_carts),
                "summary": {
                    "totalValue": sum(cart["totalAmount"] for cart in all_suspended_carts),
                    "totalItems": sum(cart["itemCount"] for cart in all_suspended_carts),
                    "resumableCount": len([cart for cart in all_suspended_carts if cart["canResume"]]),
                    "nearExpiry": len([cart for cart in all_suspended_carts if datetime.fromisoformat(cart["expiryDate"].replace("Z", "")) < datetime.now() + timedelta(days=1)])
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<SuspendedCart>",
                    "description": "Gets all suspended carts"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown suspended cart tool: {name}"}