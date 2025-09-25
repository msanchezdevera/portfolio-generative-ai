# Refactored sales processing with single responsibility functions

from datetime import datetime
from typing import List, Dict, Tuple, Any, Optional


def is_authorized_admin(user_data: Dict[str, Any]) -> bool:
    """
    Check if user has admin role and is active.
    
    Args:
        user_data: Dictionary containing user role and active status
        
    Returns:
        bool: True if user is an authorized admin, False otherwise
    """
    if user_data.get("role") != "admin":
        print("Access denied.")
        return False
    
    if not user_data.get("active", False):
        print("Inactive admin account.")
        return False
    
    return True


def sanitize_transaction_data(raw_transaction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Clean and convert transaction data to appropriate types.
    
    Args:
        raw_transaction: Dictionary with string values for item, price, qty
        
    Returns:
        Dict with cleaned and converted data
        
    Raises:
        ValueError: If data conversion fails
    """
    try:
        cleaned_item = raw_transaction["item"].strip()
        cleaned_price = float(raw_transaction["price"].strip())
        cleaned_quantity = int(raw_transaction["qty"].strip())
        
        return {
            "item": cleaned_item,
            "price": cleaned_price,
            "quantity": cleaned_quantity
        }
    except (ValueError, KeyError) as e:
        raise ValueError(f"Failed to process transaction data: {e}")


def calculate_sale_amount(price: float, quantity: int) -> float:
    """
    Calculate total sale amount for an item.
    
    Args:
        price: Unit price of the item
        quantity: Number of items sold
        
    Returns:
        float: Total sale amount
    """
    return price * quantity


def create_sale_record(item: str, price: float, quantity: int, sale_amount: float) -> Dict[str, Any]:
    """
    Create a formatted sale record.
    
    Args:
        item: Item name
        price: Unit price
        quantity: Quantity sold
        sale_amount: Total sale amount
        
    Returns:
        Dict containing formatted sale record
    """
    return {
        "Item": item,
        "Price": price,
        "Qty": quantity,
        "Sale": sale_amount
    }


def process_single_transaction(transaction_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """
    Process a single transaction if user is authorized.
    
    Args:
        transaction_data: Raw transaction data dictionary
        
    Returns:
        Processed sale record or None if unauthorized/invalid
    """
    # Check authorization
    if not is_authorized_admin(transaction_data):
        return None
    
    try:
        # Clean and convert data
        cleaned_data = sanitize_transaction_data(transaction_data)
        
        # Calculate sale amount
        sale_amount = calculate_sale_amount(
            cleaned_data["price"], 
            cleaned_data["quantity"]
        )
        
        # Create sale record
        return create_sale_record(
            cleaned_data["item"],
            cleaned_data["price"],
            cleaned_data["quantity"],
            sale_amount
        )
        
    except ValueError as e:
        print(f"Skipping invalid transaction: {e}")
        return None


def calculate_total_sales(sale_records: List[Dict[str, Any]]) -> float:
    """
    Calculate total sales from all sale records.
    
    Args:
        sale_records: List of sale record dictionaries
        
    Returns:
        float: Total sales amount
    """
    return sum(record["Sale"] for record in sale_records)


def display_sales_summary(total_sales: float, sale_records: List[Dict[str, Any]]) -> None:
    """
    Display formatted sales summary.
    
    Args:
        total_sales: Total sales amount
        sale_records: List of sale records to display
    """
    print("TOTAL:", total_sales)
    for record in sale_records:
        print(record["Item"], record["Price"], record["Qty"], record["Sale"])


def run(data: List[Dict[str, Any]]) -> Tuple[float, List[Dict[str, Any]]]:
    """
    Main function to process sales transaction data.
    
    Args:
        data: List of transaction dictionaries with keys:
              {"item": str, "price": str, "qty": str, "ts": "YYYY-MM-DD", "role": str, "active": bool}
              
    Returns:
        Tuple containing total sales amount and list of processed sale records
    """
    processed_sales = []
    
    # Process each transaction
    for transaction in data:
        sale_record = process_single_transaction(transaction)
        if sale_record:
            processed_sales.append(sale_record)
    
    # Calculate total
    total_sales = calculate_total_sales(processed_sales)
    
    # Display summary
    display_sales_summary(total_sales, processed_sales)
    
    return total_sales, processed_sales
