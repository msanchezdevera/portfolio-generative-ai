"""
Shopping Cart class implementation based on UML diagram
"""
from typing import List, Dict, Any


class ShoppingCart:
    """
    Shopping cart to manage products before checkout
    """
    
    def __init__(self, cart_id: int, product_id: int = None):
        """
        Initialize a Shopping Cart instance
        
        Args:
            cart_id (int): Unique identifier for the cart
            product_id (int, optional): Initial product ID
        """
        self._id = cart_id
        self._product_id = product_id
        self._products: List[Dict[str, Any]] = []
    
    @property
    def id(self) -> int:
        """Get cart ID"""
        return self._id
    
    @property
    def product_id(self) -> int:
        """Get current product ID"""
        return self._product_id
    
    @product_id.setter
    def product_id(self, product_id: int):
        """Set product ID"""
        self._product_id = product_id
    
    @property
    def products(self) -> List[Dict[str, Any]]:
        """Get all products in cart"""
        return self._products.copy()
    
    def add_product_to_cart(self, product_id: int, product_name: str, 
                           price: float, quantity: int = 1) -> bool:
        """
        Add a product to the shopping cart
        
        Args:
            product_id (int): Product identifier
            product_name (str): Name of the product
            price (float): Price per unit
            quantity (int): Quantity to add (default: 1)
            
        Returns:
            bool: True if product added successfully
        """
        # Check if product already exists in cart
        for product in self._products:
            if product['id'] == product_id:
                product['quantity'] += quantity
                return True
        
        # Add new product to cart
        product = {
            'id': product_id,
            'name': product_name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        self._products.append(product)
        self._product_id = product_id
        return True
    
    def remove_product_from_cart(self, product_id: int, quantity: int = None) -> bool:
        """
        Remove a product from the shopping cart
        
        Args:
            product_id (int): Product identifier to remove
            quantity (int, optional): Specific quantity to remove. If None, removes all
            
        Returns:
            bool: True if product removed successfully
        """
        for i, product in enumerate(self._products):
            if product['id'] == product_id:
                if quantity is None or quantity >= product['quantity']:
                    # Remove entire product
                    self._products.pop(i)
                else:
                    # Reduce quantity
                    product['quantity'] -= quantity
                    product['total'] = product['price'] * product['quantity']
                return True
        return False
    
    def check_out(self) -> Dict[str, Any]:
        """
        Process checkout and return order summary
        
        Returns:
            dict: Checkout summary with total amount and product details
        """
        if not self._products:
            return {
                'success': False,
                'message': 'Cart is empty',
                'total': 0,
                'products': []
            }
        
        total_amount = sum(product['total'] for product in self._products)
        checkout_summary = {
            'success': True,
            'cart_id': self._id,
            'total': total_amount,
            'products': self._products.copy(),
            'product_count': len(self._products),
            'item_count': sum(product['quantity'] for product in self._products)
        }
        
        # Clear cart after checkout
        self._products.clear()
        self._product_id = None
        
        return checkout_summary
    
    def get_total(self) -> float:
        """
        Calculate total amount in cart
        
        Returns:
            float: Total amount
        """
        return sum(product['total'] for product in self._products)
    
    def get_item_count(self) -> int:
        """
        Get total number of items in cart
        
        Returns:
            int: Total item count
        """
        return sum(product['quantity'] for product in self._products)
    
    def is_empty(self) -> bool:
        """
        Check if cart is empty
        
        Returns:
            bool: True if cart is empty
        """
        return len(self._products) == 0
    
    def __str__(self) -> str:
        return f"ShoppingCart(id={self._id}, items={len(self._products)}, total=${self.get_total():.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()