"""
Products Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (4 total):
1. products_search - Search for products by various criteria
2. products_get_by_id - Get detailed information about a specific product
3. products_get_recommended_products - Get recommended products based on a specific product
4. products_get_product_availability - Get product availability across different locations

This controller handles all product-related operations including product catalog search,
detailed product information, recommendation engine, and inventory availability checking.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
import string
from mcp.types import Tool

class ProductsController:
    """Controller for Products-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of products-related tools"""
        return [
            Tool(
                name="products_search",
                description="Search for products by various criteria",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search query for products (name, description, SKU)"
                        },
                        "categoryId": {
                            "type": "string",
                            "description": "Filter by category ID"
                        },
                        "minPrice": {
                            "type": "number",
                            "description": "Minimum price filter"
                        },
                        "maxPrice": {
                            "type": "number",
                            "description": "Maximum price filter"
                        },
                        "inStock": {
                            "type": "boolean",
                            "description": "Filter by stock availability"
                        },
                        "sortBy": {
                            "type": "string",
                            "enum": ["name", "price", "popularity", "rating", "newest"],
                            "description": "Sort results by",
                            "default": "name"
                        },
                        "sortOrder": {
                            "type": "string",
                            "enum": ["asc", "desc"],
                            "description": "Sort order",
                            "default": "asc"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of results to return",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
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
                            "description": "The product ID to retrieve"
                        },
                        "includeVariants": {
                            "type": "boolean",
                            "description": "Include product variants in response",
                            "default": True
                        },
                        "includeImages": {
                            "type": "boolean",
                            "description": "Include product images in response",
                            "default": True
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
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
                            "enum": ["related", "frequently_bought_together", "customers_also_viewed", "similar"],
                            "description": "Type of recommendations to get",
                            "default": "related"
                        },
                        "limit": {
                            "type": "number",
                            "description": "Maximum number of recommendations to return",
                            "default": 10
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
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
                        "variantId": {
                            "type": "string",
                            "description": "Specific variant ID (optional)"
                        },
                        "storeId": {
                            "type": "string",
                            "description": "Specific store ID to check (optional)"
                        },
                        "zipCode": {
                            "type": "string",
                            "description": "Zip code to find nearby stores"
                        },
                        "radius": {
                            "type": "number",
                            "description": "Search radius in miles from zip code",
                            "default": 25
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["productId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle products tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "products_search":
            query = arguments.get("query", "")
            limit = arguments.get("limit", 25)
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/Search",
                "searchCriteria": {
                    "query": query,
                    "categoryId": arguments.get("categoryId"),
                    "minPrice": arguments.get("minPrice"),
                    "maxPrice": arguments.get("maxPrice"),
                    "inStock": arguments.get("inStock"),
                    "sortBy": arguments.get("sortBy", "name"),
                    "sortOrder": arguments.get("sortOrder", "asc")
                },
                "totalResults": 45,
                "results": [
                    {
                        "productId": "PROD001",
                        "sku": "WH-001",
                        "name": "Wireless Bluetooth Headphones",
                        "description": "Premium noise-cancelling wireless headphones with 30-hour battery life",
                        "price": 99.99,
                        "currency": "USD",
                        "category": {
                            "categoryId": "CAT001",
                            "name": "Electronics"
                        },
                        "brand": "TechBrand",
                        "rating": 4.5,
                        "reviewCount": 127,
                        "inStock": True,
                        "stockQuantity": 50,
                        "images": [
                            f"{base_url}/images/products/PROD001_1.jpg",
                            f"{base_url}/images/products/PROD001_2.jpg"
                        ],
                        "variants": [
                            {"variantId": "VAR001", "color": "Black", "size": "Standard"},
                            {"variantId": "VAR002", "color": "White", "size": "Standard"}
                        ]
                    },
                    {
                        "productId": "PROD002",
                        "sku": "PC-001",
                        "name": "Protective Phone Case",
                        "description": "Durable protective case for smartphones with shock absorption",
                        "price": 19.99,
                        "currency": "USD",
                        "category": {
                            "categoryId": "CAT002",
                            "name": "Accessories"
                        },
                        "brand": "ProtectCase",
                        "rating": 4.2,
                        "reviewCount": 89,
                        "inStock": True,
                        "stockQuantity": 150,
                        "images": [
                            f"{base_url}/images/products/PROD002_1.jpg"
                        ],
                        "variants": [
                            {"variantId": "VAR003", "color": "Clear", "phoneModel": "iPhone 14"},
                            {"variantId": "VAR004", "color": "Black", "phoneModel": "iPhone 14"}
                        ]
                    }
                ][:limit]
            }
        
        elif name == "products_get_by_id":
            product_id = arguments.get("productId", "PROD001")
            include_variants = arguments.get("includeVariants", True)
            include_images = arguments.get("includeImages", True)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}",
                "productId": product_id,
                "sku": "WH-001",
                "name": "Wireless Bluetooth Headphones",
                "description": "Premium noise-cancelling wireless headphones with superior sound quality and 30-hour battery life. Features include active noise cancellation, quick charge, and premium comfort padding.",
                "longDescription": "Experience audio like never before with these premium wireless headphones. Engineered with advanced noise-cancelling technology and high-fidelity drivers for an immersive listening experience.",
                "price": 99.99,
                "currency": "USD",
                "compareAtPrice": 149.99,
                "category": {
                    "categoryId": "CAT001",
                    "name": "Electronics",
                    "breadcrumb": "Home > Electronics > Audio > Headphones"
                },
                "brand": "TechBrand",
                "manufacturer": "TechBrand Inc.",
                "rating": 4.5,
                "reviewCount": 127,
                "inStock": True,
                "stockQuantity": 50,
                "weight": "0.7 lbs",
                "dimensions": "7.1 x 6.7 x 3.2 inches",
                "tags": ["wireless", "bluetooth", "noise-cancelling", "premium"],
                "specifications": {
                    "batteryLife": "30 hours",
                    "chargingTime": "2 hours",
                    "bluetoothVersion": "5.0",
                    "range": "33 feet",
                    "driverSize": "40mm",
                    "impedance": "32 ohm",
                    "warranty": "2 years"
                },
                "images": [
                    {
                        "url": f"{base_url}/images/products/PROD001_main.jpg",
                        "alt": "Wireless Bluetooth Headphones - Main View",
                        "isPrimary": True
                    },
                    {
                        "url": f"{base_url}/images/products/PROD001_side.jpg",
                        "alt": "Wireless Bluetooth Headphones - Side View",
                        "isPrimary": False
                    }
                ] if include_images else None,
                "variants": [
                    {
                        "variantId": "VAR001",
                        "color": "Black",
                        "size": "Standard",
                        "price": 99.99,
                        "sku": "WH-001-BLK",
                        "stockQuantity": 30,
                        "images": [f"{base_url}/images/products/VAR001.jpg"]
                    },
                    {
                        "variantId": "VAR002",
                        "color": "White",
                        "size": "Standard",
                        "price": 99.99,
                        "sku": "WH-001-WHT",
                        "stockQuantity": 20,
                        "images": [f"{base_url}/images/products/VAR002.jpg"]
                    }
                ] if include_variants else None,
                "seo": {
                    "title": "Wireless Bluetooth Headphones - Premium Audio Experience",
                    "metaDescription": "Shop premium wireless Bluetooth headphones with noise cancellation and 30-hour battery life.",
                    "canonicalUrl": f"{base_url}/products/{product_id}"
                }
            }
        
        elif name == "products_get_recommended_products":
            product_id = arguments.get("productId", "PROD001")
            recommendation_type = arguments.get("recommendationType", "related")
            limit = arguments.get("limit", 10)
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Recommendations",
                "productId": product_id,
                "recommendationType": recommendation_type,
                "recommendations": [
                    {
                        "productId": "PROD002",
                        "name": "Wireless Charging Pad",
                        "price": 29.99,
                        "currency": "USD",
                        "rating": 4.3,
                        "image": f"{base_url}/images/products/PROD002_thumb.jpg",
                        "score": 0.95,
                        "reason": "Customers who bought headphones also purchased this"
                    },
                    {
                        "productId": "PROD003",
                        "name": "Premium Audio Cable",
                        "price": 19.99,
                        "currency": "USD",
                        "rating": 4.1,
                        "image": f"{base_url}/images/products/PROD003_thumb.jpg",
                        "score": 0.89,
                        "reason": "Compatible accessory"
                    },
                    {
                        "productId": "PROD004",
                        "name": "Noise-Cancelling Earbuds",
                        "price": 149.99,
                        "currency": "USD",
                        "rating": 4.7,
                        "image": f"{base_url}/images/products/PROD004_thumb.jpg",
                        "score": 0.87,
                        "reason": "Similar product in same category"
                    }
                ][:limit]
            }
        
        elif name == "products_get_product_availability":
            product_id = arguments.get("productId", "PROD001")
            variant_id = arguments.get("variantId")
            store_id = arguments.get("storeId")
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/{product_id}/Availability",
                "productId": product_id,
                "variantId": variant_id,
                "available": True,
                "totalQuantity": 85,
                "reservedQuantity": 5,
                "availableQuantity": 80,
                "locations": [
                    {
                        "storeId": "STORE001",
                        "storeName": "Downtown Main Store",
                        "address": {
                            "street": "123 Main Street",
                            "city": "Seattle",
                            "state": "WA",
                            "zipCode": "98101",
                            "country": "USA"
                        },
                        "coordinates": {
                            "latitude": 47.6062,
                            "longitude": -122.3321
                        },
                        "distance": 2.5,
                        "quantity": 30,
                        "reserved": 2,
                        "available": 28,
                        "lastUpdated": datetime.now().isoformat() + "Z",
                        "storeHours": {
                            "monday": "9:00 AM - 9:00 PM",
                            "tuesday": "9:00 AM - 9:00 PM",
                            "wednesday": "9:00 AM - 9:00 PM",
                            "thursday": "9:00 AM - 9:00 PM",
                            "friday": "9:00 AM - 10:00 PM",
                            "saturday": "10:00 AM - 10:00 PM",
                            "sunday": "11:00 AM - 7:00 PM"
                        },
                        "services": ["pickup", "curbside", "delivery"]
                    },
                    {
                        "storeId": "STORE002",
                        "storeName": "Westfield Mall Store",
                        "address": {
                            "street": "456 Mall Drive",
                            "city": "Bellevue",
                            "state": "WA",
                            "zipCode": "98004",
                            "country": "USA"
                        },
                        "coordinates": {
                            "latitude": 47.6101,
                            "longitude": -122.2015
                        },
                        "distance": 8.2,
                        "quantity": 25,
                        "reserved": 1,
                        "available": 24,
                        "lastUpdated": datetime.now().isoformat() + "Z",
                        "services": ["pickup", "delivery"]
                    },
                    {
                        "storeId": "WH001",
                        "storeName": "Distribution Center",
                        "type": "warehouse",
                        "quantity": 30,
                        "reserved": 2,
                        "available": 28,
                        "estimatedDelivery": "2-3 business days",
                        "shippingMethods": ["standard", "express", "overnight"]
                    }
                ] if not store_id else [loc for loc in [
                    # Same locations as above but filtered
                ] if loc.get("storeId") == store_id],
                "variants": [
                    {
                        "variantId": "VAR001",
                        "color": "Black",
                        "totalQuantity": 45,
                        "availableQuantity": 42
                    },
                    {
                        "variantId": "VAR002",
                        "color": "White",
                        "totalQuantity": 40,
                        "availableQuantity": 38
                    }
                ] if not variant_id else None
            }
        
        else:
            return {"error": f"Unknown products tool: {name}"}