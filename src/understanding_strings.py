"""
 un string es de manera sencilla una serie de caracteres.
 En python todo lo que se encuentre dentro de las commillas simples
''o dobles commilas "" es considerado un string

    "Esto es un string"
    'Esto tambien es un string'

    'le dije a un amigo, "¡python es mi lenguaje favorito!"'
    "El lenguaje 'python' lleva el nombre por Monty python,
    no por la serpiente"

"""

name = "clase de programacion"
print(name)
print(name.title())
print(name)


"""

Un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.


El punto . despues de una variable seguida
del metodo title() dice que se tiene que ejecutar
el metodo title() en la variable name.

todo los metodos van seguidos de parentesis 
porque en ocasiones necesitan informacion adicional
para funcionar, lo cual iria dentro de los parentesis.
En esta ocasion el metodo .title() no requiere 
informacion adicional para ejecutarse.


"""

print(name.upper())
print(name.lower())


# concarenacion de STRINGS
print("CONCATENACION DE STRINGS")
first_name= "esteban"
last_name= "trejo"
full_name= first_name +" "+ last_name
print(full_name)

print("Hola, "+ full_name.title() +"!")

