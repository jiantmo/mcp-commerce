#!/usr/bin/env python3
"""
Test script to validate the MCP server can be registered properly
"""

import sys
import asyncio
from mcp_dynamics365_commerce_server.server import Dynamics365CommerceServer

def test_server_initialization():
    """Test if the server can be initialized"""
    try:
        server = Dynamics365CommerceServer()
        print("✓ Server initialization: SUCCESS")
        return True
    except Exception as e:
        print(f"✗ Server initialization: FAILED - {e}")
        return False

def test_controllers():
    """Test if all controllers can provide tools"""
    try:
        server = Dynamics365CommerceServer()
        
        # Test key controllers
        customer_tools = server.customer_controller.get_tools()
        products_tools = server.products_controller.get_tools()
        cart_tools = server.cart_controller.get_tools()
        sales_order_tools = server.sales_order_controller.get_tools()
        
        print(f"✓ Customer controller: {len(customer_tools)} tools")
        print(f"✓ Products controller: {len(products_tools)} tools")
        print(f"✓ Cart controller: {len(cart_tools)} tools") 
        print(f"✓ Sales Order controller: {len(sales_order_tools)} tools")
        
        # Count total tools across all controllers
        all_tools = []
        all_tools.extend(server.customer_controller.get_tools())
        all_tools.extend(server.sales_order_controller.get_tools())
        all_tools.extend(server.cart_controller.get_tools())
        all_tools.extend(server.products_controller.get_tools())
        all_tools.extend(server.org_units_controller.get_tools())
        all_tools.extend(server.loyalty_card_controller.get_tools())
        all_tools.extend(server.shifts_controller.get_tools())
        all_tools.extend(server.address_controller.get_tools())
        all_tools.extend(server.barcode_controller.get_tools())
        all_tools.extend(server.cash_declaration_controller.get_tools())
        all_tools.extend(server.cities_controller.get_tools())
        all_tools.extend(server.counties_controller.get_tools())
        all_tools.extend(server.country_region_controller.get_tools())
        all_tools.extend(server.credit_memo_controller.get_tools())
        all_tools.extend(server.suspended_cart_controller.get_tools())
        all_tools.extend(server.tender_types_controller.get_tools())
        all_tools.extend(server.reason_codes_controller.get_tools())
        all_tools.extend(server.pricing_controller.get_tools())
        all_tools.extend(server.delivery_options_controller.get_tools())
        all_tools.extend(server.customer_group_controller.get_tools())
        all_tools.extend(server.currency_controller.get_tools())
        all_tools.extend(server.customer_balance_controller.get_tools())
        all_tools.extend(server.device_configuration_controller.get_tools())
        all_tools.extend(server.language_controller.get_tools())
        all_tools.extend(server.app_info_controller.get_tools())
        all_tools.extend(server.async_service_controller.get_tools())
        all_tools.extend(server.attribute_controller.get_tools())
        all_tools.extend(server.attribute_group_controller.get_tools())
        all_tools.extend(server.audit_event_controller.get_tools())
        all_tools.extend(server.card_type_controller.get_tools())
        all_tools.extend(server.catalogs_controller.get_tools())
        all_tools.extend(server.categories_controller.get_tools())
        all_tools.extend(server.commission_sales_group_controller.get_tools())
        all_tools.extend(server.district_controller.get_tools())
        all_tools.extend(server.environment_configuration_controller.get_tools())
        all_tools.extend(server.extension_package_definition_controller.get_tools())
        all_tools.extend(server.extensible_enumeration_controller.get_tools())
        all_tools.extend(server.gift_card_controller.get_tools())
        all_tools.extend(server.hardware_profiles_controller.get_tools())
        all_tools.extend(server.image_controller.get_tools())
        all_tools.extend(server.income_expense_accounts_controller.get_tools())
        all_tools.extend(server.kits_controller.get_tools())
        all_tools.extend(server.localized_string_controller.get_tools())
        all_tools.extend(server.notification_controller.get_tools())
        all_tools.extend(server.number_sequence_controller.get_tools())
        all_tools.extend(server.operations_controller.get_tools())
        all_tools.extend(server.product_lists_controller.get_tools())
        all_tools.extend(server.purchase_order_controller.get_tools())
        all_tools.extend(server.recommendation_controller.get_tools())
        all_tools.extend(server.receipt_controller.get_tools())
        all_tools.extend(server.report_datasets_controller.get_tools())
        all_tools.extend(server.search_controller.get_tools())
        all_tools.extend(server.shift_reconciliation_lines_controller.get_tools())
        all_tools.extend(server.state_province_controller.get_tools())
        all_tools.extend(server.store_safe_controller.get_tools())
        all_tools.extend(server.tax_controller.get_tools())
        all_tools.extend(server.tender_drop_and_declare_operation_controller.get_tools())
        all_tools.extend(server.transfer_order_controller.get_tools())
        all_tools.extend(server.unit_of_measure_controller.get_tools())
        all_tools.extend(server.warehouse_controller.get_tools())
        all_tools.extend(server.zipcodes_controller.get_tools())
        all_tools.extend(server.publishing_controller.get_tools())
        all_tools.extend(server.non_sales_transaction_tender_operations_controller.get_tools())
        all_tools.extend(server.sales_orders_fulfillment_controller.get_tools())
        all_tools.extend(server.scan_result_controller.get_tools())
        all_tools.extend(server.stock_count_journal_controller.get_tools())
        
        print(f"✓ Total MCP tools available: {len(all_tools)}")
        return True
    except Exception as e:
        print(f"✗ Controllers test: FAILED - {e}")
        return False

async def test_async_functionality():
    """Test if async functionality works"""
    try:
        server = Dynamics365CommerceServer()
        
        # Test a simple tool call
        result = await server.handle_call_tool(
            "customer_search", 
            {"query": "test", "store_id": "test"}
        )
        
        print("✓ Async tool call: SUCCESS")
        return True
    except Exception as e:
        print(f"✗ Async tool call: FAILED - {e}")
        return False

def main():
    """Main validation function"""
    print("🔍 Validating MCP Dynamics 365 Commerce Server...")
    print("=" * 50)
    
    success = True
    
    # Test 1: Server initialization
    if not test_server_initialization():
        success = False
    
    # Test 2: Controllers
    if not test_controllers():
        success = False
    
    # Test 3: Async functionality
    if not asyncio.run(test_async_functionality()):
        success = False
    
    print("=" * 50)
    if success:
        print("🎉 ALL TESTS PASSED - MCP server is ready for registration!")
        print("\nNext steps:")
        print("1. Reload VS Code window")
        print("2. Open GitHub Copilot Chat")  
        print("3. Look for 'MCP Server: d365-commerce' in Add More Tools...")
        return 0
    else:
        print("❌ SOME TESTS FAILED - Fix issues before registration")
        return 1

if __name__ == "__main__":
    sys.exit(main())
