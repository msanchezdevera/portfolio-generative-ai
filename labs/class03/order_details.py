"""
OrderDetails class implementation based on UML diagram
"""
from datetime import datetime
from typing import Optional


class OrderDetails:
    """
    OrderDetails class to manage specific details of an order
    """
    
    def __init__(self, detail_id: int, order_id: int, shipping_address: str,
                 shipping_type: str = "standard", shipping_cost: float = 0.0,
                 billing_address: str = "", created_date: datetime = None):
        """
        Initialize an OrderDetails instance
        
        Args:
            detail_id (int): Unique identifier for the order detail
            order_id (int): ID of the associated order
            shipping_address (str): Shipping address for this detail
            shipping_type (str): Type of shipping (default: "standard")
            shipping_cost (float): Cost of shipping (default: 0.0)
            billing_address (str): Billing address for this detail
            created_date (datetime, optional): Creation date (defaults to now)
        """
        self._id = detail_id
        self._order_id = order_id
        self._shipping_address = shipping_address
        self._shipping_type = shipping_type
        self._shipping_cost = shipping_cost
        self._billing_address = billing_address
        self._created_date = created_date or datetime.now()
    
    @property
    def id(self) -> int:
        """Get order detail ID"""
        return self._id
    
    @property
    def order_id(self) -> int:
        """Get associated order ID"""
        return self._order_id
    
    @order_id.setter
    def order_id(self, order_id: int):
        """Set order ID"""
        self._order_id = order_id
    
    @property
    def shipping_address(self) -> str:
        """Get shipping address"""
        return self._shipping_address
    
    @shipping_address.setter
    def shipping_address(self, address: str):
        """Set shipping address"""
        self._shipping_address = address
    
    @property
    def shipping_type(self) -> str:
        """Get shipping type"""
        return self._shipping_type
    
    @shipping_type.setter
    def shipping_type(self, shipping_type: str):
        """Set shipping type"""
        self._shipping_type = shipping_type
    
    @property
    def shipping_cost(self) -> float:
        """Get shipping cost"""
        return self._shipping_cost
    
    @shipping_cost.setter
    def shipping_cost(self, cost: float):
        """Set shipping cost"""
        self._shipping_cost = cost
    
    @property
    def billing_address(self) -> str:
        """Get billing address"""
        return self._billing_address
    
    @billing_address.setter
    def billing_address(self, address: str):
        """Set billing address"""
        self._billing_address = address
    
    @property
    def created_date(self) -> datetime:
        """Get creation date"""
        return self._created_date
    
    @created_date.setter
    def created_date(self, date: datetime):
        """Set creation date"""
        self._created_date = date
    
    def cancel_order(self) -> bool:
        """
        Cancel this specific order detail
        
        Returns:
            bool: True if cancellation successful
        """
        # Logic to cancel this specific order detail
        print(f"Order detail {self._id} for order {self._order_id} has been cancelled")
        return True
    
    def update_shipping_address(self, new_address: str) -> bool:
        """
        Update the shipping address for this order detail
        
        Args:
            new_address (str): New shipping address
            
        Returns:
            bool: True if address updated successfully
        """
        old_address = self._shipping_address
        self._shipping_address = new_address
        print(f"Shipping address updated from '{old_address}' to '{new_address}'")
        return True
    
    def calculate_total_cost(self, product_cost: float = 0.0) -> float:
        """
        Calculate total cost including shipping
        
        Args:
            product_cost (float): Cost of products (default: 0.0)
            
        Returns:
            float: Total cost including shipping
        """
        return product_cost + self._shipping_cost
    
    def get_detail_summary(self) -> dict:
        """
        Get summary of order detail
        
        Returns:
            dict: Order detail summary
        """
        return {
            'detail_id': self._id,
            'order_id': self._order_id,
            'shipping_address': self._shipping_address,
            'shipping_type': self._shipping_type,
            'shipping_cost': self._shipping_cost,
            'billing_address': self._billing_address,
            'created_date': self._created_date.isoformat()
        }
    
    def __str__(self) -> str:
        return f"OrderDetail(id={self._id}, order={self._order_id}, shipping_cost=${self._shipping_cost:.2f})"
    
    def __repr__(self) -> str:
        return self.__str__()