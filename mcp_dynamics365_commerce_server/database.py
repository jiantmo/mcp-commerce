"""
Mock Database Manager for Dynamics 365 Commerce MCP Server

Provides in-memory database with demo data for all commerce entities.
Implements simple CRUD operations for each entity type.
"""

import json
import uuid
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional
import random
from decimal import Decimal

class MockDatabase:
    """In-memory mock database with demo data"""
    
    def __init__(self):
        self._data = {}
        self._initialize_demo_data()
    
    def _initialize_demo_data(self):
        """Initialize database with comprehensive demo data"""
        
        # Countries and Regions
        self._data['countries'] = [
            {'id': 'US', 'name': 'United States', 'code': 'US', 'language_id': 'en-US'},
            {'id': 'CA', 'name': 'Canada', 'code': 'CA', 'language_id': 'en-CA'},
            {'id': 'GB', 'name': 'United Kingdom', 'code': 'GB', 'language_id': 'en-GB'}
        ]
        
        # States/Provinces
        self._data['states'] = [
            {'id': 'WA', 'name': 'Washington', 'country_id': 'US', 'code': 'WA'},
            {'id': 'CA', 'name': 'California', 'country_id': 'US', 'code': 'CA'},
            {'id': 'NY', 'name': 'New York', 'country_id': 'US', 'code': 'NY'},
            {'id': 'ON', 'name': 'Ontario', 'country_id': 'CA', 'code': 'ON'}
        ]
        
        # Cities
        self._data['cities'] = [
            {'id': 'SEA', 'name': 'Seattle', 'state_id': 'WA', 'country_id': 'US'},
            {'id': 'LA', 'name': 'Los Angeles', 'state_id': 'CA', 'country_id': 'US'},
            {'id': 'NYC', 'name': 'New York City', 'state_id': 'NY', 'country_id': 'US'},
            {'id': 'TOR', 'name': 'Toronto', 'state_id': 'ON', 'country_id': 'CA'}
        ]
        
        # Customers
        self._data['customers'] = [
            {
                'id': 'CUST001',
                'account_number': 'ACC001',
                'first_name': 'John',
                'last_name': 'Smith',
                'email': 'john.smith@example.com',
                'phone': '+1-555-0101',
                'created_date': (datetime.now() - timedelta(days=365)).isoformat(),
                'customer_group': 'REGULAR',
                'loyalty_card_number': 'LOY001',
                'addresses': [
                    {
                        'id': 'ADDR001',
                        'type': 'Primary',
                        'street': '123 Main St',
                        'city': 'Seattle',
                        'state': 'WA',
                        'zip': '98101',
                        'country': 'US'
                    }
                ]
            },
            {
                'id': 'CUST002',
                'account_number': 'ACC002',
                'first_name': 'Jane',
                'last_name': 'Doe',
                'email': 'jane.doe@example.com',
                'phone': '+1-555-0102',
                'created_date': (datetime.now() - timedelta(days=200)).isoformat(),
                'customer_group': 'VIP',
                'loyalty_card_number': 'LOY002',
                'addresses': []
            }
        ]
        
        # Products
        self._data['products'] = [
            {
                'id': 'PROD001',
                'name': 'Wireless Bluetooth Headphones',
                'description': 'High-quality wireless headphones with noise cancellation',
                'sku': 'WBH001',
                'price': 199.99,
                'cost': 89.99,
                'category_id': 'CAT001',
                'brand': 'TechBrand',
                'weight': 0.8,
                'dimensions': {'length': 20, 'width': 18, 'height': 8},
                'color': 'Black',
                'size': 'One Size',
                'inventory_quantity': 150,
                'images': ['https://example.com/images/wbh001_1.jpg'],
                'attributes': {'warranty': '2 years', 'battery_life': '30 hours'}
            },
            {
                'id': 'PROD002',
                'name': 'Smartphone Case',
                'description': 'Durable protective case for smartphones',
                'sku': 'SC002',
                'price': 29.99,
                'cost': 12.99,
                'category_id': 'CAT002',
                'brand': 'ProtectTech',
                'weight': 0.1,
                'dimensions': {'length': 15, 'width': 7.5, 'height': 1},
                'color': 'Blue',
                'size': 'Universal',
                'inventory_quantity': 300,
                'images': ['https://example.com/images/sc002_1.jpg'],
                'attributes': {'material': 'Silicone', 'compatibility': 'Most smartphones'}
            }
        ]
        
        # Categories
        self._data['categories'] = [
            {
                'id': 'CAT001',
                'name': 'Electronics',
                'description': 'Electronic devices and accessories',
                'parent_id': None,
                'level': 1,
                'sort_order': 1
            },
            {
                'id': 'CAT002',
                'name': 'Accessories',
                'description': 'Phone and device accessories',
                'parent_id': 'CAT001',
                'level': 2,
                'sort_order': 1
            }
        ]
        
        # Stores
        self._data['stores'] = [
            {
                'id': 'STORE001',
                'name': 'Seattle Downtown',
                'address': '456 Commerce St, Seattle, WA 98102',
                'phone': '+1-555-0201',
                'email': 'seattle@example.com',
                'hours': {
                    'monday': '9:00-21:00',
                    'tuesday': '9:00-21:00',
                    'wednesday': '9:00-21:00',
                    'thursday': '9:00-21:00',
                    'friday': '9:00-21:00',
                    'saturday': '10:00-20:00',
                    'sunday': '11:00-19:00'
                },
                'inventory': {
                    'PROD001': 50,
                    'PROD002': 120
                }
            },
            {
                'id': 'STORE002',
                'name': 'Los Angeles West',
                'address': '789 Retail Ave, Los Angeles, CA 90210',
                'phone': '+1-555-0202',
                'email': 'la@example.com',
                'hours': {
                    'monday': '10:00-22:00',
                    'tuesday': '10:00-22:00',
                    'wednesday': '10:00-22:00',
                    'thursday': '10:00-22:00',
                    'friday': '10:00-22:00',
                    'saturday': '10:00-21:00',
                    'sunday': '11:00-20:00'
                },
                'inventory': {
                    'PROD001': 75,
                    'PROD002': 200
                }
            }
        ]
        
        # Carts
        self._data['carts'] = [
            {
                'id': 'CART001',
                'customer_id': 'CUST001',
                'store_id': 'STORE001',
                'created_date': datetime.now().isoformat(),
                'status': 'Active',
                'currency': 'USD',
                'lines': [
                    {
                        'id': 'LINE001',
                        'product_id': 'PROD001',
                        'quantity': 1,
                        'unit_price': 199.99,
                        'line_total': 199.99,
                        'discount_amount': 0.00
                    }
                ],
                'subtotal': 199.99,
                'tax_amount': 16.00,
                'total': 215.99,
                'discount_codes': [],
                'delivery_mode': 'Standard'
            }
        ]
        
        # Sales Orders
        self._data['sales_orders'] = [
            {
                'id': 'SO001',
                'order_number': 'ORD001',
                'customer_id': 'CUST001',
                'store_id': 'STORE001',
                'order_date': (datetime.now() - timedelta(days=5)).isoformat(),
                'status': 'Fulfilled',
                'currency': 'USD',
                'lines': [
                    {
                        'id': 'SOLINE001',
                        'product_id': 'PROD002',
                        'quantity': 2,
                        'unit_price': 29.99,
                        'line_total': 59.98,
                        'status': 'Fulfilled'
                    }
                ],
                'subtotal': 59.98,
                'tax_amount': 4.80,
                'shipping_amount': 5.99,
                'total': 70.77,
                'payment_status': 'Paid',
                'shipping_address': {
                    'street': '123 Main St',
                    'city': 'Seattle',
                    'state': 'WA',
                    'zip': '98101',
                    'country': 'US'
                }
            }
        ]
        
        # Loyalty Cards
        self._data['loyalty_cards'] = [
            {
                'id': 'LOY001',
                'card_number': 'LOY001',
                'customer_id': 'CUST001',
                'points_balance': 1250,
                'tier': 'Silver',
                'created_date': (datetime.now() - timedelta(days=300)).isoformat(),
                'status': 'Active',
                'transactions': [
                    {
                        'id': 'LOYT001',
                        'date': (datetime.now() - timedelta(days=5)).isoformat(),
                        'points': 70,
                        'type': 'Earned',
                        'order_id': 'SO001'
                    }
                ]
            }
        ]
        
        # Shifts
        self._data['shifts'] = [
            {
                'id': 'SHIFT001',
                'store_id': 'STORE001',
                'employee_id': 'EMP001',
                'start_time': datetime.now().replace(hour=9, minute=0).isoformat(),
                'end_time': None,
                'status': 'Open',
                'cash_drawer': {
                    'starting_amount': 200.00,
                    'current_amount': 450.00,
                    'total_sales': 250.00
                }
            }
        ]
        
        # Additional entities for comprehensive coverage
        self._data['gift_cards'] = []
        self._data['discounts'] = []
        self._data['tender_types'] = [
            {'id': 'CASH', 'name': 'Cash', 'type': 'Cash'},
            {'id': 'CREDIT', 'name': 'Credit Card', 'type': 'Card'},
            {'id': 'DEBIT', 'name': 'Debit Card', 'type': 'Card'}
        ]
        self._data['reason_codes'] = [
            {'id': 'RC001', 'name': 'Customer Return', 'type': 'Return'},
            {'id': 'RC002', 'name': 'Damaged Item', 'type': 'Return'},
            {'id': 'RC003', 'name': 'Price Override', 'type': 'Override'}
        ]
        self._data['delivery_options'] = [
            {'id': 'STANDARD', 'name': 'Standard Delivery', 'cost': 5.99, 'days': 3},
            {'id': 'EXPRESS', 'name': 'Express Delivery', 'cost': 12.99, 'days': 1},
            {'id': 'PICKUP', 'name': 'Store Pickup', 'cost': 0.00, 'days': 0}
        ]
        
        # Initialize empty collections for other entities
        empty_collections = [
            'addresses', 'barcodes', 'cash_declarations', 'counties', 'credit_memos',
            'suspended_carts', 'currencies', 'customer_groups', 'customer_balances',
            'device_configurations', 'languages', 'app_info', 'async_services',
            'attributes', 'attribute_groups', 'audit_events', 'card_types',
            'catalogs', 'commission_sales_groups', 'districts', 'environment_configurations',
            'extension_packages', 'extensible_enumerations', 'hardware_profiles',
            'images', 'income_expense_accounts', 'kits', 'localized_strings',
            'notifications', 'number_sequences', 'operations', 'product_lists',
            'purchase_orders', 'recommendations', 'receipts', 'report_datasets',
            'search_results', 'shift_reconciliation_lines', 'store_safes', 'taxes',
            'tender_operations', 'transfer_orders', 'units_of_measure', 'warehouses',
            'zipcodes', 'publications', 'non_sales_tender_operations',
            'fulfillment_orders', 'scan_results', 'stock_count_journals'
        ]
        
        for collection in empty_collections:
            self._data[collection] = []

    # Generic CRUD operations
    def create(self, collection: str, item: Dict[str, Any]) -> str:
        """Create a new item in the specified collection"""
        if collection not in self._data:
            self._data[collection] = []
        
        # Generate ID if not provided
        if 'id' not in item:
            item['id'] = self._generate_id(collection)
        
        # Add timestamps
        if 'created_date' not in item:
            item['created_date'] = datetime.now().isoformat()
        item['modified_date'] = datetime.now().isoformat()
        
        self._data[collection].append(item)
        return item['id']
    
    def read(self, collection: str, item_id: str) -> Optional[Dict[str, Any]]:
        """Read an item by ID from the specified collection"""
        if collection not in self._data:
            return None
        
        for item in self._data[collection]:
            if item.get('id') == item_id:
                return item.copy()
        return None
    
    def update(self, collection: str, item_id: str, updates: Dict[str, Any]) -> bool:
        """Update an item in the specified collection"""
        if collection not in self._data:
            return False
        
        for i, item in enumerate(self._data[collection]):
            if item.get('id') == item_id:
                item.update(updates)
                item['modified_date'] = datetime.now().isoformat()
                self._data[collection][i] = item
                return True
        return False
    
    def delete(self, collection: str, item_id: str) -> bool:
        """Delete an item from the specified collection"""
        if collection not in self._data:
            return False
        
        for i, item in enumerate(self._data[collection]):
            if item.get('id') == item_id:
                del self._data[collection][i]
                return True
        return False
    
    def list(self, collection: str, limit: int = 100, offset: int = 0, 
             filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """List items from the specified collection with optional filters"""
        if collection not in self._data:
            return []
        
        items = self._data[collection][:]
        
        # Apply filters
        if filters:
            for key, value in filters.items():
                items = [item for item in items if item.get(key) == value]
        
        # Apply pagination
        return items[offset:offset + limit]
    
    def search(self, collection: str, query: str, fields: List[str] = None, 
              limit: int = 100) -> List[Dict[str, Any]]:
        """Search items in the specified collection"""
        if collection not in self._data:
            return []
        
        results = []
        query_lower = query.lower()
        
        for item in self._data[collection]:
            if self._item_matches_query(item, query_lower, fields):
                results.append(item.copy())
                if len(results) >= limit:
                    break
        
        return results
    
    def count(self, collection: str, filters: Optional[Dict[str, Any]] = None) -> int:
        """Count items in the specified collection"""
        if collection not in self._data:
            return 0
        
        items = self._data[collection]
        
        if filters:
            count = 0
            for item in items:
                if all(item.get(k) == v for k, v in filters.items()):
                    count += 1
            return count
        
        return len(items)
    
    # Helper methods
    def _generate_id(self, collection: str) -> str:
        """Generate a unique ID for the collection"""
        prefix = collection.upper()[:4]
        return f"{prefix}{len(self._data[collection]) + 1:03d}"
    
    def _item_matches_query(self, item: Dict[str, Any], query: str, 
                           fields: List[str] = None) -> bool:
        """Check if an item matches the search query"""
        if not query:
            return True
        
        search_fields = fields or ['name', 'description', 'email', 'phone', 'sku']
        
        for field in search_fields:
            if field in item:
                value = str(item[field]).lower()
                if query in value:
                    return True
        
        return False
    
    # Specialized methods for complex operations
    def get_customer_orders(self, customer_id: str) -> List[Dict[str, Any]]:
        """Get all orders for a specific customer"""
        return [order.copy() for order in self._data['sales_orders'] 
                if order.get('customer_id') == customer_id]
    
    def get_product_inventory(self, product_id: str, store_id: str = None) -> int:
        """Get inventory quantity for a product"""
        if store_id:
            store = self.read('stores', store_id)
            if store and 'inventory' in store:
                return store['inventory'].get(product_id, 0)
        else:
            # Return total inventory across all stores
            total = 0
            for store in self._data['stores']:
                total += store.get('inventory', {}).get(product_id, 0)
            return total
        return 0
    
    def calculate_cart_total(self, cart_id: str) -> Dict[str, float]:
        """Calculate cart totals"""
        cart = self.read('carts', cart_id)
        if not cart:
            return {'subtotal': 0, 'tax': 0, 'total': 0}
        
        subtotal = sum(line.get('line_total', 0) for line in cart.get('lines', []))
        tax = subtotal * 0.08  # Simple 8% tax rate
        total = subtotal + tax
        
        return {
            'subtotal': round(subtotal, 2),
            'tax': round(tax, 2),
            'total': round(total, 2)
        }

# Global database instance
_db_instance = None

def get_database() -> MockDatabase:
    """Get the global database instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = MockDatabase()
    return _db_instance