"""
Country Region Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (3 total):
1. country_region_get_country_regions_for_shipping - Gets the translated countries/regions with delivery modes configured for the current channel
2. country_region_get_country_regions_by_language_id - Get all the countries/regions filter by Language Id
3. country_region_get_country_regions - Get all the countries/regions

This controller handles country and region operations for address management and international commerce.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class CountryRegionController:
    """Controller for Country Region-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of country region-related tools"""
        return [
            Tool(
                name="country_region_get_country_regions_for_shipping",
                description="Gets the translated countries/regions with delivery modes configured for the current channel",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "queryResultSettings": {
                            "type": "object",
                            "description": "Query result settings for paging and sorting",
                            "properties": {
                                "paging": {
                                    "type": "object",
                                    "properties": {
                                        "skip": {"type": "number", "description": "Number of records to skip", "default": 0},
                                        "top": {"type": "number", "description": "Number of records to take", "default": 50}
                                    }
                                },
                                "sorting": {
                                    "type": "object",
                                    "properties": {
                                        "columns": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "columnName": {"type": "string"},
                                                    "isDescending": {"type": "boolean", "default": False}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
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
                name="country_region_get_country_regions_by_language_id",
                description="Get all the countries/regions filter by Language Id",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "languageId": {
                            "type": "string",
                            "description": "Language identifier for localization"
                        },
                        "queryResultSettings": {
                            "type": "object",
                            "description": "Query result settings for paging and sorting",
                            "properties": {
                                "paging": {
                                    "type": "object",
                                    "properties": {
                                        "skip": {"type": "number", "description": "Number of records to skip", "default": 0},
                                        "top": {"type": "number", "description": "Number of records to take", "default": 50}
                                    }
                                },
                                "sorting": {
                                    "type": "object",
                                    "properties": {
                                        "columns": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "columnName": {"type": "string"},
                                                    "isDescending": {"type": "boolean", "default": False}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": ["languageId"]
                }
            ),
            Tool(
                name="country_region_get_country_regions",
                description="Get all the countries/regions",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "queryResultSettings": {
                            "type": "object",
                            "description": "Query result settings for paging and sorting",
                            "properties": {
                                "paging": {
                                    "type": "object",
                                    "properties": {
                                        "skip": {"type": "number", "description": "Number of records to skip", "default": 0},
                                        "top": {"type": "number", "description": "Number of records to take", "default": 50}
                                    }
                                },
                                "sorting": {
                                    "type": "object",
                                    "properties": {
                                        "columns": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "columnName": {"type": "string"},
                                                    "isDescending": {"type": "boolean", "default": False}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://your-commerce-site.com"
                        }
                    },
                    "required": []
                }
            )
        ]
    
    def _get_country_regions_data(self, language_id: str = "en-US") -> List[Dict[str, Any]]:
        """Get mock country regions data with localization support"""
        base_data = [
            {
                "countryRegionId": "US",
                "countryRegionName": "United States" if language_id.startswith("en") else "États-Unis" if language_id.startswith("fr") else "Estados Unidos",
                "isoCode": "US",
                "threeLetterIsoCode": "USA",
                "currencyCode": "USD",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["en-US", "es-US"],
                "timeZones": ["EST", "CST", "MST", "PST"],
                "phoneNumberFormat": "+1 (XXX) XXX-XXXX",
                "postalCodeFormat": "XXXXX-XXXX",
                "shippingEnabled": True,
                "deliveryModes": ["Standard", "Express", "Overnight"],
                "taxCalculationEnabled": True
            },
            {
                "countryRegionId": "CA",
                "countryRegionName": "Canada" if language_id.startswith("en") else "Canada" if language_id.startswith("fr") else "Canadá",
                "isoCode": "CA", 
                "threeLetterIsoCode": "CAN",
                "currencyCode": "CAD",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["en-CA", "fr-CA"],
                "timeZones": ["AST", "EST", "CST", "MST", "PST"],
                "phoneNumberFormat": "+1 (XXX) XXX-XXXX",
                "postalCodeFormat": "XXX XXX",
                "shippingEnabled": True,
                "deliveryModes": ["Standard", "Express"],
                "taxCalculationEnabled": True
            },
            {
                "countryRegionId": "MX",
                "countryRegionName": "Mexico" if language_id.startswith("en") else "Mexique" if language_id.startswith("fr") else "México",
                "isoCode": "MX",
                "threeLetterIsoCode": "MEX",
                "currencyCode": "MXN",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["es-MX", "en-US"],
                "timeZones": ["CST", "MST", "PST"],
                "phoneNumberFormat": "+52 XX XXXX XXXX",
                "postalCodeFormat": "XXXXX",
                "shippingEnabled": True,
                "deliveryModes": ["Standard"],
                "taxCalculationEnabled": True
            },
            {
                "countryRegionId": "GB",
                "countryRegionName": "United Kingdom" if language_id.startswith("en") else "Royaume-Uni" if language_id.startswith("fr") else "Reino Unido",
                "isoCode": "GB",
                "threeLetterIsoCode": "GBR",
                "currencyCode": "GBP",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["en-GB"],
                "timeZones": ["GMT", "BST"],
                "phoneNumberFormat": "+44 XXXX XXXXXX",
                "postalCodeFormat": "XX## #XX",
                "shippingEnabled": False,
                "deliveryModes": [],
                "taxCalculationEnabled": True
            },
            {
                "countryRegionId": "FR",
                "countryRegionName": "France" if language_id.startswith("en") else "France" if language_id.startswith("fr") else "Francia",
                "isoCode": "FR",
                "threeLetterIsoCode": "FRA",
                "currencyCode": "EUR",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["fr-FR", "en-US"],
                "timeZones": ["CET", "CEST"],
                "phoneNumberFormat": "+33 X XX XX XX XX",
                "postalCodeFormat": "XXXXX",
                "shippingEnabled": False,
                "deliveryModes": [],
                "taxCalculationEnabled": True
            },
            {
                "countryRegionId": "DE",
                "countryRegionName": "Germany" if language_id.startswith("en") else "Allemagne" if language_id.startswith("fr") else "Alemania",
                "isoCode": "DE",
                "threeLetterIsoCode": "DEU",
                "currencyCode": "EUR",
                "languageId": language_id,
                "isActive": True,
                "supportedLanguages": ["de-DE", "en-US"],
                "timeZones": ["CET", "CEST"],
                "phoneNumberFormat": "+49 XXX XXXXXXX",
                "postalCodeFormat": "XXXXX",
                "shippingEnabled": False,
                "deliveryModes": [],
                "taxCalculationEnabled": True
            }
        ]
        return base_data
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle country region tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "country_region_get_country_regions_for_shipping":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get only countries with shipping enabled
            all_countries = [country for country in self._get_country_regions_data() if country["shippingEnabled"]]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "countryRegionName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["countryRegionName", "countryRegionId", "currencyCode"]:
                    all_countries.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_countries = all_countries[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CountryRegions/ForShipping",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_countries),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_countries),
                    "hasPreviousPage": skip > 0,
                    "results": paged_countries
                },
                "countryRegions": paged_countries,
                "totalCount": len(all_countries),
                "shippingEnabledCount": len(all_countries),
                "supportedDeliveryModes": list(set([mode for country in all_countries for mode in country["deliveryModes"]])),
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<CountryRegionInfo>",
                    "description": "Gets the translated countries/regions with delivery modes configured for the current channel"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "country_region_get_country_regions_by_language_id":
            language_id = arguments.get("languageId", "en-US")
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get countries with specified language
            all_countries = self._get_country_regions_data(language_id)
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "countryRegionName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["countryRegionName", "countryRegionId", "currencyCode"]:
                    all_countries.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_countries = all_countries[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CountryRegions/ByLanguage/{language_id}",
                "languageId": language_id,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_countries),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_countries),
                    "hasPreviousPage": skip > 0,
                    "results": paged_countries
                },
                "countryRegions": paged_countries,
                "totalCount": len(all_countries),
                "localizedCount": len(all_countries),
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "PageResult<CountryRegionInfo>",
                    "description": "Get all the countries/regions filter by Language Id"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "country_region_get_country_regions":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Get all countries
            all_countries = self._get_country_regions_data()
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "countryRegionName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["countryRegionName", "countryRegionId", "currencyCode"]:
                    all_countries.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_countries = all_countries[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/CountryRegions",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_countries),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_countries),
                    "hasPreviousPage": skip > 0,
                    "results": paged_countries
                },
                "countryRegions": paged_countries,
                "totalCount": len(all_countries),
                "activeCount": len([country for country in all_countries if country["isActive"]]),
                "shippingEnabledCount": len([country for country in all_countries if country["shippingEnabled"]]),
                "supportedCurrencies": list(set([country["currencyCode"] for country in all_countries])),
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<CountryRegionInfo>",
                    "description": "Get all the countries/regions"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown country region tool: {name}"}