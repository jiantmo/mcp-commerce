"""
Cash Declaration Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. cash_declaration_get_cash_declarations - Gets cash declarations with paging support

This controller handles cash declaration operations including cash counting and declaration management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
from mcp.types import Tool

class CashDeclarationController:
    """Controller for Cash Declaration-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of cash declaration-related tools"""
        return [
            Tool(
                name="cash_declaration_get_cash_declarations",
                description="Gets cash declarations with paging support",
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
        """Handle cash declaration tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "cash_declaration_get_cash_declarations":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock cash declarations data
            all_declarations = [
                {
                    "declarationId": "DECL001",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "employeeId": "EMP001",
                    "employeeName": "John Smith",
                    "shiftId": "SHIFT001",
                    "registerId": "REG001",
                    "declarationType": "StartOfShift",
                    "declarationDate": "2024-01-10T09:00:00Z",
                    "totalAmount": 200.00,
                    "currency": "USD",
                    "denominations": [
                        {"denomination": 100.00, "count": 1, "total": 100.00},
                        {"denomination": 50.00, "count": 1, "total": 50.00},
                        {"denomination": 20.00, "count": 2, "total": 40.00},
                        {"denomination": 10.00, "count": 1, "total": 10.00}
                    ],
                    "status": "Completed",
                    "notes": "Opening cash count"
                },
                {
                    "declarationId": "DECL002",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "employeeId": "EMP001",
                    "employeeName": "John Smith",
                    "shiftId": "SHIFT001",
                    "registerId": "REG001",
                    "declarationType": "CashDrop",
                    "declarationDate": "2024-01-10T14:30:00Z",
                    "totalAmount": 500.00,
                    "currency": "USD",
                    "denominations": [
                        {"denomination": 100.00, "count": 3, "total": 300.00},
                        {"denomination": 50.00, "count": 2, "total": 100.00},
                        {"denomination": 20.00, "count": 5, "total": 100.00}
                    ],
                    "status": "Completed",
                    "notes": "Mid-shift cash drop - exceeded limit"
                },
                {
                    "declarationId": "DECL003",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "employeeId": "EMP001",
                    "employeeName": "John Smith",
                    "shiftId": "SHIFT001",
                    "registerId": "REG001",
                    "declarationType": "EndOfShift",
                    "declarationDate": "2024-01-10T17:30:00Z",
                    "totalAmount": 185.75,
                    "currency": "USD",
                    "denominations": [
                        {"denomination": 100.00, "count": 1, "total": 100.00},
                        {"denomination": 20.00, "count": 3, "total": 60.00},
                        {"denomination": 10.00, "count": 2, "total": 20.00},
                        {"denomination": 5.00, "count": 1, "total": 5.00},
                        {"denomination": 0.75, "count": 1, "total": 0.75}
                    ],
                    "status": "Completed",
                    "notes": "End of shift closing count"
                }
            ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "declarationDate")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["declarationId", "storeId", "employeeId", "declarationType"]:
                    all_declarations.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["totalAmount"]:
                    all_declarations.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["declarationDate"]:
                    all_declarations.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_declarations = all_declarations[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CashDeclarations",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_declarations),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_declarations),
                    "hasPreviousPage": skip > 0,
                    "results": paged_declarations
                },
                "cashDeclarations": paged_declarations,
                "totalCount": len(all_declarations),
                "summary": {
                    "totalDeclaredAmount": sum(decl["totalAmount"] for decl in all_declarations),
                    "declarationsByType": {
                        "StartOfShift": len([d for d in all_declarations if d["declarationType"] == "StartOfShift"]),
                        "CashDrop": len([d for d in all_declarations if d["declarationType"] == "CashDrop"]),
                        "EndOfShift": len([d for d in all_declarations if d["declarationType"] == "EndOfShift"])
                    }
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<CashDeclaration>",
                    "description": "Gets cash declarations with paging support"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown cash declaration tool: {name}"}