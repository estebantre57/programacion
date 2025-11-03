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




# Syntax error con strings
message = "una fortaleza de python es su comunidad"
print(message)

message = "una fortaleza de 'python' es su comunidad"
print(message)

# concarenacion con f-strings
famous_person= "Esteban Trejo"
quote = "python is love"

# concatenacion convencional
message = famous_person +" una vez dijo "+ quote 
print(message)

# concatenacion con fstrings
"""
() - se llaman paréntesis
{} - llaves
[] - corchetes
"""
message_f_string = f"{famous_person} una vez dijo {quote}"
print(message_f_string)

#actividad 
"""
 1)elige un personaje famoso e igualado a una variable de tipo string
 2)elige una frase famosa de esa persona e igualala a una variable de tipo string
 3)Genera un mensaje con las dos variables utilizando f-strings
 4)Imprime el mensaje

"""

famous_person= "aristoteles"
quote = "La sabiduría comienza en la reflexión."
message_f_string = f"{famous_person} una vez dijo: '{quote}'"
print(message_f_string)


# Whitespaces
"""
Whitespaces se refiere a cualquier caracter que no se imprime,
es decir, un tabulador y finales de linea. los whitespaces
se utilizan comunmente para organizar las salidas (print)
de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

# ejemplos
print("Python")
print("\tPython")  # tabulador
print("\t\tPython")  # tabulador 

# Ejemplos de salto de linea
print("languajes de programacion:\nPython\nJavaScript")
print("carlos")
print("tovar")




print(message)






# Eliminacion de espacios en blanco
programming_language = " python javascript "
print(programming_language)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())
