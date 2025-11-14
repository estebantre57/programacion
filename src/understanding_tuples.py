"""
    Las tuplas son listas de elementos que no pueden cambiar
    su tamaño. Las tuplas son listas inmutables
"""

"""
    Se utilizan los () para definir una tupla

    Ejemplo:
"""

#Rectangulo (largo, ancho)
rectangle_dimensions = (200,50)
print(rectangle_dimensions)
print(f"largo: {rectangle_dimensions[0]} mm") # 200
print(f"ancho: {rectangle_dimensions[1]} mm") # 50

# Vamos a intentar modificar una tupla 
# rectangle_dimensions[0] = 250 # Esto genera un error
# rectangle_dimensions[1] = 100  # Esto genera un error

for dimension in rectangle_dimensions:
    print(dimension)
    
"""
    No podemos modificar una tupla, ni tampoco agregar/eliminar
    elementos. Lo que si podemos hacer es cambiar la 
    asignacion a una variable que almacena una tupla
"""

rectangle_dimensions = (300,150) # Tupla
