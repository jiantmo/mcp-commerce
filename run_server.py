#!/usr/bin/env python3
"""
Dynamics 365 Commerce MCP Server Startup Script
This script starts the MCP server normally and waits for connections
"""

import asyncio
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Start MCP Server"""
    try:
        print("🚀 Starting Dynamics 365 Commerce MCP Server...")
        print("📊 Number of tools: 386")
        print("🔌 Connection method: stdio")
        print("⚡ Status: Ready to receive connections...")
        print("💡 Tip: Configure this server in Claude Desktop or other MCP clients")
        print("🛑 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Import and run the main server
        from mcp_dynamics365_commerce_server.server import main as server_main
        asyncio.run(server_main())
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Server startup failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
