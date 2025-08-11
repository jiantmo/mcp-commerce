"""
Delivery Options Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (2 total):
1. delivery_options_get_delivery_options - Get the delivery options for the channel
2. delivery_options_calculate_shipping_cost - Calculate shipping cost for delivery

This controller handles delivery option operations for shipping and fulfillment.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
from mcp.types import Tool

class DeliveryOptionsController:
    """Controller for Delivery Options-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of delivery options-related tools"""
        return [
            Tool(
                name="delivery_options_get_delivery_options",
                description="Get the delivery options for the channel",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "Channel or location identifier"
                        },
                        "shippingAddress": {
                            "type": "object",
                            "description": "Shipping address for delivery options",
                            "properties": {
                                "street": {"type": "string"},
                                "city": {"type": "string"},
                                "state": {"type": "string"},
                                "zipCode": {"type": "string"},
                                "country": {"type": "string"}
                            }
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
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["id", "shippingAddress"]
                }
            ),
            Tool(
                name="delivery_options_calculate_shipping_cost",
                description="Calculate shipping cost for delivery",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "address": {"type": "object"},
                        "items": {"type": "array"},
                        "deliveryMethod": {"type": "string"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["address", "items"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle delivery options tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "delivery_options_get_delivery_options":
            channel_id = arguments.get("id", "CHANNEL001")
            shipping_address = arguments.get("shippingAddress", {})
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            city = shipping_address.get("city", "Seattle")
            state = shipping_address.get("state", "WA")
            country = shipping_address.get("country", "US")
            
            # Generate delivery options based on location
            all_delivery_options = []
            
            # Standard delivery options
            all_delivery_options.extend([
                {
                    "deliveryOptionId": "STANDARD",
                    "deliveryOptionName": "Standard Shipping",
                    "description": "Standard ground shipping",
                    "deliveryMethodCode": "GROUND",
                    "isActive": True,
                    "cost": 5.99,
                    "currency": "USD",
                    "estimatedDeliveryDays": random.randint(3, 7),
                    "minimumDeliveryDays": 3,
                    "maximumDeliveryDays": 7,
                    "estimatedDeliveryDate": (datetime.now() + timedelta(days=5)).isoformat() + "Z",
                    "carrier": "FedEx",
                    "carrierServiceCode": "FDXG",
                    "trackingAvailable": True,
                    "signatureRequired": False,
                    "insuranceIncluded": False,
                    "weightLimit": 150.0,
                    "dimensionLimits": {"length": 108, "width": 165, "height": 165},
                    "availabilityMessage": "Available for this address",
                    "deliveryInstructions": "Leave at door if not home",
                    "businessDaysOnly": True
                },
                {
                    "deliveryOptionId": "EXPRESS",
                    "deliveryOptionName": "Express Shipping",
                    "description": "Fast express delivery",
                    "deliveryMethodCode": "EXPRESS",
                    "isActive": True,
                    "cost": 12.99,
                    "currency": "USD",
                    "estimatedDeliveryDays": 2,
                    "minimumDeliveryDays": 1,
                    "maximumDeliveryDays": 2,
                    "estimatedDeliveryDate": (datetime.now() + timedelta(days=2)).isoformat() + "Z",
                    "carrier": "FedEx",
                    "carrierServiceCode": "FDXE",
                    "trackingAvailable": True,
                    "signatureRequired": False,
                    "insuranceIncluded": True,
                    "weightLimit": 150.0,
                    "dimensionLimits": {"length": 108, "width": 165, "height": 165},
                    "availabilityMessage": "Available for this address",
                    "deliveryInstructions": "Expedited handling",
                    "businessDaysOnly": True
                },
                {
                    "deliveryOptionId": "OVERNIGHT",
                    "deliveryOptionName": "Overnight Shipping",
                    "description": "Next business day delivery",
                    "deliveryMethodCode": "OVERNIGHT",
                    "isActive": True,
                    "cost": 24.99,
                    "currency": "USD",
                    "estimatedDeliveryDays": 1,
                    "minimumDeliveryDays": 1,
                    "maximumDeliveryDays": 1,
                    "estimatedDeliveryDate": (datetime.now() + timedelta(days=1)).isoformat() + "Z",
                    "carrier": "FedEx",
                    "carrierServiceCode": "FDXO",
                    "trackingAvailable": True,
                    "signatureRequired": True,
                    "insuranceIncluded": True,
                    "weightLimit": 150.0,
                    "dimensionLimits": {"length": 108, "width": 165, "height": 165},
                    "availabilityMessage": "Available for next business day",
                    "deliveryInstructions": "Signature required",
                    "businessDaysOnly": True
                }
            ])
            
            # Add local pickup if in supported area
            if state in ["WA", "CA", "OR"]:
                all_delivery_options.append({
                    "deliveryOptionId": "PICKUP",
                    "deliveryOptionName": "Store Pickup",
                    "description": "Pick up at local store",
                    "deliveryMethodCode": "PICKUP",
                    "isActive": True,
                    "cost": 0.00,
                    "currency": "USD",
                    "estimatedDeliveryDays": 0,
                    "minimumDeliveryDays": 0,
                    "maximumDeliveryDays": 1,
                    "estimatedDeliveryDate": (datetime.now() + timedelta(hours=2)).isoformat() + "Z",
                    "carrier": "Store",
                    "carrierServiceCode": "PICKUP",
                    "trackingAvailable": False,
                    "signatureRequired": True,
                    "insuranceIncluded": False,
                    "weightLimit": None,
                    "dimensionLimits": None,
                    "availabilityMessage": "Ready for pickup in 2 hours",
                    "deliveryInstructions": "Bring ID and order confirmation",
                    "businessDaysOnly": False,
                    "pickupLocation": {
                        "storeId": "STORE001",
                        "storeName": "Downtown Store",
                        "address": "123 Main St",
                        "city": city,
                        "state": state,
                        "zipCode": "98101",
                        "phone": "+1-206-555-0100",
                        "hours": "Mon-Sat 9AM-9PM, Sun 10AM-6PM"
                    }
                })
            
            # Add same day delivery for major cities
            if city.lower() in ["seattle", "los angeles", "new york", "chicago", "boston"]:
                all_delivery_options.append({
                    "deliveryOptionId": "SAME_DAY",
                    "deliveryOptionName": "Same Day Delivery",
                    "description": "Delivered today",
                    "deliveryMethodCode": "SAME_DAY",
                    "isActive": True,
                    "cost": 19.99,
                    "currency": "USD",
                    "estimatedDeliveryDays": 0,
                    "minimumDeliveryDays": 0,
                    "maximumDeliveryDays": 0,
                    "estimatedDeliveryDate": (datetime.now() + timedelta(hours=4)).isoformat() + "Z",
                    "carrier": "Local Courier",
                    "carrierServiceCode": "SAME_DAY",
                    "trackingAvailable": True,
                    "signatureRequired": False,
                    "insuranceIncluded": False,
                    "weightLimit": 50.0,
                    "dimensionLimits": {"length": 36, "width": 36, "height": 36},
                    "availabilityMessage": "Available until 2 PM for same day delivery",
                    "deliveryInstructions": "Call when arriving",
                    "businessDaysOnly": False,
                    "cutoffTime": "14:00:00"
                })
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "cost")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["deliveryOptionName", "carrier", "deliveryMethodCode"]:
                    all_delivery_options.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["cost", "estimatedDeliveryDays"]:
                    all_delivery_options.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_options = all_delivery_options[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/DeliveryOptions/{channel_id}",
                "channelId": channel_id,
                "shippingAddress": shipping_address,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_delivery_options),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_delivery_options),
                    "hasPreviousPage": skip > 0,
                    "results": paged_options
                },
                "deliveryOptions": paged_options,
                "totalCount": len(all_delivery_options),
                "summary": {
                    "fastestOption": min(all_delivery_options, key=lambda x: x["estimatedDeliveryDays"]),
                    "cheapestOption": min(all_delivery_options, key=lambda x: x["cost"]),
                    "freeOptions": [opt for opt in all_delivery_options if opt["cost"] == 0.00],
                    "sameDayAvailable": any(opt["deliveryOptionId"] == "SAME_DAY" for opt in all_delivery_options),
                    "pickupAvailable": any(opt["deliveryOptionId"] == "PICKUP" for opt in all_delivery_options)
                },
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<DeliveryOption>",
                    "description": "Get the delivery options for the channel"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "delivery_options_calculate_shipping_cost":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/DeliveryOptions/CalculateShippingCost",
                "shippingCost": round(random.uniform(5.99, 25.99), 2),
                "deliveryTime": "3-5 business days",
                "carrier": "Standard Shipping"
            }
        else:
            return {"error": f"Unknown delivery options tool: {name}"}