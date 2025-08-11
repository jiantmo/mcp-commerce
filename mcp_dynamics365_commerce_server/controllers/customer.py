"""
Customer Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (10 total):
1. customer_get_order_shipments_history - Get order shipments history for a customer
2. customer_create_entity - Create a new customer entity  
3. customer_update_entity - Update an existing customer entity
4. customer_get_order_history - Get order history for a customer
5. customer_search - Search for customers by various criteria
6. customer_get_purchase_history - Get purchase history for a customer
7. customer_get_by_account_numbers - Get customers list from account numbers
8. customer_get_customer_search_fields - Get customer search fields for the store
9. customer_search_by_fields - Search for customers by specified fields
10. customer_post_nontransactional_activity_loyalty_points - Post non-transactional loyalty points

This controller handles all customer-related operations including customer management,
order tracking, purchase history, customer search functionality, and loyalty point management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool

class CustomerController:
    """Controller for Customer-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of customer-related tools"""
        return [
            Tool(
                name="customer_get_order_shipments_history",
                description="Get order shipments history for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {
                            "type": "string",
                            "description": "The customer ID to get shipments history for"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["customerId"]
                }
            ),
            Tool(
                name="customer_create_entity",
                description="Create a new customer entity",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Customer name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer email address"
                        },
                        "phone": {
                            "type": "string",
                            "description": "Customer phone number"
                        },
                        "address": {
                            "type": "object",
                            "description": "Customer address",
                            "properties": {
                                "street": {"type": "string"},
                                "city": {"type": "string"},
                                "state": {"type": "string"},
                                "zipCode": {"type": "string"},
                                "country": {"type": "string"}
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["name", "email"]
                }
            ),
            Tool(
                name="customer_update_entity",
                description="Update an existing customer entity",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {
                            "type": "string",
                            "description": "The customer ID to update"
                        },
                        "name": {
                            "type": "string",
                            "description": "Updated customer name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Updated customer email address"
                        },
                        "phone": {
                            "type": "string",
                            "description": "Updated customer phone number"
                        },
                        "address": {
                            "type": "object",
                            "description": "Updated customer address",
                            "properties": {
                                "street": {"type": "string"},
                                "city": {"type": "string"},
                                "state": {"type": "string"},
                                "zipCode": {"type": "string"},
                                "country": {"type": "string"}
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["customerId"]
                }
            ),
            Tool(
                name="customer_get_order_history",
                description="Get order history for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {
                            "type": "string",
                            "description": "The customer ID to get order history for"
                        },
                        "startDate": {
                            "type": "string",
                            "description": "Start date for order history (ISO format)"
                        },
                        "endDate": {
                            "type": "string",
                            "description": "End date for order history (ISO format)"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of orders to return",
                            "default": 50
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["customerId"]
                }
            ),
            Tool(
                name="customer_search",
                description="Search for customers by various criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (name, email, phone, etc.)"
                        },
                        "searchBy": {
                            "type": "string",
                            "enum": ["name", "email", "phone", "customerId"],
                            "description": "Field to search by",
                            "default": "name"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of results to return",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["query"]
                }
            ),
            Tool(
                name="customer_get_purchase_history",
                description="Get purchase history for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {
                            "type": "string",
                            "description": "The customer ID to get purchase history for"
                        },
                        "startDate": {
                            "type": "string",
                            "description": "Start date for purchase history (ISO format)"
                        },
                        "endDate": {
                            "type": "string",
                            "description": "End date for purchase history (ISO format)"
                        },
                        "categoryId": {
                            "type": "string",
                            "description": "Filter by product category ID"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of purchases to return",
                            "default": 50
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["customerId"]
                }
            ),
            Tool(
                name="customer_get_by_account_numbers",
                description="Get customers list from the list of customer account numbers",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "accountNumbers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of customer account numbers"
                        },
                        "searchLocationValue": {
                            "type": "string",
                            "description": "Search location value"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of customers to return",
                            "default": 50
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["accountNumbers"]
                }
            ),
            Tool(
                name="customer_get_customer_search_fields",
                description="Get the customer search fields for the store set in headquarters",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "storeId": {
                            "type": "string",
                            "description": "Store ID to get search fields for"
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
                name="customer_search_by_fields",
                description="Search for customers by specified fields",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "searchFields": {
                            "type": "object",
                            "description": "Customer fields to search by",
                            "properties": {
                                "firstName": {"type": "string"},
                                "lastName": {"type": "string"},
                                "email": {"type": "string"},
                                "phone": {"type": "string"},
                                "city": {"type": "string"},
                                "zipCode": {"type": "string"},
                                "loyaltyCardNumber": {"type": "string"}
                            }
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of results to return",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["searchFields"]
                }
            ),
            Tool(
                name="customer_post_loyalty_points",
                description="Post non-transactional activity loyalty points for a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "loyaltyCardNumber": {
                            "type": "string",
                            "description": "Loyalty card number"
                        },
                        "customerId": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "activityType": {
                            "type": "string",
                            "enum": ["birthday", "anniversary", "signup", "referral", "survey", "social_media"],
                            "description": "Type of non-transactional activity"
                        },
                        "points": {
                            "type": "number",
                            "description": "Number of points to award"
                        },
                        "description": {
                            "type": "string",
                            "description": "Description of the activity"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["loyaltyCardNumber", "activityType", "points"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "customer_get_order_shipments_history":
            customer_id = arguments.get("customerId", "CUST001")
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/OrderShipmentsHistory",
                "customerId": customer_id,
                "shipments": [
                    {
                        "shipmentId": "SHIP001",
                        "orderId": "ORDER001",
                        "trackingNumber": "TRACK123456",
                        "status": "Delivered",
                        "deliveryDate": "2024-01-15T10:30:00Z",
                        "carrier": "FedEx",
                        "items": [
                            {"productId": "PROD001", "productName": "Sample Product", "quantity": 2}
                        ]
                    },
                    {
                        "shipmentId": "SHIP002",
                        "orderId": "ORDER002",
                        "trackingNumber": "TRACK789012",
                        "status": "In Transit",
                        "estimatedDelivery": "2024-01-20T15:00:00Z",
                        "carrier": "UPS"
                    }
                ]
            }
        
        elif name == "customer_create_entity":
            customer_id = f"CUST_{''.join(random.choices(string.ascii_uppercase + string.digits, k=9))}"
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Customers",
                "customerId": customer_id,
                "name": arguments.get("name", "John Doe"),
                "email": arguments.get("email", "john.doe@example.com"),
                "phone": arguments.get("phone"),
                "address": arguments.get("address"),
                "status": "Active",
                "created": datetime.now().isoformat() + "Z",
                "loyaltyCardNumber": f"LC{random.randint(100000, 999999)}"
            }
        
        elif name == "customer_update_entity":
            customer_id = arguments.get("customerId", "CUST001")
            return {
                "api": f"PUT {base_url}/api/CommerceRuntime/Customers/{customer_id}",
                "customerId": customer_id,
                "updated": True,
                "lastModified": datetime.now().isoformat() + "Z",
                "updatedFields": {
                    "name": arguments.get("name"),
                    "email": arguments.get("email"),
                    "phone": arguments.get("phone"),
                    "address": arguments.get("address")
                }
            }
        
        elif name == "customer_get_order_history":
            customer_id = arguments.get("customerId", "CUST001")
            limit = arguments.get("limit", 50)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/OrderHistory",
                "customerId": customer_id,
                "totalOrders": 15,
                "orders": [
                    {
                        "orderId": "ORDER001",
                        "orderDate": "2024-01-10T14:30:00Z",
                        "total": 125.99,
                        "currency": "USD",
                        "status": "Completed",
                        "itemCount": 3,
                        "shippingAddress": {
                            "street": "123 Main St",
                            "city": "Seattle",
                            "state": "WA",
                            "zipCode": "98101"
                        }
                    },
                    {
                        "orderId": "ORDER002",
                        "orderDate": "2024-01-05T09:15:00Z",
                        "total": 89.50,
                        "currency": "USD",
                        "status": "Delivered",
                        "itemCount": 2,
                        "deliveryDate": "2024-01-08T16:20:00Z"
                    }
                ][:limit]
            }
        
        elif name == "customer_search":
            query = arguments.get("query", "")
            search_by = arguments.get("searchBy", "name")
            limit = arguments.get("limit", 25)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/Search",
                "query": query,
                "searchBy": search_by,
                "totalResults": 3,
                "results": [
                    {
                        "customerId": "CUST001",
                        "name": "John Doe",
                        "email": "john.doe@example.com",
                        "phone": "+1-555-0123",
                        "status": "Active",
                        "lastPurchaseDate": "2024-01-10T14:30:00Z",
                        "totalSpent": 1250.75
                    },
                    {
                        "customerId": "CUST002",
                        "name": "Jane Smith",
                        "email": "jane.smith@example.com",
                        "phone": "+1-555-0124",
                        "status": "Active",
                        "lastPurchaseDate": "2024-01-08T11:20:00Z",
                        "totalSpent": 890.25
                    }
                ][:limit]
            }
        
        elif name == "customer_get_purchase_history":
            customer_id = arguments.get("customerId", "CUST001")
            limit = arguments.get("limit", 50)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/PurchaseHistory",
                "customerId": customer_id,
                "totalPurchases": 8,
                "purchases": [
                    {
                        "transactionId": "TXN001",
                        "date": "2024-01-10T14:30:00Z",
                        "storeId": "STORE001",
                        "storeName": "Main Store",
                        "items": [
                            {
                                "productId": "PROD001",
                                "productName": "Wireless Headphones",
                                "category": "Electronics",
                                "quantity": 1,
                                "unitPrice": 99.99,
                                "total": 99.99
                            },
                            {
                                "productId": "PROD002",
                                "productName": "Phone Case",
                                "category": "Accessories",
                                "quantity": 2,
                                "unitPrice": 13.00,
                                "total": 26.00
                            }
                        ],
                        "subtotal": 125.99,
                        "tax": 10.08,
                        "total": 136.07
                    }
                ][:limit]
            }
        
        elif name == "customer_get_by_account_numbers":
            account_numbers = arguments.get("accountNumbers", ["CUST001", "CUST002"])
            search_location_value = arguments.get("searchLocationValue", "")
            limit = arguments.get("limit", 50)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/GetByAccountNumbers",
                "accountNumbers": account_numbers,
                "searchLocationValue": search_location_value,
                "totalCustomers": len(account_numbers),
                "customers": [
                    {
                        "accountNumber": account_num,
                        "customerId": account_num,
                        "name": f"Customer {account_num[-3:]}",
                        "email": f"customer{account_num[-3:]}@example.com",
                        "phone": f"+1-555-0{random.randint(100, 199)}",
                        "status": "Active",
                        "createdDate": "2023-06-15T00:00:00Z",
                        "lastUpdated": datetime.now().isoformat() + "Z",
                        "address": {
                            "street": f"{random.randint(100, 999)} Main St",
                            "city": "Seattle",
                            "state": "WA",
                            "zipCode": f"981{random.randint(10, 99)}",
                            "country": "USA"
                        },
                        "loyaltyCardNumber": f"LC{random.randint(100000, 999999)}"
                    }
                    for account_num in account_numbers
                ][:limit]
            }
        
        elif name == "customer_get_customer_search_fields":
            store_id = arguments.get("storeId", "STORE001")
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/GetCustomerSearchFields",
                "storeId": store_id,
                "searchFields": [
                    {
                        "fieldName": "firstName",
                        "displayName": "First Name",
                        "fieldType": "string",
                        "isRequired": False,
                        "maxLength": 50,
                        "isSearchable": True,
                        "orderIndex": 1
                    },
                    {
                        "fieldName": "lastName", 
                        "displayName": "Last Name",
                        "fieldType": "string",
                        "isRequired": False,
                        "maxLength": 50,
                        "isSearchable": True,
                        "orderIndex": 2
                    },
                    {
                        "fieldName": "email",
                        "displayName": "Email Address",
                        "fieldType": "email",
                        "isRequired": False,
                        "maxLength": 100,
                        "isSearchable": True,
                        "orderIndex": 3
                    },
                    {
                        "fieldName": "phone",
                        "displayName": "Phone Number",
                        "fieldType": "phone",
                        "isRequired": False,
                        "maxLength": 20,
                        "isSearchable": True,
                        "orderIndex": 4
                    },
                    {
                        "fieldName": "city",
                        "displayName": "City",
                        "fieldType": "string",
                        "isRequired": False,
                        "maxLength": 50,
                        "isSearchable": True,
                        "orderIndex": 5
                    },
                    {
                        "fieldName": "zipCode",
                        "displayName": "ZIP Code",
                        "fieldType": "string",
                        "isRequired": False,
                        "maxLength": 10,
                        "isSearchable": True,
                        "orderIndex": 6
                    },
                    {
                        "fieldName": "loyaltyCardNumber",
                        "displayName": "Loyalty Card Number",
                        "fieldType": "string",
                        "isRequired": False,
                        "maxLength": 20,
                        "isSearchable": True,
                        "orderIndex": 7
                    }
                ],
                "totalFields": 7,
                "storeConfiguration": {
                    "enableAdvancedSearch": True,
                    "defaultSearchField": "lastName",
                    "maxSearchResults": 100
                }
            }
        
        elif name == "customer_search_by_fields":
            search_fields = arguments.get("searchFields", {})
            limit = arguments.get("limit", 25)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Customers/SearchByFields",
                "searchCriteria": search_fields,
                "totalResults": 5,
                "results": [
                    {
                        "customerId": "CUST001",
                        "accountNumber": "CUST001",
                        "firstName": search_fields.get("firstName", "John"),
                        "lastName": search_fields.get("lastName", "Doe"),
                        "email": search_fields.get("email", "john.doe@example.com"),
                        "phone": search_fields.get("phone", "+1-555-0123"),
                        "address": {
                            "street": "123 Main Street",
                            "city": search_fields.get("city", "Seattle"),
                            "state": "WA",
                            "zipCode": search_fields.get("zipCode", "98101"),
                            "country": "USA"
                        },
                        "loyaltyCardNumber": search_fields.get("loyaltyCardNumber", f"LC{random.randint(100000, 999999)}"),
                        "status": "Active",
                        "createdDate": "2023-03-15T10:30:00Z",
                        "lastPurchaseDate": "2024-01-10T14:30:00Z",
                        "totalSpent": 1875.50,
                        "totalOrders": 12,
                        "tier": "Gold",
                        "matchScore": 0.95,
                        "matchedFields": list(search_fields.keys())
                    },
                    {
                        "customerId": "CUST002",
                        "accountNumber": "CUST002", 
                        "firstName": "Jane",
                        "lastName": search_fields.get("lastName", "Smith"),
                        "email": "jane.smith@example.com",
                        "phone": "+1-555-0124",
                        "address": {
                            "street": "456 Oak Avenue",
                            "city": search_fields.get("city", "Bellevue"),
                            "state": "WA",
                            "zipCode": "98004",
                            "country": "USA"
                        },
                        "loyaltyCardNumber": f"LC{random.randint(100000, 999999)}",
                        "status": "Active",
                        "createdDate": "2023-07-22T09:15:00Z",
                        "lastPurchaseDate": "2024-01-08T11:20:00Z",
                        "totalSpent": 945.25,
                        "totalOrders": 7,
                        "tier": "Silver",
                        "matchScore": 0.87,
                        "matchedFields": ["lastName", "city"]
                    }
                ][:limit]
            }
        
        elif name == "customer_post_nontransactional_activity_loyalty_points":
            loyalty_card_number = arguments.get("loyaltyCardNumber")
            customer_id = arguments.get("customerId")
            activity_type = arguments.get("activityType")
            points = arguments.get("points")
            description = arguments.get("description", f"{activity_type.title()} bonus points")
            
            transaction_id = f"NONTXN_{''.join(random.choices(string.ascii_uppercase + string.digits, k=12))}"
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Customers/PostNonTransactionalActivityLoyaltyPoints",
                "loyaltyCardNumber": loyalty_card_number,
                "customerId": customer_id,
                "transactionId": transaction_id,
                "activityType": activity_type,
                "points": points,
                "description": description,
                "status": "completed",
                "processedTime": datetime.now().isoformat() + "Z",
                "expirationDate": (datetime.now() + timedelta(days=365)).isoformat() + "Z",
                "loyaltyProgram": {
                    "programId": "PROG001",
                    "programName": "Rewards Plus"
                },
                "customerDetails": {
                    "customerId": customer_id,
                    "name": "Customer Name",
                    "currentPoints": 2450 + points,
                    "tier": "Silver",
                    "newTier": "Gold" if (2450 + points) >= 3000 else "Silver"
                },
                "pointsBreakdown": {
                    "previousBalance": 2450,
                    "pointsAdded": points,
                    "newBalance": 2450 + points,
                    "pendingPoints": 0
                },
                "notifications": {
                    "emailSent": True,
                    "smsSent": False,
                    "pushNotificationSent": True
                }
            }
        
        else:
            return {"error": f"Unknown customer tool: {name}"}