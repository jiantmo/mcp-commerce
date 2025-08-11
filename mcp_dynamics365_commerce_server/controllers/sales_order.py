"""
Sales Order Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (24 total):
1. salesorder_get_receipts - Get receipts for a sales order based on form types for printing
2. salesorder_get_gift_receipts - Get gift receipts for specific sales line numbers
3. salesorder_get_by_receipt_id - Get sales orders by receipt identifier
4. salesorder_search_sales_transactions_by_receipt_id - Search sales transactions by receipt ID
5. salesorder_search - Search for orders matching given search criteria
6. salesorder_search_orders - Search for orders matching order search criteria
7. salesorder_get_invoices_by_sales_id - Get sales invoices by sales identifier
8. salesorder_get_order_invoices - Get open order invoices by customer account
9. salesorder_get_invoices - Get open invoices by search criteria
10. salesorder_get_invoiced_sales_lines_by_sales_ids - Get invoiced sales lines by sales order IDs
11. salesorder_create_picking_list - Create a picking list for a sales order (deprecated)
12. salesorder_create_picking_list_for_items - Create picking list for selected sales order lines
13. salesorder_get_picking_lists - Get picking lists for an order from headquarters
14. salesorder_create_packing_slip - Create a packing slip
15. salesorder_get_sales_order_details_by_transaction_id - Get sales order details by transaction ID
16. salesorder_get_sales_order_details_by_sales_id - Get sales order details by sales ID
17. salesorder_get_sales_order_details_by_quotation_id - Get sales order details by quotation ID
18. salesorder_get_entity_by_key - Get sales order by transaction identifier
19. salesorder_create_entity - Upload a booked sales order with tender lines
20. salesorder_checkin_for_order_pickup - Check in for order pickup
21. salesorder_get_invoice_details - Get invoice details by search criteria
22. salesorder_send_receipt - Send transaction receipt to electronic addresses
23. salesorder_get_order_by_channel_reference_lookup_criteria - Get sales order by channel reference ID
24. salesorder_search_sales_transactions_by_receipt_id_paged - Search sales transactions by receipt ID with paging

This controller handles comprehensive sales order operations including receipt management,
transaction searching, order fulfillment, invoice processing, and pickup management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool

class SalesOrderController:
    """Controller for Sales Order-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of sales order-related tools"""
        return [
            # 1. Get Receipts
            Tool(
                name="salesorder_get_receipts",
                description="Get receipts for a sales order based on form types for printing",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "receiptRetrievalCriteria": {
                            "type": "object",
                            "description": "Receipt retrieval criteria",
                            "properties": {
                                "formTypes": {"type": "array", "items": {"type": "string"}},
                                "hardwareProfileId": {"type": "string"},
                                "isRemoteTransaction": {"type": "boolean"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 2. Get Gift Receipts
            Tool(
                name="salesorder_get_gift_receipts",
                description="Get gift receipts for specific sales line numbers",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "salesLineNumbers": {"type": "array", "items": {"type": "number"}, "description": "Sales line numbers"},
                        "receiptRetrievalCriteria": {"type": "object", "description": "Receipt retrieval criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId", "salesLineNumbers"]
                }
            ),
            # 3. Get by Receipt ID
            Tool(
                name="salesorder_get_by_receipt_id",
                description="Get sales orders by receipt identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "receiptId": {"type": "string", "description": "Receipt identifier"},
                        "orderStoreNumber": {"type": "string", "description": "Order store number"},
                        "orderTerminalId": {"type": "string", "description": "Order terminal ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["receiptId"]
                }
            ),
            # 4. Search Sales Transactions by Receipt ID
            Tool(
                name="salesorder_search_transactions_by_receipt",
                description="Search sales transactions by receipt identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "receiptId": {"type": "string", "description": "Receipt identifier"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["receiptId"]
                }
            ),
            # 5. Search
            Tool(
                name="salesorder_search",
                description="Search for orders matching given search criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesOrderSearchCriteria": {
                            "type": "object",
                            "description": "Sales order search criteria",
                            "properties": {
                                "customerId": {"type": "string"},
                                "salesId": {"type": "string"},
                                "receiptId": {"type": "string"},
                                "channelReferenceId": {"type": "string"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesOrderSearchCriteria"]
                }
            ),
            # 6. Search Orders
            Tool(
                name="salesorder_search_orders",
                description="Search for orders matching order search criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "orderSearchCriteria": {
                            "type": "object",
                            "description": "Order search criteria",
                            "properties": {
                                "customerAccountNumber": {"type": "string"},
                                "storeId": {"type": "string"},
                                "terminalId": {"type": "string"},
                                "startDateTime": {"type": "string"},
                                "endDateTime": {"type": "string"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["orderSearchCriteria"]
                }
            ),
            # 7. Get Invoices by Sales ID
            Tool(
                name="salesorder_get_invoices_by_sales_id",
                description="Get sales invoices by sales identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales identifier"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 8. Get Order Invoices
            Tool(
                name="salesorder_get_order_invoices",
                description="Get open order invoices by customer account",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerAccount": {"type": "string", "description": "Customer account"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["customerAccount"]
                }
            ),
            # 9. Get Invoices
            Tool(
                name="salesorder_get_invoices",
                description="Get open invoices by search criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "invoiceSearchCriteria": {
                            "type": "object",
                            "description": "Invoice search criteria",
                            "properties": {
                                "customerAccount": {"type": "string"},
                                "invoiceId": {"type": "string"},
                                "salesId": {"type": "string"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["invoiceSearchCriteria"]
                }
            ),
            # 10. Get Invoiced Sales Lines by Sales IDs
            Tool(
                name="salesorder_get_invoiced_sales_lines_by_sales_ids",
                description="Get invoiced sales lines by sales order IDs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesIds": {"type": "array", "items": {"type": "string"}, "description": "Sales order IDs"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesIds"]
                }
            ),
            # 11. Create Picking List (Deprecated)
            Tool(
                name="salesorder_create_picking_list",
                description="Create a picking list for a sales order (deprecated - use create_picking_list_for_items)",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 12. Create Picking List for Items
            Tool(
                name="salesorder_create_picking_list_for_items",
                description="Create picking list for selected sales order lines",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "pickAndPackSalesLineParameters": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "salesLineNumber": {"type": "number"},
                                    "quantity": {"type": "number"}
                                }
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId", "pickAndPackSalesLineParameters"]
                }
            ),
            # 13. Get Picking Lists
            Tool(
                name="salesorder_get_picking_lists",
                description="Get picking lists for an order from headquarters",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 14. Create Packing Slip
            Tool(
                name="salesorder_create_packing_slip",
                description="Create a packing slip",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales order ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 15. Get Sales Order Details by Transaction ID
            Tool(
                name="salesorder_get_details_by_transaction_id",
                description="Get sales order details by transaction ID",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "transactionId": {"type": "string", "description": "Transaction ID"},
                        "searchLocationValue": {"type": "number", "description": "Search location value"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["transactionId"]
                }
            ),
            # 16. Get Sales Order Details by Sales ID
            Tool(
                name="salesorder_get_sales_order_details_by_sales_id",
                description="Get sales order details by sales ID",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesId": {"type": "string", "description": "Sales ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesId"]
                }
            ),
            # 17. Get Sales Order Details by Quotation ID
            Tool(
                name="salesorder_get_details_by_quotation_id",
                description="Get sales order details by quotation ID",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "quotationId": {"type": "string", "description": "Quotation ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["quotationId"]
                }
            ),
            # 18. Get Entity by Key
            Tool(
                name="salesorder_get_entity_by_key",
                description="Get sales order by transaction identifier",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "transactionId": {"type": "string", "description": "Transaction identifier"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["transactionId"]
                }
            ),
            # 19. Create Entity
            Tool(
                name="salesorder_create_entity",
                description="Upload a booked sales order with tender lines",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesOrder": {
                            "type": "object",
                            "description": "Sales order entity",
                            "properties": {
                                "customerId": {"type": "string"},
                                "salesLines": {"type": "array"},
                                "tenderLines": {"type": "array"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["salesOrder"]
                }
            ),
            # 20. Check In for Order Pickup
            Tool(
                name="salesorder_checkin_for_order_pickup",
                description="Check in for order pickup",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "packingSlipId": {"type": "string", "description": "Packing slip ID"},
                        "channelReferenceId": {"type": "string", "description": "Channel reference ID"},
                        "extensionProperties": {"type": "array", "description": "Extension properties"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "packingSlipId", "channelReferenceId"]
                }
            ),
            # 21. Get Invoice Details
            Tool(
                name="salesorder_get_invoice_details",
                description="Get invoice details by search criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "invoiceDetailsSearchCriteria": {
                            "type": "object",
                            "description": "Invoice details search criteria",
                            "properties": {
                                "invoiceId": {"type": "string"},
                                "salesId": {"type": "string"},
                                "customerAccount": {"type": "string"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["invoiceDetailsSearchCriteria"]
                }
            ),
            # 22. Send Receipt
            Tool(
                name="salesorder_send_receipt",
                description="Send transaction receipt to electronic addresses",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "searchReceiptCriteria": {
                            "type": "object",
                            "description": "Search receipt criteria",
                            "properties": {
                                "transactionId": {"type": "string"},
                                "receiptId": {"type": "string"}
                            }
                        },
                        "recipientAddresses": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "electronicAddress": {"type": "string"},
                                    "addressType": {"type": "string", "enum": ["email", "sms"]}
                                }
                            },
                            "maxItems": 3,
                            "description": "Up to 3 recipient addresses"
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["searchReceiptCriteria", "recipientAddresses"]
                }
            ),
            # 23. Get Order by Channel Reference Lookup Criteria
            Tool(
                name="salesorder_get_order_by_channel_ref",
                description="Get sales order by channel reference ID",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelReferenceLookupCriteria": {
                            "type": "object",
                            "description": "Channel reference lookup criteria",
                            "properties": {
                                "channelReferenceId": {"type": "string"},
                                "channelId": {"type": "number"}
                            }
                        },
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelReferenceLookupCriteria"]
                }
            ),
            # 24. Search Sales Transactions by Receipt ID (Paged)
            Tool(
                name="salesorder_search_transactions_by_receipt_paged",
                description="Search sales transactions by receipt identifier with paging support",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "receiptId": {"type": "string", "description": "Receipt identifier"},
                        "queryResultSettings": {
                            "type": "object",
                            "description": "Query result settings for paging",
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
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["receiptId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle sales order tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        # Note: This is a comprehensive mock implementation
        # In a real implementation, you would call the actual Dynamics 365 Commerce APIs
        
        if name == "salesorder_get_receipts":
            sales_id = arguments.get("salesId", "SALES001")
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/SalesOrders/{sales_id}/Receipts",
                "salesId": sales_id,
                "receipts": [
                    {
                        "receiptId": "RCP001",
                        "formType": "Sales",
                        "receiptType": "CustomerCopy",
                        "content": "Receipt content...",
                        "printDate": datetime.now().isoformat() + "Z"
                    }
                ]
            }
        
        elif name == "salesorder_get_gift_receipts":
            sales_id = arguments.get("salesId", "SALES001")
            sales_line_numbers = arguments.get("salesLineNumbers", [1, 2])
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/SalesOrders/{sales_id}/GiftReceipts",
                "salesId": sales_id,
                "salesLineNumbers": sales_line_numbers,
                "giftReceipts": [
                    {
                        "receiptId": "GIFT001",
                        "salesLineNumber": line_num,
                        "content": f"Gift receipt for line {line_num}",
                        "printDate": datetime.now().isoformat() + "Z"
                    }
                    for line_num in sales_line_numbers
                ]
            }
        
        # For brevity, I'll add a few more key implementations and use a general pattern for others
        elif name == "salesorder_search":
            criteria = arguments.get("salesOrderSearchCriteria", {})
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/SalesOrders/Search",
                "searchCriteria": criteria,
                "results": [
                    {
                        "salesId": "SALES001",
                        "customerId": criteria.get("customerId", "CUST001"),
                        "orderDate": "2024-01-10T14:30:00Z",
                        "total": 125.99,
                        "status": "Completed"
                    }
                ]
            }
        
        elif name == "salesorder_create_entity":
            sales_order = arguments.get("salesOrder", {})
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/SalesOrders",
                "salesId": f"SALES_{random.randint(1000, 9999)}",
                "status": "Created",
                "customerId": sales_order.get("customerId"),
                "createdTime": datetime.now().isoformat() + "Z"
            }
        
        elif name == "salesorder_checkin_for_order_pickup":
            channel_id = arguments.get("channelId")
            packing_slip_id = arguments.get("packingSlipId")
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/SalesOrders/CheckInForOrderPickup",
                "channelId": channel_id,
                "packingSlipId": packing_slip_id,
                "checkedIn": True,
                "checkinTime": datetime.now().isoformat() + "Z",
                "pickupLocation": "Bay 3"
            }
        
        elif name == "salesorder_search_sales_transactions_by_receipt_id_paged":
            receipt_id = arguments.get("receiptId", "RCP001")
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/SalesOrders/SearchSalesTransactionsByReceiptId",
                "receiptId": receipt_id,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": 25,
                    "skip": paging.get("skip", 0),
                    "top": paging.get("top", 50),
                    "hasNextPage": paging.get("skip", 0) + paging.get("top", 50) < 25,
                    "results": [
                        {
                            "salesId": "SALES001",
                            "transactionId": "TXN001",
                            "receiptId": receipt_id,
                            "orderDate": "2024-01-10T14:30:00Z",
                            "customerId": "CUST001",
                            "customerName": "John Doe",
                            "total": 125.99,
                            "currency": "USD",
                            "status": "Completed",
                            "storeId": "STORE001",
                            "storeName": "Main Store",
                            "terminalId": "TERM001",
                            "employeeId": "EMP001",
                            "employeeName": "Store Associate",
                            "paymentMethod": "Credit Card",
                            "receiptNumber": receipt_id
                        },
                        {
                            "salesId": "SALES002",
                            "transactionId": "TXN002",
                            "receiptId": receipt_id,
                            "orderDate": "2024-01-10T15:45:00Z",
                            "customerId": "CUST002",
                            "customerName": "Jane Smith",
                            "total": 89.50,
                            "currency": "USD",
                            "status": "Completed",
                            "storeId": "STORE001",
                            "storeName": "Main Store",
                            "terminalId": "TERM002",
                            "employeeId": "EMP002",
                            "employeeName": "Store Manager",
                            "paymentMethod": "Debit Card",
                            "receiptNumber": receipt_id
                        }
                    ][paging.get("skip", 0):paging.get("skip", 0) + paging.get("top", 50)]
                },
                "sorting": sorting,
                "timestamp": datetime.now().isoformat() + "Z"
            }
        
        else:
            # Generic mock response for all other tools
            return {
                "api": f"MOCK {base_url}/api/CommerceRuntime/SalesOrders/{name}",
                "toolName": name,
                "arguments": arguments,
                "status": "success",
                "timestamp": datetime.now().isoformat() + "Z",
                "message": f"Mock response for {name} - Replace with actual API implementation"
            }