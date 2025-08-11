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
# Newly added controllers
from .controllers.app_info import AppInfoController
from .controllers.async_service import AsyncServiceController
from .controllers.attribute import AttributeController
from .controllers.attribute_group import AttributeGroupController
from .controllers.audit_event import AuditEventController
from .controllers.card_type import CardTypeController
from .controllers.catalogs import CatalogsController
from .controllers.categories import CategoriesController
from .controllers.commission_sales_group import CommissionSalesGroupController
from .controllers.district import DistrictController
from .controllers.environment_configuration import EnvironmentConfigurationController
from .controllers.extension_package_definition import ExtensionPackageDefinitionController
from .controllers.extensible_enumeration import ExtensibleEnumerationController
from .controllers.gift_card import GiftCardController
from .controllers.hardware_profiles import HardwareProfilesController
from .controllers.image import ImageController
from .controllers.income_expense_accounts import IncomeExpenseAccountsController
from .controllers.kits import KitsController
from .controllers.localized_string import LocalizedStringController
from .controllers.notification import NotificationController
from .controllers.number_sequence import NumberSequenceController
from .controllers.operations import OperationsController
from .controllers.product_lists import ProductListsController
from .controllers.purchase_order import PurchaseOrderController
from .controllers.recommendation import RecommendationController
from .controllers.receipt import ReceiptController
from .controllers.report_datasets import ReportDatasetsController
from .controllers.search import SearchController
from .controllers.shift_reconciliation_lines import ShiftReconciliationLinesController
from .controllers.state_province import StateProvinceController
from .controllers.store_safe import StoreSafeController
from .controllers.tax import TaxController
from .controllers.tender_drop_and_declare_operation import TenderDropAndDeclareOperationController
from .controllers.transfer_order import TransferOrderController
from .controllers.unit_of_measure import UnitOfMeasureController
from .controllers.warehouse import WarehouseController
from .controllers.zipcodes import ZipcodesController
from .controllers.publishing import PublishingController
from .controllers.non_sales_transaction_tender_operations import NonSalesTransactionTenderOperationsController
from .controllers.sales_orders_fulfillment import SalesOrdersFulfillmentController
from .controllers.scan_result import ScanResultController
from .controllers.stock_count_journal import StockCountJournalController

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
        # Newly added controllers instances
        self.app_info_controller = AppInfoController()
        self.async_service_controller = AsyncServiceController()
        self.attribute_controller = AttributeController()
        self.attribute_group_controller = AttributeGroupController()
        self.audit_event_controller = AuditEventController()
        self.card_type_controller = CardTypeController()
        self.catalogs_controller = CatalogsController()
        self.categories_controller = CategoriesController()
        self.commission_sales_group_controller = CommissionSalesGroupController()
        self.district_controller = DistrictController()
        self.environment_configuration_controller = EnvironmentConfigurationController()
        self.extension_package_definition_controller = ExtensionPackageDefinitionController()
        self.extensible_enumeration_controller = ExtensibleEnumerationController()
        self.gift_card_controller = GiftCardController()
        self.hardware_profiles_controller = HardwareProfilesController()
        self.image_controller = ImageController()
        self.income_expense_accounts_controller = IncomeExpenseAccountsController()
        self.kits_controller = KitsController()
        self.localized_string_controller = LocalizedStringController()
        self.notification_controller = NotificationController()
        self.number_sequence_controller = NumberSequenceController()
        self.operations_controller = OperationsController()
        self.product_lists_controller = ProductListsController()
        self.purchase_order_controller = PurchaseOrderController()
        self.recommendation_controller = RecommendationController()
        self.receipt_controller = ReceiptController()
        self.report_datasets_controller = ReportDatasetsController()
        self.search_controller = SearchController()
        self.shift_reconciliation_lines_controller = ShiftReconciliationLinesController()
        self.state_province_controller = StateProvinceController()
        self.store_safe_controller = StoreSafeController()
        self.tax_controller = TaxController()
        self.tender_drop_and_declare_operation_controller = TenderDropAndDeclareOperationController()
        self.transfer_order_controller = TransferOrderController()
        self.unit_of_measure_controller = UnitOfMeasureController()
        self.warehouse_controller = WarehouseController()
        self.zipcodes_controller = ZipcodesController()
        self.publishing_controller = PublishingController()
        self.non_sales_transaction_tender_operations_controller = NonSalesTransactionTenderOperationsController()
        self.sales_orders_fulfillment_controller = SalesOrdersFulfillmentController()
        self.scan_result_controller = ScanResultController()
        self.stock_count_journal_controller = StockCountJournalController()
        
        # Register all tools (aggregate only; actual exposure is via the list_tools handler below)
        self._register_tools()
    
    def _register_tools(self):
        """Aggregate tools from all controllers. The MCP exposure happens in the list_tools handler."""
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
        # Newly added
        all_tools.extend(self.app_info_controller.get_tools())
        all_tools.extend(self.async_service_controller.get_tools())
        all_tools.extend(self.attribute_controller.get_tools())
        all_tools.extend(self.attribute_group_controller.get_tools())
        all_tools.extend(self.audit_event_controller.get_tools())
        all_tools.extend(self.card_type_controller.get_tools())
        all_tools.extend(self.catalogs_controller.get_tools())
        all_tools.extend(self.categories_controller.get_tools())
        all_tools.extend(self.commission_sales_group_controller.get_tools())
        all_tools.extend(self.district_controller.get_tools())
        all_tools.extend(self.environment_configuration_controller.get_tools())
        all_tools.extend(self.extension_package_definition_controller.get_tools())
        all_tools.extend(self.extensible_enumeration_controller.get_tools())
        all_tools.extend(self.gift_card_controller.get_tools())
        all_tools.extend(self.hardware_profiles_controller.get_tools())
        all_tools.extend(self.image_controller.get_tools())
        all_tools.extend(self.income_expense_accounts_controller.get_tools())
        all_tools.extend(self.kits_controller.get_tools())
        all_tools.extend(self.localized_string_controller.get_tools())
        all_tools.extend(self.notification_controller.get_tools())
        all_tools.extend(self.number_sequence_controller.get_tools())
        all_tools.extend(self.operations_controller.get_tools())
        all_tools.extend(self.product_lists_controller.get_tools())
        all_tools.extend(self.purchase_order_controller.get_tools())
        all_tools.extend(self.recommendation_controller.get_tools())
        all_tools.extend(self.receipt_controller.get_tools())
        all_tools.extend(self.report_datasets_controller.get_tools())
        all_tools.extend(self.search_controller.get_tools())
        all_tools.extend(self.shift_reconciliation_lines_controller.get_tools())
        all_tools.extend(self.state_province_controller.get_tools())
        all_tools.extend(self.store_safe_controller.get_tools())
        all_tools.extend(self.tax_controller.get_tools())
        all_tools.extend(self.tender_drop_and_declare_operation_controller.get_tools())
        all_tools.extend(self.transfer_order_controller.get_tools())
        all_tools.extend(self.unit_of_measure_controller.get_tools())
        all_tools.extend(self.warehouse_controller.get_tools())
        all_tools.extend(self.zipcodes_controller.get_tools())
        all_tools.extend(self.publishing_controller.get_tools())
        all_tools.extend(self.non_sales_transaction_tender_operations_controller.get_tools())
        all_tools.extend(self.sales_orders_fulfillment_controller.get_tools())
        all_tools.extend(self.scan_result_controller.get_tools())
        all_tools.extend(self.stock_count_journal_controller.get_tools())
        
        # Store for optional debugging/reference
        self._all_tools_cached = all_tools
    
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
            # Newly added routing
            elif name.startswith("appinfo_"):
                result = await self.app_info_controller.handle_tool(name, arguments)
            elif name.startswith("async_service_"):
                result = await self.async_service_controller.handle_tool(name, arguments)
            elif name.startswith("attribute_"):
                result = await self.attribute_controller.handle_tool(name, arguments)
            elif name.startswith("attribute_group_"):
                result = await self.attribute_group_controller.handle_tool(name, arguments)
            elif name.startswith("audit_event_"):
                result = await self.audit_event_controller.handle_tool(name, arguments)
            elif name.startswith("card_type_"):
                result = await self.card_type_controller.handle_tool(name, arguments)
            elif name.startswith("catalogs_"):
                result = await self.catalogs_controller.handle_tool(name, arguments)
            elif name.startswith("categories_"):
                result = await self.categories_controller.handle_tool(name, arguments)
            elif name.startswith("commission_sales_"):
                result = await self.commission_sales_group_controller.handle_tool(name, arguments)
            elif name.startswith("district_"):
                result = await self.district_controller.handle_tool(name, arguments)
            elif name.startswith("env_config_"):
                result = await self.environment_configuration_controller.handle_tool(name, arguments)
            elif name.startswith("ext_pkg_def_"):
                result = await self.extension_package_definition_controller.handle_tool(name, arguments)
            elif name.startswith("extensible_enum_"):
                result = await self.extensible_enumeration_controller.handle_tool(name, arguments)
            elif name.startswith("gift_card_"):
                result = await self.gift_card_controller.handle_tool(name, arguments)
            elif name.startswith("hardware_profiles_"):
                result = await self.hardware_profiles_controller.handle_tool(name, arguments)
            elif name.startswith("image_"):
                result = await self.image_controller.handle_tool(name, arguments)
            elif name.startswith("income_expense_"):
                result = await self.income_expense_accounts_controller.handle_tool(name, arguments)
            elif name.startswith("kits_"):
                result = await self.kits_controller.handle_tool(name, arguments)
            elif name.startswith("localized_string_"):
                result = await self.localized_string_controller.handle_tool(name, arguments)
            elif name.startswith("notification_"):
                result = await self.notification_controller.handle_tool(name, arguments)
            elif name.startswith("number_sequence_"):
                result = await self.number_sequence_controller.handle_tool(name, arguments)
            elif name.startswith("operations_"):
                result = await self.operations_controller.handle_tool(name, arguments)
            elif name.startswith("product_lists_"):
                result = await self.product_lists_controller.handle_tool(name, arguments)
            elif name.startswith("purchase_order_"):
                result = await self.purchase_order_controller.handle_tool(name, arguments)
            elif name.startswith("recommendation_"):
                result = await self.recommendation_controller.handle_tool(name, arguments)
            elif name.startswith("receipt_"):
                result = await self.receipt_controller.handle_tool(name, arguments)
            elif name.startswith("report_datasets_"):
                result = await self.report_datasets_controller.handle_tool(name, arguments)
            elif name.startswith("search_"):
                result = await self.search_controller.handle_tool(name, arguments)
            elif name.startswith("shift_recon_"):
                result = await self.shift_reconciliation_lines_controller.handle_tool(name, arguments)
            elif name.startswith("state_province_"):
                result = await self.state_province_controller.handle_tool(name, arguments)
            elif name.startswith("store_safe_"):
                result = await self.store_safe_controller.handle_tool(name, arguments)
            elif name.startswith("tax_"):
                result = await self.tax_controller.handle_tool(name, arguments)
            elif name.startswith("tender_drop_"):
                result = await self.tender_drop_and_declare_operation_controller.handle_tool(name, arguments)
            elif name.startswith("transfer_order_"):
                result = await self.transfer_order_controller.handle_tool(name, arguments)
            elif name.startswith("unit_of_measure_"):
                result = await self.unit_of_measure_controller.handle_tool(name, arguments)
            elif name.startswith("warehouse_"):
                result = await self.warehouse_controller.handle_tool(name, arguments)
            elif name.startswith("zipcodes_"):
                result = await self.zipcodes_controller.handle_tool(name, arguments)
            elif name.startswith("publishing_"):
                result = await self.publishing_controller.handle_tool(name, arguments)
            elif name.startswith("non_sales_tender_"):
                result = await self.non_sales_transaction_tender_operations_controller.handle_tool(name, arguments)
            elif name.startswith("fulfillment_"):
                result = await self.sales_orders_fulfillment_controller.handle_tool(name, arguments)
            elif name.startswith("scan_result_"):
                result = await self.scan_result_controller.handle_tool(name, arguments)
            elif name.startswith("stock_count_"):
                result = await self.stock_count_journal_controller.handle_tool(name, arguments)
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
        # Newly added
        all_tools.extend(server_instance.app_info_controller.get_tools())
        all_tools.extend(server_instance.async_service_controller.get_tools())
        all_tools.extend(server_instance.attribute_controller.get_tools())
        all_tools.extend(server_instance.attribute_group_controller.get_tools())
        all_tools.extend(server_instance.audit_event_controller.get_tools())
        all_tools.extend(server_instance.card_type_controller.get_tools())
        all_tools.extend(server_instance.catalogs_controller.get_tools())
        all_tools.extend(server_instance.categories_controller.get_tools())
        all_tools.extend(server_instance.commission_sales_group_controller.get_tools())
        all_tools.extend(server_instance.district_controller.get_tools())
        all_tools.extend(server_instance.environment_configuration_controller.get_tools())
        all_tools.extend(server_instance.extension_package_definition_controller.get_tools())
        all_tools.extend(server_instance.extensible_enumeration_controller.get_tools())
        all_tools.extend(server_instance.gift_card_controller.get_tools())
        all_tools.extend(server_instance.hardware_profiles_controller.get_tools())
        all_tools.extend(server_instance.image_controller.get_tools())
        all_tools.extend(server_instance.income_expense_accounts_controller.get_tools())
        all_tools.extend(server_instance.kits_controller.get_tools())
        all_tools.extend(server_instance.localized_string_controller.get_tools())
        all_tools.extend(server_instance.notification_controller.get_tools())
        all_tools.extend(server_instance.number_sequence_controller.get_tools())
        all_tools.extend(server_instance.operations_controller.get_tools())
        all_tools.extend(server_instance.product_lists_controller.get_tools())
        all_tools.extend(server_instance.purchase_order_controller.get_tools())
        all_tools.extend(server_instance.recommendation_controller.get_tools())
        all_tools.extend(server_instance.receipt_controller.get_tools())
        all_tools.extend(server_instance.report_datasets_controller.get_tools())
        all_tools.extend(server_instance.search_controller.get_tools())
        all_tools.extend(server_instance.shift_reconciliation_lines_controller.get_tools())
        all_tools.extend(server_instance.state_province_controller.get_tools())
        all_tools.extend(server_instance.store_safe_controller.get_tools())
        all_tools.extend(server_instance.tax_controller.get_tools())
        all_tools.extend(server_instance.tender_drop_and_declare_operation_controller.get_tools())
        all_tools.extend(server_instance.transfer_order_controller.get_tools())
        all_tools.extend(server_instance.unit_of_measure_controller.get_tools())
        all_tools.extend(server_instance.warehouse_controller.get_tools())
        all_tools.extend(server_instance.zipcodes_controller.get_tools())
        all_tools.extend(server_instance.publishing_controller.get_tools())
        all_tools.extend(server_instance.non_sales_transaction_tender_operations_controller.get_tools())
        all_tools.extend(server_instance.sales_orders_fulfillment_controller.get_tools())
        all_tools.extend(server_instance.scan_result_controller.get_tools())
        all_tools.extend(server_instance.stock_count_journal_controller.get_tools())
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