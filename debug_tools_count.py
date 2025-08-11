#!/usr/bin/env python3
"""
Debug script to analyze tool count and registration in MCP server
"""

import os
from mcp_dynamics365_commerce_server.server import Dynamics365CommerceServer

def analyze_tools():
    """Analyze all tools registered in the server"""
    
    print("MCP Tools Analysis")
    print("=" * 60)
    
    # Initialize server
    server = Dynamics365CommerceServer()
    
    # Get tools from each controller
    controllers = [
        ('customer_controller', server.customer_controller),
        ('sales_order_controller', server.sales_order_controller),
        ('cart_controller', server.cart_controller),
        ('products_controller', server.products_controller),
        ('org_units_controller', server.org_units_controller),
        ('loyalty_card_controller', server.loyalty_card_controller),
        ('shifts_controller', server.shifts_controller),
        ('address_controller', server.address_controller),
        ('barcode_controller', server.barcode_controller),
        ('cash_declaration_controller', server.cash_declaration_controller),
        ('cities_controller', server.cities_controller),
        ('counties_controller', server.counties_controller),
        ('country_region_controller', server.country_region_controller),
        ('credit_memo_controller', server.credit_memo_controller),
        ('suspended_cart_controller', server.suspended_cart_controller),
        ('tender_types_controller', server.tender_types_controller),
        ('reason_codes_controller', server.reason_codes_controller),
        ('pricing_controller', server.pricing_controller),
        ('delivery_options_controller', server.delivery_options_controller),
        ('customer_group_controller', server.customer_group_controller),
        ('currency_controller', server.currency_controller),
        ('customer_balance_controller', server.customer_balance_controller),
        ('device_configuration_controller', server.device_configuration_controller),
        ('language_controller', server.language_controller),
        # Additional controllers
        ('app_info_controller', server.app_info_controller),
        ('async_service_controller', server.async_service_controller),
        ('attribute_controller', server.attribute_controller),
        ('attribute_group_controller', server.attribute_group_controller),
        ('audit_event_controller', server.audit_event_controller),
        ('card_type_controller', server.card_type_controller),
        ('catalogs_controller', server.catalogs_controller),
        ('categories_controller', server.categories_controller),
        ('commission_sales_group_controller', server.commission_sales_group_controller),
        ('district_controller', server.district_controller),
        ('environment_configuration_controller', server.environment_configuration_controller),
        ('extension_package_definition_controller', server.extension_package_definition_controller),
        ('extensible_enumeration_controller', server.extensible_enumeration_controller),
        ('gift_card_controller', server.gift_card_controller),
        ('hardware_profiles_controller', server.hardware_profiles_controller),
        ('image_controller', server.image_controller),
        ('income_expense_accounts_controller', server.income_expense_accounts_controller),
        ('kits_controller', server.kits_controller),
        ('localized_string_controller', server.localized_string_controller),
        ('notification_controller', server.notification_controller),
        ('number_sequence_controller', server.number_sequence_controller),
        ('operations_controller', server.operations_controller),
        ('product_lists_controller', server.product_lists_controller),
        ('purchase_order_controller', server.purchase_order_controller),
        ('recommendation_controller', server.recommendation_controller),
        ('receipt_controller', server.receipt_controller),
        ('report_datasets_controller', server.report_datasets_controller),
        ('search_controller', server.search_controller),
        ('shift_reconciliation_lines_controller', server.shift_reconciliation_lines_controller),
        ('state_province_controller', server.state_province_controller),
        ('store_safe_controller', server.store_safe_controller),
        ('tax_controller', server.tax_controller),
        ('tender_drop_and_declare_operation_controller', server.tender_drop_and_declare_operation_controller),
        ('transfer_order_controller', server.transfer_order_controller),
        ('unit_of_measure_controller', server.unit_of_measure_controller),
        ('warehouse_controller', server.warehouse_controller),
        ('zipcodes_controller', server.zipcodes_controller),
        ('publishing_controller', server.publishing_controller),
        ('non_sales_transaction_tender_operations_controller', server.non_sales_transaction_tender_operations_controller),
        ('sales_orders_fulfillment_controller', server.sales_orders_fulfillment_controller),
        ('scan_result_controller', server.scan_result_controller),
        ('stock_count_journal_controller', server.stock_count_journal_controller),
    ]
    
    total_tools = 0
    all_tool_names = []
    
    print("Controller Analysis:")
    print("-" * 40)
    
    for controller_name, controller in controllers:
        try:
            tools = controller.get_tools()
            tool_count = len(tools)
            total_tools += tool_count
            
            tool_names = [tool.name for tool in tools]
            all_tool_names.extend(tool_names)
            
            print(f"{controller_name:<50} {tool_count:>3} tools")
            
            # Show first few tool names for verification
            if tool_count > 0:
                sample_tools = tool_names[:3]
                if len(tool_names) > 3:
                    sample_tools.append("...")
                print(f"  Sample tools: {', '.join(sample_tools)}")
            else:
                print("  No tools found!")
        
        except Exception as e:
            print(f"{controller_name:<50} ERROR: {e}")
    
    print("-" * 60)
    print(f"Total Tools: {total_tools}")
    
    # Check for duplicates
    duplicate_tools = set()
    seen_tools = set()
    for tool_name in all_tool_names:
        if tool_name in seen_tools:
            duplicate_tools.add(tool_name)
        seen_tools.add(tool_name)
    
    if duplicate_tools:
        print(f"WARNING: Found {len(duplicate_tools)} duplicate tool names:")
        for dup in sorted(duplicate_tools):
            print(f"  - {dup}")
    
    print(f"\nUnique Tools: {len(seen_tools)}")
    
    # Show distribution by prefix
    print("\nTool Distribution by Prefix:")
    print("-" * 30)
    prefixes = {}
    for tool_name in all_tool_names:
        prefix = tool_name.split('_')[0]
        prefixes[prefix] = prefixes.get(prefix, 0) + 1
    
    for prefix, count in sorted(prefixes.items()):
        print(f"{prefix:<20} {count:>3} tools")
    
    return total_tools, len(seen_tools), all_tool_names

def compare_with_server_registration():
    """Compare with actual server registration"""
    print("\n" + "=" * 60)
    print("Server Registration Analysis")
    print("=" * 60)
    
    server = Dynamics365CommerceServer()
    
    # Get tools as they would be registered in list_tools
    registered_tools = []
    
    # This mirrors the list_tools function in server.py
    registered_tools.extend(server.customer_controller.get_tools())
    registered_tools.extend(server.sales_order_controller.get_tools())
    registered_tools.extend(server.cart_controller.get_tools())
    registered_tools.extend(server.products_controller.get_tools())
    registered_tools.extend(server.org_units_controller.get_tools())
    registered_tools.extend(server.loyalty_card_controller.get_tools())
    registered_tools.extend(server.shifts_controller.get_tools())
    registered_tools.extend(server.address_controller.get_tools())
    registered_tools.extend(server.barcode_controller.get_tools())
    registered_tools.extend(server.cash_declaration_controller.get_tools())
    registered_tools.extend(server.cities_controller.get_tools())
    registered_tools.extend(server.counties_controller.get_tools())
    registered_tools.extend(server.country_region_controller.get_tools())
    registered_tools.extend(server.credit_memo_controller.get_tools())
    registered_tools.extend(server.suspended_cart_controller.get_tools())
    registered_tools.extend(server.tender_types_controller.get_tools())
    registered_tools.extend(server.reason_codes_controller.get_tools())
    registered_tools.extend(server.pricing_controller.get_tools())
    registered_tools.extend(server.delivery_options_controller.get_tools())
    registered_tools.extend(server.customer_group_controller.get_tools())
    registered_tools.extend(server.currency_controller.get_tools())
    registered_tools.extend(server.customer_balance_controller.get_tools())
    registered_tools.extend(server.device_configuration_controller.get_tools())
    registered_tools.extend(server.language_controller.get_tools())
    # Newly added
    registered_tools.extend(server.app_info_controller.get_tools())
    registered_tools.extend(server.async_service_controller.get_tools())
    registered_tools.extend(server.attribute_controller.get_tools())
    registered_tools.extend(server.attribute_group_controller.get_tools())
    registered_tools.extend(server.audit_event_controller.get_tools())
    registered_tools.extend(server.card_type_controller.get_tools())
    registered_tools.extend(server.catalogs_controller.get_tools())
    registered_tools.extend(server.categories_controller.get_tools())
    registered_tools.extend(server.commission_sales_group_controller.get_tools())
    registered_tools.extend(server.district_controller.get_tools())
    registered_tools.extend(server.environment_configuration_controller.get_tools())
    registered_tools.extend(server.extension_package_definition_controller.get_tools())
    registered_tools.extend(server.extensible_enumeration_controller.get_tools())
    registered_tools.extend(server.gift_card_controller.get_tools())
    registered_tools.extend(server.hardware_profiles_controller.get_tools())
    registered_tools.extend(server.image_controller.get_tools())
    registered_tools.extend(server.income_expense_accounts_controller.get_tools())
    registered_tools.extend(server.kits_controller.get_tools())
    registered_tools.extend(server.localized_string_controller.get_tools())
    registered_tools.extend(server.notification_controller.get_tools())
    registered_tools.extend(server.number_sequence_controller.get_tools())
    registered_tools.extend(server.operations_controller.get_tools())
    registered_tools.extend(server.product_lists_controller.get_tools())
    registered_tools.extend(server.purchase_order_controller.get_tools())
    registered_tools.extend(server.recommendation_controller.get_tools())
    registered_tools.extend(server.receipt_controller.get_tools())
    registered_tools.extend(server.report_datasets_controller.get_tools())
    registered_tools.extend(server.search_controller.get_tools())
    registered_tools.extend(server.shift_reconciliation_lines_controller.get_tools())
    registered_tools.extend(server.state_province_controller.get_tools())
    registered_tools.extend(server.store_safe_controller.get_tools())
    registered_tools.extend(server.tax_controller.get_tools())
    registered_tools.extend(server.tender_drop_and_declare_operation_controller.get_tools())
    registered_tools.extend(server.transfer_order_controller.get_tools())
    registered_tools.extend(server.unit_of_measure_controller.get_tools())
    registered_tools.extend(server.warehouse_controller.get_tools())
    registered_tools.extend(server.zipcodes_controller.get_tools())
    registered_tools.extend(server.publishing_controller.get_tools())
    registered_tools.extend(server.non_sales_transaction_tender_operations_controller.get_tools())
    registered_tools.extend(server.sales_orders_fulfillment_controller.get_tools())
    registered_tools.extend(server.scan_result_controller.get_tools())
    registered_tools.extend(server.stock_count_journal_controller.get_tools())
    
    print(f"Tools registered in server: {len(registered_tools)}")
    
    return len(registered_tools)

def main():
    """Main analysis function"""
    total_tools, unique_tools, all_tool_names = analyze_tools()
    registered_count = compare_with_server_registration()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Expected tools (from README): 386")
    print(f"Total tools found: {total_tools}")
    print(f"Unique tools: {unique_tools}")
    print(f"Registered in server: {registered_count}")
    print(f"Claude Desktop shows: 320 (reported)")
    
    print(f"\nDiscrepancy Analysis:")
    if total_tools != 386:
        print(f"  - Missing {386 - total_tools} tools from expected count")
    if unique_tools != total_tools:
        print(f"  - {total_tools - unique_tools} duplicate tool names found")
    if registered_count != unique_tools:
        print(f"  - Registration mismatch: {abs(registered_count - unique_tools)} tools")
    if registered_count != 320:
        print(f"  - Claude Desktop shows {320}, server has {registered_count}")

if __name__ == "__main__":
    main()