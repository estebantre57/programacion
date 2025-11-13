# List comprehensions

"""
Una list comprehension combina el for loop
y la creacion de nuevos elementos en una 
sola linea de codigo y tambien, automaticamente
agrega el nuevo elemento en la lista, es decir,
sin utilizar append
"""

Squeres=[value**2 for value in range(1,11)]
print(Squeres)

# Numeros pares con el range
even_number_0_100 = list(range(0,101,2))
print(even_number_0_100)

# Numeros pares utilizando list comprehension
evens_number_0_100 = [value for value in range(0,101)if value%2 > 0]
print (f"evens list comprehension:", evens_number_0_100)




