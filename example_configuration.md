# Configuration Examples

## Setting Up Your Dynamics 365 Commerce Base URL

The MCP server requires a valid Dynamics 365 Commerce instance URL to function properly.

### Finding Your Commerce Instance URL

1. **From Dynamics 365 Commerce Portal:**
   - Log in to your Dynamics 365 Commerce portal
   - Go to your environment settings
   - Look for the "Commerce Runtime API" or "Retail Server" URL
   - It typically follows the pattern: `https://[tenant].commerce.dynamics.com`

2. **Common URL Patterns:**
   ```
   https://contoso.commerce.dynamics.com
   https://contoso-retail.commerce.dynamics.com
   https://fabrikam.commerce.dynamics.com/prod
   https://adventureworks.commerce.dynamics.com
   ```

### Configuration Methods

#### Option 1: Environment Variable (Recommended)
```bash
# Set permanently (add to your shell profile)
export DYNAMICS365_BASE_URL="https://contoso.commerce.dynamics.com"

# Test the configuration
echo $DYNAMICS365_BASE_URL
```

#### Option 2: Claude Desktop Configuration
Edit your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "dynamics365-commerce": {
      "command": "python",
      "args": ["C:/github/mcp-commerce/mcp_dynamics365_commerce_server/server.py"],
      "env": {
        "DYNAMICS365_BASE_URL": "https://contoso.commerce.dynamics.com"
      }
    }
  }
}
```

#### Option 3: Development/Testing
For development, you can create a `.env` file in the project root:
```env
DYNAMICS365_BASE_URL=https://contoso.commerce.dynamics.com
```

### Validation

Run the test script to validate your configuration:
```bash
python test_mcp_server.py
```

The server will log warnings if:
- No URL is configured
- The URL appears to be a placeholder
- The URL doesn't use HTTPS

### Authentication Notes

**Important:** This MCP server currently provides mock implementations. For production use with real Dynamics 365 Commerce APIs, you'll need to implement:

1. **OAuth 2.0 Authentication**
2. **API Key Management**
3. **Token Refresh Logic**
4. **Error Handling for Authentication Failures**

### Troubleshooting

**Problem:** Server shows "Configuration warning"
- **Solution:** Set the DYNAMICS365_BASE_URL environment variable

**Problem:** "Base URL appears to be a placeholder"
- **Solution:** Replace placeholder URLs with your actual Commerce instance URL

**Problem:** "Base URL must use HTTPS"
- **Solution:** Ensure your URL starts with `https://`

**Problem:** API calls fail with authentication errors
- **Solution:** This is expected with mock implementations. Real authentication needs to be implemented for production use.

### Example Real URLs (Replace with your actual URLs)

```bash
# US Commercial Cloud
export DYNAMICS365_BASE_URL="https://contoso.commerce.dynamics.com"

# European Cloud
export DYNAMICS365_BASE_URL="https://contoso.commerce.dynamics.com"

# With Environment Suffix
export DYNAMICS365_BASE_URL="https://contoso.commerce.dynamics.com/prod"

# Custom Domain (if configured)
export DYNAMICS365_BASE_URL="https://commerce.contoso.com"
```