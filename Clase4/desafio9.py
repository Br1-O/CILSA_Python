"""
Retomar el ejercicio del desafío anterior pero solo CARGAR en la LISTA aquellas notas que estén entre 6 y 10 (inclusive)
 
MOSTRAR el contenido de cada uno de los valores que existen en la LISTA.
"""

print("Ingrese las notas a cargar (que son mayores a 6 y menores a 10): \n (Cuando haya finalizado la carga de notas ingrese 'FIN')\n")

#RESOLUCIÓN

grade = 0
minor_grade = 6
greater_grade = 10
grade_list = []
exit = False

while not exit:
    grade = input("Ingrese una nota: ")
    if grade == "FIN" or grade == "fin":
        exit = True
    else:
        if minor_grade <= float(grade) <= greater_grade:
            grade_list.append(grade)
        else:
            print("¡ERROR! Las notas cargadas deben ser mayores a 6 y menores a 10")

if grade_list:
    print("\nLas notas ingresadas fueron:")
    for grade in grade_list:
        print(grade)
else:
    print("\nNo se han ingresado notas.")