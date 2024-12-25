"""
Realizar un programa que escriba los datos de un diccionario en un archivo.

Los datos a guardar son: nombre, apellido, edad, email.

El diccionario puede estar creado previamente o pueden generarlo desde el teclado.

Pueden elegir:

Un diccionario con datos de una sola persona.
Un diccionario que contiene datos de varias personas (usando diccionarios o listas)
"""

#Function with type hinting instead of interface
def write_into_file(persons : dict[int, dict[str, str | int]]) -> bool:

    success = False

    try:
        with open("persons_data.txt", "w") as file:
            for field, person in persons.items():
                file.write(str(field) + " " + " ".join(map(str, person.values())) + "," + "\n")
            file.close()
        success = True
        print("¡Los datos se han guardado correctamente en el archivo!")
    except Exception as e:
        print(f"¡Ocurrió un error ({e}) al escribir en el archivo!")

    return success

persons = {
    1: {"Nombre" : "Bruno", "Apellido" : "Ortuño", "Edad" : 34, "Email" : "bruno.ortuno@gmail.com"},
    2: {"Nombre" : "Esteban", "Apellido" : "Quito", "Edad" : 43, "Email" : "esteban.quito@gmail.com"}
}

write_into_file(persons)
