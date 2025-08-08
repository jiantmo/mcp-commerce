"""
Address Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. address_get_address_purposes - Gets the address purposes

This controller handles address-related operations including address purpose management
and address validation functionality.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class AddressController:
    """Controller for Address-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of address-related tools"""
        return [
            Tool(
                name="address_get_address_purposes",
                description="Gets the address purposes",
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
        """Handle address tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "address_get_address_purposes":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock address purposes data
            all_purposes = [
                {
                    "addressPurposeId": "HOME",
                    "name": "Home",
                    "description": "Primary residential address",
                    "isActive": True,
                    "displayOrder": 1,
                    "isDefault": True,
                    "allowMultiple": False,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "BUSINESS",
                    "name": "Business",
                    "description": "Business or work address",
                    "isActive": True,
                    "displayOrder": 2,
                    "isDefault": False,
                    "allowMultiple": True,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "SHIPPING",
                    "name": "Shipping",
                    "description": "Shipping and delivery address",
                    "isActive": True,
                    "displayOrder": 3,
                    "isDefault": False,
                    "allowMultiple": True,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "BILLING",
                    "name": "Billing",
                    "description": "Billing and invoice address",
                    "isActive": True,
                    "displayOrder": 4,
                    "isDefault": False,
                    "allowMultiple": False,
                    "isRequired": True,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "PICKUP",
                    "name": "Pickup",
                    "description": "Store pickup location",
                    "isActive": True,
                    "displayOrder": 5,
                    "isDefault": False,
                    "allowMultiple": True,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "GIFT",
                    "name": "Gift Delivery",
                    "description": "Gift recipient delivery address",
                    "isActive": True,
                    "displayOrder": 6,
                    "isDefault": False,
                    "allowMultiple": True,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "EMERGENCY",
                    "name": "Emergency Contact",
                    "description": "Emergency contact address",
                    "isActive": True,
                    "displayOrder": 7,
                    "isDefault": False,
                    "allowMultiple": False,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                },
                {
                    "addressPurposeId": "TEMP",
                    "name": "Temporary",
                    "description": "Temporary address",
                    "isActive": False,
                    "displayOrder": 8,
                    "isDefault": False,
                    "allowMultiple": True,
                    "isRequired": False,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": "2024-01-15T10:30:00Z"
                }
            ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "displayOrder")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["name", "description", "addressPurposeId"]:
                    all_purposes.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["displayOrder"]:
                    all_purposes.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["isActive", "isDefault", "isRequired", "allowMultiple"]:
                    all_purposes.sort(key=lambda x: x.get(column_name, False), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_purposes = all_purposes[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Addresses/GetAddressPurposes",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_purposes),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_purposes),
                    "hasPreviousPage": skip > 0,
                    "results": paged_purposes
                },
                "addressPurposes": paged_purposes,
                "totalCount": len(all_purposes),
                "activeCount": len([p for p in all_purposes if p["isActive"]]),
                "defaultPurpose": next((p for p in all_purposes if p["isDefault"]), None),
                "requiredPurposes": [p for p in all_purposes if p["isRequired"]],
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<AddressPurpose>",
                    "description": "Gets the address purposes with paging and sorting support"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown address tool: {name}"}