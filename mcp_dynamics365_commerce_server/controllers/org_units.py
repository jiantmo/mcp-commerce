"""
Organizational Units Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (3 total):
1. orgunits_get_locations_by_area - Get store locations within a specific area or region
2. orgunits_get_available_inventory - Get available inventory for an organizational unit (store/warehouse)
3. orgunits_get_store_hours - Get operating hours for a specific store or organizational unit

This controller handles all organizational unit operations including store locating,
inventory management across locations, and store operational information.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class OrgUnitsController:
    """Controller for Organizational Units-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of org units-related tools"""
        return [
            Tool(
                name="orgunits_get_locations_by_area",
                description="Get store locations within a specific area or region",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "area": {
                            "type": "string",
                            "description": "Area, city, or region to search for locations"
                        },
                        "zipCode": {
                            "type": "string",
                            "description": "Zip code to search around"
                        },
                        "radius": {
                            "type": "number",
                            "description": "Search radius in miles",
                            "default": 25
                        },
                        "storeType": {
                            "type": "string",
                            "enum": ["retail", "warehouse", "pickup_point", "all"],
                            "description": "Type of store locations to return",
                            "default": "all"
                        },
                        "services": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["pickup", "curbside", "delivery", "returns"]
                            },
                            "description": "Filter by available services"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of locations to return",
                            "default": 50
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="orgunits_get_available_inventory",
                description="Get available inventory for an organizational unit (store/warehouse)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "orgUnitId": {
                            "type": "string",
                            "description": "The organizational unit ID to get inventory for"
                        },
                        "productId": {
                            "type": "string",
                            "description": "Filter inventory for a specific product"
                        },
                        "categoryId": {
                            "type": "string",
                            "description": "Filter inventory by product category"
                        },
                        "lowStockThreshold": {
                            "type": "number",
                            "description": "Show only items below this stock threshold"
                        },
                        "includeReserved": {
                            "type": "boolean",
                            "description": "Include reserved/allocated inventory in results",
                            "default": False
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of inventory items to return",
                            "default": 100
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["orgUnitId"]
                }
            ),
            Tool(
                name="orgunits_get_store_hours",
                description="Get operating hours for a specific store or organizational unit",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "orgUnitId": {
                            "type": "string",
                            "description": "The organizational unit ID to get hours for"
                        },
                        "date": {
                            "type": "string",
                            "description": "Specific date to get hours for (ISO format). If not provided, returns regular hours"
                        },
                        "includeHolidays": {
                            "type": "boolean",
                            "description": "Include holiday hours in the response",
                            "default": True
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["orgUnitId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle org units tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "orgunits_get_locations_by_area":
            area = arguments.get("area", "Seattle")
            zip_code = arguments.get("zipCode")
            radius = arguments.get("radius", 25)
            store_type = arguments.get("storeType", "all")
            limit = arguments.get("limit", 50)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/OrgUnits/LocationsByArea",
                "searchCriteria": {
                    "area": area,
                    "zipCode": zip_code,
                    "radius": radius,
                    "storeType": store_type
                },
                "totalLocations": 8,
                "locations": [
                    {
                        "orgUnitId": "STORE001",
                        "storeNumber": "001",
                        "name": "Seattle Downtown Store",
                        "type": "retail",
                        "status": "active",
                        "address": {
                            "street": "123 Pine Street",
                            "city": "Seattle",
                            "state": "WA",
                            "zipCode": "98101",
                            "country": "USA"
                        },
                        "coordinates": {
                            "latitude": 47.6062,
                            "longitude": -122.3321
                        },
                        "distance": 2.1 if zip_code else None,
                        "contact": {
                            "phone": "+1-206-555-0101",
                            "email": "seattle.downtown@store.com",
                            "manager": "John Smith"
                        },
                        "services": ["pickup", "curbside", "delivery", "returns"],
                        "hours": {
                            "monday": "9:00 AM - 9:00 PM",
                            "tuesday": "9:00 AM - 9:00 PM",
                            "wednesday": "9:00 AM - 9:00 PM",
                            "thursday": "9:00 AM - 9:00 PM",
                            "friday": "9:00 AM - 10:00 PM",
                            "saturday": "10:00 AM - 10:00 PM",
                            "sunday": "11:00 AM - 7:00 PM"
                        },
                        "specialHours": {
                            "2024-12-25": "Closed",
                            "2024-01-01": "12:00 PM - 6:00 PM"
                        },
                        "amenities": ["parking", "wifi", "customer_service", "atm"],
                        "departments": ["electronics", "clothing", "home_goods", "groceries"]
                    },
                    {
                        "orgUnitId": "STORE002",
                        "storeNumber": "002",
                        "name": "Bellevue Mall Store",
                        "type": "retail",
                        "status": "active",
                        "address": {
                            "street": "456 Bellevue Square",
                            "city": "Bellevue",
                            "state": "WA",
                            "zipCode": "98004",
                            "country": "USA"
                        },
                        "coordinates": {
                            "latitude": 47.6101,
                            "longitude": -122.2015
                        },
                        "distance": 8.5 if zip_code else None,
                        "contact": {
                            "phone": "+1-425-555-0102",
                            "email": "bellevue.mall@store.com",
                            "manager": "Sarah Johnson"
                        },
                        "services": ["pickup", "delivery", "returns"],
                        "hours": {
                            "monday": "10:00 AM - 9:00 PM",
                            "tuesday": "10:00 AM - 9:00 PM",
                            "wednesday": "10:00 AM - 9:00 PM",
                            "thursday": "10:00 AM - 9:00 PM",
                            "friday": "10:00 AM - 10:00 PM",
                            "saturday": "10:00 AM - 10:00 PM",
                            "sunday": "11:00 AM - 7:00 PM"
                        },
                        "amenities": ["parking", "wifi", "customer_service", "food_court"],
                        "departments": ["electronics", "clothing", "beauty"]
                    },
                    {
                        "orgUnitId": "WH001",
                        "name": "Seattle Distribution Center",
                        "type": "warehouse",
                        "status": "active",
                        "address": {
                            "street": "789 Industrial Way",
                            "city": "Seattle",
                            "state": "WA",
                            "zipCode": "98108",
                            "country": "USA"
                        },
                        "coordinates": {
                            "latitude": 47.5480,
                            "longitude": -122.3240
                        },
                        "contact": {
                            "phone": "+1-206-555-0199",
                            "email": "warehouse.seattle@company.com"
                        },
                        "services": ["delivery", "bulk_orders"],
                        "operatingHours": "24/7",
                        "capacity": "1M+ items"
                    }
                ][:limit]
            }
        
        elif name == "orgunits_get_available_inventory":
            org_unit_id = arguments.get("orgUnitId", "STORE001")
            product_id = arguments.get("productId")
            category_id = arguments.get("categoryId")
            include_reserved = arguments.get("includeReserved", False)
            limit = arguments.get("limit", 100)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/OrgUnits/{org_unit_id}/Inventory",
                "orgUnitId": org_unit_id,
                "orgUnitName": "Seattle Downtown Store",
                "lastUpdated": datetime.now().isoformat() + "Z",
                "filters": {
                    "productId": product_id,
                    "categoryId": category_id,
                    "includeReserved": include_reserved
                },
                "totalItems": 156,
                "inventory": [
                    {
                        "productId": "PROD001",
                        "sku": "WH-001",
                        "productName": "Wireless Bluetooth Headphones",
                        "category": {
                            "categoryId": "CAT001",
                            "name": "Electronics"
                        },
                        "quantity": 25,
                        "reserved": 3 if include_reserved else None,
                        "available": 22,
                        "minStock": 5,
                        "maxStock": 50,
                        "reorderPoint": 10,
                        "location": "A-1-5",
                        "lastReceived": "2024-01-08T14:30:00Z",
                        "lastSold": "2024-01-10T16:45:00Z",
                        "unitCost": 65.00,
                        "retailPrice": 99.99,
                        "status": "in_stock"
                    },
                    {
                        "productId": "PROD002",
                        "sku": "PC-001",
                        "productName": "Protective Phone Case",
                        "category": {
                            "categoryId": "CAT002",
                            "name": "Accessories"
                        },
                        "quantity": 45,
                        "reserved": 2 if include_reserved else None,
                        "available": 43,
                        "minStock": 10,
                        "maxStock": 100,
                        "reorderPoint": 20,
                        "location": "B-2-3",
                        "lastReceived": "2024-01-09T09:15:00Z",
                        "lastSold": "2024-01-10T18:20:00Z",
                        "unitCost": 8.50,
                        "retailPrice": 19.99,
                        "status": "in_stock"
                    },
                    {
                        "productId": "PROD003",
                        "sku": "CB-001",
                        "productName": "USB-C Cable",
                        "category": {
                            "categoryId": "CAT002",
                            "name": "Accessories"
                        },
                        "quantity": 3,
                        "reserved": 1 if include_reserved else None,
                        "available": 2,
                        "minStock": 5,
                        "maxStock": 25,
                        "reorderPoint": 8,
                        "location": "B-1-7",
                        "lastReceived": "2024-01-05T11:00:00Z",
                        "lastSold": "2024-01-10T14:10:00Z",
                        "unitCost": 3.25,
                        "retailPrice": 12.99,
                        "status": "low_stock",
                        "reorderNeeded": True
                    }
                ][:limit]
            }
        
        elif name == "orgunits_get_store_hours":
            org_unit_id = arguments.get("orgUnitId", "STORE001")
            date = arguments.get("date")
            include_holidays = arguments.get("includeHolidays", True)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/OrgUnits/{org_unit_id}/Hours",
                "orgUnitId": org_unit_id,
                "orgUnitName": "Seattle Downtown Store",
                "timeZone": "America/Los_Angeles",
                "currentTime": datetime.now().isoformat() + "Z",
                "isOpen": True,
                "nextStateChange": "2024-01-11T21:00:00Z",
                "regularHours": {
                    "monday": {
                        "open": "09:00",
                        "close": "21:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "tuesday": {
                        "open": "09:00",
                        "close": "21:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "wednesday": {
                        "open": "09:00",
                        "close": "21:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "thursday": {
                        "open": "09:00",
                        "close": "21:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "friday": {
                        "open": "09:00",
                        "close": "22:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "saturday": {
                        "open": "10:00",
                        "close": "22:00",
                        "is24Hour": False,
                        "isClosed": False
                    },
                    "sunday": {
                        "open": "11:00",
                        "close": "19:00",
                        "is24Hour": False,
                        "isClosed": False
                    }
                },
                "specialHours": [
                    {
                        "date": "2024-12-25",
                        "description": "Christmas Day",
                        "isClosed": True,
                        "open": None,
                        "close": None
                    },
                    {
                        "date": "2024-12-24",
                        "description": "Christmas Eve",
                        "isClosed": False,
                        "open": "09:00",
                        "close": "18:00"
                    },
                    {
                        "date": "2024-01-01",
                        "description": "New Year's Day",
                        "isClosed": False,
                        "open": "12:00",
                        "close": "18:00"
                    }
                ] if include_holidays else None,
                "todayHours": {
                    "date": "2024-01-10",
                    "dayOfWeek": "Wednesday",
                    "open": "09:00",
                    "close": "21:00",
                    "isClosed": False,
                    "isHoliday": False
                } if not date else {
                    "date": date,
                    "open": "09:00",
                    "close": "21:00",
                    "isClosed": False
                },
                "services": {
                    "curbsidePickup": {
                        "available": True,
                        "hours": "Same as store hours",
                        "lastOrder": "30 minutes before close"
                    },
                    "customerService": {
                        "available": True,
                        "hours": "Same as store hours",
                        "phone": "+1-206-555-0101"
                    },
                    "returns": {
                        "available": True,
                        "hours": "Same as store hours",
                        "cutoff": "1 hour before close"
                    }
                }
            }
        
        else:
            return {"error": f"Unknown org units tool: {name}"}