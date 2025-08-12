"""
Tender Types Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (2 total):
1. tender_types_get_tender_types - Gets tender types
2. tender_types_round_amount_by_tender_type - Round amount by tender type

This controller handles tender type operations including retrieval and amount rounding.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url
import math

class TenderTypesController:
    """Controller for Tender Types-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of tender types-related tools"""
        return [
            Tool(
                name="tender_types_get_tender_types",
                description="Gets tender types",
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
                name="tender_types_round_amount_by_tender_type",
                description="Round amount by tender type",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "amount": {
                            "type": "number",
                            "description": "Amount to round"
                        },
                        "tenderTypeId": {
                            "type": "string",
                            "description": "Tender type identifier for rounding rules"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["amount", "tenderTypeId"]
                }
            )
        ]
    
    def _get_tender_types_data(self) -> List[Dict[str, Any]]:
        """Get mock tender types data"""
        return [
            {
                "tenderTypeId": "CASH",
                "tenderTypeName": "Cash",
                "description": "Physical cash payment",
                "isActive": True,
                "allowOverpayment": True,
                "allowUnderpayment": False,
                "roundingMethod": "NearestCent",
                "roundingValue": 0.01,
                "minimumAmount": 0.00,
                "maximumAmount": 10000.00,
                "requiresValidation": False,
                "requiresSignature": False,
                "allowChangeBack": True,
                "changeTenderTypeId": "CASH",
                "currencyCode": "USD",
                "displayOrder": 1
            },
            {
                "tenderTypeId": "CREDIT_CARD",
                "tenderTypeName": "Credit Card", 
                "description": "Credit card payment",
                "isActive": True,
                "allowOverpayment": False,
                "allowUnderpayment": False,
                "roundingMethod": "Exact",
                "roundingValue": 0.01,
                "minimumAmount": 1.00,
                "maximumAmount": 50000.00,
                "requiresValidation": True,
                "requiresSignature": True,
                "allowChangeBack": False,
                "changeTenderTypeId": "CASH",
                "currencyCode": "USD",
                "displayOrder": 2,
                "supportedCards": ["Visa", "MasterCard", "American Express", "Discover"]
            },
            {
                "tenderTypeId": "DEBIT_CARD",
                "tenderTypeName": "Debit Card",
                "description": "Debit card payment",
                "isActive": True,
                "allowOverpayment": False,
                "allowUnderpayment": False,
                "roundingMethod": "Exact",
                "roundingValue": 0.01,
                "minimumAmount": 1.00,
                "maximumAmount": 25000.00,
                "requiresValidation": True,
                "requiresSignature": False,
                "allowChangeBack": True,
                "changeTenderTypeId": "CASH",
                "currencyCode": "USD",
                "displayOrder": 3,
                "supportedCards": ["Visa", "MasterCard"]
            },
            {
                "tenderTypeId": "GIFT_CARD",
                "tenderTypeName": "Gift Card",
                "description": "Store gift card payment",
                "isActive": True,
                "allowOverpayment": False,
                "allowUnderpayment": True,
                "roundingMethod": "Exact",
                "roundingValue": 0.01,
                "minimumAmount": 0.01,
                "maximumAmount": 5000.00,
                "requiresValidation": True,
                "requiresSignature": False,
                "allowChangeBack": False,
                "changeTenderTypeId": None,
                "currencyCode": "USD",
                "displayOrder": 4
            },
            {
                "tenderTypeId": "CHECK",
                "tenderTypeName": "Check",
                "description": "Personal or business check",
                "isActive": False,
                "allowOverpayment": False,
                "allowUnderpayment": False,
                "roundingMethod": "Exact",
                "roundingValue": 0.01,
                "minimumAmount": 10.00,
                "maximumAmount": 5000.00,
                "requiresValidation": True,
                "requiresSignature": True,
                "allowChangeBack": True,
                "changeTenderTypeId": "CASH",
                "currencyCode": "USD",
                "displayOrder": 5
            },
            {
                "tenderTypeId": "LOYALTY_POINTS",
                "tenderTypeName": "Loyalty Points",
                "description": "Reward points redemption",
                "isActive": True,
                "allowOverpayment": False,
                "allowUnderpayment": True,
                "roundingMethod": "WholePoints",
                "roundingValue": 1.00,
                "minimumAmount": 1.00,
                "maximumAmount": 1000.00,
                "requiresValidation": True,
                "requiresSignature": False,
                "allowChangeBack": False,
                "changeTenderTypeId": None,
                "currencyCode": "USD",
                "displayOrder": 6,
                "pointsConversionRate": 0.01  # 100 points = $1.00
            }
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle tender types tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "tender_types_get_tender_types":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get all tender types
            all_tender_types = self._get_tender_types_data()
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "displayOrder")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["tenderTypeName", "tenderTypeId", "description"]:
                    all_tender_types.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["displayOrder", "minimumAmount", "maximumAmount"]:
                    all_tender_types.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["isActive", "allowOverpayment", "requiresValidation"]:
                    all_tender_types.sort(key=lambda x: x.get(column_name, False), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_tender_types = all_tender_types[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/TenderTypes",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_tender_types),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_tender_types),
                    "hasPreviousPage": skip > 0,
                    "results": paged_tender_types
                },
                "tenderTypes": paged_tender_types,
                "totalCount": len(all_tender_types),
                "activeCount": len([tt for tt in all_tender_types if tt["isActive"]]),
                "summary": {
                    "cashEnabled": any(tt["tenderTypeId"] == "CASH" and tt["isActive"] for tt in all_tender_types),
                    "cardPaymentEnabled": any(tt["tenderTypeId"] in ["CREDIT_CARD", "DEBIT_CARD"] and tt["isActive"] for tt in all_tender_types),
                    "giftCardEnabled": any(tt["tenderTypeId"] == "GIFT_CARD" and tt["isActive"] for tt in all_tender_types),
                    "loyaltyPointsEnabled": any(tt["tenderTypeId"] == "LOYALTY_POINTS" and tt["isActive"] for tt in all_tender_types)
                },
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<TenderType>",
                    "description": "Gets tender types"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "tender_types_round_amount_by_tender_type":
            amount = arguments.get("amount", 0.00)
            tender_type_id = arguments.get("tenderTypeId", "CASH")
            
            # Get tender type details
            tender_types = self._get_tender_types_data()
            tender_type = next((tt for tt in tender_types if tt["tenderTypeId"] == tender_type_id), tender_types[0])
            
            # Apply rounding based on tender type rules
            rounding_method = tender_type.get("roundingMethod", "Exact")
            rounding_value = tender_type.get("roundingValue", 0.01)
            
            if rounding_method == "NearestCent":
                rounded_amount = round(amount, 2)
            elif rounding_method == "Exact":
                rounded_amount = amount
            elif rounding_method == "WholePoints":
                # Round to nearest whole point value
                rounded_amount = round(amount / rounding_value) * rounding_value
            elif rounding_method == "RoundUp":
                rounded_amount = math.ceil(amount / rounding_value) * rounding_value
            elif rounding_method == "RoundDown":
                rounded_amount = math.floor(amount / rounding_value) * rounding_value
            else:
                rounded_amount = round(amount, 2)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/TenderTypes/{tender_type_id}/RoundAmount",
                "originalAmount": amount,
                "roundedAmount": round(rounded_amount, 2),
                "tenderTypeId": tender_type_id,
                "tenderTypeName": tender_type.get("tenderTypeName", "Unknown"),
                "roundingMethod": rounding_method,
                "roundingValue": rounding_value,
                "roundingDifference": round(rounded_amount - amount, 2),
                "currency": tender_type.get("currencyCode", "USD"),
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "decimal", 
                    "description": "Round amount by tender type"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown tender types tool: {name}"}