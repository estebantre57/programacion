message = "This is my first python variable "
another_message = 'I am really, really, really happy'
message = "I love python"

# print() -> use to show messages in terminal
# print() -> se utiliza para mostrar mensajes en la terminal
print(message)
print(another_message)
print(message, another_message, message)
print(another_message, message)

print(message)

"""

los nombres de variables en python deben nomrarse solo con:
 -letras,numeros y guiones bajos (espacios)
 -deben comenzar con una letra o un guion bajo, pero no con un numero:
      ejemplo correcto: message_1( :) )
      ejemplo incorrecto: 1_message (x)
 -no utilizar espacios para separar palabras en un nombre de variable
 -no utilizar palabras reservadas de python para nombrar variables o archivos
 -deben de ser cortos pero descriptivos
 -deben de ser en ingles 
 -nombres de las variables en minusculas
 
 """

esteban_message = "hola, soy esteban y estoy aprendiendo python"
print(esteban_message)

""""
I love python
I am really, really, really happy
I love python I am really, really, really happy I love python
I am really, really, really happy I love python
I love python
Traceback (most recent call last):
  File "C:/Users/esteb/projects/programacion/src/understanding_variables.py", line 31, in <module>
    print(esteban_mesage)
          ^^^^^^^^^^^^^^
NameError: name 'esteban_mesage' is not defined. Did you mean: 'esteban_message'?
nameError: significa que olvidamos establecer el nombre de una variable antes de usarla

"""