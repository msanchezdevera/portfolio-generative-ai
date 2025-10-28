from typing import List, Optional, Tuple

def compute_stats(nums: List[float]) -> Optional[Tuple[float, float, float]]:
    """
    Calcula estadísticas básicas de una lista de números.
    
    Esta función calcula el valor mínimo, máximo y promedio de una lista
    de números de punto flotante.
    
    Args:
        nums: Lista de números de punto flotante para analizar.
              No debe estar vacía.
    
    Returns:
        Una tupla con (mínimo, máximo, promedio) si la lista tiene elementos.
        None si la lista está vacía.
    
    Raises:
        TypeError: Si nums no es una lista o contiene elementos no numéricos.
        ValueError: Si nums contiene valores NaN o infinitos.
    
    Examples:
        >>> compute_stats([1.0, 2.0, 3.0, 4.0, 5.0])
        (1.0, 5.0, 3.0)
        
        >>> compute_stats([10.5])
        (10.5, 10.5, 10.5)
        
        >>> compute_stats([])
        None
        
        >>> compute_stats([-5.0, 0.0, 5.0])
        (-5.0, 5.0, 0.0)
    """
    # Validación: lista vacía
    if not nums:
        return None
    
    # Validación: tipo de entrada
    if not isinstance(nums, list):
        raise TypeError(f"Se esperaba una lista, se recibió {type(nums).__name__}")
    
    # Validación: elementos numéricos y valores válidos
    for i, x in enumerate(nums):
        if not isinstance(x, (int, float)):
            raise TypeError(f"Elemento en índice {i} no es numérico: {type(x).__name__}")
        if x != x:  # Verificar NaN (NaN != NaN es True)
            raise ValueError(f"Elemento en índice {i} es NaN")
        if x == float('inf') or x == float('-inf'):
            raise ValueError(f"Elemento en índice {i} es infinito")
    
    # Cálculo de estadísticas
    mn = nums[0]
    mx = nums[0]
    s = 0.0
    
    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
        s += x
    
    avg = s / len(nums)
    
    return mn, mx, avg


# Ejemplos de uso
if __name__ == "__main__":
    print("=== Ejemplos de uso de compute_stats ===\n")
    
    # Ejemplo 1: Lista normal de números
    print("1. Lista de números enteros:")
    result = compute_stats([1.0, 2.0, 3.0, 4.0, 5.0])
    print(f"   Input: [1.0, 2.0, 3.0, 4.0, 5.0]")
    print(f"   Output: {result}")
    print(f"   Min: {result[0]}, Max: {result[1]}, Avg: {result[2]}\n")
    
    # Ejemplo 2: Un solo elemento
    print("2. Un solo elemento:")
    result = compute_stats([10.5])
    print(f"   Input: [10.5]")
    print(f"   Output: {result}\n")
    
    # Ejemplo 3: Lista vacía
    print("3. Lista vacía:")
    result = compute_stats([])
    print(f"   Input: []")
    print(f"   Output: {result}\n")
    
    # Ejemplo 4: Números negativos
    print("4. Números negativos y cero:")
    result = compute_stats([-5.0, 0.0, 5.0])
    print(f"   Input: [-5.0, 0.0, 5.0]")
    print(f"   Output: {result}\n")
    
    # Ejemplo 5: Números decimales
    print("5. Números decimales:")
    result = compute_stats([1.5, 2.7, 3.2, 4.8, 5.1])
    print(f"   Input: [1.5, 2.7, 3.2, 4.8, 5.1]")
    print(f"   Output: {result}\n")
    
    # Ejemplo 6: Manejo de errores
    print("6. Manejo de errores:")
    try:
        compute_stats("not a list")
    except TypeError as e:
        print(f"   TypeError capturado: {e}\n")
    
    try:
        compute_stats([1, 2, "three"])
    except TypeError as e:
        print(f"   TypeError capturado: {e}\n")