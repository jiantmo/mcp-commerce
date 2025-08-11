"""
Language Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (1 total):
1. language_get_languages - Gets collection of supported languages

This controller handles language operations for internationalization and localization.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool

class LanguageController:
    """Controller for Language-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of language-related tools"""
        return [
            Tool(
                name="language_get_languages",
                description="Gets collection of supported languages",
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
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle language tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        
        if name == "language_get_languages":
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            sorting = query_settings.get("sorting", {"columns": []})
            
            # Mock supported languages data
            all_languages = [
                {
                    "languageId": "en-US",
                    "languageName": "English (United States)",
                    "nativeName": "English",
                    "cultureCode": "en-US",
                    "countryRegion": "US",
                    "countryRegionName": "United States",
                    "isActive": True,
                    "isDefault": True,
                    "isRightToLeft": False,
                    "currencyCode": "USD",
                    "currencySymbol": "$",
                    "dateFormat": "MM/dd/yyyy",
                    "timeFormat": "h:mm:ss tt",
                    "numberFormat": "#,##0.00",
                    "completenessPercent": 100.0,
                    "lastUpdated": "2024-01-01T00:00:00Z",
                    "translators": ["Microsoft Localization Team"],
                    "supportLevel": "Full"
                },
                {
                    "languageId": "es-US",
                    "languageName": "Spanish (United States)",
                    "nativeName": "Español (Estados Unidos)",
                    "cultureCode": "es-US",
                    "countryRegion": "US",
                    "countryRegionName": "United States",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "USD",
                    "currencySymbol": "$",
                    "dateFormat": "dd/MM/yyyy",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "#.##0,00",
                    "completenessPercent": 95.5,
                    "lastUpdated": "2024-01-15T00:00:00Z",
                    "translators": ["Microsoft Localization Team", "Regional Partners"],
                    "supportLevel": "Full"
                },
                {
                    "languageId": "fr-CA",
                    "languageName": "French (Canada)",
                    "nativeName": "Français (Canada)",
                    "cultureCode": "fr-CA",
                    "countryRegion": "CA",
                    "countryRegionName": "Canada",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "CAD",
                    "currencySymbol": "$",
                    "dateFormat": "yyyy-MM-dd",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "# ##0,00",
                    "completenessPercent": 92.3,
                    "lastUpdated": "2024-01-10T00:00:00Z",
                    "translators": ["Microsoft Localization Team"],
                    "supportLevel": "Full"
                },
                {
                    "languageId": "de-DE",
                    "languageName": "German (Germany)",
                    "nativeName": "Deutsch (Deutschland)",
                    "cultureCode": "de-DE",
                    "countryRegion": "DE",
                    "countryRegionName": "Germany",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "EUR",
                    "currencySymbol": "€",
                    "dateFormat": "dd.MM.yyyy",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "#.##0,00",
                    "completenessPercent": 88.7,
                    "lastUpdated": "2024-01-05T00:00:00Z",
                    "translators": ["Microsoft Localization Team", "German Language Partners"],
                    "supportLevel": "Partial"
                },
                {
                    "languageId": "ja-JP",
                    "languageName": "Japanese (Japan)",
                    "nativeName": "Japanese (Japan)",
                    "cultureCode": "ja-JP",
                    "countryRegion": "JP",
                    "countryRegionName": "Japan",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "JPY",
                    "currencySymbol": "¥",
                    "dateFormat": "yyyy/MM/dd",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "#,##0",
                    "completenessPercent": 85.2,
                    "lastUpdated": "2023-12-20T00:00:00Z",
                    "translators": ["Microsoft Japan", "Localization Partners"],
                    "supportLevel": "Partial"
                },
                {
                    "languageId": "zh-CN",
                    "languageName": "Chinese (Simplified, China)",
                    "nativeName": "Chinese (Simplified, China)",
                    "cultureCode": "zh-CN",
                    "countryRegion": "CN",
                    "countryRegionName": "China",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "CNY",
                    "currencySymbol": "¥",
                    "dateFormat": "yyyy/M/d",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "#,##0.00",
                    "completenessPercent": 82.1,
                    "lastUpdated": "2023-12-15T00:00:00Z",
                    "translators": ["Microsoft China", "Regional Partners"],
                    "supportLevel": "Partial"
                },
                {
                    "languageId": "ar-SA",
                    "languageName": "Arabic (Saudi Arabia)",
                    "nativeName": "العربية (المملكة العربية السعودية)",
                    "cultureCode": "ar-SA",
                    "countryRegion": "SA",
                    "countryRegionName": "Saudi Arabia",
                    "isActive": False,
                    "isDefault": False,
                    "isRightToLeft": True,
                    "currencyCode": "SAR",
                    "currencySymbol": "ريال",
                    "dateFormat": "dd/MM/yyyy",
                    "timeFormat": "hh:mm:ss tt",
                    "numberFormat": "#,##0.00",
                    "completenessPercent": 65.4,
                    "lastUpdated": "2023-11-30T00:00:00Z",
                    "translators": ["Microsoft Middle East", "Arabic Language Specialists"],
                    "supportLevel": "Basic",
                    "status": "In Development"
                },
                {
                    "languageId": "pt-BR",
                    "languageName": "Portuguese (Brazil)",
                    "nativeName": "Português (Brasil)",
                    "cultureCode": "pt-BR",
                    "countryRegion": "BR",
                    "countryRegionName": "Brazil",
                    "isActive": True,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "BRL",
                    "currencySymbol": "R$",
                    "dateFormat": "dd/MM/yyyy",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "#.##0,00",
                    "completenessPercent": 78.9,
                    "lastUpdated": "2024-01-08T00:00:00Z",
                    "translators": ["Microsoft Brazil", "Portuguese Language Team"],
                    "supportLevel": "Partial"
                },
                {
                    "languageId": "ru-RU",
                    "languageName": "Russian (Russia)",
                    "nativeName": "русский (Россия)",
                    "cultureCode": "ru-RU",
                    "countryRegion": "RU",
                    "countryRegionName": "Russia",
                    "isActive": False,
                    "isDefault": False,
                    "isRightToLeft": False,
                    "currencyCode": "RUB",
                    "currencySymbol": "₽",
                    "dateFormat": "dd.MM.yyyy",
                    "timeFormat": "HH:mm:ss",
                    "numberFormat": "# ##0,00",
                    "completenessPercent": 71.3,
                    "lastUpdated": "2023-10-15T00:00:00Z",
                    "translators": ["Regional Partners"],
                    "supportLevel": "Basic",
                    "status": "Limited Support"
                }
            ]
            
            # Apply sorting if specified
            if sorting.get("columns"):
                sort_column = sorting["columns"][0]
                column_name = sort_column.get("columnName", "languageName")
                is_descending = sort_column.get("isDescending", False)
                
                if column_name in ["languageName", "languageId", "nativeName", "countryRegionName"]:
                    all_languages.sort(key=lambda x: x.get(column_name, ""), reverse=is_descending)
                elif column_name in ["completenessPercent"]:
                    all_languages.sort(key=lambda x: x.get(column_name, 0), reverse=is_descending)
                elif column_name in ["isActive", "isDefault", "isRightToLeft"]:
                    all_languages.sort(key=lambda x: x.get(column_name, False), reverse=is_descending)
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_languages = all_languages[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Languages",
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(all_languages),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(all_languages),
                    "hasPreviousPage": skip > 0,
                    "results": paged_languages
                },
                "supportedLanguages": paged_languages,
                "totalCount": len(all_languages),
                "summary": {
                    "activeLanguages": len([lang for lang in all_languages if lang["isActive"]]),
                    "inactiveLanguages": len([lang for lang in all_languages if not lang["isActive"]]),
                    "defaultLanguage": next((lang for lang in all_languages if lang.get("isDefault", False)), None),
                    "rightToLeftLanguages": len([lang for lang in all_languages if lang.get("isRightToLeft", False)]),
                    "averageCompleteness": round(sum(lang["completenessPercent"] for lang in all_languages) / len(all_languages), 1),
                    "supportLevels": {
                        "Full": len([lang for lang in all_languages if lang.get("supportLevel") == "Full"]),
                        "Partial": len([lang for lang in all_languages if lang.get("supportLevel") == "Partial"]),
                        "Basic": len([lang for lang in all_languages if lang.get("supportLevel") == "Basic"])
                    }
                },
                "regions": {
                    "northAmerica": ["en-US", "es-US", "fr-CA"],
                    "europe": ["de-DE", "ru-RU"],
                    "asia": ["ja-JP", "zh-CN"],
                    "middleEast": ["ar-SA"],
                    "southAmerica": ["pt-BR"]
                },
                "localizationInfo": {
                    "translationTeams": len(set([translator for lang in all_languages for translator in lang.get("translators", [])])),
                    "lastGlobalUpdate": max([lang["lastUpdated"] for lang in all_languages]),
                    "nextScheduledReview": (datetime.now().replace(month=datetime.now().month + 3, day=1)).isoformat() + "Z",
                    "translationTools": ["Microsoft Translator", "Community Contributions", "Professional Services"]
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<SupportedLanguage>",
                    "description": "Gets collection of supported languages"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown language tool: {name}"}