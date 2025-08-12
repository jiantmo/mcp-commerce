# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server for Dynamics 365 Commerce that provides 380+ tools across 50+ controllers for interacting with Dynamics 365 Commerce Retail Server Customer Consumer APIs. The project is written in Python and provides comprehensive mock implementations for development and testing.

## Development Commands

### Running the Server
```bash
# Start the MCP server
python run_server.py

# Alternative: Run directly
python mcp_dynamics365_commerce_server/server.py

# Run with specific Python (if needed)
python3 mcp_dynamics365_commerce_server/server.py
```

### Installing Dependencies
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install from pyproject.toml
pip install -e .
```

### Testing
```bash
# Test server functionality
python debug_tools_count.py

# Demo configured server
python demo_configured_server.py
```

## Configuration

### Environment Variables
The server requires configuration via environment variables:

- **DYNAMICS365_BASE_URL** (primary): Full URL to your Commerce instance
- **COMMERCE_BASE_URL** (fallback): Alternative environment variable name  
- **D365_BASE_URL** (fallback): Another alternative environment variable name

Default fallback URL: `https://sculxdon4av67499847-rs.su.retail.test.dynamics.com`

### Setting Environment Variables
```bash
# Windows Command Prompt
set DYNAMICS365_BASE_URL=https://yourcompany.commerce.dynamics.com

# Windows PowerShell  
$env:DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"

# Linux/macOS
export DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"
```

## Architecture

### Core Structure
```
mcp_dynamics365_commerce_server/
├── server.py                    # Main MCP server entry point with tool routing
├── config.py                    # Configuration management (env vars, validation)
├── database.py                  # Mock database for development/testing
├── controllers/                 # Individual API controllers (50+ files)
│   ├── customer.py             # Customer operations (10 tools)
│   ├── sales_order.py          # Sales order operations (24 tools) 
│   ├── cart.py                 # Cart operations (55 tools)
│   ├── products.py             # Product operations (4 tools)
│   ├── org_units.py            # Store/warehouse operations (3 tools)
│   └── [45+ other controllers] # Various Commerce API areas
```

### Controller Pattern
Each controller follows a consistent pattern:
- `get_tools()`: Returns list of MCP Tool definitions for the controller
- `handle_tool(name, arguments)`: Routes and handles specific tool calls
- Tool names prefixed with controller name (e.g., `customer_`, `cart_`, `products_`)

### Main Server (server.py)
- **Dynamics365CommerceServer**: Main server class that aggregates all controllers
- **Tool Routing**: Routes tool calls to appropriate controllers based on name prefix
- **Configuration Integration**: Validates and logs configuration status on startup
- **Error Handling**: Wraps tool responses with proper error handling

### Configuration System (config.py)
- **CommerceConfig**: Manages environment variables and URL validation
- **Validation**: Checks for placeholder URLs and proper HTTPS usage
- **API Endpoints**: Constructs full API URLs with `/api/CommerceRuntime/` path

## Key Development Patterns

### Adding New Tools
1. Choose appropriate existing controller or create new one
2. Add tool definition in controller's `get_tools()` method
3. Implement handler logic in controller's `handle_tool()` method  
4. Add routing logic in main server's `handle_call_tool()` method
5. Update tool aggregation in `list_tools()` handler

### Tool Definition Format
```python
Tool(
    name="controller_action_name",
    description="Clear description of what the tool does",
    inputSchema={
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "Parameter description"},
            "baseUrl": {"type": "string", "description": "Commerce site URL override"}
        },
        "required": ["param1"]
    }
)
```

### Mock Data Patterns
All controllers return realistic mock data including:
- Proper Commerce API response structure
- Timestamps and IDs following D365 patterns
- Nested objects and relationships
- Error responses for invalid inputs

## Modified Files Status

Based on git status, these files have pending changes:
- `mcp_dynamics365_commerce_server/config.py` (M)
- `mcp_dynamics365_commerce_server/controllers/sales_order.py` (M)

Check git diff to understand what modifications have been made before making additional changes.

## MCP Integration

### Claude Desktop Configuration
Add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "dynamics365-commerce": {
      "command": "python",
      "args": ["C:/path/to/mcp-commerce/mcp_dynamics365_commerce_server/server.py"],
      "env": {
        "DYNAMICS365_BASE_URL": "https://yourcompany.commerce.dynamics.com"
      }
    }
  }
}
```

### Tool Categories
- **Customer Management**: 10 tools for customer CRUD, search, order history
- **Cart Operations**: 55 tools for cart management, checkout, payments
- **Sales Orders**: 24 tools for order processing, receipts, invoices
- **Product Catalog**: 4 tools for product search, details, availability
- **Store Operations**: Various tools for inventory, locations, shifts
- **Additional Controllers**: 40+ specialized controllers for specific Commerce APIs

The server provides comprehensive mock implementations suitable for development, testing, and demonstration purposes.