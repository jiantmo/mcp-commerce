#!/usr/bin/env python3
"""
Demo script showing the MCP server with proper configuration
"""

import os
import asyncio
import json
from mcp_dynamics365_commerce_server.server import Dynamics365CommerceServer

async def demo_configured_server():
    """Demonstrate the server with proper configuration"""
    
    # Set the environment variable
    os.environ['DYNAMICS365_BASE_URL'] = 'https://contoso.commerce.dynamics.com'
    
    print("Dynamics 365 Commerce MCP Server - Configuration Demo")
    print("=" * 60)
    
    # Initialize server
    print("Initializing server with configured base URL...")
    server = Dynamics365CommerceServer()
    
    print(f"Server configured with: {server.config.base_url}")
    print(f"Configuration valid: {server.config.is_configured}")
    
    # Test a tool call
    print("\nTesting customer search tool...")
    result = await server.handle_call_tool("customer_search", {
        "query": "john"
    })
    
    # Parse and display the result
    response = json.loads(result.content[0].text)
    print(f"API Endpoint: {response.get('api', 'N/A')}")
    print(f"Results found: {len(response.get('results', []))}")
    
    # Show the difference between configured and unconfigured
    print("\nConfiguration Comparison:")
    print("-" * 40)
    
    # Test with unconfigured
    if 'DYNAMICS365_BASE_URL' in os.environ:
        del os.environ['DYNAMICS365_BASE_URL']
    
    from mcp_dynamics365_commerce_server.config import CommerceConfig
    unconfigured = CommerceConfig()
    
    print(f"Unconfigured URL: {unconfigured.base_url}")
    print(f"Configured URL:   https://contoso.commerce.dynamics.com")
    
    print("\nThe server now uses real environment configuration!")
    print("No more placeholder URLs in API responses!")
    print("Ready for actual Dynamics 365 Commerce integration!")

if __name__ == "__main__":
    asyncio.run(demo_configured_server())