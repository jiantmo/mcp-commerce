"""
Cart Controller for Dynamics 365 Commerce MCP Server

Available MCP Tools (55 total):
1. cart_checkout - Checkout the cart
2. cart_add_cart_lines - Add cart lines to cart
3. cart_void_cart_lines - Void cart lines in cart
4. cart_update_cart_lines - Update cart lines in cart
5. cart_refill_gift_card - Add balance to gift card
6. cart_issue_gift_card - Issue gift card
7. cart_cashout_gift_card - Cash out gift card
8. cart_add_tender_line - Add tender line to cart
9. cart_add_preprocessed_tender_line - Add pre-processed tender line
10. cart_validate_tender_line_for_add - Validate tender line for adding
11. cart_update_tender_line_signature - Update tender line signature
12. cart_void_tender_line - Void tender line
13. cart_suspend_with_journal - Suspend cart with journal entry
14. cart_resume - Resume suspended cart
15. cart_resume_from_receipt_id - Resume cart from receipt ID
16. cart_recall_order - Recall customer order
17. cart_add_invoiced_sales_lines_to_cart - Add invoiced sales lines to cart
18. cart_recall_quote - Recall quote
19. cart_recall_sales_invoice - Recall sales invoice
20. cart_add_order_invoice - Add order invoice to cart
21. cart_add_invoices - Add invoices to cart
22. cart_recalculate_order - Recalculate customer order
23. cart_update_commission_sales_group - Update commission sales group
24. cart_delivery_preferences - Get cart delivery preferences
25. cart_get_line_delivery_options - Get line delivery options
26. cart_get_line_delivery_options_by_channel_id - Get line delivery options by channel
27. cart_get_payments_history - Get payments history
28. cart_get_delivery_options - Get delivery options
29. cart_update_line_delivery_specifications - Update line delivery specifications
30. cart_add_charge - Add charge to cart
31. cart_override_charge - Override charge amount
32. cart_add_cart_line_charge - Add charge to cart line
33. cart_override_cart_line_charge - Override cart line charge
34. cart_update_delivery_specification - Update delivery specification
35. cart_override_cart_line_price - Override cart line price
36. cart_get_promotions - Get cart promotions
37. cart_add_discount_code - Add discount code
38. cart_remove_discount_codes - Remove discount codes
39. cart_remove_cart_lines - Remove cart lines
40. cart_search - Search carts by criteria
41. cart_get_card_payment_accept_point - Get card payment accept point
42. cart_retrieve_card_payment_accept_result - Retrieve card payment accept result
43. cart_add_coupons - Add coupons to cart
44. cart_remove_coupons - Remove coupons from cart
45. cart_get_charge_codes - Get charge codes
46. cart_get_max_loyalty_points_to_redeem_for_transaction_balance - Get max loyalty points for redemption
47. cart_get_declined_or_voided_card_receipts - Get declined/voided card receipts
48. cart_reset_all_charges - Reset all charges
49. cart_get_entity_by_key - Get cart entity by key
50. cart_create_entity - Create cart entity
51. cart_update_entity - Update cart entity
52. cart_delete_entity - Delete cart entity
53. cart_get_cart_by_id - Get cart by ID
54. cart_merge_carts - Merge multiple carts
55. cart_validate_cart - Validate cart before checkout

This controller handles comprehensive cart operations including checkout, line management,
gift cards, tender processing, delivery options, charges, promotions, coupons, and loyalty.
"""

from typing import Any, Dict, List
from datetime import datetime, timedelta
import random
import string
from mcp.types import Tool

class CartController:
    """Controller for Cart-related Dynamics 365 Commerce API operations"""
    
    def get_tools(self) -> List[Tool]:
        """Return list of all 55 cart-related tools"""
        return [
            # Core Cart Operations (1-14)
            Tool(name="cart_checkout", description="Checkout the cart", 
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "receiptEmail": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_add_cart_lines", description="Add cart lines to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_void_cart_lines", description="Void cart lines in cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_update_cart_lines", description="Update cart lines in cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_refill_gift_card", description="Add balance to gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "giftCardId", "amount"]}),
            
            Tool(name="cart_issue_gift_card", description="Issue gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "tenderTypeId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "giftCardId", "amount", "tenderTypeId"]}),
            
            Tool(name="cart_cashout_gift_card", description="Cash out gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "giftCardId", "amount"]}),
            
            Tool(name="cart_add_tender_line", description="Add tender line to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartTenderLine": {"type": "object"}, "cartVersion": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartTenderLine"]}),
            
            Tool(name="cart_add_preprocessed_tender_line", description="Add pre-processed tender line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "preprocessedTenderLine": {"type": "object"}, "cartVersion": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "preprocessedTenderLine"]}),
            
            Tool(name="cart_validate_tender_line_for_add", description="Validate tender line for adding",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLine": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "tenderLine"]}),
            
            Tool(name="cart_update_tender_line_signature", description="Update tender line signature",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLineId": {"type": "string"}, "signatureData": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "tenderLineId", "signatureData"]}),
            
            Tool(name="cart_void_tender_line", description="Void tender line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLineId": {"type": "string"}, "reasonCodeLines": {"type": "array"}, "isPreprocessed": {"type": "boolean"}, "forceVoid": {"type": "boolean"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "tenderLineId"]}),
            
            Tool(name="cart_suspend_with_journal", description="Suspend cart with journal entry",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "journalCartId": {"type": "string"}, "receiptNumberSequence": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "journalCartId", "receiptNumberSequence"]}),
            
            Tool(name="cart_resume", description="Resume suspended cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            # Extended Cart Operations (15-30)
            Tool(name="cart_resume_from_receipt_id", description="Resume cart from receipt ID",
                 inputSchema={"type": "object", "properties": {"receiptId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["receiptId"]}),
            
            Tool(name="cart_recall_order", description="Recall customer order",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "salesId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["transactionId", "salesId"]}),
            
            Tool(name="cart_add_invoiced_sales_lines_to_cart", description="Add invoiced sales lines to cart",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "invoicedLineIds": {"type": "array", "items": {"type": "number"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["transactionId", "invoicedLineIds"]}),
            
            Tool(name="cart_recall_quote", description="Recall quote",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "quoteId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["transactionId", "quoteId"]}),
            
            Tool(name="cart_recall_sales_invoice", description="Recall sales invoice",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "invoiceId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["transactionId", "invoiceId"]}),
            
            Tool(name="cart_add_order_invoice", description="Add order invoice to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "invoiceId": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "invoiceId"]}),
            
            Tool(name="cart_add_invoices", description="Add invoices to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "invoiceIds": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "invoiceIds"]}),
            
            Tool(name="cart_recalculate_order", description="Recalculate customer order",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_update_commission_sales_group", description="Update commission sales group",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "cartLineId": {"type": "string"}, "commissionSalesGroup": {"type": "string"}, "isUserInitiated": {"type": "boolean"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["transactionId", "cartLineId", "commissionSalesGroup"]}),
            
            Tool(name="cart_delivery_preferences", description="Get cart delivery preferences",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_line_delivery_options", description="Get line delivery options",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineShippingAddresses": {"type": "array"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_line_delivery_options_by_channel_id", description="Get line delivery options by channel",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineShippingAddresses": {"type": "array"}, "channelId": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "channelId"]}),
            
            Tool(name="cart_get_payments_history", description="Get payments history",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_delivery_options", description="Get delivery options",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "shippingAddress": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_update_line_delivery_specifications", description="Update line delivery specifications",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineDeliverySpecifications": {"type": "array"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "lineDeliverySpecifications"]}),
            
            # Charges & Pricing (30-35)
            Tool(name="cart_add_charge", description="Add charge to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "moduleTypeValue": {"type": "number"}, "chargeCode": {"type": "string"}, "calculatedAmount": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "moduleTypeValue", "chargeCode", "calculatedAmount"]}),
            
            Tool(name="cart_override_charge", description="Override charge amount",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "chargeLineId": {"type": "string"}, "amount": {"type": "number"}, "reasonCodeLines": {"type": "array"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "chargeLineId", "amount"]}),
            
            Tool(name="cart_add_cart_line_charge", description="Add charge to cart line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "moduleTypeValue": {"type": "number"}, "chargeCode": {"type": "string"}, "calculatedAmount": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLineId", "moduleTypeValue", "chargeCode", "calculatedAmount"]}),
            
            Tool(name="cart_override_cart_line_charge", description="Override cart line charge",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "chargeLineId": {"type": "string"}, "amount": {"type": "number"}, "reasonCodeLines": {"type": "array"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLineId", "chargeLineId", "amount"]}),
            
            Tool(name="cart_update_delivery_specification", description="Update delivery specification",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "deliverySpecification": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "deliverySpecification"]}),
            
            Tool(name="cart_override_cart_line_price", description="Override cart line price",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "price": {"type": "number"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLineId", "price"]}),
            
            # Promotions & Discounts (36-40)
            Tool(name="cart_get_promotions", description="Get cart promotions",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_add_discount_code", description="Add discount code",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "discountCode": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "discountCode"]}),
            
            Tool(name="cart_remove_discount_codes", description="Remove discount codes",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "discountCodes": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "discountCodes"]}),
            
            Tool(name="cart_remove_cart_lines", description="Remove cart lines",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineIds": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartLineIds"]}),
            
            Tool(name="cart_search", description="Search carts by criteria",
                 inputSchema={"type": "object", "properties": {"cartSearchCriteria": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartSearchCriteria"]}),
            
            # Payment Processing (41-42)
            Tool(name="cart_get_card_payment_accept_point", description="Get card payment accept point",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cardPaymentAcceptSettings": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cardPaymentAcceptSettings"]}),
            
            Tool(name="cart_retrieve_card_payment_accept_result", description="Retrieve card payment accept result",
                 inputSchema={"type": "object", "properties": {"resultAccessCode": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["resultAccessCode"]}),
            
            # Coupons (43-44)
            Tool(name="cart_add_coupons", description="Add coupons to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "couponCodes": {"type": "array", "items": {"type": "string"}}, "isLegacyDiscountCode": {"type": "boolean"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "couponCodes"]}),
            
            Tool(name="cart_remove_coupons", description="Remove coupons from cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "couponCodes": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "couponCodes"]}),
            
            # Additional Operations (45-48)
            Tool(name="cart_get_charge_codes", description="Get charge codes",
                 inputSchema={"type": "object", "properties": {"baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": []}),
            
            Tool(name="cart_get_max_loyalty_points_to_redeem_for_transaction_balance", description="Get max loyalty points for redemption",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "loyaltyCardNumber": {"type": "string"}, "redeemCurrency": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "loyaltyCardNumber", "redeemCurrency"]}),
            
            Tool(name="cart_get_declined_or_voided_card_receipts", description="Get declined/voided card receipts",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "preprocessedTenderLine": {"type": "object"}, "criteria": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "preprocessedTenderLine", "criteria"]}),
            
            Tool(name="cart_reset_all_charges", description="Reset all charges",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            # Entity Operations (49-55)
            Tool(name="cart_get_entity_by_key", description="Get cart entity by key",
                 inputSchema={"type": "object", "properties": {"entityKey": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["entityKey"]}),
            
            Tool(name="cart_create_entity", description="Create cart entity",
                 inputSchema={"type": "object", "properties": {"cartEntity": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartEntity"]}),
            
            Tool(name="cart_update_entity", description="Update cart entity",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartEntity": {"type": "object"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId", "cartEntity"]}),
            
            Tool(name="cart_delete_entity", description="Delete cart entity",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_cart_by_id", description="Get cart by ID",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]}),
            
            Tool(name="cart_merge_carts", description="Merge multiple carts",
                 inputSchema={"type": "object", "properties": {"primaryCartId": {"type": "string"}, "cartIdsToMerge": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["primaryCartId", "cartIdsToMerge"]}),
            
            Tool(name="cart_validate_cart", description="Validate cart before checkout",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "validationRules": {"type": "array"}, "baseUrl": {"type": "string", "default": "https://your-commerce-site.com"}}, "required": ["cartId"]})
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle cart tool calls with mock implementations"""
        base_url = arguments.get("baseUrl", "https://your-commerce-site.com")
        cart_id = arguments.get("cartId", "CART001")
        
        # Mock implementation for all 55 tools
        return {
            "api": f"MOCK {base_url}/api/CommerceRuntime/Carts/{name}",
            "toolName": name,
            "cartId": cart_id,
            "arguments": arguments,
            "status": "success",
            "timestamp": datetime.now().isoformat() + "Z",
            "message": f"Mock response for {name} - Complete with realistic cart data",
            "mockData": self._generate_mock_cart_response(name, arguments)
        }
    
    def _generate_mock_cart_response(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Generate appropriate mock response data based on the tool name"""
        if "checkout" in name:
            return {"orderId": f"ORDER_{random.randint(1000, 9999)}", "total": 125.99, "status": "Completed"}
        elif "gift_card" in name:
            return {"cardNumber": f"GC{random.randint(1000000000, 9999999999)}", "balance": 100.00}
        elif "delivery" in name:
            return {"deliveryOptions": [{"method": "Standard", "cost": 5.99, "days": "3-5"}]}
        elif "promotion" in name:
            return {"availablePromotions": [{"code": "SAVE10", "description": "10% off", "discount": 12.60}]}
        elif "charge" in name:
            return {"chargeId": f"CHG_{random.randint(100, 999)}", "amount": 2.99, "description": "Processing fee"}
        elif "loyalty" in name:
            return {"maxPointsRedeemable": 1000, "currencyValue": 50.00}
        elif "entity" in name:
            return {"entityId": f"ENT_{random.randint(1000, 9999)}", "created": datetime.now().isoformat() + "Z"}
        elif "merge" in name:
            return {"mergedCartId": arguments.get("primaryCartId", "CART001"), "itemsMerged": random.randint(5, 15)}
        elif "validate" in name:
            return {"valid": True, "validationResults": [{"rule": "MinOrderAmount", "passed": True}]}
        else:
            return {"result": "Success", "timestamp": datetime.now().isoformat() + "Z"}