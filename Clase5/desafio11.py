"""
Verificación de DNI en el sistema.
■ Descripción:
Crea una lista predefinida de números de DNI, por ejemplo: [12345678, 87654321, 11111111, 22222222].
El programa deberá permitir al usuario ingresar un número de DNI y verificar si está registrado en la lista.

■ Funcionalidades requeridas:

> Si el DNI se encuentra en la lista:
Mostrar el mensaje: "El DNI xxx se encuentra registrado en nuestro sistema."
> Si el DNI no se encuentra:
Mostrar el mensaje: "El DNI xxx no está registrado en nuestro sistema."
> Si la entrada no es un número:
Mostrar el mensaje: "Lo lamento, xxx no es un número."
> Si el programa se ejecuta sin errores:
Mostrar el mensaje: "¡El programa se ejecutó perfectamente!"

■ Mensajes adicionales:
Siempre mostrar un mensaje final al salir del programa, como: "Gracias por utilizar nuestro sistema."

■ Opcional:
Permitir al usuario realizar múltiples búsquedas hasta que decida salir escribiendo "salir".
"""

#RESOLUCIÓN:

db_DNI = [35123321, 37234432, 39345543, 41789987, 44890098]
user_input = 0

while user_input != "salir":
    try:
        user_input = ((input("""
════════════════════════════════════════════════ · ════════════════════════════════════════════════

» Por favor, ingrese el número de DNI (sin puntos) para verificar si existe en nuestro registro: 
(Una vez que haya concluido ingrese "salir")

"""))).lower()
        
        if(user_input == "salir"):
            continue
        
        user_input = int(user_input) 
        
        if user_input in db_DNI:
            print(f"\n■ El DNI {user_input} se encuentra registrado en nuestro sistema.")
        else:
            print(f"\n■ El DNI {user_input} no está registrado en nuestro sistema.")
            
    except ValueError:
        print(f"\n■ Lo lamento, {user_input} no es un número.")
    else:
        print(" \n*** ¡El programa se ejecutó perfectamente! ***")
    finally:
        if user_input == "salir":
            print("\n*** ¡Gracias por utilizar nuestro sistema! ***")