"""
Loyalty Card Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (3 total):
1. loyaltycard_issue_loyalty_card - Issue a new loyalty card to a customer
2. loyaltycard_get_loyalty_card - Get loyalty card information and current status
3. loyaltycard_get_loyalty_card_transactions - Get transaction history for a loyalty card

This controller handles all loyalty program operations including card issuance,
loyalty account management, and points/transaction history tracking.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool

class LoyaltyCardController:
    """Controller for Loyalty Card-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of loyalty card-related tools"""
        return [
            Tool(
                name="loyaltycard_issue_loyalty_card",
                description="Issue a new loyalty card to a customer",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {
                            "type": "string",
                            "description": "Customer ID to issue the loyalty card to"
                        },
                        "loyaltyProgramId": {
                            "type": "string",
                            "description": "Loyalty program to enroll customer in"
                        },
                        "cardType": {
                            "type": "string",
                            "enum": ["standard", "premium", "vip"],
                            "description": "Type of loyalty card to issue",
                            "default": "standard"
                        },
                        "initialPoints": {
                            "type": "number",
                            "description": "Initial points to credit to the card",
                            "default": 0
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
                name="loyaltycard_get_loyalty_card",
                description="Get loyalty card information and current status",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {
                            "type": "string",
                            "description": "Loyalty card ID to retrieve"
                        },
                        "cardNumber": {
                            "type": "string",
                            "description": "Loyalty card number (alternative to cardId)"
                        },
                        "customerId": {
                            "type": "string",
                            "description": "Customer ID (alternative lookup method)"
                        },
                        "includeTransactionHistory": {
                            "type": "boolean",
                            "description": "Include recent transaction history",
                            "default": False
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
                name="loyaltycard_get_loyalty_card_transactions",
                description="Get transaction history for a loyalty card",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {
                            "type": "string",
                            "description": "Loyalty card ID to get transactions for"
                        },
                        "cardNumber": {
                            "type": "string",
                            "description": "Loyalty card number (alternative to cardId)"
                        },
                        "startDate": {
                            "type": "string",
                            "description": "Start date for transaction history (ISO format)"
                        },
                        "endDate": {
                            "type": "string",
                            "description": "End date for transaction history (ISO format)"
                        },
                        "transactionType": {
                            "type": "string",
                            "enum": ["all", "earned", "redeemed", "expired", "bonus"],
                            "description": "Filter by transaction type",
                            "default": "all"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of transactions to return",
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
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle loyalty card tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "loyaltycard_issue_loyalty_card":
            customer_id = arguments.get("customerId", "CUST001")
            card_type = arguments.get("cardType", "standard")
            initial_points = arguments.get("initialPoints", 0)
            
            loyalty_card_id = f"LC_{''.join(random.choices(string.ascii_uppercase + string.digits, k=9))}"
            card_number = f"{''.join(random.choices(string.digits, k=4))}-{''.join(random.choices(string.digits, k=4))}-{''.join(random.choices(string.digits, k=4))}-{''.join(random.choices(string.digits, k=4))}"
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards",
                "loyaltyCardId": loyalty_card_id,
                "cardNumber": card_number,
                "customerId": customer_id,
                "loyaltyProgramId": arguments.get("loyaltyProgramId", "PROG001"),
                "cardType": card_type,
                "status": "Active",
                "issueDate": datetime.now().isoformat() + "Z",
                "expirationDate": (datetime.now() + timedelta(days=365*2)).isoformat() + "Z",
                "initialPoints": initial_points,
                "currentPoints": initial_points,
                "tier": {
                    "tierId": "TIER001",
                    "tierName": "Bronze" if card_type == "standard" else "Silver" if card_type == "premium" else "Gold",
                    "minimumPoints": 0,
                    "benefits": [
                        "1 point per $1 spent",
                        "Birthday bonus points",
                        "Exclusive member offers"
                    ]
                },
                "benefits": {
                    "pointsEarnRate": 1.0 if card_type == "standard" else 1.5 if card_type == "premium" else 2.0,
                    "bonusMultiplier": 1.0 if card_type == "standard" else 1.2 if card_type == "premium" else 1.5,
                    "freeShipping": card_type in ["premium", "vip"],
                    "earlyAccess": card_type == "vip",
                    "personalShopper": card_type == "vip"
                },
                "activationRequired": False,
                "digitalWalletEnabled": True,
                "notifications": {
                    "email": True,
                    "sms": False,
                    "push": True
                }
            }
        
        elif name == "loyaltycard_get_loyalty_card":
            card_id = arguments.get("cardId", "LC001")
            card_number = arguments.get("cardNumber")
            customer_id = arguments.get("customerId")
            include_history = arguments.get("includeTransactionHistory", False)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id or 'lookup'}",
                "loyaltyCardId": card_id or "LC001",
                "cardNumber": card_number or "1234-5678-9012-3456",
                "customerId": customer_id or "CUST001",
                "customerName": "John Doe",
                "loyaltyProgramId": "PROG001",
                "loyaltyProgramName": "Rewards Plus",
                "cardType": "premium",
                "status": "Active",
                "issueDate": "2023-03-15T10:30:00Z",
                "expirationDate": "2025-03-15T00:00:00Z",
                "lastActivity": "2024-01-10T14:30:00Z",
                "currentPoints": 2450,
                "pendingPoints": 125,
                "lifetimePoints": 5780,
                "tier": {
                    "tierId": "TIER002",
                    "tierName": "Silver",
                    "minimumPoints": 1000,
                    "nextTier": {
                        "tierId": "TIER003",
                        "tierName": "Gold",
                        "minimumPoints": 5000,
                        "pointsNeeded": 2550
                    },
                    "benefits": [
                        "1.5 points per $1 spent",
                        "Free shipping on all orders",
                        "Birthday bonus: 250 points",
                        "Exclusive member sales",
                        "Priority customer service"
                    ]
                },
                "pointsBreakdown": {
                    "available": 2450,
                    "pending": 125,
                    "expired": 350,
                    "redeemed": 2980
                },
                "benefits": {
                    "pointsEarnRate": 1.5,
                    "bonusMultiplier": 1.2,
                    "freeShipping": True,
                    "earlyAccess": False,
                    "personalShopper": False,
                    "extendedReturns": True,
                    "birthdayBonus": 250
                },
                "digitalWallet": {
                    "enabled": True,
                    "addedToWallet": True,
                    "walletProvider": "Apple Pay"
                },
                "preferences": {
                    "emailNotifications": True,
                    "smsNotifications": True,
                    "pushNotifications": True,
                    "paperStatements": False
                },
                "recentTransactions": [
                    {
                        "transactionId": "LTX001",
                        "date": "2024-01-10T14:30:00Z",
                        "type": "earned",
                        "points": 125,
                        "description": "Purchase at Downtown Store",
                        "orderNumber": "ORD-2024-12345",
                        "storeId": "STORE001"
                    },
                    {
                        "transactionId": "LTX002",
                        "date": "2024-01-05T16:20:00Z",
                        "type": "redeemed",
                        "points": -500,
                        "description": "Redeemed for $25 discount",
                        "orderNumber": "ORD-2024-12340",
                        "redemptionValue": 25.00
                    }
                ] if include_history else None
            }
        
        elif name == "loyaltycard_get_loyalty_card_transactions":
            card_id = arguments.get("cardId", "LC001")
            card_number = arguments.get("cardNumber")
            transaction_type = arguments.get("transactionType", "all")
            limit = arguments.get("limit", 50)
            start_date = arguments.get("startDate")
            end_date = arguments.get("endDate")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id or 'lookup'}/Transactions",
                "loyaltyCardId": card_id or "LC001",
                "cardNumber": card_number or "1234-5678-9012-3456",
                "searchCriteria": {
                    "transactionType": transaction_type,
                    "startDate": start_date,
                    "endDate": end_date,
                    "limit": limit
                },
                "totalTransactions": 25,
                "pointsSummary": {
                    "totalEarned": 3250,
                    "totalRedeemed": 1500,
                    "totalExpired": 150,
                    "currentBalance": 2450
                },
                "transactions": [
                    {
                        "transactionId": "LTX001",
                        "date": "2024-01-10T14:30:00Z",
                        "type": "earned",
                        "points": 125,
                        "description": "Purchase reward - Electronics purchase",
                        "orderNumber": "ORD-2024-12345",
                        "storeId": "STORE001",
                        "storeName": "Downtown Store",
                        "purchaseAmount": 125.00,
                        "earnRate": 1.0,
                        "bonusPoints": 0,
                        "status": "completed"
                    },
                    {
                        "transactionId": "LTX002",
                        "date": "2024-01-08T11:15:00Z",
                        "type": "redeemed",
                        "points": -500,
                        "description": "Redeemed for discount - Online order",
                        "orderNumber": "ORD-2024-12340",
                        "redemptionValue": 25.00,
                        "redemptionRate": 0.05,
                        "status": "completed"
                    },
                    {
                        "transactionId": "LTX003",
                        "date": "2024-01-05T09:45:00Z",
                        "type": "bonus",
                        "points": 200,
                        "description": "Birthday bonus points",
                        "campaignId": "BDAY2024",
                        "expirationDate": "2025-01-05T00:00:00Z",
                        "status": "completed"
                    },
                    {
                        "transactionId": "LTX004",
                        "date": "2024-01-03T16:20:00Z",
                        "type": "earned",
                        "points": 89,
                        "description": "Purchase reward - Clothing purchase",
                        "orderNumber": "ORD-2024-12338",
                        "storeId": "STORE002",
                        "storeName": "Mall Store",
                        "purchaseAmount": 89.50,
                        "earnRate": 1.0,
                        "bonusPoints": 10,
                        "bonusReason": "Double points promotion",
                        "status": "completed"
                    },
                    {
                        "transactionId": "LTX005",
                        "date": "2023-12-28T13:10:00Z",
                        "type": "expired",
                        "points": -50,
                        "description": "Points expired after 12 months",
                        "originalTransactionId": "LTX050",
                        "originalDate": "2022-12-28T00:00:00Z",
                        "status": "expired"
                    }
                ][:limit],
                "pagination": {
                    "currentPage": 1,
                    "totalPages": 1,
                    "hasMore": False
                }
            }
        
        else:
            return {"error": f"Unknown loyalty card tool: {name}"}