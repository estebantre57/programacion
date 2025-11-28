"""
    Functions
    
    Las funciones son bloques de codigo diseñados
    para realizar una tarea especifica.
    
    cuando queremos realizar la tarea que se ha definido 
    en una funcion, tenemos que llenar el nombre de 
    la funcion responsable de esto.
    
    DEfinicion de una funcion (syntax)
    
    def name_of_function(parameters):
        actions
"""

def greet_mauro():
    print("Hola mauro, que gusto verte!!! ")
    
    
# Parametros
def greet(username, msj):
    print(f"hola {username}, {msj}!!!")
    
# Argumentos
#greet_mauro()
#greet("joan ", "se te pegaron las cobijas")

"""
    Vamos a realizar un programa que genere
    el nombre completo de una persona.
    
    vamos a pasarle primer nombre, el segundo 
    y el apellido.
    
    La funcion debe regenerar el nombre completo
    y regresarlo
"""

def create_full_name(first_name,  last_name, middle_name=""):
    """
        Docstrings - this function creates the fullname
        of a person given its three names.
    """
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


user_firs_name = input("Escribe tu primer nombre: ").strip().lower()
user_middle_name = input("Escribe tu segundo nombre:").strip().lower()
user_last_name = input("Escribe tus apellidos: ").strip().lower()

# Argumentos posicionales -> positionals Arguments
print(create_full_name(
     user_firs_name,
     user_last_name,
     user_middle_name,))

# Argumentos posicionales -> positionals Arguments
full_name_key = create_full_name(
    user_firs_name,
    user_last_name,
    user_middle_name
)
print(full_name_key)


# Argumentos clave -> keyword Arguments
full_name_key = create_full_name(
    last_name=user_last_name,
    first_name=user_firs_name,
    middle_name=user_middle_name
)
print(full_name_key)


## Parametros opcionales
profe_falso = create_full_name(user_firs_name, user_last_name, )
print(profe_falso)


# Temas para estudiar a futuro
# Funciones: args, kwargs
# Manejo de datos: abrir archivos csv, .json, .yml, .txt, .xls,  
# Argumentos por linea de comandos - sys
# CLI - command line interface
# Generadores, iteradores, yield
# Testing ->