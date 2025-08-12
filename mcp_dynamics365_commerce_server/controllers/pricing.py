"""
Pricing Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (2 total):
1. pricing_calculate_sales_document - Calculates prices and discounts for products at given quantities if they are bought together in an order
2. pricing_get_price_groups - Get price groups for customer segments

This controller handles pricing calculations and discount applications.
"""

from typing import Any, Dict, List
from datetime import datetime
import random
from mcp.types import Tool
from ..config import get_base_url

class PricingController:
    """Controller for Pricing-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of pricing-related tools"""
        return [
            Tool(
                name="pricing_calculate_sales_document",
                description="Calculates prices and discounts for products at given quantities if they are bought together in an order",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "salesDocument": {
                            "type": "object",
                            "description": "Cart/sales document with products to calculate pricing for",
                            "properties": {
                                "cartId": {"type": "string"},
                                "customerId": {"type": "string"},
                                "cartLines": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "productId": {"type": "string"},
                                            "quantity": {"type": "number"},
                                            "unitPrice": {"type": "number"}
                                        }
                                    }
                                },
                                "discountCodes": {"type": "array", "items": {"type": "string"}},
                                "loyaltyCardId": {"type": "string"}
                            }
                        },
                        "baseUrl": {
                            "type": "string",
                            "description": "Base URL of the Dynamics 365 Commerce site",
                            "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"
                        }
                    },
                    "required": ["salesDocument"]
                }
            ),
            Tool(
                name="pricing_get_price_groups",
                description="Get price groups for customer segments",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "customerId": {"type": "string"},
                        "baseUrl": {"type": "string", "default": "https://sculxdon4av67499847-rs.su.retail.test.dynamics.com"}
                    }
                }
            )
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle pricing tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        if name == "pricing_calculate_sales_document":
            sales_document = arguments.get("salesDocument", {})
            cart_id = sales_document.get("cartId", "CART001")
            customer_id = sales_document.get("customerId", "CUST001")
            cart_lines = sales_document.get("cartLines", [])
            discount_codes = sales_document.get("discountCodes", [])
            loyalty_card_id = sales_document.get("loyaltyCardId")
            
            # Calculate pricing for each line
            calculated_lines = []
            subtotal = 0.0
            total_discount = 0.0
            
            for line in cart_lines:
                product_id = line.get("productId", f"PROD_{random.randint(1000, 9999)}")
                quantity = line.get("quantity", 1)
                unit_price = line.get("unitPrice", random.uniform(10.0, 200.0))
                
                # Apply quantity-based discounts
                line_discount_percent = 0.0
                if quantity >= 5:
                    line_discount_percent = 0.10  # 10% bulk discount
                elif quantity >= 3:
                    line_discount_percent = 0.05  # 5% bulk discount
                
                # Calculate line totals
                line_subtotal = unit_price * quantity
                line_discount = line_subtotal * line_discount_percent
                line_total = line_subtotal - line_discount
                
                calculated_lines.append({
                    "lineId": f"LINE_{len(calculated_lines) + 1}",
                    "productId": product_id,
                    "productName": f"Product {product_id[-4:]}",
                    "quantity": quantity,
                    "unitPrice": round(unit_price, 2),
                    "originalUnitPrice": round(unit_price, 2),
                    "lineSubtotal": round(line_subtotal, 2),
                    "lineDiscount": round(line_discount, 2),
                    "lineDiscountPercent": line_discount_percent,
                    "lineTotal": round(line_total, 2),
                    "discounts": [
                        {
                            "discountId": "BULK_DISCOUNT",
                            "discountName": f"Bulk Discount ({int(line_discount_percent * 100)}%)",
                            "discountAmount": round(line_discount, 2),
                            "discountType": "Quantity"
                        }
                    ] if line_discount > 0 else [],
                    "taxAmount": round(line_total * 0.08, 2),  # 8% tax
                    "lineTotalWithTax": round(line_total * 1.08, 2)
                })
                
                subtotal += line_total
                total_discount += line_discount
            
            # Apply cart-level discounts
            cart_discount = 0.0
            applied_discount_codes = []
            
            for discount_code in discount_codes:
                if discount_code == "SAVE10":
                    cart_discount += subtotal * 0.10
                    applied_discount_codes.append({
                        "discountCode": discount_code,
                        "discountName": "Save 10%",
                        "discountAmount": round(subtotal * 0.10, 2),
                        "discountType": "Percentage"
                    })
                elif discount_code == "SAVE20":
                    cart_discount += 20.00
                    applied_discount_codes.append({
                        "discountCode": discount_code,
                        "discountName": "Save $20",
                        "discountAmount": 20.00,
                        "discountType": "FixedAmount"
                    })
            
            # Apply loyalty discounts
            loyalty_discount = 0.0
            loyalty_points_used = 0
            if loyalty_card_id:
                # Mock loyalty discount calculation
                loyalty_discount = min(subtotal * 0.05, 50.00)  # Max $50 loyalty discount
                loyalty_points_used = int(loyalty_discount * 100)  # 100 points per dollar
            
            # Calculate final totals
            total_discount += cart_discount + loyalty_discount
            net_total = subtotal - total_discount
            tax_amount = net_total * 0.08  # 8% tax rate
            final_total = net_total + tax_amount
            
            return {
                "api": f"POST {base_url}/api/CommerceRuntime/Pricing/CalculateSalesDocument",
                "calculatedCart": {
                    "cartId": cart_id,
                    "customerId": customer_id,
                    "calculationDate": datetime.now().isoformat() + "Z",
                    "cartLines": calculated_lines,
                    "pricingSummary": {
                        "subtotal": round(subtotal, 2),
                        "totalDiscount": round(total_discount, 2),
                        "netTotal": round(net_total, 2),
                        "taxAmount": round(tax_amount, 2),
                        "finalTotal": round(final_total, 2),
                        "totalSavings": round(total_discount, 2),
                        "savingsPercent": round((total_discount / (subtotal + total_discount)) * 100, 1) if subtotal + total_discount > 0 else 0
                    },
                    "appliedDiscounts": {
                        "lineDiscounts": sum(len(line.get("discounts", [])) for line in calculated_lines),
                        "cartDiscounts": applied_discount_codes,
                        "loyaltyDiscount": {
                            "loyaltyCardId": loyalty_card_id,
                            "discountAmount": round(loyalty_discount, 2),
                            "pointsUsed": loyalty_points_used
                        } if loyalty_card_id else None
                    },
                    "taxCalculation": {
                        "taxRate": 0.08,
                        "taxableAmount": round(net_total, 2),
                        "taxAmount": round(tax_amount, 2),
                        "taxExempt": False
                    },
                    "promotions": [
                        {
                            "promotionId": "BULK_PROMO",
                            "promotionName": "Bulk Purchase Promotion",
                            "description": "Save more when you buy more",
                            "isActive": True,
                            "priority": 1
                        }
                    ],
                    "calculationFlags": {
                        "pricesCalculated": True,
                        "discountsApplied": True,
                        "taxCalculated": True,
                        "loyaltyApplied": loyalty_card_id is not None,
                        "promotionsEvaluated": True
                    }
                },
                "metadata": {
                    "supportedRoles": ["Employee", "Customer", "Anonymous", "Application"],
                    "returnType": "Cart",
                    "description": "Calculates prices and discounts for products at given quantities if they are bought together in an order"
                },
                "timestamp": datetime.now().isoformat() + "Z",
                "status": "success"
            }
        
        elif name == "pricing_get_price_groups":
            return {
                "api": f"GET {base_url}/api/CommerceRuntime/Pricing/PriceGroups",
                "priceGroups": [
                    {"id": "RETAIL", "name": "Retail", "discount": 0.0},
                    {"id": "VIP", "name": "VIP", "discount": 0.15},
                    {"id": "WHOLESALE", "name": "Wholesale", "discount": 0.25}
                ]
            }
        else:
            return {"error": f"Unknown pricing tool: {name}"}