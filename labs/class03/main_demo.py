"""
Main demonstration file showing the e-commerce system implementation
Based on the UML class diagram
"""
from datetime import datetime
from user import User
from customer import Customer
from shopping_cart import ShoppingCart
from orders import Orders, OrderStatus
from order_details import OrderDetails


def main():
    """
    Demonstrate the e-commerce system functionality
    """
    print("=== E-Commerce System Demo ===\n")
    
    # 1. Create a customer (inherits from User)
    print("1. Creating customer...")
    customer = Customer(
        user_id=1,
        email="juan.perez@email.com",
        password="secure_password_123",
        name="Juan Pérez",
        billing_address="Calle Principal 123, Ciudad, País",
        default_shipping_address="Av. Secundaria 456, Ciudad, País"
    )
    print(f"Created: {customer}")
    
    # 2. Customer login
    print("\n2. Customer login...")
    login_success = customer.login("juan.perez@email.com", "secure_password_123")
    print(f"Login successful: {login_success}")
    
    # 3. Get user session
    print("\n3. Getting user session...")
    session = customer.get_session()
    print(f"Session info: {session}")
    
    # 4. Create shopping cart
    print("\n4. Creating shopping cart...")
    cart = ShoppingCart(cart_id=101)
    print(f"Created: {cart}")
    
    # 5. Add products to cart
    print("\n5. Adding products to cart...")
    cart.add_product_to_cart(1, "Laptop Gaming", 1299.99, 1)
    cart.add_product_to_cart(2, "Mouse Inalámbrico", 29.99, 2)
    cart.add_product_to_cart(3, "Teclado Mecánico", 89.99, 1)
    print(f"Cart after adding products: {cart}")
    print(f"Products in cart: {len(cart.products)}")
    
    # 6. Show cart contents
    print("\n6. Cart contents:")
    for product in cart.products:
        print(f"  - {product['name']}: ${product['price']:.2f} x {product['quantity']} = ${product['total']:.2f}")
    print(f"Total cart value: ${cart.get_total():.2f}")
    
    # 7. Checkout process
    print("\n7. Processing checkout...")
    checkout_summary = cart.check_out()
    print(f"Checkout successful: {checkout_summary['success']}")
    print(f"Total amount: ${checkout_summary['total']:.2f}")
    
    # 8. Create order from checkout
    print("\n8. Creating order...")
    order = Orders(
        order_id=501,
        customer_id=customer.id,
        order_date=datetime.now(),
        status=OrderStatus.PENDING.value,
        price=0.0
    )
    
    # Place the order
    order_placed = order.place_order(checkout_summary)
    print(f"Order placed: {order_placed}")
    print(f"Order details: {order}")
    
    # 9. Create order details
    print("\n9. Creating order details...")
    order_detail = OrderDetails(
        detail_id=1001,
        order_id=order.id,
        shipping_address=customer.default_shipping_address,
        shipping_type="express",
        shipping_cost=15.99,
        billing_address=customer.billing_address
    )
    
    order.add_order_detail(order_detail)
    print(f"Order detail created: {order_detail}")
    
    # 10. Update order status
    print("\n10. Updating order status...")
    order.update_order_status(OrderStatus.PROCESSING.value)
    order.update_order_status(OrderStatus.SHIPPED.value)
    
    # 11. Show final order summary
    print("\n11. Final order summary:")
    summary = order.get_order_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # 12. Demonstrate order detail functionality
    print("\n12. Order detail operations...")
    detail_summary = order_detail.get_detail_summary()
    print(f"Order detail summary: {detail_summary}")
    
    total_with_shipping = order_detail.calculate_total_cost(checkout_summary['total'])
    print(f"Total cost with shipping: ${total_with_shipping:.2f}")
    
    # 13. Test cart operations
    print("\n13. Testing additional cart operations...")
    new_cart = ShoppingCart(cart_id=102)
    new_cart.add_product_to_cart(4, "Monitor 4K", 399.99, 1)
    print(f"New cart: {new_cart}")
    print(f"Is empty: {new_cart.is_empty()}")
    
    # Remove product
    new_cart.remove_product_from_cart(4)
    print(f"After removing product: {new_cart}")
    print(f"Is empty: {new_cart.is_empty()}")
    
    print("\n=== Demo completed successfully! ===")


if __name__ == "__main__":
    main()