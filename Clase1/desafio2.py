"""
Hola! luego de revisar el material "Entrada y salida de datos", sabremos que podemos solicitar datos con input y con el print podemos armar mensajes:

- usando el operador +,
- anteponiendo f al texto, y tambien
- podemos usar la coma ( , ). Ejemplo: print("Nombre:", nombre) *
*Esta última opción incluye espacios delante y detras del string entre comas y los agrega en el output

Les dejo este desafío para que se animen a completarlo:

Desarrollar un programa que muestre un mensaje de presentación de los datos de una persona.

Para eso, deben solicitar por teclado los datos de una persona: nombre, apellido, edad, correo, y luego mostrar un mensaje final con ellos.
"""

#RESOLUCIÓN:

name = input("Ingrese su nombre: \n")
lastName = input("Ingrese su apellido: \n")
age = input("Ingrese su edad \n")

""" With validation:
validInput = False

while not validInput:
    try:
        age = int(input("Ingrese su edad \n"))
        validInput = True
    except Exception as e:
        print("¡Ingrese un número entero!")
"""

email = input("Ingrese su correo electronico: \n")

print(f"¡Bienvenido! Su nombre es {name} "+ lastName +", tiene " + age + " años, y su correo electronico es:", email)