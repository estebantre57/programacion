"""
    Hacer un programa que pregunte la edad de una persona
    y responda lo sig:
        -si la edad es menor o igual a 4, entonces la entrada 
        es gratuita
        -si la edad es menor e igual a 18, pero mayor que 4 entonces la entrada cuesta 200
        -si la edad es mayor que 18, entonces la entrada cuesta 400
"""
try:
    age= int(input("ingresa tu edad:"))
    if age<=4:
        print("tu entrada es gratis")
    elif age >4 and age <=18:
        print("tu entrada tiene un costo de 200")
    elif age >18:
        print("tu entrada tiene un costo de 400")
except: print ("tuviste un error al ingresar tu edad")
    