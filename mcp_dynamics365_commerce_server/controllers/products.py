"""
Products Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (46 total):
1. products_search - Search for products by various criteria
2. products_get_by_id - Get detailed information about a specific product
3. products_get_recommended_products - Get recommended products based on a specific product
4. products_get_product_availability - Get product availability across different locations
5. products_get_categories - Get product categories
6. products_get_category_by_id - Get category details by ID
7. products_get_attributes - Get product attributes
8. products_get_product_variants - Get product variants
9. products_get_product_images - Get product images
10. products_get_product_reviews - Get product reviews
11. products_create_product_review - Create product review
12. products_get_product_pricing - Get product pricing details
13. products_get_bulk_product_info - Get bulk product information
14. products_compare_products - Compare multiple products
15. products_get_cross_sell_products - Get cross-sell products
16. products_get_up_sell_products - Get up-sell products
17. products_get_recently_viewed - Get recently viewed products
18. products_get_wishlist_products - Get wishlist products
19. products_add_to_wishlist - Add product to wishlist
20. products_remove_from_wishlist - Remove from wishlist
21. products_get_inventory_levels - Get detailed inventory levels
22. products_reserve_inventory - Reserve product inventory
23. products_release_inventory - Release reserved inventory
24. products_get_product_bundles - Get product bundles
25. products_get_kit_components - Get kit components
26. products_get_substitutes - Get product substitutes
27. products_get_assemblies - Get product assemblies
28. products_validate_product_configuration - Validate product configuration
29. products_get_dimension_values - Get dimension values
30. products_calculate_product_price - Calculate product price
31. products_get_price_adjustments - Get price adjustments
32. products_get_trade_agreements - Get trade agreements
33. products_get_discount_lines - Get discount lines
34. products_get_charge_configurations - Get charge configurations
35. products_get_tax_information - Get tax information
36. products_get_unit_conversions - Get unit conversions
37. products_get_barcode_information - Get barcode information
38. products_validate_barcode - Validate barcode
39. products_get_supplier_information - Get supplier information
40. products_get_manufacturer_information - Get manufacturer information
41. products_get_certification_information - Get certification information
42. products_get_compliance_information - Get compliance information
43. products_get_warranty_information - Get warranty information
44. products_get_shipping_information - Get shipping information
45. products_get_localized_information - Get localized information
46. products_get_seo_information - Get SEO information

This controller handles comprehensive product operations including search, details, categories, 
variants, pricing, inventory, reviews, recommendations, and all related product management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool
from ..database import get_database
from ..config import get_base_url

class ProductsController:
    """Controller for Products-related Dynamics 365 Commerce API operations"""
    
    def __init__(self):
        self.db = get_database()
    
    def get_tools(self) -> List[Tool]:
        """Return list of all 46 product-related tools"""
        return [
            Tool(
                name="products_search",
                description="Search for products by various criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query (product name, description, SKU, brand)"
                        },
                        "category_id": {
                            "type": "string",
                            "description": "Filter by category ID"
                        },
                        "brand": {
                            "type": "string",
                            "description": "Filter by brand"
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price filter"
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price filter"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return",
                            "default": 20
                        },
                        "offset": {
                            "type": "integer",
                            "description": "Number of results to skip",
                            "default": 0
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": []
                }
            ),
            Tool(
                name="products_get_by_id",
                description="Get detailed information about a specific product",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {
                            "type": "string",
                            "description": "The product ID to get details for"
                        },
                        "includeVariants": {
                            "type": "boolean",
                            "description": "Whether to include product variants",
                            "default": False
                        },
                        "includeInventory": {
                            "type": "boolean",
                            "description": "Whether to include inventory information",
                            "default": True
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["productId"]
                }
            ),
            Tool(
                name="products_get_recommended_products",
                description="Get recommended products based on a specific product",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {
                            "type": "string",
                            "description": "The product ID to get recommendations for"
                        },
                        "recommendationType": {
                            "type": "string",
                            "enum": ["similar", "frequently_bought", "related", "trending"],
                            "description": "Type of recommendation",
                            "default": "similar"
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of recommendations to return",
                            "default": 10
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["productId"]
                }
            ),
            Tool(
                name="products_get_product_availability",
                description="Get product availability across different locations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {
                            "type": "string",
                            "description": "The product ID to check availability for"
                        },
                        "storeId": {
                            "type": "string",
                            "description": "Specific store ID to check (optional)"
                        },
                        "zipCode": {
                            "type": "string",
                            "description": "ZIP code to find nearby stores (optional)"
                        },
                        "radius": {
                            "type": "number",
                            "description": "Search radius in miles",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"
                        }
                    },
                    "required": ["productId"]
                }
            ),
            
            # Categories (5-6)
            Tool(
                name="products_get_categories",
                description="Get product categories",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "parentCategoryId": {"type": "string", "description": "Parent category ID filter"},
                        "includeSubCategories": {"type": "boolean", "default": True},
                        "baseUrl": {"type": "string"}
                    }
                }
            ),
            
            Tool(
                name="products_get_category_by_id",
                description="Get category details by ID",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "categoryId": {"type": "string", "description": "Category ID"},
                        "includeProducts": {"type": "boolean", "default": False},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["categoryId"]
                }
            ),
            
            # Attributes & Variants (7-8)
            Tool(
                name="products_get_attributes",
                description="Get product attributes",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "attributeType": {"type": "string", "enum": ["all", "variant", "descriptive"]},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_product_variants",
                description="Get product variants",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "dimensionValues": {"type": "object"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Media & Reviews (9-11)
            Tool(
                name="products_get_product_images",
                description="Get product images",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "imageSize": {"type": "string", "enum": ["thumbnail", "medium", "large", "original"]},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_product_reviews",
                description="Get product reviews",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "limit": {"type": "integer", "default": 10},
                        "offset": {"type": "integer", "default": 0},
                        "sortBy": {"type": "string", "enum": ["date", "rating", "helpful"]},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_create_product_review",
                description="Create product review",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "rating": {"type": "integer", "minimum": 1, "maximum": 5},
                        "title": {"type": "string"},
                        "comment": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId", "customerId", "rating", "title"]
                }
            ),
            
            # Pricing (12-14)
            Tool(
                name="products_get_product_pricing",
                description="Get product pricing details",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "quantity": {"type": "number", "default": 1},
                        "currencyCode": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_bulk_product_info",
                description="Get bulk product information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productIds": {"type": "array", "items": {"type": "string"}},
                        "fields": {"type": "array", "items": {"type": "string"}},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productIds"]
                }
            ),
            
            Tool(
                name="products_compare_products",
                description="Compare multiple products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productIds": {"type": "array", "items": {"type": "string"}},
                        "compareFields": {"type": "array", "items": {"type": "string"}},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productIds"]
                }
            ),
            
            # Recommendations (15-17)
            Tool(
                name="products_get_cross_sell_products",
                description="Get cross-sell products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "limit": {"type": "integer", "default": 5},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_up_sell_products",
                description="Get up-sell products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "limit": {"type": "integer", "default": 5},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_recently_viewed",
                description="Get recently viewed products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {"type": "string"},
                        "limit": {"type": "integer", "default": 10},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["customerId"]
                }
            ),
            
            # Wishlist (18-20)
            Tool(
                name="products_get_wishlist_products",
                description="Get wishlist products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {"type": "string"},
                        "wishlistId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["customerId"]
                }
            ),
            
            Tool(
                name="products_add_to_wishlist",
                description="Add product to wishlist",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {"type": "string"},
                        "productId": {"type": "string"},
                        "wishlistId": {"type": "string"},
                        "quantity": {"type": "integer", "default": 1},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["customerId", "productId"]
                }
            ),
            
            Tool(
                name="products_remove_from_wishlist",
                description="Remove from wishlist",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {"type": "string"},
                        "productId": {"type": "string"},
                        "wishlistId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["customerId", "productId"]
                }
            ),
            
            # Inventory (21-23)
            Tool(
                name="products_get_inventory_levels",
                description="Get detailed inventory levels",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "warehouseId": {"type": "string"},
                        "includeReserved": {"type": "boolean", "default": True},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_reserve_inventory",
                description="Reserve product inventory",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "warehouseId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "reservationId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId", "quantity"]
                }
            ),
            
            Tool(
                name="products_release_inventory",
                description="Release reserved inventory",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "reservationId": {"type": "string"},
                        "quantity": {"type": "integer"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["reservationId"]
                }
            ),
            
            # Product Structure (24-27)
            Tool(
                name="products_get_product_bundles",
                description="Get product bundles",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_kit_components",
                description="Get kit components",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "kitProductId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["kitProductId"]
                }
            ),
            
            Tool(
                name="products_get_substitutes",
                description="Get product substitutes",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_assemblies",
                description="Get product assemblies",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Configuration & Dimensions (28-29)
            Tool(
                name="products_validate_product_configuration",
                description="Validate product configuration",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "configuration": {"type": "object"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId", "configuration"]
                }
            ),
            
            Tool(
                name="products_get_dimension_values",
                description="Get dimension values",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "dimensionType": {"type": "string", "enum": ["color", "size", "style", "configuration"]},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Pricing & Discounts (30-34)
            Tool(
                name="products_calculate_product_price",
                description="Calculate product price",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "quantity": {"type": "number", "default": 1},
                        "customerId": {"type": "string"},
                        "currencyCode": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_price_adjustments",
                description="Get price adjustments",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_trade_agreements",
                description="Get trade agreements",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_discount_lines",
                description="Get discount lines",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "customerId": {"type": "string"},
                        "quantity": {"type": "number", "default": 1},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_charge_configurations",
                description="Get charge configurations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Tax & Units (35-36)
            Tool(
                name="products_get_tax_information",
                description="Get tax information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "location": {"type": "object"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_unit_conversions",
                description="Get unit conversions",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "fromUnit": {"type": "string"},
                        "toUnit": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId", "fromUnit", "toUnit"]
                }
            ),
            
            # Barcode (37-38)
            Tool(
                name="products_get_barcode_information",
                description="Get barcode information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_validate_barcode",
                description="Validate barcode",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "barcode": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["barcode"]
                }
            ),
            
            # Supplier & Manufacturer (39-40)
            Tool(
                name="products_get_supplier_information",
                description="Get supplier information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_manufacturer_information",
                description="Get manufacturer information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Certification & Compliance (41-42)
            Tool(
                name="products_get_certification_information",
                description="Get certification information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "certificationType": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_compliance_information",
                description="Get compliance information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "region": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Warranty & Shipping (43-44)
            Tool(
                name="products_get_warranty_information",
                description="Get warranty information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            Tool(
                name="products_get_shipping_information",
                description="Get shipping information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "destination": {"type": "object"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            ),
            
            # Localization & SEO (45-46)
            Tool(
                name="products_get_localized_information",
                description="Get localized information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "languageCode": {"type": "string"},
                        "currencyCode": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId", "languageCode"]
                }
            ),
            
            Tool(
                name="products_get_seo_information",
                description="Get SEO information",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productId": {"type": "string"},
                        "baseUrl": {"type": "string"}
                    },
                    "required": ["productId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle product tool calls with database operations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        try:
            if name == "products_search":
                query = arguments.get("query", "")
                category_id = arguments.get("category_id")
                brand = arguments.get("brand")
                min_price = arguments.get("min_price")
                max_price = arguments.get("max_price")
                limit = arguments.get("limit", 20)
                offset = arguments.get("offset", 0)
                
                # Start with all products
                products = self.db.list('products', limit=1000)  # Get all for filtering
                
                # Apply filters
                if query:
                    products = [p for p in products if 
                               query.lower() in p.get('name', '').lower() or
                               query.lower() in p.get('description', '').lower() or
                               query.lower() in p.get('sku', '').lower() or
                               query.lower() in p.get('brand', '').lower()]
                
                if category_id:
                    products = [p for p in products if p.get('category_id') == category_id]
                
                if brand:
                    products = [p for p in products if p.get('brand', '').lower() == brand.lower()]
                
                if min_price is not None:
                    products = [p for p in products if p.get('price', 0) >= min_price]
                
                if max_price is not None:
                    products = [p for p in products if p.get('price', 0) <= max_price]
                
                # Apply pagination
                total_results = len(products)
                products = products[offset:offset + limit]
                
                # Enrich with inventory information
                for product in products:
                    product['total_inventory'] = sum(
                        store.get('inventory', {}).get(product['id'], 0) 
                        for store in self.db.list('stores')
                    )
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/Search",
                    "searchQuery": query,
                    "filters": {
                        "category_id": category_id,
                        "brand": brand,
                        "min_price": min_price,
                        "max_price": max_price
                    },
                    "pagination": {
                        "limit": limit,
                        "offset": offset,
                        "total": total_results
                    },
                    "products": products
                }
            
            elif name == "products_get_by_id":
                product_id = arguments.get("productId")
                include_variants = arguments.get("includeVariants", False)
                include_inventory = arguments.get("includeInventory", True)
                
                product = self.db.read('products', product_id)
                if not product:
                    return {"error": f"Product {product_id} not found"}
                
                # Enrich product data
                if include_inventory:
                    # Get inventory by store
                    product['inventory_by_store'] = {}
                    product['total_inventory'] = 0
                    
                    for store in self.db.list('stores'):
                        store_inventory = store.get('inventory', {}).get(product_id, 0)
                        product['inventory_by_store'][store['id']] = {
                            'store_name': store['name'],
                            'quantity': store_inventory
                        }
                        product['total_inventory'] += store_inventory
                
                # Get category information
                if product.get('category_id'):
                    category = self.db.read('categories', product['category_id'])
                    product['category'] = category
                
                # Add variants if requested
                if include_variants:
                    # For demo, create some simple variants
                    variants = []
                    if product.get('color'):
                        colors = ['Black', 'White', 'Blue', 'Red', 'Gray']
                        for color in colors[:3]:  # Limit to 3 variants
                            variant = product.copy()
                            variant['id'] = f"{product_id}_VAR_{color[:3].upper()}"
                            variant['color'] = color
                            variant['price'] = product['price'] + random.uniform(-10, 10)
                            variants.append(variant)
                    product['variants'] = variants
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}",
                    "product": product,
                    "includeVariants": include_variants,
                    "includeInventory": include_inventory
                }
            
            elif name == "products_get_recommended_products":
                product_id = arguments.get("productId")
                recommendation_type = arguments.get("recommendationType", "similar")
                limit = arguments.get("limit", 10)
                
                base_product = self.db.read('products', product_id)
                if not base_product:
                    return {"error": f"Product {product_id} not found"}
                
                # Get all products for recommendations
                all_products = self.db.list('products', limit=1000)
                recommendations = []
                
                if recommendation_type == "similar":
                    # Find products in same category or brand
                    for product in all_products:
                        if (product['id'] != product_id and 
                            (product.get('category_id') == base_product.get('category_id') or
                             product.get('brand') == base_product.get('brand'))):
                            recommendations.append(product)
                
                elif recommendation_type == "related":
                    # Find products that might be bought together
                    for product in all_products:
                        if product['id'] != product_id:
                            # Simple logic: products with similar price range
                            price_diff = abs(product.get('price', 0) - base_product.get('price', 0))
                            if price_diff <= base_product.get('price', 0) * 0.5:  # Within 50% price range
                                recommendations.append(product)
                
                elif recommendation_type == "frequently_bought":
                    # For demo, just return random products
                    recommendations = [p for p in all_products if p['id'] != product_id]
                    random.shuffle(recommendations)
                
                elif recommendation_type == "trending":
                    # For demo, return products sorted by name (simulating popularity)
                    recommendations = sorted([p for p in all_products if p['id'] != product_id],
                                           key=lambda x: x.get('name', ''))
                
                # Limit recommendations
                recommendations = recommendations[:limit]
                
                # Add recommendation scores (mock)
                for i, rec in enumerate(recommendations):
                    rec['recommendation_score'] = random.uniform(0.6, 0.95)
                    rec['recommendation_reason'] = self._get_recommendation_reason(
                        recommendation_type, base_product, rec
                    )
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Recommendations",
                    "baseProduct": {
                        "id": product_id,
                        "name": base_product.get('name')
                    },
                    "recommendationType": recommendation_type,
                    "recommendations": recommendations,
                    "totalRecommendations": len(recommendations)
                }
            
            elif name == "products_get_product_availability":
                product_id = arguments.get("productId")
                store_id = arguments.get("storeId")
                zip_code = arguments.get("zipCode")
                radius = arguments.get("radius", 25)
                
                product = self.db.read('products', product_id)
                if not product:
                    return {"error": f"Product {product_id} not found"}
                
                availability = []
                stores = self.db.list('stores')
                
                if store_id:
                    # Check specific store
                    stores = [s for s in stores if s['id'] == store_id]
                
                for store in stores:
                    inventory_qty = store.get('inventory', {}).get(product_id, 0)
                    
                    store_availability = {
                        "storeId": store['id'],
                        "storeName": store['name'],
                        "address": store['address'],
                        "phone": store['phone'],
                        "quantity": inventory_qty,
                        "status": "Available" if inventory_qty > 0 else "Out of Stock",
                        "reservedQuantity": random.randint(0, min(5, inventory_qty)),
                        "availableForPickup": inventory_qty > 0,
                        "estimatedArrival": None
                    }
                    
                    # Add distance if zip code provided (mock calculation)
                    if zip_code:
                        store_availability["distance"] = round(random.uniform(1, radius), 1)
                        store_availability["distanceUnit"] = "miles"
                    
                    availability.append(store_availability)
                
                # Sort by availability then distance
                availability.sort(key=lambda x: (x['quantity'] == 0, x.get('distance', 0)))
                
                total_available = sum(a['quantity'] for a in availability)
                
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Availability",
                    "productId": product_id,
                    "productName": product.get('name'),
                    "totalAvailable": total_available,
                    "searchCriteria": {
                        "storeId": store_id,
                        "zipCode": zip_code,
                        "radius": radius
                    },
                    "storeAvailability": availability,
                    "totalStores": len(availability)
                }
            
            # Handle all additional tools with mock responses
            else:
                return self._handle_mock_tool(name, arguments)
                
        except Exception as e:
            return {"error": f"Error in {name}: {str(e)}"}
    
    def _get_recommendation_reason(self, rec_type: str, base_product: Dict, 
                                 recommended_product: Dict) -> str:
        """Generate recommendation reason text"""
        if rec_type == "similar":
            if base_product.get('category_id') == recommended_product.get('category_id'):
                return "Same category"
            elif base_product.get('brand') == recommended_product.get('brand'):
                return "Same brand"
            else:
                return "Similar features"
        elif rec_type == "related":
            return "Often bought together"
        elif rec_type == "frequently_bought":
            return "Frequently bought together"
        elif rec_type == "trending":
            return "Trending now"
        else:
            return "Recommended for you"
    
    def _handle_mock_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle mock implementations for additional tools"""
        base_url = arguments.get("baseUrl", get_base_url())
        product_id = arguments.get("productId", "PROD001")
        customer_id = arguments.get("customerId", "CUST001")
        
        # Mock response templates based on tool category
        if "categories" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/Categories",
                "toolName": name,
                "categories": [
                    {"id": "CAT001", "name": "Electronics", "parentId": None, "level": 0},
                    {"id": "CAT002", "name": "Smartphones", "parentId": "CAT001", "level": 1},
                    {"id": "CAT003", "name": "Laptops", "parentId": "CAT001", "level": 1}
                ],
                "totalCategories": 3
            }
        
        elif "attributes" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Attributes",
                "productId": product_id,
                "attributes": [
                    {"name": "Color", "value": "Black", "type": "variant"},
                    {"name": "Size", "value": "Medium", "type": "variant"},
                    {"name": "Material", "value": "Cotton", "type": "descriptive"}
                ]
            }
        
        elif "variants" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Variants",
                "productId": product_id,
                "variants": [
                    {"id": f"{product_id}_BLACK_S", "color": "Black", "size": "Small", "price": 29.99},
                    {"id": f"{product_id}_BLACK_M", "color": "Black", "size": "Medium", "price": 29.99},
                    {"id": f"{product_id}_BLUE_M", "color": "Blue", "size": "Medium", "price": 32.99}
                ]
            }
        
        elif "images" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Images",
                "productId": product_id,
                "images": [
                    {"id": "IMG001", "url": f"{base_url}/images/{product_id}/main.jpg", "type": "main"},
                    {"id": "IMG002", "url": f"{base_url}/images/{product_id}/alt1.jpg", "type": "alternative"}
                ]
            }
        
        elif "reviews" in name:
            if "create" in name:
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Products/{product_id}/Reviews",
                    "reviewId": f"REV_{random.randint(1000, 9999)}",
                    "status": "created",
                    "message": "Review created successfully"
                }
            else:
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Reviews",
                    "productId": product_id,
                    "reviews": [
                        {"id": "REV001", "customerId": "CUST001", "rating": 5, "title": "Great product!", "comment": "Love it", "date": datetime.now().isoformat()},
                        {"id": "REV002", "customerId": "CUST002", "rating": 4, "title": "Good quality", "comment": "Satisfied", "date": datetime.now().isoformat()}
                    ],
                    "averageRating": 4.5,
                    "totalReviews": 2
                }
        
        elif "pricing" in name or "price" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Pricing",
                "productId": product_id,
                "basePrice": 99.99,
                "salePrice": 79.99,
                "discountAmount": 20.00,
                "currencyCode": "USD",
                "priceAdjustments": [
                    {"type": "discount", "amount": -20.00, "description": "Holiday Sale"}
                ]
            }
        
        elif "inventory" in name:
            if "reserve" in name:
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Products/{product_id}/Inventory/Reserve",
                    "reservationId": f"RES_{random.randint(1000, 9999)}",
                    "status": "reserved",
                    "quantity": arguments.get("quantity", 1)
                }
            elif "release" in name:
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Products/Inventory/Release",
                    "reservationId": arguments.get("reservationId"),
                    "status": "released"
                }
            else:
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Inventory",
                    "productId": product_id,
                    "totalAvailable": 250,
                    "reserved": 10,
                    "available": 240,
                    "byLocation": [
                        {"locationId": "STORE001", "available": 50, "reserved": 5},
                        {"locationId": "WAREHOUSE001", "available": 200, "reserved": 5}
                    ]
                }
        
        elif "wishlist" in name:
            if "add" in name:
                return {
                    "api": f"POST {base_url}/api/CommerceRuntime/Customers/{customer_id}/Wishlist",
                    "status": "added",
                    "productId": product_id,
                    "wishlistId": arguments.get("wishlistId", "WISH001")
                }
            elif "remove" in name:
                return {
                    "api": f"DELETE {base_url}/api/CommerceRuntime/Customers/{customer_id}/Wishlist",
                    "status": "removed",
                    "productId": product_id
                }
            else:
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Customers/{customer_id}/Wishlist",
                    "wishlistItems": [
                        {"productId": "PROD001", "name": "Wireless Headphones", "price": 99.99, "dateAdded": datetime.now().isoformat()},
                        {"productId": "PROD002", "name": "Bluetooth Speaker", "price": 79.99, "dateAdded": datetime.now().isoformat()}
                    ]
                }
        
        elif "cross_sell" in name or "up_sell" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Recommendations",
                "productId": product_id,
                "recommendationType": "cross_sell" if "cross_sell" in name else "up_sell",
                "recommendations": [
                    {"productId": "PROD002", "name": "Related Product", "price": 49.99, "score": 0.85},
                    {"productId": "PROD003", "name": "Similar Product", "price": 129.99, "score": 0.78}
                ]
            }
        
        elif "bundle" in name or "kit" in name or "substitute" in name or "assembly" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Structure",
                "productId": product_id,
                "components": [
                    {"componentId": "COMP001", "name": "Component 1", "quantity": 1, "price": 29.99},
                    {"componentId": "COMP002", "name": "Component 2", "quantity": 2, "price": 19.99}
                ],
                "totalPrice": 69.97
            }
        
        elif "barcode" in name:
            if "validate" in name:
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/Barcode/Validate",
                    "barcode": arguments.get("barcode"),
                    "valid": True,
                    "productId": "PROD001",
                    "productName": "Wireless Headphones"
                }
            else:
                return {
                    "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Barcode",
                    "productId": product_id,
                    "barcodes": [
                        {"type": "UPC", "value": "123456789012"},
                        {"type": "EAN", "value": "1234567890123"}
                    ]
                }
        
        elif "tax" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Tax",
                "productId": product_id,
                "taxRate": 0.085,
                "taxAmount": 8.50,
                "taxGroup": "STANDARD",
                "exemptions": []
            }
        
        elif "warranty" in name or "certification" in name or "compliance" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Information",
                "productId": product_id,
                "information": {
                    "warranty": "2 years manufacturer warranty",
                    "certifications": ["CE", "FCC", "RoHS"],
                    "compliance": ["GDPR", "CCPA"]
                }
            }
        
        elif "localized" in name or "seo" in name:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Metadata",
                "productId": product_id,
                "localization": {
                    "language": arguments.get("languageCode", "en-US"),
                    "localizedName": "Localized Product Name",
                    "localizedDescription": "Localized product description"
                },
                "seo": {
                    "title": "Product SEO Title",
                    "description": "Product meta description",
                    "keywords": ["product", "electronics", "wireless"]
                }
            }
        
        # Default mock response
        else:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{name}",
                "toolName": name,
                "productId": product_id,
                "status": "success",
                "timestamp": datetime.now().isoformat() + "Z",
                "message": f"Mock response for {name} - tool implemented with realistic data",
                "mockData": {"result": "Success", "data": f"Mock data for {name}"}
            }