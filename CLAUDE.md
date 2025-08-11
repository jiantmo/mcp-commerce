# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server that provides tools for interacting with Dynamics 365 Commerce Retail Server Customer Consumer APIs. The server exposes 125+ tools organized across 19+ controllers, enabling AI assistants to perform comprehensive commerce operations.

## Key Architecture

### Server Structure
- **Main Server**: `mcp_dynamics365_commerce_server/server.py` - Entry point that initializes all controllers and handles tool routing
- **Controllers**: Individual modules in `mcp_dynamics365_commerce_server/controllers/` - Each handles a specific API domain (customers, products, carts, etc.)
- **Tool Routing**: Tools are routed by name prefix (e.g., `customer_*` → CustomerController, `cart_*` → CartController)

### Key Controllers
- **CustomerController**: Customer management, order history, search, loyalty points (10 tools)
- **CartController**: Shopping cart operations, checkout, payments, discounts (55 tools)  
- **SalesOrderController**: Order management, receipts, invoices, fulfillment (24 tools)
- **ProductsController**: Product search, details, recommendations, availability (4 tools)
- **OrgUnitsController**: Store locations, inventory, hours (3 tools)

## Development Commands

### Running the Server
```bash
# Start the MCP server directly
python mcp_dynamics365_commerce_server/server.py

# Or use the convenience script
python run_server.py
```

### Testing
```bash
# Run the validation test
python test_mcp_server.py
```

### Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt

# Or install as editable package
pip install -e .
```

### TypeScript Build (for npm package.json)
```bash
# Build TypeScript (if applicable)
npm run build

# Development mode
npm run dev
```

## Database and Implementation Details

### Mock Database
The server uses an in-memory database (`database.py`) with comprehensive demo data:

- **Customers**: Sample customer records with addresses, loyalty cards, purchase history
- **Products**: Electronics and accessories with pricing, inventory, categories
- **Stores**: Multiple store locations with individual inventory levels
- **Carts**: Active shopping carts with line items and totals
- **Sales Orders**: Completed orders with payment and shipping information
- **Loyalty Cards**: Customer loyalty programs with points and transactions
- **Categories**: Product categorization hierarchy
- **Geographic Data**: Countries, states, cities for address management

### CRUD Operations
All controllers support standard Create, Read, Update, Delete operations:
- `create(collection, data)` - Add new entities
- `read(collection, id)` - Retrieve by ID
- `update(collection, id, changes)` - Modify existing entities
- `delete(collection, id)` - Remove entities
- `list(collection, filters, pagination)` - List with filtering
- `search(collection, query, fields)` - Full-text search

### Implemented Controllers (with database integration)
- **CustomerController**: Full CRUD with order history, search, loyalty points (10 tools)
- **ProductsController**: Search, details, recommendations, availability (4 tools)
- **CartController**: Complete shopping cart lifecycle from creation to checkout (8 tools)
- **Other Controllers**: Basic CRUD operations following template pattern

## Tool Implementation Pattern

Each controller follows this pattern:

1. **`__init__()`**: Initializes database connection via `get_database()`
2. **`get_tools()`**: Returns list of MCP Tool definitions with schemas
3. **`handle_tool(name, arguments)`**: Routes tool calls to database operations
4. **Database Operations**: Uses CRUD methods to interact with mock data
5. **Error Handling**: Try/catch blocks with consistent error responses
6. **Response Format**: Always includes API endpoint and structured data

Tool names use prefixed naming conventions for routing:
- `customer_*` → CustomerController
- `products_*` → ProductsController  
- `cart_*` → CartController
- etc.

### Example Implementation Workflow
1. Tool receives arguments (e.g., customer ID, product search query)
2. Controller validates input and checks entity existence  
3. Database operations perform CRUD on relevant collections
4. Response includes API endpoint info and updated/retrieved data
5. Business logic (calculations, validations) applied as needed

## Configuration

The server accepts a `baseUrl` parameter for all tools to specify the Dynamics 365 Commerce site URL. When integrating with real APIs:

1. Replace mock implementations with actual HTTP requests
2. Add proper authentication (OAuth 2.0, API keys)
3. Implement SSL/TLS certificate handling
4. Add rate limiting and error handling for network issues

## Environment Variables

**Required Configuration:**
- `DYNAMICS365_BASE_URL`: Your Dynamics 365 Commerce instance URL (e.g., `https://yourcompany.commerce.dynamics.com`)

**Alternative Environment Variable Names:**
- `COMMERCE_BASE_URL`: Alternative to DYNAMICS365_BASE_URL
- `D365_BASE_URL`: Alternative to DYNAMICS365_BASE_URL

**Configuration Validation:**
The server validates configuration on startup and logs warnings if:
- No base URL is configured
- The URL appears to be a placeholder
- The URL doesn't use HTTPS

**Setting Environment Variables:**

*Windows Command Prompt:*
```cmd
set DYNAMICS365_BASE_URL=https://yourcompany.commerce.dynamics.com
```

*Windows PowerShell:*
```powershell
$env:DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"
```

*Linux/macOS:*
```bash
export DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"
```

## MCP Integration

Configure in Claude Desktop (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "dynamics365-commerce": {
      "command": "python",
      "args": ["/path/to/mcp-commerce/mcp_dynamics365_commerce_server/server.py"],
      "env": {
        "DYNAMICS365_BASE_URL": "https://yourcompany.commerce.dynamics.com"
      }
    }
  }
}
```

**Important:** Replace `yourcompany` with your actual Dynamics 365 Commerce tenant name.

**Common Commerce Instance URL Patterns:**
- `https://[tenant].commerce.dynamics.com`
- `https://[tenant]-retail.commerce.dynamics.com`
- `https://[tenant].commerce.dynamics.com/[environment]`