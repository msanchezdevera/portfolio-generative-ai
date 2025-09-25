"""
User class implementation based on UML diagram
"""
from datetime import datetime
from typing import Optional


class User:
    """
    Represents a user in the system with basic authentication functionality
    """
    
    def __init__(self, user_id: int, email: str, password: str):
        """
        Initialize a User instance
        
        Args:
            user_id (int): Unique identifier for the user
            email (str): User's email address
            password (str): User's password (should be hashed in production)
        """
        self._id = user_id
        self._email = email
        self._password = password
        self._last_login: Optional[datetime] = None
    
    @property
    def id(self) -> int:
        """Get user ID"""
        return self._id
    
    @property
    def email(self) -> str:
        """Get user email"""
        return self._email
    
    @email.setter
    def email(self, email: str):
        """Set user email"""
        self._email = email
    
    @property
    def password(self) -> str:
        """Get user password (in production, this should return a hash)"""
        return self._password
    
    @password.setter
    def password(self, password: str):
        """Set user password (should be hashed in production)"""
        self._password = password
    
    @property
    def last_login(self) -> Optional[datetime]:
        """Get last login timestamp"""
        return self._last_login
    
    def get_session(self) -> dict:
        """
        Get user session information
        
        Returns:
            dict: Session information including user ID and last login
        """
        return {
            "user_id": self._id,
            "email": self._email,
            "last_login": self._last_login,
            "is_active": True
        }
    
    def login(self, email: str, password: str) -> bool:
        """
        Authenticate user login
        
        Args:
            email (str): Email to verify
            password (str): Password to verify
            
        Returns:
            bool: True if login successful, False otherwise
        """
        if self._email == email and self._password == password:
            self._last_login = datetime.now()
            return True
        return False
    
    def __str__(self) -> str:
        return f"User(id={self._id}, email={self._email})"
    
    def __repr__(self) -> str:
        return self.__str__()