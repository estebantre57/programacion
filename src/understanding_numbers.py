# Numbers

"""
 Integers - Enteros

 son numeros si punto decimal,
 -infty , ...,-3,-2,-1,0,1,2,3,..., infty

  Ejemplo:
    age = 33

 los podemos sumar (+), restar (-), multiplicar (*), dividir (/).

 potencias (**2, **3, etc)

 modulo (dividendo%divisor) 
 
"""

number_1 = 39
number_2 = 13

suma = number_1 + number_2
difference = number_1 - number_2
multiplication = number_1 * number_2
division = number_1 / number_2
modulo = number_1 % number_2
power = number_1 ** 2

print("Suma: ", suma)
print("difference: ", difference)
print("multiplicación: ", multiplication)
print("división: ", division)
print("módulo: ", modulo)
print("power: ", power)

print("la suma es del tipo", type(suma))
print("la diferencia es del tipo", type(difference))
print("la multiplicación es del tipo", type(multiplication))
print("la división es del tipo", type(division))
print("el módulo es del tipo", type(modulo))
print("la potencia es del tipo", type(power))


# floats

"""
 floats - Rales

 son numeros con punto decimal,
  van desde -infty infty

  Ejemplo:

    # Tipado dinamico
    age = 25.5

 los podemos sumar (+), restar (-), multiplicar (*), dividir (/).
 
"""

print(0.1+0.1)
print(0.2-0.2)
print(0.2*0.2)



### imprimir la edad de alguien 
age = 33
message = "esteban tiene " + str(age) + " años"
print(message)

"""
typeError:python no puede reconocer el tipo de informacion que se esta utilizando.

para convertir a string utilizo:str()
"""

message_f = f"esteban tiene {age} años"
print(message_f)