"""
Counties Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. counties_get_counties - Get all the counties filtered by country/region and state province

This controller handles county-related operations for address management and geographic data.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class CountiesController:
    """Controller for Counties-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of counties-related tools"""
        return [
            Tool(
                name="counties_get_counties",
                description="Get all the counties filtered by country/region and state province",
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
                    "required": ["countryRegionId", "stateProvinceId"]
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle counties tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "counties_get_counties":
            country_region_id = arguments.get("countryRegionId", "US")
            state_province_id = arguments.get("stateProvinceId", "WA")
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock counties data based on location filters
            all_counties = []
            if country_region_id == "US" and state_province_id == "WA":
                all_counties = [
                    {
                        "countyId": "KING",
                        "countyName": "King County",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "United States",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Washington",
                        "population": 2269675,
                        "area": 2307.3,  # square miles
                        "countySeat": "Seattle",
                        "isActive": True,
                        "timeZone": "Pacific Standard Time",
                        "majorCities": ["Seattle", "Bellevue", "Kent", "Renton", "Federal Way"],
                        "establishedDate": "1852-12-22T00:00:00Z"
                    },
                    {
                        "countyId": "PIERCE",
                        "countyName": "Pierce County",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "United States",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Washington",
                        "population": 904980,
                        "area": 1679.0,
                        "countySeat": "Tacoma",
                        "isActive": True,
                        "timeZone": "Pacific Standard Time",
                        "majorCities": ["Tacoma", "Lakewood", "Puyallup", "Auburn", "University Place"],
                        "establishedDate": "1852-12-22T00:00:00Z"
                    },
                    {
                        "countyId": "SNOHOMISH",
                        "countyName": "Snohomish County",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "United States",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Washington",
                        "population": 827957,
                        "area": 2087.3,
                        "countySeat": "Everett",
                        "isActive": True,
                        "timeZone": "Pacific Standard Time",
                        "majorCities": ["Everett", "Edmonds", "Lynnwood", "Mukilteo", "Mill Creek"],
                        "establishedDate": "1861-01-14T00:00:00Z"
                    },
                    {
                        "countyId": "SPOKANE",
                        "countyName": "Spokane County",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "United States",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Washington",
                        "population": 539339,
                        "area": 1764.0,
                        "countySeat": "Spokane",
                        "isActive": True,
                        "timeZone": "Pacific Standard Time",
                        "majorCities": ["Spokane", "Spokane Valley", "Cheney", "Liberty Lake"],
                        "establishedDate": "1858-01-29T00:00:00Z"
                    }
                ]
            elif country_region_id == "US" and state_province_id == "CA":
                all_counties = [
                    {
                        "countyId": "LA",
                        "countyName": "Los Angeles County",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "United States",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "California",
                        "population": 10014009,
                        "area": 4751.0,
                        "countySeat": "Los Angeles",
                        "isActive": True,
                        "timeZone": "Pacific Standard Time",
                        "majorCities": ["Los Angeles", "Long Beach", "Glendale", "Santa Clarita", "Lakewood"],
                        "establishedDate": "1850-02-18T00:00:00Z"
                    }
                ]
            else:
                # Generic mock data for other locations
                all_counties = [
                    {
                        "countyId": f"COUNTY_{random.randint(100, 999)}",
                        "countyName": f"Sample County {random.randint(1, 3)}",
                        "countryRegionId": country_region_id,
                        "countryRegionName": "Sample Country",
                        "stateProvinceId": state_province_id,
                        "stateProvinceName": "Sample State",
                        "population": random.randint(50000, 2000000),
                        "area": round(random.uniform(500.0, 3000.0), 1),
                        "countySeat": f"Sample City {random.randint(1, 5)}",
                        "isActive": True,
                        "timeZone": "Sample Time Zone",
                        "majorCities": [f"City {i}" for i in range(1, 4)],
                        "establishedDate": "1850-01-01T00:00:00Z"
                    }
                ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "countyName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["countyName", "countryRegionId", "stateProvinceId", "countySeat"]:
                    all_counties.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["population", "area"]:
                    all_counties.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_counties = all_counties[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Counties",
                "countryRegionId": country_region_id,
                "stateProvinceId": state_province_id,
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_counties),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_counties),
                    "hasPreviousPage": skip > 0,
                    "results": paged_counties
                },
                "counties": paged_counties,
                "totalCount": len(all_counties),
                "summary": {
                    "totalPopulation": sum(county["population"] for county in all_counties),
                    "totalArea": sum(county["area"] for county in all_counties),
                    "activeCounties": len([county for county in all_counties if county["isActive"]]),
                    "averagePopulation": round(sum(county["population"] for county in all_counties) / len(all_counties) if all_counties else 0, 0)
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<CountyInfo>",
                    "description": "Get all the counties filtered by country/region and state province"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown counties tool: {name}"}