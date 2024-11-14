"""
Crear un programa que permita ingresar varios números enteros positivos.

El programa debe mostrar el número más grande de los que se ingresaron.

Instrucciones:

El programa pedirá números enteros positivos uno por uno.
Cuando se ingrese el número 0, el programa debe finalizar.
El programa mostrará el número más grande que se haya ingresado (excepto el 0).

Nota: El programa comienza con un valor inicial de -1 para el número más grande. Este valor no afecta el resultado, ya que siempre se actualiza con el primer número que sea mayor a -1.
"""

#RESOLUCIÓN:

greatest_num = -1

print(
    """
Ingrese cuantos números desee para encontrar el máximo entre ellos: 
(cuando termine de ingresar números ingrese el número 0 para realizar el cálculo)
    """)

while True:
    num = int(input("Ingrese un número: "))
    if num == 0:
        break
    else:
        if num > greatest_num:
            greatest_num = num

print(f"\nEl mayor de los números ingresados es: {greatest_num}.")

