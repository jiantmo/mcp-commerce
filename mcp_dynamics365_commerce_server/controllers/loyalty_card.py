"""
Loyalty Card Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (10 total):
1. loyaltycard_issue_loyalty_card - Issue a new loyalty card to a customer
2. loyaltycard_get_loyalty_card - Get loyalty card information and current status
3. loyaltycard_get_loyalty_card_transactions - Get transaction history for a loyalty card
4. loyaltycard_get_loyalty_card_balance - Get loyalty card points balance
5. loyaltycard_earn_points - Add earned points to a loyalty card
6. loyaltycard_redeem_points - Redeem points from a loyalty card
7. loyaltycard_transfer_points - Transfer points between loyalty cards
8. loyaltycard_get_loyalty_programs - Get available loyalty programs
9. loyaltycard_update_loyalty_card - Update loyalty card information
10. loyaltycard_block_loyalty_card - Block or unblock a loyalty card

This controller handles all loyalty program operations including card issuance,
loyalty account management, points/transaction history tracking, points transfers,
and loyalty program management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool
from ..config import get_base_url

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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="loyaltycard_get_loyalty_card_balance",
                description="Get loyalty card points balance",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {"type": "string", "description": "Loyalty card ID"},
                        "cardNumber": {"type": "string", "description": "Loyalty card number"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": []
                }
            ),
            Tool(
                name="loyaltycard_earn_points",
                description="Add earned points to a loyalty card",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {"type": "string", "description": "Loyalty card ID"},
                        "points": {"type": "number", "description": "Points to earn"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "reason": {"type": "string", "description": "Reason for earning points"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["cardId", "points"]
                }
            ),
            Tool(
                name="loyaltycard_redeem_points",
                description="Redeem points from a loyalty card",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {"type": "string", "description": "Loyalty card ID"},
                        "points": {"type": "number", "description": "Points to redeem"},
                        "redemptionType": {"type": "string", "description": "Type of redemption"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["cardId", "points"]
                }
            ),
            Tool(
                name="loyaltycard_transfer_points",
                description="Transfer points between loyalty cards",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "fromCardId": {"type": "string", "description": "Source card ID"},
                        "toCardId": {"type": "string", "description": "Destination card ID"},
                        "points": {"type": "number", "description": "Points to transfer"},
                        "reason": {"type": "string", "description": "Transfer reason"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["fromCardId", "toCardId", "points"]
                }
            ),
            Tool(
                name="loyaltycard_get_loyalty_programs",
                description="Get available loyalty programs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "includeInactive": {"type": "boolean", "default": False},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    }
                }
            ),
            Tool(
                name="loyaltycard_update_loyalty_card",
                description="Update loyalty card information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {"type": "string", "description": "Loyalty card ID"},
                        "updateData": {"type": "object", "description": "Update data"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["cardId", "updateData"]
                }
            ),
            Tool(
                name="loyaltycard_block_loyalty_card",
                description="Block or unblock a loyalty card",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "cardId": {"type": "string", "description": "Loyalty card ID"},
                        "isBlocked": {"type": "boolean", "description": "Block status"},
                        "reason": {"type": "string", "description": "Block/unblock reason"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["cardId", "isBlocked"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle loyalty card tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
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
        elif name == "loyaltycard_get_loyalty_card_balance":
            card_id = arguments.get("cardId", "LC001")
            card_number = arguments.get("cardNumber")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id or 'lookup'}/Balance",
                "loyaltyCardId": card_id or "LC001",
                "cardNumber": card_number or "1234-5678-9012-3456",
                "balance": {
                    "available": 2450,
                    "pending": 125,
                    "expired": 0,
                    "totalLifetime": 5780
                },
                "lastUpdated": datetime.now().isoformat() + "Z"
            }
        
        elif name == "loyaltycard_earn_points":
            card_id = arguments.get("cardId", "LC001")
            points = arguments.get("points", 100)
            transaction_id = arguments.get("transactionId", f"TXN{random.randint(100000, 999999)}")
            reason = arguments.get("reason", "Purchase reward")
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id}/EarnPoints",
                "transactionId": transaction_id,
                "loyaltyCardId": card_id,
                "pointsEarned": points,
                "reason": reason,
                "earnedAt": datetime.now().isoformat() + "Z",
                "newBalance": 2450 + points,
                "status": "completed"
            }
        
        elif name == "loyaltycard_redeem_points":
            card_id = arguments.get("cardId", "LC001")
            points = arguments.get("points", 500)
            redemption_type = arguments.get("redemptionType", "discount")
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id}/RedeemPoints",
                "transactionId": f"RED{random.randint(100000, 999999)}",
                "loyaltyCardId": card_id,
                "pointsRedeemed": points,
                "redemptionType": redemption_type,
                "redemptionValue": points * 0.05,  # 5 cents per point
                "redeemedAt": datetime.now().isoformat() + "Z",
                "newBalance": max(0, 2450 - points),
                "status": "completed"
            }
        
        elif name == "loyaltycard_transfer_points":
            from_card_id = arguments.get("fromCardId")
            to_card_id = arguments.get("toCardId")
            points = arguments.get("points", 100)
            reason = arguments.get("reason", "Point transfer")
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards/TransferPoints",
                "transferId": f"TRF{random.randint(100000, 999999)}",
                "fromCardId": from_card_id,
                "toCardId": to_card_id,
                "pointsTransferred": points,
                "reason": reason,
                "transferredAt": datetime.now().isoformat() + "Z",
                "fromCardNewBalance": max(0, 2450 - points),
                "toCardNewBalance": 1800 + points,
                "status": "completed"
            }
        
        elif name == "loyaltycard_get_loyalty_programs":
            include_inactive = arguments.get("includeInactive", False)
            
            programs = [
                {
                    "programId": "PROG001",
                    "programName": "Rewards Plus",
                    "description": "Earn points on every purchase",
                    "status": "Active",
                    "earnRate": 1.0,
                    "minimumAge": 13,
                    "joinDate": "2023-01-01T00:00:00Z",
                    "tiers": [
                        {"tierId": "TIER001", "tierName": "Bronze", "minimumPoints": 0},
                        {"tierId": "TIER002", "tierName": "Silver", "minimumPoints": 1000},
                        {"tierId": "TIER003", "tierName": "Gold", "minimumPoints": 5000}
                    ]
                },
                {
                    "programId": "PROG002",
                    "programName": "VIP Elite",
                    "description": "Premium membership with exclusive benefits",
                    "status": "Active",
                    "earnRate": 2.0,
                    "minimumAge": 18,
                    "joinDate": "2023-01-01T00:00:00Z",
                    "membershipFee": 99.99,
                    "tiers": [
                        {"tierId": "TIER004", "tierName": "VIP", "minimumPoints": 0},
                        {"tierId": "TIER005", "tierName": "VIP Elite", "minimumPoints": 10000}
                    ]
                }
            ]
            
            if include_inactive:
                programs.append({
                    "programId": "PROG003",
                    "programName": "Legacy Rewards",
                    "description": "Discontinued program",
                    "status": "Inactive",
                    "endDate": "2023-12-31T23:59:59Z"
                })
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/LoyaltyPrograms",
                "programs": programs,
                "totalCount": len(programs)
            }
        
        elif name == "loyaltycard_update_loyalty_card":
            card_id = arguments.get("cardId")
            update_data = arguments.get("updateData", {})
            
            return {
                "api": f"PATCH {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id}",
                "loyaltyCardId": card_id,
                "updatedFields": list(update_data.keys()),
                "updatedAt": datetime.now().isoformat() + "Z",
                "success": True,
                "changes": update_data
            }
        
        elif name == "loyaltycard_block_loyalty_card":
            card_id = arguments.get("cardId")
            is_blocked = arguments.get("isBlocked", True)
            reason = arguments.get("reason", "Security concern")
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/LoyaltyCards/{card_id}/Block",
                "loyaltyCardId": card_id,
                "isBlocked": is_blocked,
                "reason": reason,
                "actionPerformedAt": datetime.now().isoformat() + "Z",
                "newStatus": "Blocked" if is_blocked else "Active",
                "success": True
            }
        
        else:
            return {"error": f"Unknown loyalty card tool: {name}"}