from typing import Any, Dict, List
from datetime import datetime
from mcp.types import Tool
from ..config import get_base_url

class ProductListsController:
    def get_tools(self) -> List[Tool]:
        return [
            Tool(name="product_lists_search", description="Gets product lists filtered by search criteria.", inputSchema={"type":"object","properties":{"productListSearchCriteria":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListSearchCriteria"]}),
            Tool(name="product_lists_add_product_list_lines", description="Creates product list lines.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"productListLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId","productListLines"]}),
            Tool(name="product_lists_update_product_list_lines", description="Updates product list lines.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"productListLines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId","productListLines"]}),
            Tool(name="product_lists_get_product_list_lines", description="Gets product list lines.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"searchText":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId"]}),
            Tool(name="product_lists_remove_product_list_lines", description="Removes lines from product list.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"lines":{"type":"array"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId","lines"]}),
            Tool(name="product_lists_copy_cart_to_product_list", description="Copies cart content to product list lines.", inputSchema={"type":"object","properties":{"cartId":{"type":"string"},"destinationProductListId":{"type":"string"},"isRewrite":{"type":"boolean"},"isQuantityAggregate":{"type":"boolean"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["cartId","destinationProductListId","isRewrite","isQuantityAggregate"]}),
            Tool(name="product_lists_get_entity_by_key", description="Gets a single product list by id.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId"]}),
            Tool(name="product_lists_create_entity", description="Creates product list.", inputSchema={"type":"object","properties":{"productList":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productList"]}),
            Tool(name="product_lists_patch_entity", description="Patch update product list.", inputSchema={"type":"object","properties":{"productList":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productList"]}),
            Tool(name="product_lists_update_entity", description="Update product list.", inputSchema={"type":"object","properties":{"productList":{"type":"object"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productList"]}),
            Tool(name="product_lists_delete_entity", description="Delete product list.", inputSchema={"type":"object","properties":{"productListId":{"type":"string"},"baseUrl":{"type":"string","default":"https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}},"required":["productListId"]})
        ]

    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        base_url=arguments.get("baseUrl", get_base_url())
        return {"api": f"MOCK {base_url}/api/CommerceRuntime/ProductLists/{name}", "toolName": name, "arguments": arguments, "status":"success", "timestamp": datetime.now().isoformat()+"Z", "mockData": {"result": "Success"}}
