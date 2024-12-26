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

import os
import platform

person_interface = {"Nombre" : "-", "Edad" : 0, "Ciudad" : "-"}
fields = list(person_interface.keys())
people_interface = {}

people_all_data = people_interface.copy()
people_file_path = "datos.csv"

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  # Clean console for Windows
    else:
        os.system("clear")  # Clean console for macOS y Linux

def show_menu():

    menu = """
╔══════════════════════════════════════════════════════════╗
║   ■ Ingrese el número de la acción que desea realizar:   ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║   1. Mostrar el listado completo de personas             ║
║                                                          ║
║   2. Buscar una persona por su nombre o apellido         ║
║                                                          ║
║   · Mostrar el listado filtrado por:                     ║
║                                                          ║
║       3. Edad                                            ║
║       4. Ciudad                                          ║
║                                                          ║
║   0. Salir                                               ║
╚══════════════════════════════════════════════════════════╝
    """
    print(menu)

def get_int_from_input():

    selected_option = 0

    while True:
        try:
            selected_option = int(input())
            break
        except ValueError:
            print("¡La opción seleccionada debe ser un número entero!")
    
    return selected_option

def get_confirmation_yn(message = "\n¿Desea volver al menu principal? \n Ingrese: SI ó NO\n"):

    selected_option = (input(message)[0]).strip().lower()

    while selected_option != "n" and selected_option != "s":
        print("\n¡La opción seleccionada debe ser SI o NO!")
        selected_option = (input(message)[0]).strip().lower()
    
    return selected_option

def read_from_file(file_path = ""):

    """
    Reads the data from a file given the file path as str and returns it
    """

    content = ""

    try:
        with open(file_path, mode="r", encoding='latin-1') as file:
            content = file.readlines()
            file.close()
    except Exception as e:
        print(f"¡No se pudo leer los datos desde el archivo {file_path} a causa del error: {e}!")

    return content

def export_to_csv_file(people = people_interface):
    
    success = False

    file_name = input("Ingrese el nombre con el que desea guardar el archivo: \n") + ".csv"

    try:
        with open(file_name, mode="w", encoding='latin-1') as file:
            file.write(f"{fields[0]}, {fields[1]}, {fields[2]}\n")
            for person in people.values():
                file.write(f"{person['Nombre']}, {person['Edad']}, {person['Ciudad']} \n")
            file.close()
        print(f"¡El archivo {file_name} fue creado exitosamente!")
        success = True
    except Exception as e:
        print(f"¡No se pudo crear el archivo {file_name} a causa del error: {e}!")

    return success

def load_data_into_dict(file_path = ""):

    """
    Loads the data from a file given the file path as str, puts its content into the proper dictionary structure and returns it.
    """

    data = people_interface.copy()

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

def display_data(people= people_interface, message="■ El listado de las personas registradas es: "):
    if people:
        print(message)

        # Column headers with fixed width
        print(f"""
    | {"id".ljust(3)} | {"Nombre".ljust(35)} | {"Edad".ljust(5)} | {"Ciudad".ljust(25)} |
    {"-" * 80}""")

        # Rows with fixed-width columns
        for id, person in people.items():
            print(f"    | {str(id).ljust(3)} | {person['Nombre'].ljust(35)} | {str(person['Edad']).ljust(5)} | {person['Ciudad'].ljust(25)} |")
    else:
        print("\nNo hay datos para mostrar.")

def filter_data_by(filter = 0):

    filtered_data = people_interface.copy()

    if filter == 3:
        print("\nIngrese la edad minima inclusive que desea que se muestre en el filtrado:")
        min_age = get_int_from_input()
        print("\nIngrese la edad máxima inclusive que desea que se muestre en el filtrado:")
        max_age = get_int_from_input()

        for id, person in people_all_data.items():
            if min_age <= person["Edad"] <= max_age:
                filtered_data[id] = person

    if filter == 4:
        print("\nSeleccione la ciudad de residencia de las personas que desea listar:")
        
        available_cities = []

        for person in people_all_data.values():
            if person["Ciudad"] not in available_cities:
                available_cities.append(person["Ciudad"])
        
        for index, city in enumerate(available_cities):
            print(f"{index+1}. {city}")

        selected_city = available_cities[get_int_from_input() - 1]

        for id, person in people_all_data.items():
            if person["Ciudad"] == selected_city:
                filtered_data[id] = person

    if filter == 2:
        person_name = (input("\nIngrese el nombre o apellido de la persona que desea buscar:\n")).strip().lower()

        for id, person in people_all_data.items():
            names = ((person["Nombre"]).lower()).split()
            if person_name in names:
                filtered_data[id] = person

    return filtered_data

def perform_action(option = 0):
        if option == 1:
            display_data(people_all_data, "\n ■ El listado de todas las personas registradas es: ")
        elif option == 3:
            repeat = "s"
            while repeat == "s":
                filtered_data = filter_data_by(3)
                display_data(filtered_data, "\n ■ El listado de las personas registradas filtradas por ese rango de edad es: ")

                save_into_file = get_confirmation_yn("\n¿Desea guardar el listado actual en un nuevo archivo? \n Ingrese: SI ó NO\n")
                if save_into_file == "s" : export_to_csv_file(filtered_data)

                repeat = get_confirmation_yn("\n¿Desea realizar una nueva busqueda por rango de edad? \n Ingrese: SI ó NO\n")
                clear_console()
        elif option == 4:
            repeat = "s"
            while repeat == "s":
                filtered_data = filter_data_by(4)
                display_data(filtered_data, "\n ■ El listado de las personas registradas en esa ciudad es: ")
                        
                save_into_file = get_confirmation_yn("\n¿Desea guardar el listado actual en un nuevo archivo? \n Ingrese: SI ó NO\n")
                if save_into_file == "s" : export_to_csv_file(filtered_data)
                
                repeat = get_confirmation_yn("\n¿Desea realizar una nueva busqueda por ciudad? \n Ingrese: SI ó NO\n")
                clear_console()
        elif option == 2:
            repeat = "s"
            while repeat == "s":
                filtered_data = filter_data_by(2)
                display_data(filtered_data, "\n ■ El listado de las personas registradas con ese nombre o apellido es: ")

                save_into_file = get_confirmation_yn("\n¿Desea guardar el listado actual en un nuevo archivo? \n Ingrese: SI ó NO\n")
                if save_into_file == "s" : export_to_csv_file(filtered_data)

                repeat = get_confirmation_yn("\n¿Desea realizar una nueva busqueda por nombre o apellido? \n Ingrese: SI ó NO\n")
                clear_console()
        elif option == 0:
            clear_console()
            print("\n¡Adiós! ¡Nos vemos la próxima!")
            global execute
            execute = "n"
            return
        else:
            print("¡Opción inválida!")

def main():
    global people_all_data 
    people_all_data = load_data_into_dict(people_file_path)
    global execute 
    execute = "s"

    while execute == "s":
        show_menu()
        option = get_int_from_input()
        clear_console()
        perform_action(option)
        if option != 0:
            execute = get_confirmation_yn()
            clear_console()

main()