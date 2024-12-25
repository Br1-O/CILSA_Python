"""
Un profesor debe cargar un conjunto de notas de exámenes.

Debemos realizar un programa que pueda cargar el nombre y la nota de cada alumno utilizando DICCIONARIOS.

Luego debo informar el nombre y la nota tanto de los aprobados como de los desaprobados.

Aquellas notas que sean mayores a 6 y menores o iguales a 10 están aprobadas.
"""

pass_above_grade = 6
min_grade = 1
greater_grade = 10

student_interface = {"Nombre" : "-", "Nota" : 1, "Estado" : "Desaprobado"}
students = {1:student_interface}

current_student = 1
exit = False

while not exit:

    student = student_interface.copy()

    student["Nombre"] = input('Ingrese el nombre del alumno: | Para salir del programa ingrese "fin":\n')

    if student["Nombre"] == "FIN" or student["Nombre"] == "fin":
        exit = True
    else:
        while True:
            try:
                student["Nota"]  = float(input("Ingrese la nota del alumno:\n"))
                break
            except ValueError:
                print("¡La nota del alumno debe ser un número!")

        if min_grade <= float(student["Nota"]) <= greater_grade:
            if pass_above_grade < float(student["Nota"]):
                student["Estado"] = "Aprobado"
            students[current_student] = student
            current_student += 1
        else:
            print("¡ERROR! Las notas cargadas deben ser mayores a 1 y menores a 10")

if students:
    fields = list(student_interface.keys())

    print("\n El listado de los alumnos ingresados es: \n")

    for key, student in students.items():
        
        print(str(key) + " - " + fields[0] + ": " + student["Nombre"] + " | " + fields[1] + ": " + str(student["Nota"]) + " | " + fields[2] + ": " + student["Estado"] + "\n")
else:
    print("\nNo se han ingresado notas.")