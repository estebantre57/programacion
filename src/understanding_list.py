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
El metodo append() toma un solo argumento: el elemento que se desea agregar a la lista.

"""
print("\n Agregar elementos a una lista: metodo append()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) 
motorcycles.append("ducati")
print(motorcycles)

"""
Insertar elementos en una lista
  -insert(): inserta un elemento en una posicion especifica de la lista.
El metodo insert(index, element) toma dos argumentos
"""
print("\n Insertar elementos en una lista: metodo insert()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
print(motorcycles[0])


"""
  Eliminar elementos de una lista
- del: elimina un elemento de la lista en una posicion especifica de la lista.
La declaracion del index elimina el elemento en la posicion especificada
"""

print("\n Eliminar elementos de una lista: declaracion del index\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
del motorcycles[0]
print(motorcycles)


""""
Elimina metodos de una lista
  -pop(): elimina el ultimo elemento de la lista
  El metodo pop() no requiere argumentos y elimina el ultimo elemento de la lista.
"""

print("\n Eliminar elementos de una lista: metodo pop()\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f'La motocicleta que fue eliminada es {popped_motorcycle}.')

"""
  Eliminar elementos de una lista 
     -pop(index): elimina un elemento en una posicion especifica de la lista.
El metodo pop(index) toma un argumento: el indice del elemento que se desea eliminar y devolver.
"""

print("\n Eliminar elementos de una lista: metodo pop(index)\n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(f'La motocicleta que fue eliminada es {popped_motorcycle}.')


"""
  Eliminar elementos de una lista
    -remove(value): elimina la primera ocurrencia de un valor especifico en la lista.
El metodo remove(value) toma un argumento: el valor que se desea eliminar de la lista.
"""

print("\n Eliminar elementos de una lista: metodo remove()\n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati", "honda"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)


# Ejemplo practico de remove()

print("\n Ejemplo practico de remove()\n")

names = ["ana", "juan", "pedro", "maria"]
print(names)
deleted_name = input("\n \n ingresa el nombre que deseas eliminar de la lista: ")
names.remove(deleted_name.strip().lower())
print(names)