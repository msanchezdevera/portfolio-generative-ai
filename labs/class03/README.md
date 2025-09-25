# E-Commerce System Implementation

Este proyecto implementa un sistema de comercio electrónico basado en el diagrama UML de clases proporcionado.

## Estructura de Clases

### 1. User (`user.py`)
- **Atributos:**
  - `id`: Identificador único del usuario
  - `email`: Correo electrónico del usuario
  - `password`: Contraseña del usuario
  - `lastLogin`: Último inicio de sesión

- **Métodos:**
  - `getSession()`: Obtiene información de la sesión del usuario
  - `login()`: Autentica al usuario

### 2. Customer (`customer.py`)
- **Hereda de:** User
- **Atributos adicionales:**
  - `name`: Nombre del cliente
  - `billingAddress`: Dirección de facturación
  - `defaultShippingAddress`: Dirección de envío por defecto

- **Métodos:**
  - `signUp()`: Registro de nuevo cliente
  - `login()`: Inicio de sesión con lógica específica de cliente

### 3. Shopping Cart (`shopping_cart.py`)
- **Atributos:**
  - `id`: Identificador del carrito
  - `productId`: ID del producto actual
  - Lista interna de productos

- **Métodos:**
  - `addProductToCart()`: Añadir producto al carrito
  - `removeProductFromCart()`: Remover producto del carrito
  - `checkOut()`: Procesar la compra

### 4. Orders (`orders.py`)
- **Atributos:**
  - `id`: Identificador de la orden
  - `customerId`: ID del cliente
  - `orderDate`: Fecha de la orden
  - `status`: Estado de la orden
  - `price`: Precio total

- **Métodos:**
  - `updateOrderStatus()`: Actualizar estado de la orden
  - `placeOrder()`: Crear orden desde carrito
  - `cancelOrder()`: Cancelar orden

### 5. Order Details (`order_details.py`)
- **Atributos:**
  - `id`: Identificador del detalle
  - `orderId`: ID de la orden asociada
  - `shippingAddress`: Dirección de envío
  - `shippingType`: Tipo de envío
  - `shippingCost`: Costo de envío
  - `billingAddress`: Dirección de facturación
  - `createdDate`: Fecha de creación

- **Métodos:**
  - `cancelOrder()`: Cancelar este detalle específico

## Relaciones entre Clases

1. **Customer hereda de User** (relación de herencia)
2. **Customer tiene relación 1:0..* con Shopping Cart**
3. **Customer tiene relación 1:1 con Orders**
4. **Orders tiene relación 1:1 con Order Details**

## Uso del Sistema

### Ejecutar la Demostración
```bash
python main_demo.py
```

### Ejemplo de Uso Básico

```python
from customer import Customer
from shopping_cart import ShoppingCart
from orders import Orders

# Crear cliente
customer = Customer(
    user_id=1,
    email="cliente@email.com",
    password="password123",
    name="Juan Pérez",
    billing_address="Dirección de facturación",
    default_shipping_address="Dirección de envío"
)

# Iniciar sesión
customer.login("cliente@email.com", "password123")

# Crear carrito
cart = ShoppingCart(cart_id=101)

# Añadir productos
cart.add_product_to_cart(1, "Producto 1", 29.99, 2)

# Procesar compra
checkout = cart.check_out()

# Crear orden
order = Orders(order_id=501, customer_id=customer.id)
order.place_order(checkout)
```

## Características Implementadas

- ✅ Herencia (Customer extiende User)
- ✅ Encapsulación (propiedades privadas con getters/setters)
- ✅ Composición (Orders contiene OrderDetails)
- ✅ Manejo de estados (OrderStatus enum)
- ✅ Validación de datos
- ✅ Manejo de errores
- ✅ Documentación completa
- ✅ Ejemplo funcional completo

## Archivos

- `user.py` - Clase base User
- `customer.py` - Clase Customer que hereda de User
- `shopping_cart.py` - Clase ShoppingCart para manejo de carrito
- `orders.py` - Clase Orders para manejo de órdenes
- `order_details.py` - Clase OrderDetails para detalles de órdenes
- `main_demo.py` - Demostración completa del sistema
- `README.md` - Esta documentación

## Estados de Orden

El sistema incluye los siguientes estados de orden:
- `pending` - Pendiente
- `confirmed` - Confirmada
- `processing` - Procesando
- `shipped` - Enviada
- `delivered` - Entregada
- `cancelled` - Cancelada

## Notas de Implementación

1. **Seguridad**: En un entorno de producción, las contraseñas deberían estar hasheadas
2. **Base de Datos**: Esta implementación usa estructuras en memoria; en producción se usaría una base de datos
3. **Validaciones**: Se incluyen validaciones básicas que pueden expandirse según necesidades
4. **Logging**: Se usa `print()` para simplicidad; en producción se usaría un sistema de logging apropiado