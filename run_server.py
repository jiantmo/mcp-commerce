#!/usr/bin/env python3
"""
Dynamics 365 Commerce MCP Server 启动脚本
这个脚本会正常启动 MCP 服务器并等待连接
"""

import asyncio
import sys
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """启动 MCP 服务器"""
    try:
        print("🚀 启动 Dynamics 365 Commerce MCP 服务器...")
        print("📊 工具数量: 386 个")
        print("🔌 连接方式: stdio")
        print("⚡ 状态: 准备接收连接...")
        print("💡 提示: 在 Claude Desktop 或其他 MCP 客户端中配置此服务器")
        print("🛑 按 Ctrl+C 停止服务器")
        print("-" * 50)
        
        # 导入并运行主服务器
        from mcp_dynamics365_commerce_server.server import main as server_main
        asyncio.run(server_main())
        
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
        sys.exit(0)
    except Exception as e:
        print(f"❌ 服务器启动失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
