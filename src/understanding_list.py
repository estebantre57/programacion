# listas
# una lista es una coleccion ordenada y mutable de elementos.
# se pueden crear listas usando corchetes [] y separando los elementos con comas.
fruits = ["manzana", "banana", "cereza"]
print(fruits)  # salida: ['manzana', 'banana', 'cereza']

# Acceso de elementos
print(fruits[0].upper())  # salida: MANZANA
print(fruits[1])  # salida: banana
print(fruits[2].title())  # salida: cereza

# print(fruits[3])  # Esto generará un error de indice fuera de rango

# acceder al ultimo elemento
print(fruits[-1])  # salida: cereza
print(fruits[-2])  # salida: banana
print(fruits[-3])  # salida: manzana


my_favorite_fruit = fruits[0].title()
messages = f'mi fruta favorita es {fruits[0].title()}.'
print(messages)  # salida: mi fruta favorita es Manzana.

"""
Agregar elementos a una lista
-append(): agrega un elemento al final de la lista.

"""
print("\n Agregar elementos a una lista: metodo append()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) 
motorcycles.append("ducati")
print(motorcycles)

"""
Insertar elementos en una lista
  -insert(): inserta un elemento en una posicion especifica de la lista.
"""
print("\n Insertar elementos en una lista: metodo insert()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
print(motorcycles[0])

