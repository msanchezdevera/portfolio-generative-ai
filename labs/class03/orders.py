"""
Orders class implementation based on UML diagram
"""
from datetime import datetime
from typing import List, Optional
from enum import Enum


class OrderStatus(Enum):
    """Enumeration for order status"""
    PENDING = "pending"
    CONFIRMED = "confirmed" 
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Orders:
    """
    Orders class to manage customer orders
    """
    
    def __init__(self, order_id: int, customer_id: int, 
                 order_date: datetime = None, status: str = "pending", price: float = 0.0):
        """
        Initialize an Orders instance
        
        Args:
            order_id (int): Unique identifier for the order
            customer_id (int): ID of the customer placing the order
            order_date (datetime, optional): Date of the order (defaults to now)
            status (str): Status of the order (default: "pending")
            price (float): Total price of the order (default: 0.0)
        """
        self._id = order_id
        self._customer_id = customer_id
        self._order_date = order_date or datetime.now()
        self._status = status
        self._price = price
        self._order_details: List['OrderDetails'] = []
    
    @property
    def id(self) -> int:
        """Get order ID"""
        return self._id
    
    @property
    def customer_id(self) -> int:
        """Get customer ID"""
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, customer_id: int):
        """Set customer ID"""
        self._customer_id = customer_id
    
    @property
    def order_date(self) -> datetime:
        """Get order date"""
        return self._order_date
    
    @order_date.setter
    def order_date(self, order_date: datetime):
        """Set order date"""
        self._order_date = order_date
    
    @property
    def status(self) -> str:
        """Get order status"""
        return self._status
    
    @status.setter
    def status(self, status: str):
        """Set order status"""
        self._status = status
    
    @property
    def price(self) -> float:
        """Get order price"""
        return self._price
    
    @price.setter
    def price(self, price: float):
        """Set order price"""
        self._price = price
    
    @property
    def order_details(self) -> List['OrderDetails']:
        """Get order details"""
        return self._order_details.copy()
    
    def update_order_status(self, new_status: str) -> bool:
        """
        Update the status of the order
        
        Args:
            new_status (str): New status for the order
            
        Returns:
            bool: True if status updated successfully
        """
        try:
            # Validate status
            OrderStatus(new_status)
            self._status = new_status
            print(f"Order {self._id} status updated to: {new_status}")
            return True
        except ValueError:
            print(f"Invalid status: {new_status}")
            return False
    
    def place_order(self, cart_summary: dict) -> bool:
        """
        Place an order based on shopping cart summary
        
        Args:
            cart_summary (dict): Summary from shopping cart checkout
            
        Returns:
            bool: True if order placed successfully
        """
        if not cart_summary.get('success', False):
            return False
        
        self._price = cart_summary.get('total', 0.0)
        self._status = OrderStatus.CONFIRMED.value
        
        # Import here to avoid circular imports
        from order_details import OrderDetails
        
        # Create order details for each product
        for product in cart_summary.get('products', []):
            order_detail = OrderDetails(
                detail_id=len(self._order_details) + 1,
                order_id=self._id,
                shipping_address=f"Default shipping address for customer {self._customer_id}",
                shipping_type="standard",
                shipping_cost=5.99,
                billing_address=f"Default billing address for customer {self._customer_id}",
                created_date=datetime.now()
            )
            self._order_details.append(order_detail)
        
        print(f"Order {self._id} placed successfully with total: ${self._price:.2f}")
        return True
    
    def cancel_order(self) -> bool:
        """
        Cancel the order if it's still possible
        
        Returns:
            bool: True if order cancelled successfully
        """
        if self._status in [OrderStatus.SHIPPED.value, OrderStatus.DELIVERED.value]:
            print(f"Cannot cancel order {self._id}: Order already {self._status}")
            return False
        
        self._status = OrderStatus.CANCELLED.value
        print(f"Order {self._id} has been cancelled")
        return True
    
    def add_order_detail(self, order_detail: 'OrderDetails') -> bool:
        """
        Add order detail to this order
        
        Args:
            order_detail (OrderDetails): Order detail to add
            
        Returns:
            bool: True if added successfully
        """
        self._order_details.append(order_detail)
        return True
    
    def get_order_summary(self) -> dict:
        """
        Get complete order summary
        
        Returns:
            dict: Order summary with all details
        """
        return {
            'order_id': self._id,
            'customer_id': self._customer_id,
            'order_date': self._order_date.isoformat(),
            'status': self._status,
            'price': self._price,
            'details_count': len(self._order_details)
        }
    
    def __str__(self) -> str:
        return f"Order(id={self._id}, customer={self._customer_id}, status={self._status}, total=${self._price:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()