"""
Las listas tambien pueden almacenar numeros y de hecho
son ideales para almacenarlos
Python ofrece cantidad de funciones integradas para 
trabajar con listas de numeros

por ejemplo, funcion range() que genera una lista de numeros

"""

# la funcion range() genera una lista de numeros
# en un rango determinado
# por ejemplo, range(1, 10) genera numeros del 0 al 9
numbers = list(range(10))
print(numbers) # salida [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers)) # salida <class 'list'>

# podemos realizar lo mismo con un for loop:
for num in range(10):
    print(num)
    # print(type(num)) # salida <class 'int'> 

print("\nNumeros del 1 al 4:")
for num in range(1, 5):
    print(num)
    # print(type(num)) # salida <class 'int'>

numbers_1_to_4= list(range(1, 5))
print(numbers_1_to_4) # salida [1, 2, 3, 4]

print("\nNumeros impares:")
for num in range(1, 10, 2):# numeros impares del 1 al 9
    print(num)
odd_numbers = list(range(1, 10, 2))
print(odd_numbers) # salida [1, 3, 5, 7, 9]

print("\nNumeros pares:")
for num in range(2, 10, 2):# numeros pares del 2 al 8
    print(num)
even_numbers = list(range(2, 10, 2))
print(even_numbers) # salida [2, 4, 6, 8, 10]

# podemos crear cualquier tipo de lista de numeros
# Utilizando range() y list()
print("\n Primeros 10 numeros al cuadrado:")
squares = []
for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares) # salida [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Metodos built-in para listas de numeros
print("\nMetodos built-in para listas de numeros:")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Lista de digitos: {digits}")
print(f"Valor minimo: {min(digits)}") # salida 0
print(f"Valor maximo: {max(digits)}") # salida 9
print(f"Suma de todos los digitos: {sum(digits)}") # salida 45





