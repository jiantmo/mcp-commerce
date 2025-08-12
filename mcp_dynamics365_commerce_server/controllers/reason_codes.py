"""
Reason Codes Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (3 total):
1. reason_codes_get_reason_codes - Gets the reason codes
2. reason_codes_get_return_order_reason_codes - Gets return order reason codes
3. reason_codes_get_reason_codes_by_id - Gets the reason codes by group or single identifier

This controller handles reason code operations for various business processes.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class ReasonCodesController:
    """Controller for Reason Codes-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of reason codes-related tools"""
        return [
            Tool(
                name="reason_codes_get_reason_codes",
                description="Gets the reason codes",
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="reason_codes_get_return_order_reason_codes",
                description="Gets return order reason codes",
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="reason_codes_get_reason_codes_by_id",
                description="Gets the reason codes by group or single identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "reasonCodeGroupId": {
                            "type": "string",
                            "description": "Reason code group identifier or single reason code ID"
                        },
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["reasonCodeGroupId"]
                }
            )
        ]
    
    def _get_all_reason_codes_data(self) -> List[Dict[str, Any]]:
        """Get mock reason codes data"""
        return [
            # Discount reason codes
            {
                "reasonCodeId": "DISC_MANAGER",
                "reasonCodeName": "Manager Discount",
                "description": "Manager approved discount",
                "groupId": "DISCOUNTS",
                "groupName": "Discount Reasons",
                "reasonCodeType": "Discount",
                "isActive": True,
                "requiresApproval": True,
                "maxDiscountPercent": 25.0,
                "displayOrder": 1,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "DISC_EMPLOYEE",
                "reasonCodeName": "Employee Discount",
                "description": "Employee discount applied",
                "groupId": "DISCOUNTS",
                "groupName": "Discount Reasons",
                "reasonCodeType": "Discount",
                "isActive": True,
                "requiresApproval": False,
                "maxDiscountPercent": 15.0,
                "displayOrder": 2,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "DISC_DAMAGED",
                "reasonCodeName": "Damaged Item",
                "description": "Item has damage requiring discount",
                "groupId": "DISCOUNTS",
                "groupName": "Discount Reasons",
                "reasonCodeType": "Discount",
                "isActive": True,
                "requiresApproval": True,
                "maxDiscountPercent": 50.0,
                "displayOrder": 3,
                "canBeOverridden": False
            },
            # Return reason codes
            {
                "reasonCodeId": "RET_DEFECTIVE",
                "reasonCodeName": "Defective Product",
                "description": "Product is defective or malfunctioning",
                "groupId": "RETURNS",
                "groupName": "Return Reasons",
                "reasonCodeType": "Return",
                "isActive": True,
                "requiresApproval": False,
                "allowRefund": True,
                "allowExchange": True,
                "displayOrder": 1,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "RET_WRONG_SIZE",
                "reasonCodeName": "Wrong Size",
                "description": "Customer selected wrong size",
                "groupId": "RETURNS",
                "groupName": "Return Reasons",
                "reasonCodeType": "Return",
                "isActive": True,
                "requiresApproval": False,
                "allowRefund": True,
                "allowExchange": True,
                "displayOrder": 2,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "RET_NOT_SATISFIED",
                "reasonCodeName": "Not Satisfied",
                "description": "Customer not satisfied with product",
                "groupId": "RETURNS",
                "groupName": "Return Reasons",
                "reasonCodeType": "Return",
                "isActive": True,
                "requiresApproval": False,
                "allowRefund": True,
                "allowExchange": True,
                "displayOrder": 3,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "RET_CHANGED_MIND",
                "reasonCodeName": "Changed Mind",
                "description": "Customer changed their mind",
                "groupId": "RETURNS",
                "groupName": "Return Reasons",
                "reasonCodeType": "Return",
                "isActive": True,
                "requiresApproval": False,
                "allowRefund": False,
                "allowExchange": True,
                "displayOrder": 4,
                "canBeOverridden": False
            },
            # Void reason codes
            {
                "reasonCodeId": "VOID_CUSTOMER_REQUEST",
                "reasonCodeName": "Customer Request",
                "description": "Customer requested to void transaction",
                "groupId": "VOIDS",
                "groupName": "Void Reasons",
                "reasonCodeType": "Void",
                "isActive": True,
                "requiresApproval": True,
                "displayOrder": 1,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "VOID_PRICING_ERROR",
                "reasonCodeName": "Pricing Error",
                "description": "Incorrect pricing on transaction",
                "groupId": "VOIDS",
                "groupName": "Void Reasons",
                "reasonCodeType": "Void",
                "isActive": True,
                "requiresApproval": True,
                "displayOrder": 2,
                "canBeOverridden": False
            },
            # Cash management reason codes
            {
                "reasonCodeId": "CASH_SHORTAGE",
                "reasonCodeName": "Cash Shortage",
                "description": "Cash drawer shortage",
                "groupId": "CASH_MGMT",
                "groupName": "Cash Management",
                "reasonCodeType": "CashManagement",
                "isActive": True,
                "requiresApproval": True,
                "displayOrder": 1,
                "canBeOverridden": False
            },
            {
                "reasonCodeId": "CASH_OVERAGE",
                "reasonCodeName": "Cash Overage",
                "description": "Cash drawer overage",
                "groupId": "CASH_MGMT",
                "groupName": "Cash Management", 
                "reasonCodeType": "CashManagement",
                "isActive": True,
                "requiresApproval": True,
                "displayOrder": 2,
                "canBeOverridden": False
            }
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle reason codes tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "reason_codes_get_reason_codes":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get all reason codes
            all_reason_codes = self._get_all_reason_codes_data()
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "displayOrder")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["reasonCodeName", "reasonCodeId", "description", "groupName"]:
                    all_reason_codes.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["displayOrder"]:
                    all_reason_codes.sort(key=lambda x: (x.get("groupId", ""), x.get(column_name, 0)), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_codes = all_reason_codes[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/ReasonCodes",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_reason_codes),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_reason_codes),
                    "hasPreviousPage": skip > 0,
                    "results": paged_codes
                },
                "reasonCodes": paged_codes,
                "totalCount": len(all_reason_codes),
                "groupsSummary": {
                    "DISCOUNTS": len([rc for rc in all_reason_codes if rc["groupId"] == "DISCOUNTS"]),
                    "RETURNS": len([rc for rc in all_reason_codes if rc["groupId"] == "RETURNS"]),
                    "VOIDS": len([rc for rc in all_reason_codes if rc["groupId"] == "VOIDS"]),
                    "CASH_MGMT": len([rc for rc in all_reason_codes if rc["groupId"] == "CASH_MGMT"])
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<ReasonCode>",
                    "description": "Gets the reason codes"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "reason_codes_get_return_order_reason_codes":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get only return reason codes
            all_reason_codes = self._get_all_reason_codes_data()
            return_codes = [rc for rc in all_reason_codes if rc["reasonCodeType"] == "Return"]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "displayOrder")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["reasonCodeName", "reasonCodeId", "description"]:
                    return_codes.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["displayOrder"]:
                    return_codes.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_codes = return_codes[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/ReasonCodes/ReturnOrder",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(return_codes),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(return_codes),
                    "hasPreviousPage": skip > 0,
                    "results": paged_codes
                },
                "reasonCodes": paged_codes,
                "totalCount": len(return_codes),
                "returnSummary": {
                    "allowRefundCount": len([rc for rc in return_codes if rc.get("allowRefund", False)]),
                    "allowExchangeCount": len([rc for rc in return_codes if rc.get("allowExchange", False)]),
                    "requireApprovalCount": len([rc for rc in return_codes if rc.get("requiresApproval", False)])
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<ReasonCode>",
                    "description": "Gets return order reason codes"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "reason_codes_get_reason_codes_by_id":
            reason_code_group_id = arguments.get("reasonCodeGroupId", "DISCOUNTS")
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get reason codes by group or single ID
            all_reason_codes = self._get_all_reason_codes_data()
            
            # Check if it's a single reason code ID or group ID
            single_code = next((rc for rc in all_reason_codes if rc["reasonCodeId"] == reason_code_group_id), None)
            if single_code:
                filtered_codes = [single_code]
            else:
                filtered_codes = [rc for rc in all_reason_codes if rc["groupId"] == reason_code_group_id]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "displayOrder")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["reasonCodeName", "reasonCodeId", "description"]:
                    filtered_codes.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["displayOrder"]:
                    filtered_codes.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_codes = filtered_codes[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/ReasonCodes/{reason_code_group_id}",
                "reasonCodeGroupId": reason_code_group_id,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(filtered_codes),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(filtered_codes),
                    "hasPreviousPage": skip > 0,
                    "results": paged_codes
                },
                "reasonCodes": paged_codes,
                "totalCount": len(filtered_codes),
                "isSingleCode": single_code is not None,
                "groupInfo": {
                    "groupId": filtered_codes[0]["groupId"] if filtered_codes else None,
                    "groupName": filtered_codes[0]["groupName"] if filtered_codes else None,
                    "reasonCodeType": filtered_codes[0]["reasonCodeType"] if filtered_codes else None
                } if filtered_codes else None,
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<ReasonCode>",
                    "description": "Gets the reason codes by group or single identifier"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown reason codes tool: {name}"}