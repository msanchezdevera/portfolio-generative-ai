""" 
Generar una funcion fizzBuzz y documentar su uso

La función fizzBuzz toma un número entero n y devuelve una lista de cadenas.
Para cada número de 1 a n, si el número es divisible por 3, se agrega "Fizz" a la lista,
si es divisible por 5, se agrega "Buzz", y si es divisible por ambos, se agrega "FizzBuzz".

Ejemplo de uso:
```python
result = fizzBuzz(15)
print(result)
```
Esto imprimirá:
```
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```
"""

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result