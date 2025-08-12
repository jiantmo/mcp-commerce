"""
Shifts Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (20 total):
1. shifts_get_shift - Get information about a specific shift
2. shifts_get_by_status - Get shifts by status
3. shifts_get_by_status_filter_by_user_role - Get shifts by status filtered by user role
4. shifts_get_by_retrieval_criteria - Get shifts by retrieval criteria
5. shifts_upsert_and_validate_shifts - Insert or update and validate shifts
6. shifts_delete_shifts - Delete shifts (not supported in online context)
7. shifts_open - Open a new shift
8. shifts_close - Close a shift
9. shifts_blind_close - Blind close a shift
10. shifts_force_delete - Forcefully delete a shift
11. shifts_resume - Resume a shift
12. shifts_use - Use an existing shift
13. shifts_suspend - Suspend a shift
14. shifts_post_shift - Handle POST requests to create new shift
15. shifts_patch_shift - Handle PATCH requests to update existing shift
16. shifts_get_x_report - Get X report for a shift
17. shifts_get_z_report - Get Z report
18. shifts_validate_cash_drawer_limit - Validate cash drawer limit
19. shifts_get_suspended_carts_by_shift - Get suspended carts for a shift
20. shifts_void_suspended_carts - Void suspended transactions for a shift

This controller handles all employee shift operations including shift management,
cash handling, performance tracking, shift lifecycle operations, and reporting.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool
from ..config import get_base_url

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
                        "shiftId": {"type": "string", "description": "The shift ID to retrieve"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId"]
                }
            ),
            Tool(
                name="shifts_get_by_status",
                description="Get shifts by status",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "statusValue": {"type": "number", "description": "Status value"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["statusValue"]
                }
            ),
            Tool(
                name="shifts_get_by_status_filter_by_user_role",
                description="Get shifts by status filtered by user role",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "statusValue": {"type": "number", "description": "Status value"},
                        "filterByUserRole": {"type": "boolean", "description": "Filter by user role"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["statusValue", "filterByUserRole"]
                }
            ),
            Tool(
                name="shifts_get_by_retrieval_criteria",
                description="Get shifts by retrieval criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftRetrievalCriteria": {"type": "object", "description": "Shift retrieval criteria"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftRetrievalCriteria"]
                }
            ),
            Tool(
                name="shifts_upsert_and_validate_shifts",
                description="Insert or update and validate shifts",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "shifts": {"type": "array", "description": "Collection of shifts"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["terminalId", "shifts"]
                }
            ),
            Tool(
                name="shifts_delete_shifts",
                description="Delete shifts (not supported in online context)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    }
                }
            ),
            Tool(
                name="shifts_open",
                description="Open a new shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    }
                }
            ),
            Tool(
                name="shifts_close",
                description="Close a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "forceClose": {"type": "boolean", "description": "Force close flag"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "transactionId", "forceClose"]
                }
            ),
            Tool(
                name="shifts_blind_close",
                description="Blind close a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "forceClose": {"type": "boolean", "description": "Force close flag"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "transactionId", "forceClose"]
                }
            ),
            Tool(
                name="shifts_force_delete",
                description="Forcefully delete a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "transactionId"]
                }
            ),
            Tool(
                name="shifts_resume",
                description="Resume a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "cashDrawer": {"type": "string", "description": "Cash drawer"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "cashDrawer"]
                }
            ),
            Tool(
                name="shifts_use",
                description="Use an existing shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId"]
                }
            ),
            Tool(
                name="shifts_suspend",
                description="Suspend a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "transactionId"]
                }
            ),
            Tool(
                name="shifts_post_shift",
                description="Handle POST requests to create new shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shift": {"type": "object", "description": "Shift object"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shift"]
                }
            ),
            Tool(
                name="shifts_patch_shift",
                description="Handle PATCH requests to update existing shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "delta": {"type": "object", "description": "Delta changes"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "delta"]
                }
            ),
            Tool(
                name="shifts_get_x_report",
                description="Get X report for a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "terminalId": {"type": "string", "description": "Terminal ID"},
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "hardwareProfileId": {"type": "string", "description": "Hardware profile ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "terminalId", "transactionId", "hardwareProfileId"]
                }
            ),
            Tool(
                name="shifts_get_z_report",
                description="Get Z report",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "hardwareProfileId": {"type": "string", "description": "Hardware profile ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["transactionId", "hardwareProfileId"]
                }
            ),
            Tool(
                name="shifts_validate_cash_drawer_limit",
                description="Validate cash drawer limit",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftTerminalId": {"type": "string", "description": "Shift terminal ID"},
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftTerminalId", "shiftId"]
                }
            ),
            Tool(
                name="shifts_get_suspended_carts_by_shift",
                description="Get suspended carts for a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftTerminalId": {"type": "string", "description": "Shift terminal ID"},
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftTerminalId", "shiftId"]
                }
            ),
            Tool(
                name="shifts_void_suspended_carts",
                description="Void suspended transactions for a shift",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "shiftId": {"type": "number", "description": "Shift ID"},
                        "shiftTerminalId": {"type": "string", "description": "Shift terminal ID"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    },
                    "required": ["shiftId", "shiftTerminalId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle shifts tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "shifts_get_shift":
            shift_id = arguments.get("shiftId", "1")
            terminal_id = arguments.get("terminalId", "TERM001")
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/{shift_id}/{terminal_id}",
                "shiftId": shift_id,
                "terminalId": terminal_id,
                "employeeId": "EMP001",
                "employeeName": "John Smith",
                "status": "Open",
                "startTime": datetime.now().isoformat() + "Z",
                "currentCashAmount": 250.00,
                "transactionCount": 15,
                "totalSales": 1250.75
            }
        
        elif name == "shifts_get_by_status":
            status_value = arguments.get("statusValue", 1)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/GetByStatus/{status_value}",
                "statusValue": status_value,
                "shifts": [
                    {
                        "shiftId": f"SHIFT{i:03d}",
                        "employeeId": f"EMP{i:03d}",
                        "status": "Open" if status_value == 1 else "Closed",
                        "startTime": datetime.now().isoformat() + "Z"
                    }
                    for i in range(1, 4)
                ]
            }
        
        elif name == "shifts_get_by_status_filter_by_user_role":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/GetByStatusFilterByUserRole",
                "statusValue": arguments.get("statusValue", 1),
                "filterByUserRole": arguments.get("filterByUserRole", True),
                "shifts": [
                    {
                        "shiftId": "SHIFT001",
                        "employeeId": "EMP001",
                        "role": "Cashier",
                        "status": "Open",
                        "startTime": datetime.now().isoformat() + "Z"
                    }
                ]
            }
        
        elif name == "shifts_get_by_retrieval_criteria":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/GetByRetrievalCriteria",
                "criteria": arguments.get("shiftRetrievalCriteria", {}),
                "shifts": [
                    {
                        "shiftId": "SHIFT001",
                        "employeeId": "EMP001",
                        "storeId": "STORE001",
                        "terminalId": "TERM001",
                        "status": "Open",
                        "startTime": datetime.now().isoformat() + "Z"
                    }
                ]
            }
        
        elif name == "shifts_upsert_and_validate_shifts":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/UpsertAndValidate",
                "success": True,
                "validationResults": {
                    "isValid": True,
                    "errors": [],
                    "warnings": []
                },
                "processedShifts": len(arguments.get("shifts", []))
            }
        
        elif name == "shifts_delete_shifts":
            return {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Shifts",
                "success": False,
                "error": "Delete shifts is not supported in the online context",
                "errorCode": "OPERATION_NOT_SUPPORTED"
            }
        
        elif name == "shifts_open":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Open",
                "shiftId": f"SHIFT{random.randint(1000, 9999)}",
                "employeeId": "EMP001",
                "terminalId": "TERM001",
                "startTime": datetime.now().isoformat() + "Z",
                "status": "Open",
                "startingCash": 200.00,
                "currentCash": 200.00
            }
        
        elif name == "shifts_close":
            shift_id = arguments.get("shiftId", 1)
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Close",
                "shiftId": shift_id,
                "terminalId": arguments.get("terminalId", "TERM001"),
                "endTime": datetime.now().isoformat() + "Z",
                "status": "Closed",
                "finalCashAmount": 475.25,
                "totalSales": 1250.75,
                "transactionCount": 15,
                "cashVariance": 0.00
            }
        
        elif name == "shifts_blind_close":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/BlindClose",
                "shiftId": arguments.get("shiftId", 1),
                "endTime": datetime.now().isoformat() + "Z",
                "status": "Blind Closed",
                "message": "Shift closed without cash count verification"
            }
        
        elif name == "shifts_force_delete":
            return {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Shifts/ForceDelete",
                "shiftId": arguments.get("shiftId", 1),
                "success": True,
                "message": "Shift forcefully deleted",
                "deletedAt": datetime.now().isoformat() + "Z"
            }
        
        elif name == "shifts_resume":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Resume",
                "shiftId": arguments.get("shiftId", 1),
                "terminalId": arguments.get("terminalId", "TERM001"),
                "resumedAt": datetime.now().isoformat() + "Z",
                "status": "Open",
                "cashDrawer": arguments.get("cashDrawer", "DRAWER001")
            }
        
        elif name == "shifts_use":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Use",
                "shiftId": arguments.get("shiftId", 1),
                "terminalId": arguments.get("terminalId", "TERM001"),
                "usedAt": datetime.now().isoformat() + "Z",
                "status": "In Use"
            }
        
        elif name == "shifts_suspend":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/Suspend",
                "shiftId": arguments.get("shiftId", 1),
                "suspendedAt": datetime.now().isoformat() + "Z",
                "status": "Suspended",
                "reason": "Employee break"
            }
        
        elif name == "shifts_post_shift":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts",
                "createdShift": {
                    "shiftId": f"SHIFT{random.randint(1000, 9999)}",
                    "createdAt": datetime.now().isoformat() + "Z",
                    "status": "Created"
                }
            }
        
        elif name == "shifts_patch_shift":
            return {
                "api": f"PATCH {base_url}/api/CommerceRuntime/Shifts/{arguments.get('shiftId', 1)}",
                "shiftId": arguments.get("shiftId", 1),
                "updatedAt": datetime.now().isoformat() + "Z",
                "changes": arguments.get("delta", {}),
                "success": True
            }
        
        elif name == "shifts_get_x_report":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/XReport",
                "reportType": "X Report",
                "shiftId": arguments.get("shiftId", 1),
                "generatedAt": datetime.now().isoformat() + "Z",
                "receipt": {
                    "receiptId": f"X{random.randint(100000, 999999)}",
                    "content": "X Report - Shift Summary",
                    "format": "text/plain"
                }
            }
        
        elif name == "shifts_get_z_report":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/ZReport",
                "reportType": "Z Report",
                "generatedAt": datetime.now().isoformat() + "Z",
                "receipt": {
                    "receiptId": f"Z{random.randint(100000, 999999)}",
                    "content": "Z Report - End of Day Summary",
                    "format": "text/plain"
                }
            }
        
        elif name == "shifts_validate_cash_drawer_limit":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/ValidateCashDrawerLimit",
                "shiftId": arguments.get("shiftId", 1),
                "currentCash": 275.50,
                "cashLimit": 500.00,
                "isWithinLimit": True,
                "recommendation": "Normal operation"
            }
        
        elif name == "shifts_get_suspended_carts_by_shift":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Shifts/GetSuspendedCarts",
                "shiftId": arguments.get("shiftId", 1),
                "suspendedCarts": [
                    {
                        "cartId": f"CART{i:03d}",
                        "customerId": f"CUST{i:03d}",
                        "suspendedAt": datetime.now().isoformat() + "Z",
                        "totalAmount": round(random.uniform(50, 500), 2)
                    }
                    for i in range(1, 4)
                ]
            }
        
        elif name == "shifts_void_suspended_carts":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Shifts/VoidSuspendedCarts",
                "shiftId": arguments.get("shiftId", 1),
                "voidedAt": datetime.now().isoformat() + "Z",
                "voidedCount": 3,
                "success": True
            }
        
        else:
            return {"error": f"Unknown shifts tool: {name}"}
