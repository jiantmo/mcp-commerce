"""
Customer Group Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. customer_group_get_customer_groups - Gets collection of customer group

This controller handles customer group operations for customer categorization and targeting.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class CustomerGroupController:
    """Controller for Customer Group-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of customer group-related tools"""
        return [
            Tool(
                name="customer_group_get_customer_groups",
                description="Gets collection of customer group",
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
        """Handle customer group tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "customer_group_get_customer_groups":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock customer groups data
            all_customer_groups = [
                {
                    "customerGroupId": "RETAIL",
                    "customerGroupName": "Retail Customers",
                    "description": "Regular retail customers",
                    "isActive": True,
                    "isDefault": True,
                    "customerCount": 15420,
                    "discountGroup": "RETAIL_DISC",
                    "priceGroup": "RETAIL_PRICE",
                    "taxGroup": "STANDARD_TAX",
                    "paymentTerms": "Net30",
                    "creditLimit": 5000.00,
                    "currency": "USD",
                    "allowCreditHold": True,
                    "requireApprovalForCredit": False,
                    "autoApplyDiscounts": True,
                    "loyaltyProgram": "REWARDS_PLUS",
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "VIP",
                    "customerGroupName": "VIP Customers",
                    "description": "High-value VIP customers",
                    "isActive": True,
                    "isDefault": False,
                    "customerCount": 892,
                    "discountGroup": "VIP_DISC",
                    "priceGroup": "VIP_PRICE",
                    "taxGroup": "PREMIUM_TAX",
                    "paymentTerms": "Net15",
                    "creditLimit": 25000.00,
                    "currency": "USD",
                    "allowCreditHold": False,
                    "requireApprovalForCredit": False,
                    "autoApplyDiscounts": True,
                    "loyaltyProgram": "VIP_REWARDS",
                    "minimumSpend": 10000.00,
                    "specialBenefits": ["Free shipping", "Priority support", "Exclusive offers"],
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "WHOLESALE",
                    "customerGroupName": "Wholesale Customers",
                    "description": "Bulk purchase wholesale customers",
                    "isActive": True,
                    "isDefault": False,
                    "customerCount": 234,
                    "discountGroup": "WHOLESALE_DISC",
                    "priceGroup": "WHOLESALE_PRICE",
                    "taxGroup": "WHOLESALE_TAX",
                    "paymentTerms": "Net60",
                    "creditLimit": 100000.00,
                    "currency": "USD",
                    "allowCreditHold": True,
                    "requireApprovalForCredit": True,
                    "autoApplyDiscounts": True,
                    "minimumOrderQuantity": 100,
                    "volumeDiscountTier": "TIER_3",
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "EMPLOYEE",
                    "customerGroupName": "Employee Customers",
                    "description": "Company employees",
                    "isActive": True,
                    "isDefault": False,
                    "customerCount": 156,
                    "discountGroup": "EMPLOYEE_DISC",
                    "priceGroup": "EMPLOYEE_PRICE",
                    "taxGroup": "EMPLOYEE_TAX",
                    "paymentTerms": "Immediate",
                    "creditLimit": 2000.00,
                    "currency": "USD",
                    "allowCreditHold": False,
                    "requireApprovalForCredit": False,
                    "autoApplyDiscounts": True,
                    "employeeDiscountPercent": 15.0,
                    "maxEmployeeDiscount": 500.00,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "STUDENT",
                    "customerGroupName": "Student Customers",
                    "description": "Students with valid ID",
                    "isActive": True,
                    "isDefault": False,
                    "customerCount": 1847,
                    "discountGroup": "STUDENT_DISC",
                    "priceGroup": "STUDENT_PRICE",
                    "taxGroup": "STANDARD_TAX",
                    "paymentTerms": "Immediate",
                    "creditLimit": 1000.00,
                    "currency": "USD",
                    "allowCreditHold": True,
                    "requireApprovalForCredit": True,
                    "autoApplyDiscounts": True,
                    "studentDiscountPercent": 10.0,
                    "verificationRequired": True,
                    "validationPeriod": 365,  # days
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "SENIOR",
                    "customerGroupName": "Senior Citizens",
                    "description": "Senior citizen customers (65+)",
                    "isActive": True,
                    "isDefault": False,
                    "customerCount": 743,
                    "discountGroup": "SENIOR_DISC",
                    "priceGroup": "SENIOR_PRICE",
                    "taxGroup": "STANDARD_TAX",
                    "paymentTerms": "Net30",
                    "creditLimit": 3000.00,
                    "currency": "USD",
                    "allowCreditHold": True,
                    "requireApprovalForCredit": False,
                    "autoApplyDiscounts": True,
                    "seniorDiscountPercent": 5.0,
                    "ageVerificationRequired": True,
                    "minimumAge": 65,
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                },
                {
                    "customerGroupId": "INACTIVE",
                    "customerGroupName": "Inactive Customers",
                    "description": "Inactive or suspended customers",
                    "isActive": False,
                    "isDefault": False,
                    "customerCount": 423,
                    "discountGroup": None,
                    "priceGroup": "RETAIL_PRICE",
                    "taxGroup": "STANDARD_TAX",
                    "paymentTerms": "Immediate",
                    "creditLimit": 0.00,
                    "currency": "USD",
                    "allowCreditHold": True,
                    "requireApprovalForCredit": True,
                    "autoApplyDiscounts": False,
                    "restrictPurchases": True,
                    "reasonForInactive": "Credit issues",
                    "createdDate": "2023-01-01T00:00:00Z",
                    "lastModified": datetime.now().isoformat() + "Z"
                }
            ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "customerGroupName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["customerGroupName", "customerGroupId", "description"]:
                    all_customer_groups.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["customerCount", "creditLimit"]:
                    all_customer_groups.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["isActive", "isDefault"]:
                    all_customer_groups.sort(key=lambda x: x.get(column_name, False), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_groups = all_customer_groups[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CustomerGroups",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_customer_groups),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_customer_groups),
                    "hasPreviousPage": skip > 0,
                    "results": paged_groups
                },
                "customerGroups": paged_groups,
                "totalCount": len(all_customer_groups),
                "summary": {
                    "activeGroups": len([group for group in all_customer_groups if group["isActive"]]),
                    "totalCustomers": sum(group["customerCount"] for group in all_customer_groups),
                    "defaultGroup": next((group for group in all_customer_groups if group.get("isDefault", False)), None),
                    "averageCreditLimit": sum(group["creditLimit"] for group in all_customer_groups) / len(all_customer_groups),
                    "groupsWithDiscounts": len([group for group in all_customer_groups if group.get("discountGroup")])
                },
                "groupCategories": {
                    "retail": ["RETAIL"],
                    "premium": ["VIP"],
                    "business": ["WHOLESALE"],
                    "special": ["EMPLOYEE", "STUDENT", "SENIOR"],
                    "inactive": ["INACTIVE"]
                },
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<CustomerGroup>",
                    "description": "Gets collection of customer group"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown customer group tool: {name}"}