"""
Desarrollar un programa que tenga un diccionario con nombres, apellidos y DNIs.

A continuación, se deberá ingresar 3 personas con los datos y al final informar su contenido por cada persona.
 
Ejemplo:

#1 Creamos un diccionario vacío para almacenar los datos de las personas

#2 Pedimos al usuario que ingrese los datos para 3 personas

for i in range(3):

    #2.1 INPUT del nombre   

    #2.2 INPUT del apellido 

    #2.3 INPUT del dni

    #2.4 Creamos un nuevo diccionario con los datos ingresados, por ejemplo : persona = { "nombre": nombre, "apellido": apellido, "dni": dni }

    #2.5 Agregamos el diccionario de la persona al diccionario general de personas, por ejemplo: personas[i+1] = persona

#3 Mostramos los datos ingresados para cada persona: podemos usar items():
"""

person_interface = {"Nombre" : "-", "Apellido" : "-", "DNI" : 00000000}
persons_interface = {1: person_interface}
fields = list(person_interface.keys())

persons = persons_interface
max_persons = 3

for i in range(max_persons):
    person = person_interface.copy()
    person["Nombre"] = input('\nIngrese el nombre de la persona: \n')
    person["Apellido"] = input('Ingrese el apellido de la persona: \n')
    while True:
        try:
            person["DNI"] = int(input('Ingrese el número de DNI de la persona: \n'))
            break
        except:
            print("¡El número de DNI sólo puede contener números!")
    persons[i+1] = person

if persons:

    print("\n El listado de las personas ingresadas es: \n")

    for key, person in persons.items():
        
        print(str(key) + " - " + fields[0] + ": " + person["Nombre"] + " | " + fields[1] + ": " + person["Apellido"] + " | " + fields[2] + ": " + str(person["DNI"]) + "\n")

    print("\n El listado de las personas ingresadas que superan los 40 millones en su DNI es: \n")

    for key, person in persons.items():

        if person["DNI"] > 40000000:
            print(str(key) + " - " + fields[0] + ": " + person["Nombre"] + " | " + fields[1] + ": " + person["Apellido"] + " | " + fields[2] + ": " + str(person["DNI"]) + "\n")
else:
    print("\nNo se han ingresado personas.")