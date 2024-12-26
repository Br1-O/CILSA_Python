"""
Objetivo: Crear un programa en Python que permita filtrar datos de personas según un rango de edades. Pueden utilizar el archivo datos.csv
 
Requisitos:

Leer el archivo CSV:

Cargar los datos del archivo datos.csv en una estructura que te resulte cómoda (por ejemplo, una lista de diccionarios).

Pedir datos al usuario:

Solicitar al usuario que ingrese un rango de edades (edad mínima y edad máxima).
Filtrar la información:

Mostrar los datos completos de las personas que se encuentren dentro del rango de edades especificado.

Opciones adicionales (opcionales):

Agregar un menú de opciones.
Agregar más filtros, como búsqueda por nombre o ciudad.
Usar otro archivo .csv con una estructura diferente, pero implementar algún tipo de filtrado.
Guardar los resultados filtrados en un nuevo archivo CSV o TXT.
"""



person_interface = {"Nombre" : "-", "Edad" : 0, "Ciudad" : "-"}
fields = list(person_interface.keys())
people_interface = {1:person_interface}

people_file_path = "datos.csv"

def show_menu():

    menu = """

    ■ Ingrese el número de la acción que desea realizar:

    1. Mostrar el listado completo de personas

    · Mostrar el listado filtrado por:

        2. Edad
        3. Ciudad

    4. Salir

    """
    print(menu)

def get_selected_option():

    selected_option = 0

    while True:
        try:
            selected_option = int(input())
            break
        except TypeError:
            print("¡La opción seleccionada debe ser un número entero!")
    
    return selected_option

def read_from_file(file_path = ""):

    """
    Reads the data from a file given the file path as str and returns it
    """

    content = ""

    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            file.close()
    except Exception as e:
        print(f"¡No se pudo leer los datos desde el archivo {file_path} a causa del error: {e}!")

    return content

def load_data_into_dict(file_path = ""):

    """
    Loads the data from a file given the file path as str, puts its content into the proper dictionary structure and returns it.
    """

    data = people_interface

    try:
        for index, line in enumerate(read_from_file(file_path)):
            if index == 0: 
                continue

            #create list for line content
            line_content = line.split(",")

            person = person_interface.copy()

            #load data from content list into person instance
            person["Nombre"] = line_content[0].strip() 
            person["Edad"] = int(line_content[1].strip())
            person["Ciudad"] = line_content[2].strip() 

            #load person into data dict
            data[index] = person
    except Exception as e:
        print(f"¡No se pudo cargar los datos desde el archivo {file_path} a causa del error: {e}!")

    return data

def display_data(people = people_interface):

    print("■ El listado de las personas registradas es: ")

    print(f"""

| id |      {fields[0]}      | {fields[1]} |      {fields[2]}      |

""")

    for id, person in people.items():
        print(" "+str(id)+" | "+ person["Nombre"]+" | "+str(person["Edad"])+" | "+ str(person["Ciudad"])+"\n")


def perform_action(option = 0):

    if option == 1:
        display_data(load_data_into_dict(people_file_path))
    elif option == 2:
        return
    elif option == 3:
        return
    elif option == 4:
        print("¡Adiós!")
        return
    else:
        print("¡Opción inválida!")
        show_menu()
        option = get_selected_option()
        perform_action(option)

def main():
    show_menu()
    option = get_selected_option()
    perform_action(option)

main()



