"""
Realizar un programa en el cual:

> Se ingrese por teclado 2 números y haga una división, mostrando su resultado en pantalla.
> Si los datos ingresado por teclado NO son numeros, mostrar algún mensaje al usuario informado el error.
> Si la división es sobre cero, capturar el error y mostrar al usuario un mensaje indicando ese error.
"""

#RESOLUCIÓN:

result = 0
print("Ingrese dos números para poder realizar su división: \n")

try:
    num1 = float(input("Ingrese el número del dividendo: "))
    num2 = float(input("Ingrese el número del divisor: "))

    result = num1/num2
except ZeroDivisionError:
    print("\n¡No puede dividir por cero!")
except ValueError:
    print("\nDebe ingresar sólo números para poder realizar la operación.")
except Exception:
    print("\nOcurrió un error, la operación no pudo realizarse correctamente.")
else:
    print(f"\nEl resultado de la división {num1} / {num2} es: {result:.2f}")