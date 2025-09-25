"""
Customer class implementation based on UML diagram
"""
from typing import Optional, List
from user import User


class Customer(User):
    """
    Customer class that inherits from User and adds customer-specific functionality
    """
    
    def __init__(self, user_id: int, email: str, password: str, 
                 name: str, billing_address: str, default_shipping_address: str):
        """
        Initialize a Customer instance
        
        Args:
            user_id (int): Unique identifier for the user
            email (str): Customer's email address
            password (str): Customer's password
            name (str): Customer's full name
            billing_address (str): Customer's billing address
            default_shipping_address (str): Customer's default shipping address
        """
        super().__init__(user_id, email, password)
        self._name = name
        self._billing_address = billing_address
        self._default_shipping_address = default_shipping_address
    
    @property
    def name(self) -> str:
        """Get customer name"""
        return self._name
    
    @name.setter
    def name(self, name: str):
        """Set customer name"""
        self._name = name
    
    @property
    def billing_address(self) -> str:
        """Get billing address"""
        return self._billing_address
    
    @billing_address.setter
    def billing_address(self, address: str):
        """Set billing address"""
        self._billing_address = address
    
    @property
    def default_shipping_address(self) -> str:
        """Get default shipping address"""
        return self._default_shipping_address
    
    @default_shipping_address.setter
    def default_shipping_address(self, address: str):
        """Set default shipping address"""
        self._default_shipping_address = address
    
    def sign_up(self, name: str, email: str, password: str, 
                billing_address: str, shipping_address: str) -> bool:
        """
        Sign up a new customer (class method functionality)
        
        Args:
            name (str): Customer's name
            email (str): Customer's email
            password (str): Customer's password
            billing_address (str): Billing address
            shipping_address (str): Shipping address
            
        Returns:
            bool: True if signup successful
        """
        # Update customer information
        self._name = name
        self.email = email
        self.password = password
        self._billing_address = billing_address
        self._default_shipping_address = shipping_address
        return True
    
    def login(self, email: str, password: str) -> bool:
        """
        Customer login with additional customer-specific logic
        
        Args:
            email (str): Email to verify
            password (str): Password to verify
            
        Returns:
            bool: True if login successful
        """
        if super().login(email, password):
            # Additional customer login logic can be added here
            print(f"Customer {self._name} logged in successfully")
            return True
        return False
    
    def __str__(self) -> str:
        return f"Customer(id={self.id}, name={self._name}, email={self.email})"
    
    def __repr__(self) -> str:
        return self.__str__()