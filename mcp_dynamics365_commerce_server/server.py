#!/usr/bin/env python3

import asyncio
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional
import json
import random
import string

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)
from pydantic import BaseModel
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import controller tools
from .controllers.customer import CustomerController
from .controllers.sales_order import SalesOrderController
from .controllers.cart import CartController
from .controllers.products import ProductsController
from .controllers.org_units import OrgUnitsController
from .controllers.loyalty_card import LoyaltyCardController
from .controllers.shifts import ShiftsController
from .controllers.address import AddressController
from .controllers.barcode import BarcodeController
from .controllers.cash_declaration import CashDeclarationController
from .controllers.cities import CitiesController
from .controllers.counties import CountiesController
from .controllers.country_region import CountryRegionController
from .controllers.credit_memo import CreditMemoController
from .controllers.suspended_cart import SuspendedCartController
from .controllers.tender_types import TenderTypesController
from .controllers.reason_codes import ReasonCodesController
from .controllers.pricing import PricingController
from .controllers.delivery_options import DeliveryOptionsController
from .controllers.customer_group import CustomerGroupController
from .controllers.currency import CurrencyController
from .controllers.customer_balance import CustomerBalanceController
from .controllers.device_configuration import DeviceConfigurationController
from .controllers.language import LanguageController

class Dynamics365CommerceServer:
    def __init__(self):
        self.server = Server("mcp-dynamics365-commerce-server")
        
        # Initialize controllers
        self.customer_controller = CustomerController()
        self.sales_order_controller = SalesOrderController()
        self.cart_controller = CartController()
        self.products_controller = ProductsController()
        self.org_units_controller = OrgUnitsController()
        self.loyalty_card_controller = LoyaltyCardController()
        self.shifts_controller = ShiftsController()
        self.address_controller = AddressController()
        self.barcode_controller = BarcodeController()
        self.cash_declaration_controller = CashDeclarationController()
        self.cities_controller = CitiesController()
        self.counties_controller = CountiesController()
        self.country_region_controller = CountryRegionController()
        self.credit_memo_controller = CreditMemoController()
        self.suspended_cart_controller = SuspendedCartController()
        self.tender_types_controller = TenderTypesController()
        self.reason_codes_controller = ReasonCodesController()
        self.pricing_controller = PricingController()
        self.delivery_options_controller = DeliveryOptionsController()
        self.customer_group_controller = CustomerGroupController()
        self.currency_controller = CurrencyController()
        self.customer_balance_controller = CustomerBalanceController()
        self.device_configuration_controller = DeviceConfigurationController()
        self.language_controller = LanguageController()
        
        # Register all tools
        self._register_tools()
    
    def _register_tools(self):
        """Register all tools from all controllers"""
        all_tools = []
        
        # Collect tools from all controllers
        all_tools.extend(self.customer_controller.get_tools())
        all_tools.extend(self.sales_order_controller.get_tools())
        all_tools.extend(self.cart_controller.get_tools())
        all_tools.extend(self.products_controller.get_tools())
        all_tools.extend(self.org_units_controller.get_tools())
        all_tools.extend(self.loyalty_card_controller.get_tools())
        all_tools.extend(self.shifts_controller.get_tools())
        all_tools.extend(self.address_controller.get_tools())
        all_tools.extend(self.barcode_controller.get_tools())
        all_tools.extend(self.cash_declaration_controller.get_tools())
        all_tools.extend(self.cities_controller.get_tools())
        all_tools.extend(self.counties_controller.get_tools())
        all_tools.extend(self.country_region_controller.get_tools())
        all_tools.extend(self.credit_memo_controller.get_tools())
        all_tools.extend(self.suspended_cart_controller.get_tools())
        all_tools.extend(self.tender_types_controller.get_tools())
        all_tools.extend(self.reason_codes_controller.get_tools())
        all_tools.extend(self.pricing_controller.get_tools())
        all_tools.extend(self.delivery_options_controller.get_tools())
        all_tools.extend(self.customer_group_controller.get_tools())
        all_tools.extend(self.currency_controller.get_tools())
        all_tools.extend(self.customer_balance_controller.get_tools())
        all_tools.extend(self.device_configuration_controller.get_tools())
        all_tools.extend(self.language_controller.get_tools())
        
        # Register tools with server
        for tool in all_tools:
            self.server.list_tools().append(tool)
    
    async def handle_call_tool(self, name: str, arguments: Dict[str, Any]) -> CallToolResult:
        """Handle tool calls by delegating to appropriate controller"""
        try:
            logger.info(f"Calling tool: {name} with arguments: {arguments}")
            
            # Route to appropriate controller based on tool name prefix
            if name.startswith("customer_"):
                result = await self.customer_controller.handle_tool(name, arguments)
            elif name.startswith("salesorder_"):
                result = await self.sales_order_controller.handle_tool(name, arguments)
            elif name.startswith("cart_"):
                result = await self.cart_controller.handle_tool(name, arguments)
            elif name.startswith("products_"):
                result = await self.products_controller.handle_tool(name, arguments)
            elif name.startswith("orgunits_"):
                result = await self.org_units_controller.handle_tool(name, arguments)
            elif name.startswith("loyaltycard_"):
                result = await self.loyalty_card_controller.handle_tool(name, arguments)
            elif name.startswith("shifts_"):
                result = await self.shifts_controller.handle_tool(name, arguments)
            elif name.startswith("address_"):
                result = await self.address_controller.handle_tool(name, arguments)
            elif name.startswith("barcode_"):
                result = await self.barcode_controller.handle_tool(name, arguments)
            elif name.startswith("cash_declaration_"):
                result = await self.cash_declaration_controller.handle_tool(name, arguments)
            elif name.startswith("cities_"):
                result = await self.cities_controller.handle_tool(name, arguments)
            elif name.startswith("counties_"):
                result = await self.counties_controller.handle_tool(name, arguments)
            elif name.startswith("country_region_"):
                result = await self.country_region_controller.handle_tool(name, arguments)
            elif name.startswith("credit_memo_"):
                result = await self.credit_memo_controller.handle_tool(name, arguments)
            elif name.startswith("suspended_cart_"):
                result = await self.suspended_cart_controller.handle_tool(name, arguments)
            elif name.startswith("tender_types_"):
                result = await self.tender_types_controller.handle_tool(name, arguments)
            elif name.startswith("reason_codes_"):
                result = await self.reason_codes_controller.handle_tool(name, arguments)
            elif name.startswith("pricing_"):
                result = await self.pricing_controller.handle_tool(name, arguments)
            elif name.startswith("delivery_options_"):
                result = await self.delivery_options_controller.handle_tool(name, arguments)
            elif name.startswith("customer_group_"):
                result = await self.customer_group_controller.handle_tool(name, arguments)
            elif name.startswith("currency_"):
                result = await self.currency_controller.handle_tool(name, arguments)
            elif name.startswith("customer_balance_"):
                result = await self.customer_balance_controller.handle_tool(name, arguments)
            elif name.startswith("device_configuration_"):
                result = await self.device_configuration_controller.handle_tool(name, arguments)
            elif name.startswith("language_"):
                result = await self.language_controller.handle_tool(name, arguments)
            else:
                result = {"error": f"Unknown tool: {name}"}
            
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=json.dumps(result, indent=2, default=str)
                    )
                ]
            )
        
        except Exception as e:
            logger.error(f"Error calling tool {name}: {e}")
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=json.dumps({"error": str(e)}, indent=2)
                    )
                ]
            )

async def main():
    """Main entry point for the MCP server"""
    server_instance = Dynamics365CommerceServer()
    
    # Set up the server handlers
    @server_instance.server.list_tools()
    async def list_tools() -> List[Tool]:
        """List available tools"""
        all_tools = []
        all_tools.extend(server_instance.customer_controller.get_tools())
        all_tools.extend(server_instance.sales_order_controller.get_tools())
        all_tools.extend(server_instance.cart_controller.get_tools())
        all_tools.extend(server_instance.products_controller.get_tools())
        all_tools.extend(server_instance.org_units_controller.get_tools())
        all_tools.extend(server_instance.loyalty_card_controller.get_tools())
        all_tools.extend(server_instance.shifts_controller.get_tools())
        all_tools.extend(server_instance.address_controller.get_tools())
        all_tools.extend(server_instance.barcode_controller.get_tools())
        all_tools.extend(server_instance.cash_declaration_controller.get_tools())
        all_tools.extend(server_instance.cities_controller.get_tools())
        all_tools.extend(server_instance.counties_controller.get_tools())
        all_tools.extend(server_instance.country_region_controller.get_tools())
        all_tools.extend(server_instance.credit_memo_controller.get_tools())
        all_tools.extend(server_instance.suspended_cart_controller.get_tools())
        all_tools.extend(server_instance.tender_types_controller.get_tools())
        all_tools.extend(server_instance.reason_codes_controller.get_tools())
        all_tools.extend(server_instance.pricing_controller.get_tools())
        all_tools.extend(server_instance.delivery_options_controller.get_tools())
        all_tools.extend(server_instance.customer_group_controller.get_tools())
        all_tools.extend(server_instance.currency_controller.get_tools())
        all_tools.extend(server_instance.customer_balance_controller.get_tools())
        all_tools.extend(server_instance.device_configuration_controller.get_tools())
        all_tools.extend(server_instance.language_controller.get_tools())
        return all_tools
    
    @server_instance.server.call_tool()
    async def call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
        """Handle tool calls"""
        return await server_instance.handle_call_tool(name, arguments)
    
    # Run the server
    async with stdio_server() as (read_stream, write_stream):
        await server_instance.server.run(
            read_stream,
            write_stream,
            server_instance.server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())