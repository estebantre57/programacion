"""
  Vamos a realizar un programa que pregunte al usuario
  por su edad y muestra un mensaje
  diferente segun el rango de edad en el que
  se encuentre:
"""

try:
    age = int(input("por favor,introduce tu edad: "))
    
except:
    age = -1
    print("Tuviste un error, ingresaste un caracter no valido")
    
if age >= 100:
        print("Tienes mas de un siglo de vida.")
elif age >= 18 and age <= 100:
    print("Eres mayor de edad")
elif age < 18 and age >= 0:
        print("Eres menor de edad. ")
else:
    print("Tuviste un error")
        
print("Hola Esteban")


# Multiple if
guisos = ["deshebrada", 'asado', "salsa verde", "pozole"]
if "asado" in guisos:
    print("si hay asado")
else:
    print("no hay asado")
    
if "tamales" in guisos:
    print("Hay tamales")
else:
    print("no hay tamales")
    
if "salsa verde" in guisos:
    print("si hay salsa verde")
    