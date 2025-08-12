"""
Credit Memo Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. credit_memo_get_credit_memo_by_id - Get credit memo by identifier

This controller handles credit memo operations including retrieval and processing.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
from mcp.types import Tool
from ..config import get_base_url

class CreditMemoController:
    """Controller for Credit Memo-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of credit memo-related tools"""
        return [
            Tool(
                name="credit_memo_get_credit_memo_by_id",
                description="Get credit memo by identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "creditMemoId": {
                            "type": "string",
                            "description": "Credit memo identifier to retrieve"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["creditMemoId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle credit memo tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "credit_memo_get_credit_memo_by_id":
            credit_memo_id = arguments.get("creditMemoId", "CM001")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CreditMemos/{credit_memo_id}",
                "creditMemoId": credit_memo_id,
                "creditMemo": {
                    "creditMemoId": credit_memo_id,
                    "creditMemoNumber": f"CM-{random.randint(100000, 999999)}",
                    "customerId": f"CUST_{random.randint(1000, 9999)}",
                    "customerName": "John Doe",
                    "originalTransactionId": f"TXN_{random.randint(10000, 99999)}",
                    "originalOrderId": f"ORDER_{random.randint(1000, 9999)}",
                    "issueDate": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat() + "Z",
                    "expiryDate": (datetime.now() + timedelta(days=365)).isoformat() + "Z",
                    "amount": round(random.uniform(25.0, 500.0), 2),
                    "currency": "USD",
                    "balance": round(random.uniform(15.0, 500.0), 2),
                    "status": random.choice(["Active", "Partially Used", "Expired", "Cancelled"]),
                    "reason": "Product Return",
                    "reasonCode": "RETURN_DEFECTIVE",
                    "storeId": "STORE001",
                    "storeName": "Downtown Store",
                    "employeeId": "EMP001",
                    "employeeName": "Store Associate",
                    "isActive": True,
                    "canBeUsed": True,
                    "usageHistory": [
                        {
                            "transactionId": f"TXN_{random.randint(10000, 99999)}",
                            "usageDate": (datetime.now() - timedelta(days=5)).isoformat() + "Z",
                            "amountUsed": 10.00,
                            "description": "Partial payment for new purchase"
                        }
                    ],
                    "restrictions": {
                        "minimumPurchaseAmount": 0.00,
                        "validStores": ["STORE001", "STORE002"],
                        "excludedCategories": [],
                        "maxUsagePerTransaction": 500.00
                    },
                    "createdBy": "EMP001",
                    "approvedBy": "MGR001",
                    "approvalDate": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat() + "Z",
                    "notes": "Credit memo issued for defective product return"
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "CreditMemo",
                    "description": "Get credit memo by identifier"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown credit memo tool: {name}"}