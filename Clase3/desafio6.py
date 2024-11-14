"""
Realizar un programa donde se ingresen 5 números e informe el promedio de los números ingresados.
"""

print("Ingrese 5 números para calcular su promedio: \n")

maxNumbers = 5
total = 0

for i in range(maxNumbers):
    num = int(input("Ingrese un número: "))
    total += num

avg = total/maxNumbers

print(f"El promedio de los números ingresados es: {avg}.")