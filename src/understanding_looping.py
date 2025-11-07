
magicians = ["ron", "harry", "snape", "hermione"]

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()}, ese fue un gran hechizo!")
    print("\n")
    
print("gracias a todos, fue un gran espectáculo!")

"""
    Identacion.
    Python utiliza la identación para determinar
    cuando una linea de codigo esta conectada
    a la linea de codigo anterior.
    
    Basicamente, se utiliza 4 espacios en blanco
    para obligarnos a escribir codigo ordenado
    y estructurado.
"""

# No olvidemos identar (donde se necesita)
# Ejemplo
magicians = ['alice', 'david', 'jorge']
for magician in magicians:
# Print(magician)  # Error -el for necesita almenos un elemento 
    print(magician) # Solución
    
# Identification Error
# Logical Error
magicians = ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:
    print(magician)
#print(f"great {magician}, I can't wait to see your next trick!")  # Correcto   
    print(f"great {magician}, I can't wait to see your next trick!")  # Correcto   
    
# Identacion innecesaria
messages = "hello Esteban"
# print(messages)  # Error - No necesita identacion


# logica error
magicians = ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:
    print(magician)
    print(f"great {magician}, I can't wait to see your next trick!")  # Error - se imprime varias veces
print("Thank you everyone, that was a great show!")  # Solución identar a la izquierda


# Error de sintaxis
magicians = ['alice', 'david', 'jorge', 'candelario']
for magician in magicians:  # Error - falta dos puntos
    print(magician)
