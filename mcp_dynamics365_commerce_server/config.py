"""
Configuration management for Dynamics 365 Commerce MCP Server

Handles environment variables and configuration settings for the MCP server.
"""

import os
from typing import Optional

class CommerceConfig:
    """Configuration manager for the Commerce MCP Server"""
    
    def __init__(self):
        self._base_url = None
        self._load_config()
    
    def _load_config(self):
        """Load configuration from environment variables"""
        # Try environment variable first
        self._base_url = os.getenv('DYNAMICS365_BASE_URL')
        
        # If not set, try common variations
        if not self._base_url:
            self._base_url = os.getenv('COMMERCE_BASE_URL')
        
        if not self._base_url:
            self._base_url = os.getenv('D365_BASE_URL')
    
    @property
    def base_url(self) -> str:
        """Get the base URL for Dynamics 365 Commerce APIs"""
        if self._base_url:
            # Ensure URL doesn't end with slash
            return self._base_url.rstrip('/')
        
        # Return a more realistic default that indicates configuration needed
        return "https://your-commerce-instance.commerce.dynamics.com"
    
    @property
    def is_configured(self) -> bool:
        """Check if the server is properly configured with a real base URL"""
        return (self._base_url is not None and 
                not self._base_url.startswith('https://your-commerce') and
                not self._base_url.startswith('https://example') and
                'your-commerce-site.com' not in self._base_url)
    
    def get_api_endpoint(self, path: str) -> str:
        """Get full API endpoint URL"""
        path = path.lstrip('/')
        return f"{self.base_url}/api/CommerceRuntime/{path}"
    
    def validate_config(self) -> tuple[bool, str]:
        """Validate the current configuration"""
        if not self._base_url:
            return False, ("No base URL configured. Set DYNAMICS365_BASE_URL environment variable "
                          "to your Dynamics 365 Commerce instance URL.")
        
        if not self.is_configured:
            return False, (f"Base URL appears to be a placeholder: {self._base_url}. "
                          "Please set DYNAMICS365_BASE_URL to your actual Commerce instance URL.")
        
        if not self._base_url.startswith('https://'):
            return False, f"Base URL must use HTTPS: {self._base_url}"
        
        return True, "Configuration is valid"
    
    def get_configuration_help(self) -> str:
        """Get help text for configuration"""
        return """
Configuration Help:
==================

To configure the Dynamics 365 Commerce MCP Server, set one of these environment variables:

1. DYNAMICS365_BASE_URL (recommended)
2. COMMERCE_BASE_URL  
3. D365_BASE_URL

Example URLs:
- https://mycompany.commerce.dynamics.com
- https://mycompany-retail.commerce.dynamics.com
- https://contoso.commerce.dynamics.com

Setting Environment Variables:
------------------------------

Windows (Command Prompt):
  set DYNAMICS365_BASE_URL=https://yourcompany.commerce.dynamics.com

Windows (PowerShell):
  $env:DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"

Linux/macOS:
  export DYNAMICS365_BASE_URL="https://yourcompany.commerce.dynamics.com"

For Claude Desktop, add to your configuration:
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
"""

# Global configuration instance
_config = None

def get_config() -> CommerceConfig:
    """Get the global configuration instance"""
    global _config
    if _config is None:
        _config = CommerceConfig()
    return _config

def get_base_url() -> str:
    """Get the configured base URL"""
    return get_config().base_url

def is_configured() -> bool:
    """Check if the server is properly configured"""
    return get_config().is_configured