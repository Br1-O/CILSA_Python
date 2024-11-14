"""
Realizar un programa en el cual se ingrese un numero entero e informe si es par.

En caso que no sea par también deberá informar al respecto.

Ayuda: para obtener un numero desde el teclado puedo usar int junto con el input, por ejemplo: numero = int(input("Ingrese un número: "))
"""

#RESOLUCIÓN:

num = int(input("Ingrese un numero para chequear si es par: "))

if num%2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")