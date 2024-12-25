"""
Retomar el desafío anterior e indicar cuantos y que DNI superan el valor de 40 millones.
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