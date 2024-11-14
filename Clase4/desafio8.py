"""
Un profesor debe cargar un conjunto de notas de exámenes.

Debemos realizar un programa que nos permita CARGAR un conjunto de notas de exámenes utilizando una LISTA.

Luego MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.

PD.: Usted define si el programa le solicita al usuario la cantidad de notas a cargar o que ingrese el valor 0 para finalizar la carga, por ejemplo.
"""

#RESOLUCIÓN:

print("Ingrese las notas a cargar: \n (Cuando haya finalizado la carga de notas ingrese 'FIN')\n")

grade = 0
grade_list = []
exit = False

while not exit:
    grade = input("Ingrese una nota: ")
    if grade == "FIN" or grade == "fin":
        exit = True
    else:
        grade_list.append(grade)

if grade_list:
    print("\nLas notas ingresadas fueron:")
    for grade in grade_list:
        print(grade)
else:
    print("\nNo se han ingresado notas.")