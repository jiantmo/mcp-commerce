"""
Customer Balance Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. customer_balance_get_customer_balance - Gets the customer balance

This controller handles customer balance operations including account balance retrieval.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
from mcp.types import Tool

class CustomerBalanceController:
    """Controller for Customer Balance-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of customer balance-related tools"""
        return [
            Tool(
                name="customer_balance_get_customer_balance",
                description="Gets the customer balance",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "accountNumber": {
                            "type": "string",
                            "description": "Customer account number"
                        },
                        "invoiceAccountNumber": {
                            "type": "string",
                            "description": "Invoice account number (optional)"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["accountNumber"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle customer balance tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "customer_balance_get_customer_balance":
            account_number = arguments.get("accountNumber", "CUST001")
            invoice_account_number = arguments.get("invoiceAccountNumber")
            
            # Generate mock customer balance data
            current_balance = round(random.uniform(-500.0, 2000.0), 2)
            credit_limit = round(random.uniform(1000.0, 10000.0), 2)
            available_credit = credit_limit - max(0, current_balance)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CustomerBalance",
                "accountNumber": account_number,
                "invoiceAccountNumber": invoice_account_number,
                "customerBalances": {
                    "customerId": account_number,
                    "customerName": f"Customer {account_number[-3:]}",
                    "accountNumber": account_number,
                    "invoiceAccountNumber": invoice_account_number or account_number,
                    "currentBalance": current_balance,
                    "creditLimit": credit_limit,
                    "availableCredit": round(available_credit, 2),
                    "currency": "USD",
                    "currencySymbol": "$",
                    "balanceType": "Outstanding" if current_balance > 0 else "Credit" if current_balance < 0 else "Zero",
                    "lastPaymentDate": (datetime.now() - timedelta(days=random.randint(1, 60))).isoformat() + "Z",
                    "lastPaymentAmount": round(random.uniform(50.0, 500.0), 2),
                    "lastStatementDate": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat() + "Z",
                    "nextStatementDate": (datetime.now() + timedelta(days=random.randint(1, 30))).isoformat() + "Z",
                    "paymentTerms": "Net30",
                    "creditStatus": "Good" if current_balance <= credit_limit * 0.8 else "Warning" if current_balance <= credit_limit else "Over Limit",
                    "accountStatus": "Active",
                    "isOnHold": current_balance > credit_limit,
                    "holdReason": "Credit limit exceeded" if current_balance > credit_limit else None,
                    "agingBuckets": {
                        "current": round(current_balance * 0.6, 2) if current_balance > 0 else 0.0,
                        "thirtyDays": round(current_balance * 0.25, 2) if current_balance > 0 else 0.0,
                        "sixtyDays": round(current_balance * 0.10, 2) if current_balance > 0 else 0.0,
                        "ninetyDays": round(current_balance * 0.05, 2) if current_balance > 0 else 0.0,
                        "overNinetyDays": round(current_balance * 0.00, 2) if current_balance > 0 else 0.0
                    },
                    "recentTransactions": [
                        {
                            "transactionId": f"TXN_{random.randint(10000, 99999)}",
                            "transactionDate": (datetime.now() - timedelta(days=5)).isoformat() + "Z",
                            "transactionType": "Invoice",
                            "amount": round(random.uniform(50.0, 200.0), 2),
                            "description": "Product purchase",
                            "referenceNumber": f"INV-{random.randint(1000, 9999)}"
                        },
                        {
                            "transactionId": f"TXN_{random.randint(10000, 99999)}",
                            "transactionDate": (datetime.now() - timedelta(days=12)).isoformat() + "Z",
                            "transactionType": "Payment",
                            "amount": -round(random.uniform(100.0, 300.0), 2),
                            "description": "Payment received",
                            "referenceNumber": f"PMT-{random.randint(1000, 9999)}"
                        },
                        {
                            "transactionId": f"TXN_{random.randint(10000, 99999)}",
                            "transactionDate": (datetime.now() - timedelta(days=20)).isoformat() + "Z",
                            "transactionType": "Invoice",
                            "amount": round(random.uniform(75.0, 250.0), 2),
                            "description": "Service charge",
                            "referenceNumber": f"INV-{random.randint(1000, 9999)}"
                        }
                    ],
                    "contactInfo": {
                        "email": f"customer{account_number[-3:]}@example.com",
                        "phone": f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
                        "preferredContactMethod": "Email"
                    },
                    "billingAddress": {
                        "street": f"{random.randint(100, 999)} Main Street",
                        "city": "Seattle",
                        "state": "WA",
                        "zipCode": f"981{random.randint(10, 99)}",
                        "country": "USA"
                    },
                    "accountSettings": {
                        "autoPayEnabled": random.choice([True, False]),
                        "statementDelivery": random.choice(["Email", "Mail", "Both"]),
                        "paymentReminders": True,
                        "creditAlerts": True
                    },
                    "riskAssessment": {
                        "riskLevel": "Low" if current_balance <= credit_limit * 0.5 else "Medium" if current_balance <= credit_limit * 0.8 else "High",
                        "creditScore": random.randint(650, 850),
                        "paymentHistory": "Good",
                        "averagePaymentDays": random.randint(15, 45),
                        "lastCreditReview": (datetime.now() - timedelta(days=random.randint(30, 365))).isoformat() + "Z"
                    }
                },
                "calculationDate": datetime.now().isoformat() + "Z",
                "balanceSummary": {
                    "totalOutstanding": max(0, current_balance),
                    "totalCredits": abs(min(0, current_balance)),
                    "netBalance": current_balance,
                    "utilizationPercentage": round((max(0, current_balance) / credit_limit) * 100, 1) if credit_limit > 0 else 0,
                    "daysUntilDue": random.randint(5, 30) if current_balance > 0 else None
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "CustomerBalances",
                    "description": "Gets the customer balance"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown customer balance tool: {name}"}