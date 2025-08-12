"""
Currency Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (2 total):
1. currency_get_currencies_amount - Gets the currencies amount
2. currency_calculate_total_currency_amount - Calculates the total currency amount

This controller handles currency operations including currency conversion and calculations.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class CurrencyController:
    """Controller for Currency-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of currency-related tools"""
        return [
            Tool(
                name="currency_get_currencies_amount",
                description="Gets the currencies amount",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "currencyCode": {
                            "type": "string",
                            "description": "Currency code (e.g., USD, EUR, GBP)"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to get currency information for"
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
                    "required": ["currencyCode", "amount"]
                }
            ),
            Tool(
                name="currency_calculate_total_currency_amount",
                description="Calculates the total currency amount",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "currenciesAmount": {
                            "type": "array",
                            "description": "Array of currency request objects",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "currencyCode": {"type": "string"},
                                    "amount": {"type": "number"},
                                    "exchangeRate": {"type": "number"}
                                },
                                "required": ["currencyCode", "amount"]
                            }
                        },
                        "baseCurrencyCode": {
                            "type": "string",
                            "description": "Base currency code for calculation",
                            "default": "USD"
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["currenciesAmount"]
                }
            )
        ]
    
    def _get_exchange_rates(self) -> Dict[str, float]:
        """Get mock exchange rates (base USD)"""
        return {
            "USD": 1.0,
            "EUR": 0.85,
            "GBP": 0.73,
            "CAD": 1.35,
            "JPY": 110.0,
            "AUD": 1.45,
            "CHF": 0.92,
            "CNY": 6.45,
            "SEK": 8.85,
            "NOK": 8.95,
            "DKK": 6.35,
            "PLN": 3.95,
            "CZK": 21.5,
            "HUF": 305.0,
            "RUB": 75.0,
            "BRL": 5.25,
            "MXN": 20.5,
            "INR": 74.0,
            "KRW": 1185.0,
            "SGD": 1.35
        }
    
    def _get_currency_info(self, currency_code: str) -> Dict[str, Any]:
        """Get currency information"""
        currency_info = {
            "USD": {"name": "US Dollar", "symbol": "$", "decimals": 2, "country": "United States"},
            "EUR": {"name": "Euro", "symbol": "€", "decimals": 2, "country": "European Union"},
            "GBP": {"name": "British Pound", "symbol": "£", "decimals": 2, "country": "United Kingdom"},
            "CAD": {"name": "Canadian Dollar", "symbol": "C$", "decimals": 2, "country": "Canada"},
            "JPY": {"name": "Japanese Yen", "symbol": "¥", "decimals": 0, "country": "Japan"},
            "AUD": {"name": "Australian Dollar", "symbol": "A$", "decimals": 2, "country": "Australia"},
            "CHF": {"name": "Swiss Franc", "symbol": "CHF", "decimals": 2, "country": "Switzerland"},
            "CNY": {"name": "Chinese Yuan", "symbol": "¥", "decimals": 2, "country": "China"},
            "SEK": {"name": "Swedish Krona", "symbol": "kr", "decimals": 2, "country": "Sweden"},
            "NOK": {"name": "Norwegian Krone", "symbol": "kr", "decimals": 2, "country": "Norway"}
        }
        return currency_info.get(currency_code, {"name": f"Unknown ({currency_code})", "symbol": currency_code, "decimals": 2, "country": "Unknown"})
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle currency tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "currency_get_currencies_amount":
            currency_code = arguments.get("currencyCode", "USD")
            amount = arguments.get("amount", 100.0)
            query_settings = arguments.get("queryResultSettings", {})
            paging = query_settings.get("paging", {"skip": 0, "top": 50})
            
            exchange_rates = self._get_exchange_rates()
            base_currency_info = self._get_currency_info(currency_code)
            
            # Generate currency amounts in different denominations
            currency_amounts = []
            
            if currency_code == "USD":
                # Generate USD denominations
                denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
                for denom in denominations:
                    if amount >= denom:
                        count = int(amount // denom)
                        if count > 0:
                            currency_amounts.append({
                                "denomination": denom,
                                "denominationName": f"${denom:.2f}" if denom >= 1 else f"{int(denom * 100)}¢",
                                "denominationType": "Bill" if denom >= 1 else "Coin",
                                "count": count,
                                "totalValue": round(count * denom, 2),
                                "currencyCode": currency_code,
                                "currencySymbol": base_currency_info["symbol"]
                            })
                            amount -= count * denom
                            amount = round(amount, 2)
            else:
                # For other currencies, create example denominations
                largest_denom = 100
                while largest_denom > 0.01 and amount > 0:
                    if amount >= largest_denom:
                        count = int(amount // largest_denom)
                        currency_amounts.append({
                            "denomination": largest_denom,
                            "denominationName": f"{base_currency_info['symbol']}{largest_denom:.2f}",
                            "denominationType": "Bill" if largest_denom >= 1 else "Coin",
                            "count": count,
                            "totalValue": round(count * largest_denom, 2),
                            "currencyCode": currency_code,
                            "currencySymbol": base_currency_info["symbol"]
                        })
                        amount -= count * largest_denom
                        amount = round(amount, 2)
                    
                    # Move to next denomination
                    if largest_denom >= 50:
                        largest_denom = 20
                    elif largest_denom >= 20:
                        largest_denom = 10
                    elif largest_denom >= 10:
                        largest_denom = 5
                    elif largest_denom >= 5:
                        largest_denom = 1
                    elif largest_denom >= 1:
                        largest_denom = 0.50
                    elif largest_denom >= 0.50:
                        largest_denom = 0.25
                    elif largest_denom >= 0.25:
                        largest_denom = 0.10
                    elif largest_denom >= 0.10:
                        largest_denom = 0.05
                    else:
                        largest_denom = 0.01
            
            # Apply paging
            skip = paging.get("skip", 0)
            top = paging.get("top", 50)
            paged_amounts = currency_amounts[skip:skip + top]
            
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Currencies/Amount",
                "currencyCode": currency_code,
                "originalAmount": arguments.get("amount", 100.0),
                "queryResultSettings": query_settings,
                "pagedResult": {
                    "totalRecordsCount": len(currency_amounts),
                    "skip": skip,
                    "top": top,
                    "hasNextPage": skip + top < len(currency_amounts),
                    "hasPreviousPage": skip > 0,
                    "results": paged_amounts
                },
                "currencyAmounts": paged_amounts,
                "currencyInfo": {
                    **base_currency_info,
                    "currencyCode": currency_code,
                    "exchangeRateToUSD": exchange_rates.get(currency_code, 1.0),
                    "isBaseCurrency": currency_code == "USD",
                    "lastUpdated": datetime.now().isoformat() + "Z"
                },
                "summary": {
                    "totalDenominations": len(currency_amounts),
                    "totalValue": sum(ca["totalValue"] for ca in currency_amounts),
                    "largestDenomination": max(ca["denomination"] for ca in currency_amounts) if currency_amounts else 0,
                    "smallestDenomination": min(ca["denomination"] for ca in currency_amounts) if currency_amounts else 0
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "PageResult<CurrencyAmount>",
                    "description": "Gets the currencies amount"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "currency_calculate_total_currency_amount":
            currencies_amount = arguments.get("currenciesAmount", [])
            base_currency_code = arguments.get("baseCurrencyCode", "USD")
            
            exchange_rates = self._get_exchange_rates()
            base_currency_info = self._get_currency_info(base_currency_code)
            
            calculation_results = []
            total_in_base_currency = 0.0
            
            for currency_request in currencies_amount:
                currency_code = currency_request.get("currencyCode", "USD")
                amount = currency_request.get("amount", 0.0)
                provided_exchange_rate = currency_request.get("exchangeRate")
                
                # Use provided exchange rate or lookup current rate
                exchange_rate = provided_exchange_rate if provided_exchange_rate else exchange_rates.get(currency_code, 1.0)
                
                # Convert to base currency
                if currency_code == base_currency_code:
                    converted_amount = amount
                else:
                    # Convert from currency to USD, then to base currency
                    usd_amount = amount / exchange_rates.get(currency_code, 1.0)
                    converted_amount = usd_amount * exchange_rates.get(base_currency_code, 1.0)
                
                currency_info = self._get_currency_info(currency_code)
                
                calculation_results.append({
                    "originalCurrencyCode": currency_code,
                    "originalAmount": amount,
                    "originalCurrencyName": currency_info["name"],
                    "originalCurrencySymbol": currency_info["symbol"],
                    "exchangeRate": exchange_rate,
                    "exchangeRateSource": "provided" if provided_exchange_rate else "system",
                    "convertedAmount": round(converted_amount, 2),
                    "baseCurrencyCode": base_currency_code,
                    "baseCurrencySymbol": base_currency_info["symbol"],
                    "calculationDate": datetime.now().isoformat() + "Z"
                })
                
                total_in_base_currency += converted_amount
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Currencies/CalculateTotal",
                "baseCurrencyCode": base_currency_code,
                "baseCurrencyInfo": base_currency_info,
                "totalAmount": {
                    "amount": round(total_in_base_currency, 2),
                    "currencyCode": base_currency_code,
                    "currencySymbol": base_currency_info["symbol"],
                    "formattedAmount": f"{base_currency_info['symbol']}{total_in_base_currency:.2f}"
                },
                "currencyCalculations": calculation_results,
                "calculationSummary": {
                    "totalCurrencies": len(currencies_amount),
                    "uniqueCurrencies": len(set(cr.get("currencyCode") for cr in currencies_amount)),
                    "originalTotalByCurrency": {
                        cr.get("currencyCode", "USD"): sum(
                            c.get("amount", 0) for c in currencies_amount 
                            if c.get("currencyCode") == cr.get("currencyCode")
                        )
                        for cr in currencies_amount
                    },
                    "totalInBaseCurrency": round(total_in_base_currency, 2),
                    "calculationDate": datetime.now().isoformat() + "Z"
                },
                "exchangeRates": {
                    code: rate for code, rate in exchange_rates.items() 
                    if any(cr.get("currencyCode") == code for cr in currencies_amount)
                },
                "metadata": {
                    "supportedRoles": ["Employee"],
                    "returnType": "CurrencyAmount",
                    "description": "Calculates the total currency amount"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        else:
            return {"error": f"Unknown currency tool: {name}"}