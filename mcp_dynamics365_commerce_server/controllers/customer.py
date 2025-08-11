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
from ..database import get_database
from ..config import get_base_url

class CustomerController:
    """Controller for Customer-related Dynamics 365 Commerce API operations"""
    
    def __init__(self):
        self.db = get_database()
    
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
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
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
                        "first_name": {
                            "type": "string",
                            "description": "Customer first name"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer last name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer email address"
                        },
                        "phone": {
                            "type": "string",
                            "description": "Customer phone number"
                        },
                        "customer_group": {
                            "type": "string",
                            "description": "Customer group (REGULAR, VIP, etc.)",
                            "default": "REGULAR"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["first_name", "last_name", "email"]
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
                        "first_name": {
                            "type": "string",
                            "description": "Customer first name"
                        },
                        "last_name": {
                            "type": "string",
                            "description": "Customer last name"
                        },
                        "email": {
                            "type": "string",
                            "description": "Customer email address"
                        },
                        "phone": {
                            "type": "string",
                            "description": "Customer phone number"
                        },
                        "customer_group": {
                            "type": "string",
                            "description": "Customer group"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
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
                        "limit": {
                            "type": "integer",
                            "description": "Number of orders to return",
                            "default": 10
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
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
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return",
                            "default": 20
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
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
                        "limit": {
                            "type": "integer",
                            "description": "Number of purchases to return",
                            "default": 20
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["customerId"]
                }
            ),
            Tool(
                name="customer_get_by_account_numbers",
                description="Get customers list from account numbers",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "accountNumbers": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of account numbers to lookup"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["accountNumbers"]
                }
            ),
            Tool(
                name="customer_get_customer_search_fields",
                description="Get customer search fields for the store",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "storeId": {
                            "type": "string",
                            "description": "Store ID to get search fields for"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["storeId"]
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
                            "description": "Search criteria with field names and values",
                            "additionalProperties": {"type": "string"}
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["searchFields"]
                }
            ),
            Tool(
                name="customer_post_nontransactional_activity_loyalty_points",
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
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["loyaltyCardNumber", "activityType", "points"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer tool calls with database operations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        try:
            if name == "customer_get_order_shipments_history":
                customer_id = arguments.get("customerId")
                customer = self.db.read('customers', customer_id)
                if not customer:
                    return {"error": f"Customer {customer_id} not found"}
                
                # Get orders for this customer and their shipments
                orders = self.db.get_customer_orders(customer_id)
                shipments = []
                
                for order in orders:
                    if order.get('status') == 'Fulfilled':
                        shipments.append({
                            "shipmentId": f"SHIP_{order['id'][-3:]}",
                            "orderId": order['id'],
                            "orderNumber": order.get('order_number', order['id']),
                            "trackingNumber": f"TRACK{random.randint(100000, 999999)}",
                            "status": "Delivered",
                            "deliveryDate": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat() + "Z",
                            "carrier": random.choice(["FedEx", "UPS", "DHL", "USPS"]),
                            "items": [
                                {
                                    "productId": line.get('product_id'),
                                    "quantity": line.get('quantity', 1)
                                } for line in order.get('lines', [])
                            ]
                        })
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/OrderShipmentsHistory",
                    "customerId": customer_id,
                    "customerName": f"{customer.get('first_name', '')} {customer.get('last_name', '')}",
                    "shipments": shipments,
                    "totalShipments": len(shipments)
                }
            
            elif name == "customer_create_entity":
                # Create new customer
                customer_data = {
                    "first_name": arguments.get("first_name"),
                    "last_name": arguments.get("last_name"),
                    "email": arguments.get("email"),
                    "phone": arguments.get("phone"),
                    "customer_group": arguments.get("customer_group", "REGULAR"),
                    "account_number": f"ACC{random.randint(100000, 999999)}",
                    "loyalty_card_number": f"LOY{random.randint(100000, 999999)}",
                    "addresses": []
                }
                
                customer_id = self.db.create('customers', customer_data)
                created_customer = self.db.read('customers', customer_id)
                
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Customers",
                    "success": True,
                    "customer": created_customer
                }
            
            elif name == "customer_update_entity":
                customer_id = arguments.get("customerId")
                customer = self.db.read('customers', customer_id)
                if not customer:
                    return {"error": f"Customer {customer_id} not found"}
                
                # Prepare updates
                updates = {}
                for field in ["first_name", "last_name", "email", "phone", "customer_group"]:
                    if field in arguments:
                        updates[field] = arguments[field]
                
                success = self.db.update('customers', customer_id, updates)
                if success:
                    updated_customer = self.db.read('customers', customer_id)
                    return {
                        "api": f"PUT {base_url}/api/CommerceRuntime/Customers/{customer_id}",
                        "success": True,
                        "customer": updated_customer
                    }
                else:
                    return {"error": "Failed to update customer"}
            
            elif name == "customer_get_order_history":
                customer_id = arguments.get("customerId")
                limit = arguments.get("limit", 10)
                
                customer = self.db.read('customers', customer_id)
                if not customer:
                    return {"error": f"Customer {customer_id} not found"}
                
                orders = self.db.get_customer_orders(customer_id)[:limit]
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/Orders",
                    "customerId": customer_id,
                    "customerName": f"{customer.get('first_name', '')} {customer.get('last_name', '')}",
                    "orders": orders,
                    "totalOrders": len(orders)
                }
            
            elif name == "customer_search":
                query = arguments.get("query")
                limit = arguments.get("limit", 20)
                
                customers = self.db.search('customers', query, 
                                         fields=['first_name', 'last_name', 'email', 'phone'], 
                                         limit=limit)
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Customers/Search?q={query}",
                    "query": query,
                    "results": customers,
                    "totalResults": len(customers)
                }
            
            elif name == "customer_get_purchase_history":
                customer_id = arguments.get("customerId")
                limit = arguments.get("limit", 20)
                
                customer = self.db.read('customers', customer_id)
                if not customer:
                    return {"error": f"Customer {customer_id} not found"}
                
                orders = self.db.get_customer_orders(customer_id)[:limit]
                
                # Calculate purchase summary
                total_spent = sum(order.get('total', 0) for order in orders)
                total_orders = len(orders)
                avg_order_value = total_spent / total_orders if total_orders > 0 else 0
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/PurchaseHistory",
                    "customerId": customer_id,
                    "customerName": f"{customer.get('first_name', '')} {customer.get('last_name', '')}",
                    "purchaseHistory": orders,
                    "summary": {
                        "totalSpent": round(total_spent, 2),
                        "totalOrders": total_orders,
                        "averageOrderValue": round(avg_order_value, 2)
                    }
                }
            
            elif name == "customer_get_by_account_numbers":
                account_numbers = arguments.get("accountNumbers", [])
                customers = []
                
                for account_number in account_numbers:
                    customer_list = self.db.list('customers', filters={'account_number': account_number})
                    customers.extend(customer_list)
                
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Customers/GetByAccountNumbers",
                    "accountNumbers": account_numbers,
                    "customers": customers,
                    "totalFound": len(customers)
                }
            
            elif name == "customer_get_customer_search_fields":
                store_id = arguments.get("storeId")
                
                # Return available search fields for customers
                search_fields = [
                    {"name": "first_name", "displayName": "First Name", "type": "string"},
                    {"name": "last_name", "displayName": "Last Name", "type": "string"},
                    {"name": "email", "displayName": "Email", "type": "string"},
                    {"name": "phone", "displayName": "Phone", "type": "string"},
                    {"name": "account_number", "displayName": "Account Number", "type": "string"},
                    {"name": "loyalty_card_number", "displayName": "Loyalty Card", "type": "string"},
                    {"name": "customer_group", "displayName": "Customer Group", "type": "enum",
                     "options": ["REGULAR", "VIP", "EMPLOYEE"]}
                ]
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Stores/{store_id}/CustomerSearchFields",
                    "storeId": store_id,
                    "searchFields": search_fields
                }
            
            elif name == "customer_search_by_fields":
                search_fields = arguments.get("searchFields", {})
                limit = arguments.get("limit", 25)
                
                customers = self.db.list('customers', limit=limit, filters=search_fields)
                
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Customers/SearchByFields",
                    "searchCriteria": search_fields,
                    "results": customers,
                    "totalResults": len(customers)
                }
            
            elif name == "customer_post_nontransactional_activity_loyalty_points":
                loyalty_card_number = arguments.get("loyaltyCardNumber")
                customer_id = arguments.get("customerId")
                activity_type = arguments.get("activityType")
                points = arguments.get("points")
                description = arguments.get("description", f"{activity_type.title()} bonus points")
                
                # Find loyalty card
                loyalty_cards = self.db.list('loyalty_cards', 
                                           filters={'card_number': loyalty_card_number})
                if not loyalty_cards:
                    return {"error": f"Loyalty card {loyalty_card_number} not found"}
                
                loyalty_card = loyalty_cards[0]
                
                # Add points transaction
                transaction = {
                    "id": f"LOYT{random.randint(100000, 999999)}",
                    "date": datetime.now().isoformat(),
                    "points": points,
                    "type": "Earned",
                    "activity_type": activity_type,
                    "description": description,
                    "customer_id": customer_id
                }
                
                # Update loyalty card
                if 'transactions' not in loyalty_card:
                    loyalty_card['transactions'] = []
                loyalty_card['transactions'].append(transaction)
                loyalty_card['points_balance'] = loyalty_card.get('points_balance', 0) + points
                
                self.db.update('loyalty_cards', loyalty_card['id'], {
                    'transactions': loyalty_card['transactions'],
                    'points_balance': loyalty_card['points_balance']
                })
                
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards/{loyalty_card_number}/PostNonTransactionalActivity",
                    "success": True,
                    "transaction": transaction,
                    "newBalance": loyalty_card['points_balance'],
                    "loyaltyCard": loyalty_card_number
                }
            
            else:
                return {"error": f"Unknown customer tool: {name}"}
                
        except Exception as e:
            return {"error": f"Error in {name}: {str(e)}"}