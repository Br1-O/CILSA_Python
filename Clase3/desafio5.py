"""
Realizar un programa en el cual se ingrese

1. El límite inferior de un intervalo
2. El límite superior del mismo intervalo
3. Un valor entero
 
Indicar si el valor entero ingresado en el punto 3 se encuentra dentro del intervalo definido por los valores del punto (1) y del punto (2).
"""

#RESOLUCIÓN:

init = int(input("Ingrese el límite inferior del intervalo: "))
end = int(input("Ingrese el límite superior del intervalo: "))
num = int(input("Ingrese un número entero para chequear si está incluido dentro del intervalo: "))

is_included = False

for i in range(init, (end + 1)):
    if i == num:
        is_included = True

if is_included:
    print(f"El número {num} está incluido dentro del intervalo [{init}, {end}].")
else:
    print(f"El número {num} no está incluido dentro del intervalo [{init}, {end}].")