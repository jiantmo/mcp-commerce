"""
Products Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (40+ total):
1. products_search - Search for products by various criteria
2. products_get_by_id - Get detailed information about a specific product
3. products_get_recommended_products - Get recommended products based on a specific product
4. products_get_product_availability - Get product availability across different locations
5. products_get - Search for products with OData query
6. products_get_by_ids - Get collection of products by IDs
7. products_compare - Compare products
8. products_search_by_category - Search products by category
9. products_search_by_text - Search products by text
10. products_get_search_suggestions - Get search suggestions
11. products_get_refiners_by_category - Get product refiners by category
12. products_get_refiners_by_text - Get product refiners by text
13. products_get_product_search_refiners - Get product search refiners
14. products_get_refiner_values_by_category - Get refiner values by category
15. products_get_refiner_values_by_text - Get refiner values by text
16. products_refine_search_by_category - Refine search by category
17. products_refine_search_by_text - Refine search by text
18. products_get_dimension_values - Get dimension values
19. products_get_variants_by_dimension_values - Get variants by dimension values
20. products_get_variants_by_components_in_slots - Get variants by components in slots
21. products_get_default_components - Get default components
22. products_get_component_by_product_slot_relation - Get component by product slot relation
23. products_get_slot_components - Get slot components
24. products_get_filtered_slot_components - Get filtered slot components
25. products_get_attribute_values - Get attribute values
26. products_get_relation_types - Get relation types
27. products_get_related_products - Get related products
28. products_get_refiners - Get refiners
29. products_changes - Get changed products
30. products_read_changed_products - Read changed products
31. products_get_deleted_listings - Get deleted listings
32. products_get_deleted_catalogs - Get deleted catalogs
33. products_get_deleted_languages - Get deleted languages
34. products_delete_listings_by_catalogs - Delete listings by catalogs
35. products_delete_listings_by_languages - Delete listings by languages
36. products_begin_read_changed_products - Begin read changed products session
37. products_end_read_changed_products - End read changed products session
38. products_update_listing_publishing_status - Update listing publishing status
39. products_get_product_availabilities - Get product availabilities
40. products_get_prices - Get prices
41. products_get_price - Get price
42. products_calculate_product_price - Calculate product price
43. products_get_active_prices - Get active prices
44. products_get_media_locations - Get media locations
45. products_get_media_blobs - Get media blobs
46. products_get_units_of_measure - Get units of measure
47. products_get_channel_product_attributes - Get channel product attributes
48. products_get_product_ratings - Get product ratings
49. products_get_estimated_availability - Get estimated availability
50. products_get_estimated_product_warehouse_availability - Get estimated product warehouse availability
51. products_update_product_warehouse_availability - Update product warehouse availability

This controller handles all product-related operations including product catalog search,
detailed product information, recommendation engine, inventory availability checking,
pricing, variants, components, attributes, and warehouse management.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
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
            ),
            Tool(
                name="products_get",
                description="Search for products with OData query",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "filter": {"type": "string", "description": "OData filter expression"},
                        "orderby": {"type": "string", "description": "OData order by expression"},
                        "top": {"type": "number", "description": "Number of results to return"},
                        "skip": {"type": "number", "description": "Number of results to skip"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    }
                }
            ),
            Tool(
                name="products_get_by_ids",
                description="Get collection of products by IDs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "productIds": {"type": "array", "items": {"type": "number"}, "description": "Product IDs"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "productIds"]
                }
            ),
            Tool(
                name="products_compare",
                description="Compare products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "productIds": {"type": "array", "items": {"type": "number"}, "description": "Product IDs to compare"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "productIds"]
                }
            ),
            Tool(
                name="products_search_by_category",
                description="Search products by category",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "categoryId": {"type": "number", "description": "Category ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "categoryId"]
                }
            ),
            Tool(
                name="products_search_by_text",
                description="Search products by text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "searchText": {"type": "string", "description": "Search text"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "searchText"]
                }
            ),
            Tool(
                name="products_get_search_suggestions",
                description="Get search suggestions",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "searchText": {"type": "string", "description": "Search text"},
                        "hitPrefix": {"type": "string", "description": "Hit prefix"},
                        "hitSuffix": {"type": "string", "description": "Hit suffix"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "searchText"]
                }
            ),
            Tool(
                name="products_get_refiners_by_category",
                description="Get product refiners by category",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "categoryId": {"type": "number", "description": "Category ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogId", "categoryId"]
                }
            ),
            Tool(
                name="products_get_refiners_by_text",
                description="Get product refiners by text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "searchText": {"type": "string", "description": "Search text"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogId", "searchText"]
                }
            ),
            Tool(
                name="products_get_product_search_refiners",
                description="Get product search refiners",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "searchCriteria": {"type": "object", "description": "Search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["searchCriteria"]
                }
            ),
            Tool(
                name="products_get_refiner_values_by_category",
                description="Get refiner values by category",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "categoryId": {"type": "number", "description": "Category ID"},
                        "refinerId": {"type": "number", "description": "Refiner ID"},
                        "refinerSourceValue": {"type": "number", "description": "Refiner source value"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogId", "categoryId", "refinerId", "refinerSourceValue"]
                }
            ),
            Tool(
                name="products_get_refiner_values_by_text",
                description="Get refiner values by text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "searchText": {"type": "string", "description": "Search text"},
                        "refinerId": {"type": "number", "description": "Refiner ID"},
                        "refinerSourceValue": {"type": "number", "description": "Refiner source value"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogId", "searchText", "refinerId", "refinerSourceValue"]
                }
            ),
            Tool(
                name="products_refine_search_by_category",
                description="Refine search by category",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "categoryId": {"type": "number", "description": "Category ID"},
                        "refinementCriteria": {"type": "array", "description": "Refinement criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "categoryId", "refinementCriteria"]
                }
            ),
            Tool(
                name="products_refine_search_by_text",
                description="Refine search by text",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "searchText": {"type": "string", "description": "Search text"},
                        "refinementCriteria": {"type": "array", "description": "Refinement criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "catalogId", "searchText", "refinementCriteria"]
                }
            ),
            Tool(
                name="products_get_dimension_values",
                description="Get dimension values",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "dimension": {"type": "number", "description": "Dimension"},
                        "matchingDimensionValues": {"type": "array", "description": "Matching dimension values"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "dimension"]
                }
            ),
            Tool(
                name="products_get_variants_by_dimension_values",
                description="Get variants by dimension values",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "matchingDimensionValues": {"type": "array", "description": "Matching dimension values"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId"]
                }
            ),
            Tool(
                name="products_get_variants_by_components_in_slots",
                description="Get variants by components in slots",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "matchingSlotToComponentRelationship": {"type": "array", "description": "Matching slot to component relationship"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId"]
                }
            ),
            Tool(
                name="products_get_default_components",
                description="Get default components",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId"]
                }
            ),
            Tool(
                name="products_get_component_by_product_slot_relation",
                description="Get component by product slot relation",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "componentRelation": {"type": "object", "description": "Component relation"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["channelId", "componentRelation"]
                }
            ),
            Tool(
                name="products_get_slot_components",
                description="Get slot components",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "slotId": {"type": "number", "description": "Slot ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "slotId"]
                }
            ),
            Tool(
                name="products_get_filtered_slot_components",
                description="Get filtered slot components",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "slotId": {"type": "number", "description": "Slot ID"},
                        "selectedComponents": {"type": "array", "description": "Selected components"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "slotId"]
                }
            ),
            Tool(
                name="products_get_attribute_values",
                description="Get attribute values",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "catalogId"]
                }
            ),
            Tool(
                name="products_get_relation_types",
                description="Get relation types",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "catalogId"]
                }
            ),
            Tool(
                name="products_get_related_products",
                description="Get related products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "relationTypeId": {"type": "number", "description": "Relation type ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "catalogId", "relationTypeId"]
                }
            ),
            Tool(
                name="products_get_refiners",
                description="Get refiners",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productSearchCriteria": {"type": "object", "description": "Product search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["productSearchCriteria"]
                }
            ),
            Tool(
                name="products_changes",
                description="Get changed products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productSearchCriteria": {"type": "object", "description": "Changed products search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["productSearchCriteria"]
                }
            ),
            Tool(
                name="products_read_changed_products",
                description="Read changed products",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productSearchCriteria": {"type": "object", "description": "Changed products search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["productSearchCriteria"]
                }
            ),
            Tool(
                name="products_get_deleted_listings",
                description="Get deleted listings",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "skip": {"type": "number", "description": "Skip count"},
                        "top": {"type": "number", "description": "Top count"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogId", "skip", "top"]
                }
            ),
            Tool(
                name="products_get_deleted_catalogs",
                description="Get deleted catalogs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    }
                }
            ),
            Tool(
                name="products_get_deleted_languages",
                description="Get deleted languages",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    }
                }
            ),
            Tool(
                name="products_delete_listings_by_catalogs",
                description="Delete listings by catalogs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "catalogIds": {"type": "array", "items": {"type": "number"}, "description": "Catalog IDs"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["catalogIds"]
                }
            ),
            Tool(
                name="products_delete_listings_by_languages",
                description="Delete listings by languages",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "languages": {"type": "array", "items": {"type": "string"}, "description": "Languages"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["languages"]
                }
            ),
            Tool(
                name="products_begin_read_changed_products",
                description="Begin read changed products session",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "changedProductSearchCriteria": {"type": "object", "description": "Changed product search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["changedProductSearchCriteria"]
                }
            ),
            Tool(
                name="products_end_read_changed_products",
                description="End read changed products session",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "session": {"type": "object", "description": "Read changed products session"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["session"]
                }
            ),
            Tool(
                name="products_update_listing_publishing_status",
                description="Update listing publishing status",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "publishingStatuses": {"type": "array", "description": "Publishing statuses"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["publishingStatuses"]
                }
            ),
            Tool(
                name="products_get_product_availabilities",
                description="Get product availabilities",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "itemIds": {"type": "array", "items": {"type": "number"}, "description": "Item IDs"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["itemIds", "channelId"]
                }
            ),
            Tool(
                name="products_get_prices",
                description="Get prices",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "itemId": {"type": "string", "description": "Item ID"},
                        "inventoryDimensionId": {"type": "string", "description": "Inventory dimension ID"},
                        "barcode": {"type": "string", "description": "Barcode"},
                        "customerAccountNumber": {"type": "string", "description": "Customer account number"},
                        "unitOfMeasureSymbol": {"type": "string", "description": "Unit of measure symbol"},
                        "quantity": {"type": "number", "description": "Quantity"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["itemId"]
                }
            ),
            Tool(
                name="products_get_price",
                description="Get price",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "customerAccountNumber": {"type": "string", "description": "Customer account number"},
                        "unitOfMeasureSymbol": {"type": "string", "description": "Unit of measure symbol"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId"]
                }
            ),
            Tool(
                name="products_calculate_product_price",
                description="Calculate product price",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "customerAccountNumber": {"type": "string", "description": "Customer account number"},
                        "unitOfMeasureSymbol": {"type": "string", "description": "Unit of measure symbol"},
                        "loyaltyCardId": {"type": "string", "description": "Loyalty card ID"},
                        "affiliationLoyaltyTiers": {"type": "array", "description": "Affiliation loyalty tiers"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId"]
                }
            ),
            Tool(
                name="products_get_active_prices",
                description="Get active prices",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "projectDomain": {"type": "object", "description": "Project domain"},
                        "productIds": {"type": "array", "items": {"type": "number"}, "description": "Product IDs"},
                        "activeDate": {"type": "string", "description": "Active date"},
                        "customerId": {"type": "string", "description": "Customer ID"},
                        "affiliationLoyaltyTiers": {"type": "array", "description": "Affiliation loyalty tiers"},
                        "includeSimpleDiscountsInContextualPrice": {"type": "boolean", "description": "Include simple discounts in contextual price"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["projectDomain", "productIds", "activeDate"]
                }
            ),
            Tool(
                name="products_get_media_locations",
                description="Get media locations",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "catalogId"]
                }
            ),
            Tool(
                name="products_get_media_blobs",
                description="Get media blobs",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "channelId": {"type": "number", "description": "Channel ID"},
                        "catalogId": {"type": "number", "description": "Catalog ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId", "channelId", "catalogId"]
                }
            ),
            Tool(
                name="products_get_units_of_measure",
                description="Get units of measure",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "recordId": {"type": "number", "description": "Record ID"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["recordId"]
                }
            ),
            Tool(
                name="products_get_channel_product_attributes",
                description="Get channel product attributes",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    }
                }
            ),
            Tool(
                name="products_get_product_ratings",
                description="Get product ratings",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "productIds": {"type": "array", "items": {"type": "number"}, "description": "Product IDs"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["productIds"]
                }
            ),
            Tool(
                name="products_get_estimated_availability",
                description="Get estimated availability",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "searchCriteria": {"type": "object", "description": "Inventory availability search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["searchCriteria"]
                }
            ),
            Tool(
                name="products_get_estimated_warehouse_availability",
                description="Get estimated product warehouse availability",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "searchCriteria": {"type": "object", "description": "Inventory availability search criteria"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["searchCriteria"]
                }
            ),
            Tool(
                name="products_update_product_warehouse_availability",
                description="Update product warehouse availability",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "quantities": {"type": "array", "description": "Product warehouse quantities"},
                        "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}
                    },
                    "required": ["quantities"]
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
        
        # Handle additional products tools
        return self._handle_additional_products_tools(name, arguments)
    
    def _get_mock_product_data(self, base_url: str, product_id: str = "PROD001") -> Dict[str, Any]:
        """Helper method to generate consistent mock product data"""
        return {
            "productId": product_id,
            "sku": f"SKU-{product_id}",
            "name": f"Product {product_id}",
            "description": f"Description for product {product_id}",
            "price": round(random.uniform(10, 500), 2),
            "currency": "USD",
            "category": {"categoryId": "CAT001", "name": "Electronics"},
            "brand": "MockBrand",
            "rating": round(random.uniform(3.5, 5.0), 1),
            "reviewCount": random.randint(10, 200),
            "inStock": True,
            "stockQuantity": random.randint(10, 100),
            "images": [f"{base_url}/images/products/{product_id}.jpg"]
        }
    
    def _handle_additional_products_tools(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle additional products tools with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "products_get":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products",
                "filter": arguments.get("filter", ""),
                "orderby": arguments.get("orderby", ""),
                "results": [self._get_mock_product_data(base_url, f"PROD{i:03d}") for i in range(1, 6)]
            }
        
        elif name == "products_get_by_ids":
            channel_id = arguments.get("channelId", 1)
            product_ids = arguments.get("productIds", [1, 2, 3])
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetByIds",
                "channelId": channel_id,
                "results": [self._get_mock_product_data(base_url, f"PROD{pid:03d}") for pid in product_ids]
            }
        
        elif name == "products_compare":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/Compare",
                "channelId": arguments.get("channelId", 1),
                "catalogId": arguments.get("catalogId", 1),
                "comparisonLines": [
                    {
                        "productId": "PROD001",
                        "attributes": {"color": "Black", "size": "Medium", "weight": "0.5 lbs"},
                        "specifications": {"warranty": "2 years", "brand": "TechBrand"}
                    },
                    {
                        "productId": "PROD002",
                        "attributes": {"color": "White", "size": "Large", "weight": "0.7 lbs"},
                        "specifications": {"warranty": "1 year", "brand": "OtherBrand"}
                    }
                ]
            }
        
        elif name == "products_search_by_category":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/SearchByCategory",
                "channelId": arguments.get("channelId", 1),
                "catalogId": arguments.get("catalogId", 1),
                "categoryId": arguments.get("categoryId", 1),
                "results": [self._get_mock_product_data(base_url, f"PROD{i:03d}") for i in range(1, 4)]
            }
        
        elif name == "products_search_by_text":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/SearchByText",
                "searchText": arguments.get("searchText", ""),
                "results": [self._get_mock_product_data(base_url, f"PROD{i:03d}") for i in range(1, 4)]
            }
        
        elif name == "products_get_search_suggestions":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetSearchSuggestions",
                "searchText": arguments.get("searchText", ""),
                "suggestions": [
                    {"text": "wireless headphones", "count": 45},
                    {"text": "wireless speakers", "count": 23},
                    {"text": "wireless charger", "count": 12}
                ]
            }
        
        elif name in ["products_get_refiners_by_category", "products_get_refiners_by_text", "products_get_product_search_refiners", "products_get_refiners"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetRefiners",
                "refiners": [
                    {
                        "refinerId": 1,
                        "name": "Brand",
                        "values": [
                            {"value": "TechBrand", "count": 25},
                            {"value": "OtherBrand", "count": 15}
                        ]
                    },
                    {
                        "refinerId": 2,
                        "name": "Price Range",
                        "values": [
                            {"value": "$0-$50", "count": 20},
                            {"value": "$50-$100", "count": 15},
                            {"value": "$100+", "count": 10}
                        ]
                    }
                ]
            }
        
        elif name in ["products_get_refiner_values_by_category", "products_get_refiner_values_by_text"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetRefinerValues",
                "refinerId": arguments.get("refinerId", 1),
                "values": [
                    {"value": "Value 1", "count": 10},
                    {"value": "Value 2", "count": 8},
                    {"value": "Value 3", "count": 5}
                ]
            }
        
        elif name in ["products_refine_search_by_category", "products_refine_search_by_text"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/RefineSearch",
                "refinedResults": [self._get_mock_product_data(base_url, f"PROD{i:03d}") for i in range(1, 4)]
            }
        
        elif name == "products_get_dimension_values":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetDimensionValues",
                "recordId": arguments.get("recordId", 1),
                "dimension": arguments.get("dimension", 1),
                "dimensionValues": [
                    {"dimensionId": 1, "value": "Small", "displayName": "Small"},
                    {"dimensionId": 2, "value": "Medium", "displayName": "Medium"},
                    {"dimensionId": 3, "value": "Large", "displayName": "Large"}
                ]
            }
        
        elif name in ["products_get_variants_by_dimension_values", "products_get_variants_by_components_in_slots"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetVariants",
                "variants": [
                    {
                        "variantId": "VAR001",
                        "productId": "PROD001",
                        "dimensions": {"size": "Small", "color": "Black"},
                        "price": 99.99,
                        "stockQuantity": 15
                    },
                    {
                        "variantId": "VAR002",
                        "productId": "PROD001",
                        "dimensions": {"size": "Medium", "color": "Black"},
                        "price": 99.99,
                        "stockQuantity": 20
                    }
                ]
            }
        
        elif name in ["products_get_default_components", "products_get_slot_components", "products_get_filtered_slot_components"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetComponents",
                "components": [
                    {
                        "componentId": "COMP001",
                        "name": "Component 1",
                        "slotId": arguments.get("slotId", 1),
                        "isRequired": True,
                        "price": 10.00
                    },
                    {
                        "componentId": "COMP002",
                        "name": "Component 2",
                        "slotId": arguments.get("slotId", 1),
                        "isRequired": False,
                        "price": 15.00
                    }
                ]
            }
        
        elif name == "products_get_component_by_product_slot_relation":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetComponentByRelation",
                "component": {
                    "componentId": "COMP001",
                    "name": "Specific Component",
                    "price": 12.50,
                    "description": "Component based on slot relation"
                }
            }
        
        elif name == "products_get_attribute_values":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetAttributeValues",
                "recordId": arguments.get("recordId", 1),
                "attributes": [
                    {"attributeId": 1, "name": "Color", "value": "Black", "displayValue": "Black"},
                    {"attributeId": 2, "name": "Size", "value": "M", "displayValue": "Medium"},
                    {"attributeId": 3, "name": "Weight", "value": "0.5", "displayValue": "0.5 lbs"}
                ]
            }
        
        elif name == "products_get_relation_types":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetRelationTypes",
                "relationTypes": [
                    {"relationTypeId": 1, "name": "Related Products", "description": "Products related to this item"},
                    {"relationTypeId": 2, "name": "Accessories", "description": "Accessories for this product"},
                    {"relationTypeId": 3, "name": "Complementary", "description": "Products that complement this item"}
                ]
            }
        
        elif name == "products_get_related_products":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetRelatedProducts",
                "relationTypeId": arguments.get("relationTypeId", 1),
                "relatedProducts": [self._get_mock_product_data(base_url, f"REL{i:03d}") for i in range(1, 4)]
            }
        
        elif name in ["products_changes", "products_read_changed_products"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/Changes",
                "changedProducts": [
                    {
                        "productId": "PROD001",
                        "changeType": "Updated",
                        "lastModified": datetime.now().isoformat() + "Z",
                        "changes": ["price", "description"]
                    },
                    {
                        "productId": "PROD002",
                        "changeType": "Created",
                        "lastModified": datetime.now().isoformat() + "Z",
                        "changes": ["all"]
                    }
                ]
            }
        
        elif name == "products_get_deleted_listings":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetDeletedListings",
                "catalogId": arguments.get("catalogId", 1),
                "deletedListings": [
                    {"listingId": "LIST001", "deletedDate": datetime.now().isoformat() + "Z"},
                    {"listingId": "LIST002", "deletedDate": datetime.now().isoformat() + "Z"}
                ]
            }
        
        elif name == "products_get_deleted_catalogs":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetDeletedCatalogs",
                "deletedCatalogs": [1, 2, 3]
            }
        
        elif name == "products_get_deleted_languages":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetDeletedLanguages",
                "deletedLanguages": ["en-US", "fr-FR", "de-DE"]
            }
        
        elif name in ["products_delete_listings_by_catalogs", "products_delete_listings_by_languages"]:
            return {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Products/DeleteListings",
                "success": True,
                "deletedCount": random.randint(1, 10),
                "message": "Listings deleted successfully"
            }
        
        elif name == "products_begin_read_changed_products":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Products/BeginReadChangedProducts",
                "session": {
                    "sessionId": f"SESSION_{random.randint(1000, 9999)}",
                    "startTime": datetime.now().isoformat() + "Z",
                    "status": "Active"
                }
            }
        
        elif name == "products_end_read_changed_products":
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Products/EndReadChangedProducts",
                "success": True,
                "endTime": datetime.now().isoformat() + "Z",
                "message": "Session ended successfully"
            }
        
        elif name == "products_update_listing_publishing_status":
            return {
                "api": f"PUT {base_url}/api/CommerceRuntime/Products/UpdateListingPublishingStatus",
                "updatedStatuses": len(arguments.get("publishingStatuses", [])),
                "success": True,
                "timestamp": datetime.now().isoformat() + "Z"
            }
        
        elif name == "products_get_product_availabilities":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetProductAvailabilities",
                "channelId": arguments.get("channelId", 1),
                "availabilities": [
                    {
                        "itemId": item_id,
                        "availableQuantity": random.randint(0, 100),
                        "totalQuantity": random.randint(50, 150),
                        "reservedQuantity": random.randint(0, 10)
                    }
                    for item_id in arguments.get("itemIds", [1, 2, 3])
                ]
            }
        
        elif name in ["products_get_prices", "products_get_price", "products_calculate_product_price"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetPrices",
                "prices": [
                    {
                        "productId": arguments.get("recordId", "PROD001"),
                        "basePrice": round(random.uniform(10, 500), 2),
                        "salePrice": round(random.uniform(8, 450), 2),
                        "currency": "USD",
                        "validFrom": datetime.now().isoformat() + "Z",
                        "validTo": (datetime.now() + timedelta(days=30)).isoformat() + "Z"
                    }
                ]
            }
        
        elif name == "products_get_active_prices":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetActivePrices",
                "activePrices": [
                    {
                        "productId": pid,
                        "activePrice": round(random.uniform(10, 500), 2),
                        "currency": "USD",
                        "effectiveDate": arguments.get("activeDate", datetime.now().isoformat() + "Z")
                    }
                    for pid in arguments.get("productIds", [1, 2, 3])
                ]
            }
        
        elif name in ["products_get_media_locations", "products_get_media_blobs"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetMedia",
                "recordId": arguments.get("recordId", 1),
                "mediaItems": [
                    {
                        "mediaId": f"MEDIA{i:03d}",
                        "url": f"{base_url}/media/products/PROD001_{i}.jpg",
                        "type": "image",
                        "altText": f"Product image {i}",
                        "isPrimary": i == 1
                    }
                    for i in range(1, 4)
                ]
            }
        
        elif name == "products_get_units_of_measure":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetUnitsOfMeasure",
                "recordId": arguments.get("recordId", 1),
                "unitsOfMeasure": [
                    {"unitId": "EA", "name": "Each", "symbol": "ea", "decimals": 0},
                    {"unitId": "KG", "name": "Kilogram", "symbol": "kg", "decimals": 3},
                    {"unitId": "LB", "name": "Pound", "symbol": "lb", "decimals": 2}
                ]
            }
        
        elif name == "products_get_channel_product_attributes":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetChannelProductAttributes",
                "attributes": [
                    {
                        "attributeId": 1,
                        "name": "Color",
                        "dataType": "Text",
                        "isRequired": True,
                        "allowedValues": ["Red", "Blue", "Green", "Black", "White"]
                    },
                    {
                        "attributeId": 2,
                        "name": "Size",
                        "dataType": "Text",
                        "isRequired": True,
                        "allowedValues": ["XS", "S", "M", "L", "XL", "XXL"]
                    }
                ]
            }
        
        elif name == "products_get_product_ratings":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetProductRatings",
                "ratings": [
                    {
                        "productId": pid,
                        "averageRating": round(random.uniform(3.0, 5.0), 1),
                        "totalReviews": random.randint(10, 200),
                        "ratingDistribution": {
                            "5": random.randint(10, 50),
                            "4": random.randint(5, 30),
                            "3": random.randint(2, 15),
                            "2": random.randint(0, 5),
                            "1": random.randint(0, 3)
                        }
                    }
                    for pid in arguments.get("productIds", [1, 2, 3])
                ]
            }
        
        elif name in ["products_get_estimated_availability", "products_get_estimated_product_warehouse_availability"]:
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Products/GetEstimatedAvailability",
                "searchCriteria": arguments.get("searchCriteria", {}),
                "estimatedAvailability": {
                    "productId": "PROD001",
                    "estimatedQuantity": random.randint(50, 200),
                    "estimatedDeliveryDate": (datetime.now() + timedelta(days=random.randint(1, 7))).isoformat() + "Z",
                    "warehouses": [
                        {
                            "warehouseId": f"WH{i:03d}",
                            "estimatedQuantity": random.randint(10, 50),
                            "distance": round(random.uniform(1, 50), 1)
                        }
                        for i in range(1, 4)
                    ]
                }
            }
        
        elif name == "products_update_product_warehouse_availability":
            return {
                "api": f"PUT {base_url}/api/CommerceRuntime/Products/UpdateProductWarehouseAvailability",
                "updateResult": {
                    "success": True,
                    "updatedCount": len(arguments.get("quantities", [])),
                    "timestamp": datetime.now().isoformat() + "Z",
                    "message": "Product warehouse availability updated successfully"
                }
            }
        
        return {"error": f"Unknown additional products tool: {name}"}