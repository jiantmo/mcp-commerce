"""
Shifts Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (4 total):
1. shifts_get_shift - Get information about a specific shift
2. shifts_open - Open a new shift for an employee
3. shifts_close - Close an existing shift
4. shifts_resume - Resume a previously suspended shift

This controller handles all employee shift operations including shift management,
cash handling, performance tracking, and shift lifecycle operations.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool

class ShiftsController:
    """Controller for Shifts-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of shifts-related tools"""
        return [
            Tool(
                name="shifts_get_shift",
                description="Get information about a specific shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {
                            "type": "string",
                            "description": "The shift ID to retrieve information for"
                        },
                        "includeTransactions": {
                            "type": "boolean",
                            "description": "Include transaction summary in the response",
                            "default": True
                        },
                        "includeEmployeeDetails": {
                            "type": "boolean",
                            "description": "Include detailed employee information",
                            "default": False
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["shiftId"]
                }
            ),
            Tool(
                name="shifts_open",
                description="Open a new shift for an employee",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "employeeId": {
                            "type": "string",
                            "description": "Employee ID opening the shift"
                        },
                        "storeId": {
                            "type": "string",
                            "description": "Store ID where the shift is being opened"
                        },
                        "registerId": {
                            "type": "string",
                            "description": "Register/POS terminal ID"
                        },
                        "startingCashAmount": {
                            "type": "number",
                            "description": "Starting cash amount in the register",
                            "default": 200.00
                        },
                        "shiftType": {
                            "type": "string",
                            "enum": ["regular", "manager", "temporary", "training"],
                            "description": "Type of shift being opened",
                            "default": "regular"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["employeeId", "storeId"]
                }
            ),
            Tool(
                name="shifts_close",
                description="Close an existing shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {
                            "type": "string",
                            "description": "The shift ID to close"
                        },
                        "endingCashAmount": {
                            "type": "number",
                            "description": "Actual cash amount at shift end"
                        },
                        "cashDropAmount": {
                            "type": "number",
                            "description": "Amount of cash dropped/deposited during shift",
                            "default": 0.00
                        },
                        "notes": {
                            "type": "string",
                            "description": "Additional notes about the shift"
                        },
                        "performCashCount": {
                            "type": "boolean",
                            "description": "Whether to perform cash count verification",
                            "default": True
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["shiftId"]
                }
            ),
            Tool(
                name="shifts_resume",
                description="Resume a previously suspended shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {
                            "type": "string",
                            "description": "The shift ID to resume"
                        },
                        "employeeId": {
                            "type": "string",
                            "description": "Employee ID resuming the shift (must match original)"
                        },
                        "registerId": {
                            "type": "string",
                            "description": "Register/POS terminal ID for resumption"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["shiftId", "employeeId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle shifts tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "shifts_get_shift":
            shift_id = arguments.get("shiftId", "SHIFT001")
            include_transactions = arguments.get("includeTransactions", True)
            include_employee_details = arguments.get("includeEmployeeDetails", False)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/{shift_id}",
                "shiftId": shift_id,
                "shiftNumber": f"S-{random.randint(100000, 999999)}",
                "employeeId": "EMP001",
                "employeeName": "John Smith",
                "employeeDetails": {
                    "employeeNumber": "E001",
                    "department": "Sales",
                    "position": "Sales Associate",
                    "hireDate": "2023-06-15T00:00:00Z",
                    "contactInfo": {
                        "email": "john.smith@store.com",
                        "phone": "+1-206-555-0150"
                    }
                } if include_employee_details else None,
                "storeId": "STORE001",
                "storeName": "Downtown Store",
                "registerId": "REG001",
                "registerName": "Register 1",
                "shiftType": "regular",
                "status": "closed",
                "startTime": "2024-01-10T09:00:00Z",
                "endTime": "2024-01-10T17:30:00Z",
                "totalDuration": "8 hours 30 minutes",
                "breaks": [
                    {
                        "breakType": "lunch",
                        "startTime": "2024-01-10T13:00:00Z",
                        "endTime": "2024-01-10T14:00:00Z",
                        "duration": "1 hour"
                    },
                    {
                        "breakType": "break",
                        "startTime": "2024-01-10T15:30:00Z",
                        "endTime": "2024-01-10T15:45:00Z",
                        "duration": "15 minutes"
                    }
                ],
                "cashManagement": {
                    "startingCashAmount": 200.00,
                    "endingCashAmount": 175.50,
                    "cashDrops": [
                        {
                            "time": "2024-01-10T12:30:00Z",
                            "amount": 500.00,
                            "reason": "Till exceeded limit"
                        }
                    ],
                    "totalCashDropped": 500.00,
                    "expectedCashAmount": 178.25,
                    "variance": -2.75,
                    "varianceReason": "Customer paid exact change, short counted"
                },
                "transactionSummary": {
                    "totalTransactions": 43,
                    "totalSales": 2450.75,
                    "totalReturns": 125.50,
                    "netSales": 2325.25,
                    "averageTransactionValue": 57.00,
                    "transactionTypes": {
                        "sales": 38,
                        "returns": 3,
                        "exchanges": 2,
                        "voids": 1
                    },
                    "paymentMethods": {
                        "cash": 875.25,
                        "creditCard": 1245.50,
                        "debitCard": 204.50,
                        "giftCard": 125.00,
                        "loyaltyPoints": 0.00
                    }
                } if include_transactions else None,
                "performance": {
                    "itemsPerHour": 15.2,
                    "customersServed": 43,
                    "averageServiceTime": "3.5 minutes",
                    "upsellSuccess": 0.12,
                    "customerSatisfaction": 4.6
                },
                "incidents": [
                    {
                        "incidentId": "INC001",
                        "time": "2024-01-10T11:45:00Z",
                        "type": "price_override",
                        "description": "Manager override for damaged item discount",
                        "amount": 15.00,
                        "approvedBy": "MGR001"
                    }
                ],
                "notes": "Regular shift, no major issues. Customer complaint resolved satisfactorily.",
                "managerApproval": {
                    "approved": True,
                    "approvedBy": "MGR001",
                    "approvalTime": "2024-01-10T17:45:00Z",
                    "approvalNotes": "Shift closed properly, variance within acceptable range"
                }
            }
        
        elif name == "shifts_open":
            employee_id = arguments.get("employeeId", "EMP001")
            store_id = arguments.get("storeId", "STORE001")
            starting_cash = arguments.get("startingCashAmount", 200.00)
            shift_type = arguments.get("shiftType", "regular")
            
            shift_id = f"SHIFT_{''.join(random.choices(string.ascii_uppercase + string.digits, k=9))}"
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Open",
                "shiftId": shift_id,
                "shiftNumber": f"S-{random.randint(100000, 999999)}",
                "employeeId": employee_id,
                "employeeName": "John Smith",
                "storeId": store_id,
                "storeName": "Downtown Store",
                "registerId": arguments.get("registerId", "REG001"),
                "registerName": "Register 1",
                "shiftType": shift_type,
                "status": "open",
                "startTime": datetime.now().isoformat() + "Z",
                "expectedEndTime": (datetime.now() + timedelta(hours=8)).isoformat() + "Z",
                "cashManagement": {
                    "startingCashAmount": starting_cash,
                    "currentCashAmount": starting_cash,
                    "cashDropLimit": 1000.00,
                    "tillId": f"TILL_{random.randint(100, 999)}",
                    "lastCashCount": datetime.now().isoformat() + "Z"
                },
                "permissions": {
                    "canProcessSales": True,
                    "canProcessReturns": True,
                    "canApplyDiscounts": shift_type in ["manager", "regular"],
                    "canVoidTransactions": shift_type == "manager",
                    "canOpenRegister": True,
                    "canPerformCashDrop": True,
                    "maxDiscountPercent": 10.0 if shift_type == "regular" else 25.0 if shift_type == "manager" else 5.0,
                    "maxVoidAmount": 100.00 if shift_type == "regular" else 500.00 if shift_type == "manager" else 50.00
                },
                "settings": {
                    "requireCustomerInfo": False,
                    "printReceiptByDefault": True,
                    "emailReceiptOption": True,
                    "loyaltyProgramActive": True,
                    "giftCardAcceptance": True
                },
                "systemInfo": {
                    "posVersion": "v2.4.1",
                    "lastSync": datetime.now().isoformat() + "Z",
                    "connectionStatus": "online",
                    "backupMode": False
                },
                "notifications": [
                    {
                        "type": "info",
                        "message": "Welcome! Your shift has been successfully opened.",
                        "timestamp": datetime.now().isoformat() + "Z"
                    },
                    {
                        "type": "reminder",
                        "message": "Remember to perform cash drops when till exceeds $1000.",
                        "timestamp": datetime.now().isoformat() + "Z"
                    }
                ]
            }
        
        elif name == "shifts_close":
            shift_id = arguments.get("shiftId", "SHIFT001")
            ending_cash = arguments.get("endingCashAmount")
            cash_drop = arguments.get("cashDropAmount", 0.00)
            perform_cash_count = arguments.get("performCashCount", True)
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/{shift_id}/Close",
                "shiftId": shift_id,
                "status": "closed",
                "endTime": datetime.now().isoformat() + "Z",
                "closedBy": "EMP001",
                "closingProcess": {
                    "cashCountPerformed": perform_cash_count,
                    "endingCashAmount": ending_cash or 185.75,
                    "expectedCashAmount": 188.50,
                    "variance": (ending_cash or 185.75) - 188.50,
                    "varianceAcceptable": abs((ending_cash or 185.75) - 188.50) <= 5.00,
                    "cashDropAmount": cash_drop,
                    "totalCashHandled": 1250.00
                },
                "finalSummary": {
                    "shiftDuration": "8 hours 35 minutes",
                    "totalTransactions": 47,
                    "totalSales": 2675.50,
                    "totalReturns": 89.25,
                    "netSales": 2586.25,
                    "averageTransaction": 55.03,
                    "largestTransaction": 235.75,
                    "smallestTransaction": 3.99
                },
                "paymentSummary": {
                    "cash": 425.75,
                    "creditCard": 1685.50,
                    "debitCard": 385.00,
                    "giftCard": 90.00,
                    "loyaltyPointsRedeemed": 89.25,
                    "totalPayments": 2675.50
                },
                "reconciliation": {
                    "salesRecorded": 2675.50,
                    "paymentsReceived": 2675.50,
                    "difference": 0.00,
                    "reconciled": True,
                    "discrepancies": []
                },
                "reportGeneration": {
                    "shiftReportGenerated": True,
                    "reportId": f"RPT_{random.randint(100000, 999999)}",
                    "reportPath": f"/reports/shift-{shift_id}-{datetime.now().strftime('%Y%m%d')}.pdf",
                    "emailSent": True,
                    "emailRecipients": ["store.manager@company.com", "accounting@company.com"]
                },
                "requiredApprovals": {
                    "managerApprovalRequired": abs((ending_cash or 185.75) - 188.50) > 3.00,
                    "accountingReviewRequired": False,
                    "auditFlagged": False
                },
                "nextSteps": [
                    "Deposit cash drops in safe",
                    "Submit shift report for manager review",
                    "Clean and secure register area"
                ],
                "notes": arguments.get("notes", "Shift completed successfully"),
                "closeTime": datetime.now().isoformat() + "Z"
            }
        
        elif name == "shifts_resume":
            shift_id = arguments.get("shiftId", "SHIFT001")
            employee_id = arguments.get("employeeId", "EMP001")
            register_id = arguments.get("registerId")
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/{shift_id}/Resume",
                "shiftId": shift_id,
                "employeeId": employee_id,
                "registerId": register_id or "REG001",
                "status": "active",
                "resumedTime": datetime.now().isoformat() + "Z",
                "originalStartTime": "2024-01-10T09:00:00Z",
                "suspendedTime": "2024-01-10T13:00:00Z",
                "suspendDuration": "45 minutes",
                "suspendReason": "Lunch break",
                "currentState": {
                    "cashAmount": 234.50,
                    "transactionsToday": 23,
                    "salesTotal": 1425.75,
                    "lastTransaction": "2024-01-10T12:55:00Z"
                },
                "resumeValidation": {
                    "employeeMatch": True,
                    "registerAvailable": True,
                    "cashVerified": True,
                    "systemSync": True,
                    "validationsPassed": 4,
                    "validationsFailed": 0
                },
                "permissions": {
                    "canProcessSales": True,
                    "canProcessReturns": True,
                    "canApplyDiscounts": True,
                    "canVoidTransactions": False,
                    "maxDiscountPercent": 10.0,
                    "maxVoidAmount": 100.00
                },
                "reminders": [
                    {
                        "type": "info",
                        "message": "Welcome back! Your shift has been resumed.",
                        "timestamp": datetime.now().isoformat() + "Z"
                    },
                    {
                        "type": "warning",
                        "message": "Remember to perform end-of-shift procedures before leaving.",
                        "timestamp": datetime.now().isoformat() + "Z"
                    }
                ],
                "expectedEndTime": "2024-01-10T17:30:00Z",
                "remainingShiftTime": "4 hours 15 minutes"
            }
        
        else:
            return {"error": f"Unknown shifts tool: {name}"}