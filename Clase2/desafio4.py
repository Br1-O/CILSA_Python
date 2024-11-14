"""
Realizar un programa en el cual se ingresen dos numeros e informe si el primero es múltiplo del segundo.

En caso contrario deberá generar un mensaje adecuado.
"""

#RESOLUCIÓN:

print("Ingrese dos números para chequear si el primer número es múltiplo del segundo número: \n")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo numero: "))

if(num1%num2 == 0):
    print(f"{num1} es múltiplo de {num2}.")
else:
    print(f"{num1} no es múltiplo de {num2}.")