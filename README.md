# MCP Dynamics 365 Commerce Server

A Model Context Protocol (MCP) server that provides tools for interacting with Dynamics 365 Commerce Retail Server Customer Consumer APIs. This server enables AI assistants to perform commerce operations through a comprehensive set of tools organized by controller.

## Features

This MCP server provides **125+ tools** organized into **19+ controllers**, covering the main Dynamics 365 Commerce API endpoints:

### 🛍️ Customer Controller (10 tools)
- `customer_get_order_shipments_history` - Get order shipments history for a customer
- `customer_create_entity` - Create a new customer entity
- `customer_update_entity` - Update an existing customer entity
- `customer_get_order_history` - Get order history for a customer
- `customer_search` - Search for customers by various criteria
- `customer_get_purchase_history` - Get purchase history for a customer
- `customer_get_by_account_numbers` - Get customers list from account numbers
- `customer_get_customer_search_fields` - Get customer search fields for the store
- `customer_search_by_fields` - Search for customers by specified fields
- `customer_post_loyalty_points` - Post non-transactional loyalty points

### 📦 Sales Order Controller (24 tools)
- `salesorder_get_receipts` - Get receipts for a sales order based on form types for printing
- `salesorder_get_gift_receipts` - Get gift receipts for specific sales line numbers
- `salesorder_get_by_receipt_id` - Get sales orders by receipt identifier
- `salesorder_search_transactions_by_receipt` - Search sales transactions by receipt ID
- `salesorder_search` - Search for orders matching given search criteria
- `salesorder_search_orders` - Search for orders matching order search criteria
- `salesorder_get_invoices_by_sales_id` - Get sales invoices by sales identifier
- `salesorder_get_order_invoices` - Get open order invoices by customer account
- `salesorder_get_invoices` - Get open invoices by search criteria
- `salesorder_get_invoiced_sales_lines_by_sales_ids` - Get invoiced sales lines by sales order IDs
- `salesorder_create_picking_list` - Create a picking list for a sales order (deprecated)
- `salesorder_create_picking_list_for_items` - Create picking list for selected sales order lines
- `salesorder_get_picking_lists` - Get picking lists for an order from headquarters
- `salesorder_create_packing_slip` - Create a packing slip
- `salesorder_get_details_by_transaction_id` - Get sales order details by transaction ID
- `salesorder_get_sales_order_details_by_sales_id` - Get sales order details by sales ID
- `salesorder_get_details_by_quotation_id` - Get sales order details by quotation ID
- `salesorder_get_entity_by_key` - Get sales order by transaction identifier
- `salesorder_create_entity` - Upload a booked sales order with tender lines
- `salesorder_checkin_for_order_pickup` - Check in for order pickup
- `salesorder_get_invoice_details` - Get invoice details by search criteria
- `salesorder_send_receipt` - Send transaction receipt to electronic addresses
- `salesorder_get_order_by_channel_ref` - Get sales order by channel reference ID
- `salesorder_search_transactions_by_receipt_paged` - Search sales transactions by receipt ID with paging

### 🛒 Cart Controller (55 tools)
- `cart_checkout` - Checkout the cart with payment processing
- `cart_add_cart_lines` - Add cart lines (items) to the cart
- `cart_void_cart_lines` - Void cart lines in the cart
- `cart_update_cart_lines` - Update existing cart lines in the cart
- `cart_refill_gift_card` - Add balance to a gift card
- `cart_issue_gift_card` - Issue a new gift card
- `cart_cashout_gift_card` - Cash out a gift card
- `cart_add_tender_line` - Add a cart tender line
- `cart_add_preprocessed_tender_line` - Add pre-processed tender line
- `cart_validate_tender_line_for_add` - Validate tender line before adding
- `cart_update_tender_line_signature` - Update cart tender line signature
- `cart_void_tender_line` - Void a cart tender line
- `cart_suspend_with_journal` - Suspend cart and make journal entry
- `cart_resume` - Resume a suspended cart
- `cart_resume_from_receipt_id` - Resume cart from receipt ID
- `cart_recall_order` - Recall customer order
- `cart_add_invoiced_sales_lines_to_cart` - Add invoiced sales lines to cart
- `cart_recall_quote` - Recall quote
- `cart_recall_sales_invoice` - Recall sales invoice
- `cart_add_order_invoice` - Add order invoice to cart
- `cart_add_invoices` - Add invoices to cart
- `cart_recalculate_order` - Recalculate customer order
- `cart_update_commission_sales_group` - Update commission sales group
- `cart_delivery_preferences` - Get cart delivery preferences
- `cart_get_line_delivery_options` - Get line delivery options
- `cart_get_line_delivery_options_by_channel_id` - Get line delivery options by channel
- `cart_get_payments_history` - Get payments history
- `cart_get_delivery_options` - Get delivery options
- `cart_update_line_delivery_specifications` - Update line delivery specifications
- `cart_add_charge` - Add charge to cart
- `cart_override_charge` - Override charge amount
- `cart_add_cart_line_charge` - Add charge to cart line
- `cart_override_cart_line_charge` - Override cart line charge
- `cart_update_delivery_specification` - Update delivery specification
- `cart_override_cart_line_price` - Override cart line price
- `cart_get_promotions` - Get cart promotions
- `cart_add_discount_code` - Add discount code
- `cart_remove_discount_codes` - Remove discount codes
- `cart_remove_cart_lines` - Remove cart lines
- `cart_search` - Search carts by criteria
- `cart_get_card_payment_accept_point` - Get card payment accept point
- `cart_retrieve_card_payment_accept_result` - Retrieve card payment accept result
- `cart_add_coupons` - Add coupons to cart
- `cart_remove_coupons` - Remove coupons from cart
- `cart_get_charge_codes` - Get charge codes
- `cart_get_max_loyalty_points_for_balance` - Get max loyalty points for redemption
- `cart_get_declined_or_voided_card_receipts` - Get declined/voided card receipts
- `cart_reset_all_charges` - Reset all charges
- `cart_get_entity_by_key` - Get cart entity by key
- `cart_create_entity` - Create cart entity
- `cart_update_entity` - Update cart entity
- `cart_delete_entity` - Delete cart entity
- `cart_get_cart_by_id` - Get cart by ID
- `cart_merge_carts` - Merge multiple carts
- `cart_validate_cart` - Validate cart before checkout

### 🏷️ Products Controller (4 tools)
- `products_search` - Search for products by various criteria
- `products_get_by_id` - Get detailed information about a specific product
- `products_get_recommended_products` - Get recommended products based on a specific product
- `products_get_product_availability` - Get product availability across different locations

### 🏪 Org Units Controller (3 tools)
- `orgunits_get_locations_by_area` - Get store locations within a specific area
- `orgunits_get_available_inventory` - Get available inventory for a store/warehouse
- `orgunits_get_store_hours` - Get operating hours for a specific store

### 💳 Loyalty Card Controller (3 tools)
- `loyaltycard_issue_loyalty_card` - Issue a new loyalty card to a customer
- `loyaltycard_get_loyalty_card` - Get loyalty card information and status
- `loyaltycard_get_loyalty_card_transactions` - Get transaction history for a loyalty card

### 👨‍💼 Shifts Controller (4 tools)
- `shifts_get_shift` - Get information about a specific shift
- `shifts_open` - Open a new shift for an employee
- `shifts_close` - Close an existing shift
- `shifts_resume` - Resume a previously suspended shift

### 🏠 Address Controller (1 tool)
- `address_get_address_purposes` - Gets the address purposes with paging and sorting support

### 🏷️ Barcode Controller (1 tool) 
- `barcode_get_barcode_by_id` - Gets barcode by identifier

### 💰 Cash Declaration Controller (1 tool)
- `cash_declaration_get_cash_declarations` - Gets cash declarations with paging support

### 🏙️ Cities Controller (1 tool)
- `cities_get_cities` - Get all the cities filtered by Country/Region, State Province and County

### 🏞️ Counties Controller (1 tool)
- `counties_get_counties` - Get all the counties filtered by country/region and state province

### 🌍 Country Region Controller (3 tools)
- `country_region_get_country_regions_for_shipping` - Gets countries/regions with delivery modes configured
- `country_region_get_country_regions_by_language_id` - Get countries/regions filtered by Language Id
- `country_region_get_country_regions` - Get all the countries/regions

### 📄 Credit Memo Controller (1 tool)
- `credit_memo_get_credit_memo_by_id` - Get credit memo by identifier

### 🛒 Suspended Cart Controller (1 tool) 
- `suspended_cart_get_all_suspended_carts` - Gets all suspended carts

### 💳 Tender Types Controller (2 tools)
- `tender_types_get_tender_types` - Gets tender types
- `tender_types_round_amount_by_tender_type` - Round amount by tender type

### ❓ Reason Codes Controller (3 tools)
- `reason_codes_get_reason_codes` - Gets the reason codes
- `reason_codes_get_return_order_reason_codes` - Gets return order reason codes
- `reason_codes_get_reason_codes_by_id` - Gets reason codes by group or single identifier

### 💲 Pricing Controller (1 tool)
- `pricing_calculate_sales_document` - Calculates prices and discounts for products at given quantities

### 🚚 Delivery Options Controller (1 tool)
- `delivery_options_get_delivery_options` - Get the delivery options for the channel

### 👥 Customer Group Controller (1 tool) 
- `customer_group_get_customer_groups` - Gets collection of customer group

### 💱 Currency Controller (2 tools)
- `currency_get_currencies_amount` - Gets the currencies amount
- `currency_calculate_total_currency_amount` - Calculates the total currency amount

### ⚖️ Customer Balance Controller (1 tool)
- `customer_balance_get_customer_balance` - Gets the customer balance

### 📱 Device Configuration Controller (1 tool)
- `device_configuration_get_device_configuration` - Gets a single device configuration

### 🌐 Language Controller (1 tool)
- `language_get_languages` - Gets collection of supported languages

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mcp-commerce
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or using pip with pyproject.toml:
   ```bash
   pip install -e .
   ```

## Configuration

### Claude Desktop

Add the server to your Claude Desktop configuration file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "dynamics365-commerce": {
      "command": "python",
      "args": ["/path/to/mcp-commerce/mcp_dynamics365_commerce_server/server.py"],
      "env": {
        "DYNAMICS365_BASE_URL": "https://your-commerce-site.com"
      }
    }
  }
}
```

### VS Code with MCP Extension

1. Install the MCP extension for VS Code
2. Add the server configuration:

```json
{
  "name": "dynamics365-commerce",
  "command": "python",
  "args": ["/path/to/mcp-commerce/mcp_dynamics365_commerce_server/server.py"],
  "env": {
    "DYNAMICS365_BASE_URL": "https://your-commerce-site.com"
  }
}
```

## Usage

Once configured, you can use the tools in your AI conversations:

### Example Customer Operations
```
"Search for customers with email containing 'john@example.com'"
"Get order history for customer CUST001"
"Create a new customer with name 'Jane Smith' and email 'jane.smith@example.com'"
```

### Example Product Operations
```
"Search for wireless headphones under $100"
"Get detailed information for product PROD001"
"Check availability of product PROD001 in Seattle area"
```

### Example Cart Operations
```
"Add product PROD001 with quantity 2 to cart CART001"
"Checkout cart CART001 with credit card payment"
"Suspend cart CART001 with reason 'customer will return later'"
```

### Example Store Operations
```
"Find stores in Seattle area with pickup service"
"Get inventory for store STORE001"
"What are the hours for store STORE001?"
```

## Mock Data

This server provides comprehensive mock data for all API endpoints, including:

- **Realistic Commerce Data:** Products, customers, orders, transactions
- **Complete Response Structures:** Following Dynamics 365 Commerce API patterns
- **Rich Metadata:** Timestamps, IDs, status information, nested objects
- **Error Handling:** Appropriate error responses for invalid requests

All mock responses include:
- API endpoint information
- Realistic sample data
- Proper data relationships
- Timestamp information
- Status and metadata fields

## Development

The server is structured with separate controllers for each API area:

```
mcp_dynamics365_commerce_server/
├── server.py                    # Main MCP server entry point
├── controllers/
│   ├── customer.py             # Customer operations
│   ├── sales_order.py          # Sales order operations  
│   ├── cart.py                 # Cart operations
│   ├── products.py             # Product operations
│   ├── org_units.py            # Store/warehouse operations
│   ├── loyalty_card.py         # Loyalty program operations
│   ├── shifts.py               # Employee shift operations
│   ├── address.py              # Address operations
│   ├── barcode.py              # Barcode operations
│   ├── cash_declaration.py     # Cash declaration operations
│   ├── cities.py               # Cities operations
│   ├── counties.py             # Counties operations
│   ├── country_region.py       # Country/region operations
│   ├── credit_memo.py          # Credit memo operations
│   ├── suspended_cart.py       # Suspended cart operations
│   ├── tender_types.py         # Tender types operations
│   ├── reason_codes.py         # Reason codes operations
│   └── pricing.py              # Pricing operations
```

### Adding New Tools

1. Choose the appropriate controller or create a new one
2. Add the tool definition to the controller's `get_tools()` method
3. Implement the handler logic in the controller's `handle_tool()` method
4. Update the main server to import and register the new controller

### Testing

Run the server directly to test:

```bash
python mcp_dynamics365_commerce_server/server.py
```

## API Reference

Each tool accepts a `baseUrl` parameter to specify your Dynamics 365 Commerce site URL. If not provided, it defaults to `https://your-commerce-site.com`.

### Authentication

This server provides mock implementations. In a production environment, you would need to:
1. Implement proper authentication (OAuth 2.0, API keys)
2. Add SSL/TLS certificate handling
3. Implement proper error handling for API failures
4. Add rate limiting and request throttling

### Real API Integration

To integrate with actual Dynamics 365 Commerce APIs:
1. Replace mock implementations with actual HTTP requests
2. Add authentication headers and tokens
3. Handle real API response formats
4. Implement proper error handling for network issues
5. Add data validation and sanitization

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## Support

For issues related to:
- **MCP Server:** Create an issue in this repository
- **Dynamics 365 Commerce:** Consult Microsoft's official documentation
- **Claude Desktop:** Check Anthropic's documentation

---

**Note:** This is a mock implementation for development and testing purposes. For production use with actual Dynamics 365 Commerce systems, additional authentication, security, and error handling implementations are required.