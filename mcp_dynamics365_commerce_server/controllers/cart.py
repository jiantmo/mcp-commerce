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
from ..database import get_database
from ..config import get_base_url

class CartController:
    """Controller for Cart-related Dynamics 365 Commerce API operations"""
    
    def __init__(self):
        self.db = get_database()
    
    def get_tools(self) -> List[Tool]:
        """Return list of all 55 cart-related tools"""
        return [
            # Core Cart Operations (1-14)
            Tool(name="cart_checkout", description="Checkout the cart", 
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "receiptEmail": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_add_cart_lines", description="Add cart lines to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_void_cart_lines", description="Void cart lines in cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_update_cart_lines", description="Update cart lines in cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLines": {"type": "array", "items": {"type": "object"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLines"]}),
            
            Tool(name="cart_refill_gift_card", description="Add balance to gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "giftCardId", "amount"]}),
            
            Tool(name="cart_issue_gift_card", description="Issue gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "tenderTypeId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "giftCardId", "amount", "tenderTypeId"]}),
            
            Tool(name="cart_cashout_gift_card", description="Cash out gift card",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "giftCardId": {"type": "string"}, "amount": {"type": "number"}, "currencyCode": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "giftCardId", "amount"]}),
            
            Tool(name="cart_add_tender_line", description="Add tender line to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartTenderLine": {"type": "object"}, "cartVersion": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartTenderLine"]}),
            
            Tool(name="cart_add_preprocessed_tender_line", description="Add pre-processed tender line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "preprocessedTenderLine": {"type": "object"}, "cartVersion": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "preprocessedTenderLine"]}),
            
            Tool(name="cart_validate_tender_line_for_add", description="Validate tender line for adding",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLine": {"type": "object"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "tenderLine"]}),
            
            Tool(name="cart_update_tender_line_signature", description="Update tender line signature",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLineId": {"type": "string"}, "signatureData": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "tenderLineId", "signatureData"]}),
            
            Tool(name="cart_void_tender_line", description="Void tender line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "tenderLineId": {"type": "string"}, "reasonCodeLines": {"type": "array"}, "isPreprocessed": {"type": "boolean"}, "forceVoid": {"type": "boolean"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "tenderLineId"]}),
            
            Tool(name="cart_suspend_with_journal", description="Suspend cart with journal entry",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "journalCartId": {"type": "string"}, "receiptNumberSequence": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "journalCartId", "receiptNumberSequence"]}),
            
            Tool(name="cart_resume", description="Resume suspended cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            # Extended Cart Operations (15-30)
            Tool(name="cart_resume_from_receipt_id", description="Resume cart from receipt ID",
                 inputSchema={"type": "object", "properties": {"receiptId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["receiptId"]}),
            
            Tool(name="cart_recall_order", description="Recall customer order",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "salesId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["transactionId", "salesId"]}),
            
            Tool(name="cart_add_invoiced_sales_lines_to_cart", description="Add invoiced sales lines to cart",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "invoicedLineIds": {"type": "array", "items": {"type": "number"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["transactionId", "invoicedLineIds"]}),
            
            Tool(name="cart_recall_quote", description="Recall quote",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "quoteId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["transactionId", "quoteId"]}),
            
            Tool(name="cart_recall_sales_invoice", description="Recall sales invoice",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "invoiceId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["transactionId", "invoiceId"]}),
            
            Tool(name="cart_add_order_invoice", description="Add order invoice to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "invoiceId": {"type": "string"}, "lineDescription": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "invoiceId"]}),
            
            Tool(name="cart_add_invoices", description="Add invoices to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "invoiceIds": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "invoiceIds"]}),
            
            Tool(name="cart_recalculate_order", description="Recalculate customer order",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_update_commission_sales_group", description="Update commission sales group",
                 inputSchema={"type": "object", "properties": {"transactionId": {"type": "string"}, "cartLineId": {"type": "string"}, "commissionSalesGroup": {"type": "string"}, "isUserInitiated": {"type": "boolean"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["transactionId", "cartLineId", "commissionSalesGroup"]}),
            
            Tool(name="cart_delivery_preferences", description="Get cart delivery preferences",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_line_delivery_options", description="Get line delivery options",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineShippingAddresses": {"type": "array"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_line_delivery_options_by_channel_id", description="Get line delivery options by channel",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineShippingAddresses": {"type": "array"}, "channelId": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "channelId"]}),
            
            Tool(name="cart_get_payments_history", description="Get payments history",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_delivery_options", description="Get delivery options",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "shippingAddress": {"type": "object"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_update_line_delivery_specifications", description="Update line delivery specifications",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "lineDeliverySpecifications": {"type": "array"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "lineDeliverySpecifications"]}),
            
            # Charges & Pricing (30-35)
            Tool(name="cart_add_charge", description="Add charge to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "moduleTypeValue": {"type": "number"}, "chargeCode": {"type": "string"}, "calculatedAmount": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "moduleTypeValue", "chargeCode", "calculatedAmount"]}),
            
            Tool(name="cart_override_charge", description="Override charge amount",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "chargeLineId": {"type": "string"}, "amount": {"type": "number"}, "reasonCodeLines": {"type": "array"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "chargeLineId", "amount"]}),
            
            Tool(name="cart_add_cart_line_charge", description="Add charge to cart line",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "moduleTypeValue": {"type": "number"}, "chargeCode": {"type": "string"}, "calculatedAmount": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLineId", "moduleTypeValue", "chargeCode", "calculatedAmount"]}),
            
            Tool(name="cart_override_cart_line_charge", description="Override cart line charge",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "chargeLineId": {"type": "string"}, "amount": {"type": "number"}, "reasonCodeLines": {"type": "array"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLineId", "chargeLineId", "amount"]}),
            
            Tool(name="cart_update_delivery_specification", description="Update delivery specification",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "deliverySpecification": {"type": "object"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "deliverySpecification"]}),
            
            Tool(name="cart_override_cart_line_price", description="Override cart line price",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineId": {"type": "string"}, "price": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLineId", "price"]}),
            
            # Promotions & Discounts (36-40)
            Tool(name="cart_get_promotions", description="Get cart promotions",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_add_discount_code", description="Add discount code",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "discountCode": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "discountCode"]}),
            
            Tool(name="cart_remove_discount_codes", description="Remove discount codes",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "discountCodes": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "discountCodes"]}),
            
            Tool(name="cart_remove_cart_lines", description="Remove cart lines",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cartLineIds": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cartLineIds"]}),
            
            Tool(name="cart_search", description="Search carts by criteria",
                 inputSchema={"type": "object", "properties": {"cartSearchCriteria": {"type": "object"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartSearchCriteria"]}),
            
            # Payment & Tender Processing (41-48)
            Tool(name="cart_get_card_payment_accept_point", description="Get card payment accept point",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "amount": {"type": "number"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "amount"]}),
            
            Tool(name="cart_retrieve_card_payment_accept_result", description="Retrieve card payment accept result",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "paymentAcceptResultAccessCode": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "paymentAcceptResultAccessCode"]}),
            
            Tool(name="cart_add_coupons", description="Add coupons to cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "coupons": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "coupons"]}),
            
            Tool(name="cart_remove_coupons", description="Remove coupons from cart",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "coupons": {"type": "array", "items": {"type": "string"}}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "coupons"]}),
            
            Tool(name="cart_get_charge_codes", description="Get charge codes",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_max_loyalty_points_to_redeem_for_transaction_balance", description="Get max loyalty points for redemption",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "loyaltyCardId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "loyaltyCardId"]}),
            
            Tool(name="cart_get_declined_or_voided_card_receipts", description="Get declined/voided card receipts",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_reset_all_charges", description="Reset all charges",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            # Core Entity Operations (49-55)
            Tool(name="cart_get_entity_by_key", description="Get cart entity by key",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_create_entity", description="Create cart entity",
                 inputSchema={"type": "object", "properties": {"customerId": {"type": "string"}, "storeId": {"type": "string"}, "currency": {"type": "string", "default": "USD"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": []}),
            
            Tool(name="cart_update_entity", description="Update cart entity",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "cart": {"type": "object"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId", "cart"]}),
            
            Tool(name="cart_delete_entity", description="Delete cart entity",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_get_cart_by_id", description="Get cart by ID",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
            
            Tool(name="cart_merge_carts", description="Merge multiple carts",
                 inputSchema={"type": "object", "properties": {"sourceCartId": {"type": "string"}, "targetCartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["sourceCartId", "targetCartId"]}),
            
            Tool(name="cart_validate_cart", description="Validate cart before checkout",
                 inputSchema={"type": "object", "properties": {"cartId": {"type": "string"}, "baseUrl": {"type": "string", "description": "Base URL of the Dynamics 365 Commerce site (uses DYNAMICS365_BASE_URL env var if not provided)"}}, "required": ["cartId"]}),
        ]
    
    async def handle_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle cart tool calls with database operations and mock implementations"""
        base_url = arguments.get("baseUrl", get_base_url())
        
        try:
            # Core operations with full database integration (original 8 tools)
            if name == "cart_create_entity":
                return await self._handle_cart_create_entity(base_url, arguments)
            elif name == "cart_get_entity_by_key":
                return await self._handle_cart_get_entity_by_key(base_url, arguments)
            elif name == "cart_add_cart_lines":
                return await self._handle_cart_add_cart_lines(base_url, arguments)
            elif name == "cart_update_cart_lines":
                return await self._handle_cart_update_cart_lines(base_url, arguments)
            elif name == "cart_remove_cart_lines":
                return await self._handle_cart_remove_cart_lines(base_url, arguments)
            elif name == "cart_checkout":
                return await self._handle_cart_checkout(base_url, arguments)
            elif name == "cart_add_discount_code":
                return await self._handle_cart_add_discount_code(base_url, arguments)
            
            # All other tools - mock implementations with realistic responses
            else:
                return await self._handle_mock_tool(name, base_url, arguments)
                
        except Exception as e:
            return {"error": f"Error in {name}: {str(e)}"}
    
    # Full database integration methods (original 8 core tools)
    async def _handle_cart_create_entity(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new shopping cart with database integration"""
        customer_id = arguments.get("customerId")
        store_id = arguments.get("storeId", "STORE001")
        currency = arguments.get("currency", "USD")
        
        cart_data = {
            "customer_id": customer_id,
            "store_id": store_id,
            "currency": currency,
            "status": "Active",
            "lines": [],
            "subtotal": 0.0,
            "tax_amount": 0.0,
            "total": 0.0,
            "discount_codes": [],
            "delivery_mode": "Standard"
        }
        
        cart_id = self.db.create('carts', cart_data)
        created_cart = self.db.read('carts', cart_id)
        
        return {
            "api": f"POST {base_url}/api/CommerceRuntime/Carts",
            "success": True,
            "cart": created_cart
        }
    
    async def _handle_cart_get_entity_by_key(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Get cart by ID with database integration"""
        cart_id = arguments.get("cartId")
        cart = self.db.read('carts', cart_id)
        
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        # Enrich cart with product details
        for line in cart.get('lines', []):
            product = self.db.read('products', line.get('product_id'))
            if product:
                line['product_name'] = product.get('name')
                line['product_sku'] = product.get('sku')
                line['product_image'] = product.get('images', [None])[0]
        
        return {
            "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}",
            "cart": cart
        }
    
    async def _handle_cart_add_cart_lines(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Add items to cart with database integration"""
        cart_id = arguments.get("cartId")
        cart_lines = arguments.get("cartLines", [])
        
        cart = self.db.read('carts', cart_id)
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        current_lines = cart.get('lines', [])
        
        for cart_line in cart_lines:
            product_id = cart_line.get('productId') or cart_line.get('product_id')
            quantity = cart_line.get('quantity', 1)
            
            if not product_id:
                continue
            
            # Get product details
            product = self.db.read('products', product_id)
            if not product:
                continue
            
            # Check if product already in cart
            existing_line = None
            for line in current_lines:
                if line.get('product_id') == product_id:
                    existing_line = line
                    break
            
            if existing_line:
                # Update quantity
                existing_line['quantity'] += quantity
                existing_line['line_total'] = existing_line['quantity'] * existing_line['unit_price']
            else:
                # Add new line
                line_id = f"LINE{len(current_lines) + 1:03d}"
                unit_price = product.get('price', 0)
                
                new_cart_line = {
                    "id": line_id,
                    "product_id": product_id,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "line_total": quantity * unit_price,
                    "discount_amount": 0.0
                }
                current_lines.append(new_cart_line)
        
        # Recalculate totals
        totals = self._calculate_cart_totals(current_lines)
        
        # Update cart
        updates = {
            'lines': current_lines,
            'subtotal': totals['subtotal'],
            'tax_amount': totals['tax'],
            'total': totals['total']
        }
        
        self.db.update('carts', cart_id, updates)
        updated_cart = self.db.read('carts', cart_id)
        
        return {
            "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Lines",
            "success": True,
            "cart": updated_cart,
            "linesAdded": len([line for line in cart_lines if line.get('productId') or line.get('product_id')])
        }
    
    async def _handle_cart_update_cart_lines(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Update cart line quantities with database integration"""
        cart_id = arguments.get("cartId")
        cart_lines = arguments.get("cartLines", [])
        
        cart = self.db.read('carts', cart_id)
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        current_lines = cart.get('lines', [])
        
        for update_line in cart_lines:
            line_id = update_line.get('lineId') or update_line.get('id')
            new_quantity = update_line.get('quantity', 0)
            
            # Find line to update
            for line in current_lines:
                if line.get('id') == line_id:
                    if new_quantity == 0:
                        # Remove line by setting quantity to 0
                        current_lines.remove(line)
                    else:
                        line['quantity'] = new_quantity
                        line['line_total'] = new_quantity * line.get('unit_price', 0)
                    break
        
        # Recalculate totals
        totals = self._calculate_cart_totals(current_lines)
        
        # Update cart
        updates = {
            'lines': current_lines,
            'subtotal': totals['subtotal'],
            'tax_amount': totals['tax'],
            'total': totals['total']
        }
        
        self.db.update('carts', cart_id, updates)
        updated_cart = self.db.read('carts', cart_id)
        
        return {
            "api": f"PUT {base_url}/api/CommerceRuntime/Carts/{cart_id}/Lines",
            "success": True,
            "cart": updated_cart,
            "linesUpdated": len(cart_lines)
        }
    
    async def _handle_cart_remove_cart_lines(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Remove items from cart with database integration"""
        cart_id = arguments.get("cartId")
        cart_line_ids = arguments.get("cartLineIds", [])
        
        cart = self.db.read('carts', cart_id)
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        current_lines = cart.get('lines', [])
        lines_removed = 0
        
        # Remove specified lines
        for line_id in cart_line_ids:
            for line in current_lines[:]:  # Use slice to avoid modification during iteration
                if line.get('id') == line_id:
                    current_lines.remove(line)
                    lines_removed += 1
                    break
        
        # Recalculate totals
        totals = self._calculate_cart_totals(current_lines)
        
        # Update cart
        updates = {
            'lines': current_lines,
            'subtotal': totals['subtotal'],
            'tax_amount': totals['tax'],
            'total': totals['total']
        }
        
        self.db.update('carts', cart_id, updates)
        updated_cart = self.db.read('carts', cart_id)
        
        return {
            "api": f"DELETE {base_url}/api/CommerceRuntime/Carts/{cart_id}/Lines",
            "success": True,
            "cart": updated_cart,
            "linesRemoved": lines_removed
        }
    
    async def _handle_cart_checkout(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Process cart checkout with database integration"""
        cart_id = arguments.get("cartId")
        receipt_email = arguments.get("receiptEmail")
        
        cart = self.db.read('carts', cart_id)
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        if not cart.get('lines'):
            return {"error": "Cannot checkout empty cart"}
        
        # Convert cart to sales order
        order_data = {
            "order_number": f"ORD{random.randint(100000, 999999)}",
            "customer_id": cart.get('customer_id'),
            "store_id": cart.get('store_id'),
            "status": "Confirmed",
            "currency": cart.get('currency'),
            "lines": cart.get('lines', []),
            "subtotal": cart.get('subtotal'),
            "tax_amount": cart.get('tax_amount'),
            "shipping_amount": 5.99,
            "total": cart.get('total', 0) + 5.99,
            "payment_method": "credit_card",
            "payment_status": "Paid",
            "receipt_email": receipt_email
        }
        
        # Create sales order
        order_id = self.db.create('sales_orders', order_data)
        
        # Update cart status
        self.db.update('carts', cart_id, {"status": "Completed"})
        
        created_order = self.db.read('sales_orders', order_id)
        
        return {
            "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Checkout",
            "success": True,
            "order": created_order,
            "transaction": {
                "id": f"TXN{random.randint(100000, 999999)}",
                "amount": created_order['total'],
                "payment_method": "credit_card",
                "status": "Approved"
            }
        }
    
    async def _handle_cart_add_discount_code(self, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Apply discount code to cart with database integration"""
        cart_id = arguments.get("cartId")
        discount_code = arguments.get("discountCode")
        
        cart = self.db.read('carts', cart_id)
        if not cart:
            return {"error": f"Cart {cart_id} not found"}
        
        # Simple discount logic
        discount_amount = 0
        discount_valid = False
        
        if discount_code.upper() in ["SAVE10", "WELCOME10"]:
            discount_amount = cart.get('subtotal', 0) * 0.1  # 10% off
            discount_valid = True
        elif discount_code.upper() in ["SAVE20", "VIP20"]:
            discount_amount = cart.get('subtotal', 0) * 0.2  # 20% off
            discount_valid = True
        elif discount_code.upper() == "FREESHIP":
            discount_amount = 5.99  # Free shipping
            discount_valid = True
        
        if not discount_valid:
            return {"error": f"Invalid discount code: {discount_code}"}
        
        # Apply discount
        current_codes = cart.get('discount_codes', [])
        if discount_code not in current_codes:
            current_codes.append(discount_code)
        
        new_total = max(0, cart.get('total', 0) - discount_amount)
        
        updates = {
            'discount_codes': current_codes,
            'total': new_total
        }
        
        self.db.update('carts', cart_id, updates)
        updated_cart = self.db.read('carts', cart_id)
        
        return {
            "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/DiscountCodes",
            "success": True,
            "cart": updated_cart,
            "appliedDiscount": {
                "code": discount_code,
                "amount": discount_amount,
                "type": "percentage" if "%" in discount_code.upper() else "fixed"
            }
        }
    
    async def _handle_mock_tool(self, name: str, base_url: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle all other cart tools with mock implementations"""
        cart_id = arguments.get("cartId", f"CART{random.randint(1000, 9999)}")
        
        # Generate realistic mock responses based on tool type
        mock_responses = {
            # Gift Card Operations
            "cart_refill_gift_card": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/RefillGiftCard",
                "success": True,
                "giftCardId": arguments.get("giftCardId", "GC123456"),
                "newBalance": random.uniform(50, 500),
                "transactionId": f"TXN{random.randint(100000, 999999)}"
            },
            "cart_issue_gift_card": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/IssueGiftCard",
                "success": True,
                "giftCardId": f"GC{random.randint(100000, 999999)}",
                "amount": arguments.get("amount", 100),
                "expirationDate": (datetime.now() + timedelta(days=365)).isoformat()
            },
            "cart_cashout_gift_card": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/CashoutGiftCard",
                "success": True,
                "giftCardId": arguments.get("giftCardId", "GC123456"),
                "cashedAmount": arguments.get("amount", 25.50),
                "remainingBalance": 0
            },
            
            # Tender Operations
            "cart_add_tender_line": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/TenderLines",
                "success": True,
                "tenderLineId": f"TL{random.randint(1000, 9999)}",
                "amount": arguments.get("cartTenderLine", {}).get("amount", 100),
                "status": "Authorized"
            },
            "cart_validate_tender_line_for_add": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/ValidateTenderLine",
                "isValid": True,
                "validationResult": "Approved",
                "tenderType": arguments.get("tenderLine", {}).get("tenderType", "CreditCard")
            },
            "cart_void_tender_line": {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Carts/{cart_id}/TenderLines/{arguments.get('tenderLineId', 'TL1234')}",
                "success": True,
                "voidedAmount": random.uniform(10, 100),
                "voidReason": "Customer Request"
            },
            
            # Cart Operations
            "cart_suspend_with_journal": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Suspend",
                "success": True,
                "suspendedCartId": cart_id,
                "receiptNumber": f"R{random.randint(100000, 999999)}",
                "suspendedAt": datetime.now().isoformat()
            },
            "cart_resume": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Resume",
                "success": True,
                "resumedCartId": cart_id,
                "resumedAt": datetime.now().isoformat()
            },
            "cart_recalculate_order": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Recalculate",
                "success": True,
                "recalculatedTotal": round(random.uniform(50, 500), 2),
                "taxAmount": round(random.uniform(5, 50), 2)
            },
            
            # Delivery Operations
            "cart_delivery_preferences": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}/DeliveryPreferences",
                "deliveryOptions": [
                    {"id": "STANDARD", "name": "Standard Delivery", "cost": 5.99, "days": 3},
                    {"id": "EXPRESS", "name": "Express Delivery", "cost": 12.99, "days": 1},
                    {"id": "PICKUP", "name": "Store Pickup", "cost": 0, "days": 0}
                ]
            },
            "cart_get_delivery_options": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}/DeliveryOptions",
                "availableOptions": [
                    {"method": "Standard", "cost": 5.99, "estimatedDays": 3},
                    {"method": "Expedited", "cost": 12.99, "estimatedDays": 1}
                ]
            },
            
            # Charge Operations
            "cart_add_charge": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Charges",
                "success": True,
                "chargeId": f"CHG{random.randint(1000, 9999)}",
                "chargeCode": arguments.get("chargeCode", "SHIPPING"),
                "amount": arguments.get("calculatedAmount", 5.99)
            },
            "cart_override_charge": {
                "api": f"PUT {base_url}/api/CommerceRuntime/Carts/{cart_id}/Charges/{arguments.get('chargeLineId', 'CHG1234')}",
                "success": True,
                "originalAmount": random.uniform(5, 15),
                "newAmount": arguments.get("amount", 0),
                "overrideReason": "Manager Approval"
            },
            
            # Promotion Operations
            "cart_get_promotions": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}/Promotions",
                "activePromotions": [
                    {"id": "PROMO1", "name": "10% Off Electronics", "discount": "10%"},
                    {"id": "PROMO2", "name": "Free Shipping", "discount": "$5.99"}
                ]
            },
            "cart_remove_discount_codes": {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Carts/{cart_id}/DiscountCodes",
                "success": True,
                "removedCodes": arguments.get("discountCodes", []),
                "newTotal": round(random.uniform(100, 300), 2)
            },
            
            # Payment Operations
            "cart_get_card_payment_accept_point": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}/CardPaymentAcceptPoint",
                "acceptPoint": {
                    "url": "https://payments.contoso.com/accept",
                    "token": f"tok_{random.randint(100000, 999999)}",
                    "expires": (datetime.now() + timedelta(minutes=15)).isoformat()
                }
            },
            "cart_get_payments_history": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}/PaymentsHistory",
                "payments": [
                    {"id": "PAY1", "amount": 50.0, "method": "Credit Card", "status": "Approved"},
                    {"id": "PAY2", "amount": 25.0, "method": "Gift Card", "status": "Applied"}
                ]
            },
            
            # Search and Validation
            "cart_search": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/Search",
                "results": [
                    {"cartId": f"CART{i}", "customerId": f"CUST{i}", "total": round(random.uniform(50, 300), 2)}
                    for i in range(1, 6)
                ]
            },
            "cart_validate_cart": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/{cart_id}/Validate",
                "isValid": True,
                "validationResults": [],
                "canCheckout": True
            },
            
            # Entity Operations
            "cart_update_entity": {
                "api": f"PUT {base_url}/api/CommerceRuntime/Carts/{cart_id}",
                "success": True,
                "updatedFields": ["customerId", "deliveryMode"],
                "cart": {"id": cart_id, "status": "Active"}
            },
            "cart_delete_entity": {
                "api": f"DELETE {base_url}/api/CommerceRuntime/Carts/{cart_id}",
                "success": True,
                "deletedCartId": cart_id,
                "deletedAt": datetime.now().isoformat()
            },
            "cart_get_cart_by_id": {
                "api": f"GET {base_url}/api/CommerceRuntime/Carts/{cart_id}",
                "cart": {
                    "id": cart_id,
                    "customerId": "CUST001",
                    "status": "Active",
                    "total": round(random.uniform(50, 300), 2),
                    "itemCount": random.randint(1, 5)
                }
            },
            "cart_merge_carts": {
                "api": f"POST {base_url}/api/CommerceRuntime/Carts/Merge",
                "success": True,
                "sourceCartId": arguments.get("sourceCartId", "CART001"),
                "targetCartId": arguments.get("targetCartId", "CART002"),
                "mergedTotal": round(random.uniform(100, 500), 2)
            }
        }
        
        # Return appropriate mock response or default
        return mock_responses.get(name, {
            "api": f"POST {base_url}/api/CommerceRuntime/Carts/{name.replace('cart_', '').replace('_', '/')}",
            "success": True,
            "cartId": cart_id,
            "operation": name,
            "timestamp": datetime.now().isoformat()
        })
    
    def _calculate_cart_totals(self, lines: List[Dict]) -> Dict[str, float]:
        """Calculate cart subtotal, tax, and total"""
        subtotal = sum(line.get('line_total', 0) for line in lines)
        tax = subtotal * 0.08  # Simple 8% tax rate
        total = subtotal + tax
        
        return {
            "subtotal": round(subtotal, 2),
            "tax": round(tax, 2),
            "total": round(total, 2)
        }