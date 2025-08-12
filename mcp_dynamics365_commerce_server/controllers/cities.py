"""
Cities Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. cities_get_cities - Get all the cities filtered by Country/Region, State Province and County

This controller handles city-related operations for address management and geographic data.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class CitiesController:
    """Controller for Cities-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of cities-related tools"""
        return [
            Tool(
                name="cities_get_cities",
                description="Get all the cities filtered by Country/Region, State Province and County",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "countryRegionId": {
                            "type": "string",
                            "description": "Country or region identifier"
                        },
                        "stateProvinceId": {
                            "type": "string",
                            "description": "State or province identifier"
                        },
                        "countyId": {
                            "type": "string",
                            "description": "County identifier"
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
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["countryRegionId", "stateProvinceId", "countyId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle cities tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "cities_get_cities":
            country_region_id = arguments.get("countryRegionId", "US")
            state_province_id = arguments.get("stateProvinceId", "WA")
            county_id = arguments.get("countyId", "KING")
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock cities data based on location filters
            all_cities = []
            if country_region_id == "US" and state_province_id == "WA":
                if county_id == "KING":
                    all_cities = [
                        {
                            "cityId": "SEA001",
                            "cityName": "Seattle",
                            "countryRegionId": country_region_id,
                            "countryRegionName": "United States",
                            "stateProvinceId": state_province_id,
                            "stateProvinceName": "Washington",
                            "countyId": county_id,
                            "countyName": "King County",
                            "population": 753675,
                            "timeZone": "Pacific Standard Time",
                            "isActive": True,
                            "postalCodes": ["98101", "98102", "98103", "98104", "98105"],
                            "latitude": 47.6062,
                            "longitude": -122.3321
                        },
                        {
                            "cityId": "BEL001",
                            "cityName": "Bellevue",
                            "countryRegionId": country_region_id,
                            "countryRegionName": "United States",
                            "stateProvinceId": state_province_id,
                            "stateProvinceName": "Washington",
                            "countyId": county_id,
                            "countyName": "King County",
                            "population": 151854,
                            "timeZone": "Pacific Standard Time",
                            "isActive": True,
                            "postalCodes": ["98004", "98005", "98006", "98007", "98008"],
                            "latitude": 47.6101,
                            "longitude": -122.2015
                        },
                        {
                            "cityId": "RED001",
                            "cityName": "Redmond",
                            "countryRegionId": country_region_id,
                            "countryRegionName": "United States",
                            "stateProvinceId": state_province_id,
                            "stateProvinceName": "Washington",
                            "countyId": county_id,
                            "countyName": "King County",
                            "population": 73256,
                            "timeZone": "Pacific Standard Time",
                            "isActive": True,
                            "postalCodes": ["98052", "98053", "98073"],
                            "latitude": 47.6740,
                            "longitude": -122.1215
                        },
                        {
                            "cityId": "KEN001",
                            "cityName": "Kent",
                            "countryRegionId": country_region_id,
                            "countryRegionName": "United States",
                            "stateProvinceId": state_province_id,
                            "stateProvinceName": "Washington",
                            "countyId": county_id,
                            "countyName": "King County",
                            "population": 136588,
                            "timeZone": "Pacific Standard Time",
                            "isActive": True,
                            "postalCodes": ["98030", "98031", "98032", "98042"],
                            "latitude": 47.3809,
                            "longitude": -122.2348
                        }
                    ]
                elif county_id == "PIERCE":
                    all_cities = [
                        {
                            "cityId": "TAC001",
                            "cityName": "Tacoma",
                            "countryRegionId": country_region_id,
                            "countryRegionName": "United States",
                            "stateProvinceId": state_province_id,
                            "stateProvinceName": "Washington",
                            "countyId": county_id,
                            "countyName": "Pierce County",
                            "population": 219346,
                            "timeZone": "Pacific Standard Time",
                            "isActive": True,
                            "postalCodes": ["98401", "98402", "98403", "98404", "98405"],
                            "latitude": 47.2529,
                            "longitude": -122.4443
                        }
                    ]
            else:
                # Generic mock data for other locations
                all_cities = [
                    {
                        "cityId": f"CITY_{random.randint(100, 999)}",
                        "cityName": f"Sample City {random.randint(1, 5)}",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "Sample Country",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Sample State",
                        "countyId": county_id,
                        "countyName": "Sample County",
                        "population": random.randint(10000, 500000),
                        "timeZone": "Sample Time Zone",
                        "isActive": True,
                        "postalCodes": [f"{random.randint(10000, 99999)}"],
                        "latitude": round(random.uniform(-90, 90), 4),
                        "longitude": round(random.uniform(-180, 180), 4)
                    }
                ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "cityName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["cityName", "countryRegionId", "stateProvinceId", "countyId"]:
                    all_cities.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["population"]:
                    all_cities.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_cities = all_cities[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Cities",
                "countryRegionId": country_region_id,
                "stateProvinceId": state_province_id,
                "countyId": county_id,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_cities),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_cities),
                    "hasPreviousPage": skip > 0,
                    "results": paged_cities
                },
                "cities": paged_cities,
                "totalCount": len(all_cities),
                "summary": {
                    "totalPopulation": sum(city["population"] for city in all_cities),
                    "activeCities": len([city for city in all_cities if city["isActive"]]),
                    "uniquePostalCodes": len(set([code for city in all_cities for code in city["postalCodes"]]))
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<CityInfo>",
                    "description": "Get all the cities filtered by Country/Region, State Province and County"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown cities tool: {name}"}