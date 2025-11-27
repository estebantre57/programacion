"""
    doctring for understanding_while_loop_104
    
    utilizamos el while loop para ejecutar un bloque de codigo mientras 
    una condicion sea verdadera
    
    Estructura basica del while loop en python 
    
        while condicion:
            # bloque de codigo a ejecutar
            
    """
    
# Ejemplo basico de un while loop
# Verificar si un numero esta en un
# rango especifico (10 y entre 20)

while True: # while loop infinito
    try:
        number = int(input("ingrese un numero entre 10 y 20:"))
    
        if number < 20 and number > 10:
            print("Numero dentro de el rango,felicitaciones!")
            break
        else:
            print("Numero fuera de el rango, intentalo de nuevo!")
    except ValueError:
        print("Entrada invalida, por favor ingrese un numero entero")
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
        
print("saliste del while yupi")

              
        
        
        
        
        
        
        
        