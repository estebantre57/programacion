"""
    Vamos a realizar un programa que sume pesos mexicanos 
    hasta que el usuario escriba la palabra "salir"
    
    El programa tambien debe decirme cuantos numeros
    ingrese el usuario, cual fue el minimoy cual fue
    el maximo.
    
"""

sum_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:
    
    print("ingresa la palabra salir para terminar" )
    user_input = input("ingresa una cantidad en pesos mexicanos:")
    
    # Centinel
    if user_input == 'salir':
        break
    
    try:
        quantity = float(user_input)
    except ValueError:
        print("cantidad no valida, ingresa nuevamente")
        continue
    except KeyboardInterrupt:
        break
    
    counter = counter + 1 # Estructura contadora
    sum_numbers += quantity # Sum_number = sum_number + quantity # Estructura acumuladora
    
    if minimum is None or quantity < minimum:
        minimum = quantity
    if minimum is None or quantity < maximum:
        minimum = quantity
        
print("SUM", sum_numbers)
print("CONTADOR", counter)
print("MAXIMO", maximum)
print("MINIMO", minimum)