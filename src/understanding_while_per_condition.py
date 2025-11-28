"""
    vamos a realizar un programa que 
    defina un PIN como contraseña
    
    Despues vamos a darle tres intentos al 
    usuario para escribir el pin.
    
    Si el usuario escribe correctamente el 
    pin , el programa debe mostrar un 
    mensaje de acceso permitido.
    
    si el usuario se euivoca, el programa 
    debe decirle cuantos intentos le quedan
    y en caso de que no le queden intentos 
    el mensaje debe decirle mensaje denegado,
    excediste tus intentos.


"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
intents = 0

while intents < MAX_ATTEMPTS:

    user_pin = input("Escribe tu PIN:")
    
    if user_pin == CORRECT_PIN:
        print("Acceso permitido. ")
        break
    else:
        intents+=1
        remaining_attemps = MAX_ATTEMPTS-intents
        if remaining_attemps>0:
            print(f"PIN INCORRECTO, te quedan {remaining_attemps} intentos ")
        else:
            print("Acceso denegado")
    