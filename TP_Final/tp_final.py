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
people_interface = {}

people_all_data = people_interface.copy()
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

def get_int_from_input():

    selected_option = 0

    while True:
        try:
            selected_option = int(input())
            break
        except ValueError:
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

def display_data(people = people_interface, message = "■ El listado de las personas registradas es: "):

    print(message)

    print(f"""

| id |      {fields[0]}      | {fields[1]} |      {fields[2]}      |

""")

    for id, person in people.items():
        print(" "+str(id+1)+" | "+ person["Nombre"]+" | "+str(person["Edad"])+" | "+ str(person["Ciudad"])+"\n")

def filter_data_by(filter = 0):

    filtered_data = people_interface.copy()

    if filter == 2:
        print("Ingrese la edad minima inclusive que desea que se muestre en el filtrado:")
        min_age = get_int_from_input()
        print("Ingrese la edad máxima inclusive que desea que se muestre en el filtrado:")
        max_age = get_int_from_input()

        for id, person in people_all_data.items():
            if min_age <= person["Edad"] <= max_age:
                filtered_data[id] = person

    if filter == 3:
        print("Seleccione la ciudad de residencia de las personas que desea listar:")
        
        available_cities = []

        for person in people_all_data.values():
            if person["Ciudad"] not in available_cities:
                available_cities.append(person["Ciudad"])
        
        for index, city in enumerate(available_cities):
            print(f"{index+1}. {city}")

        selected_city = available_cities[get_int_from_input() - 1]

        for id, person in enumerate(people_all_data.values()):
            if person["Ciudad"] == selected_city:
                filtered_data[id] = person

    return filtered_data

def export_to_csv_file(people = people_interface):
    
    success = False

    file_name = input("Ingrese el nombre con el que desea guardar el archivo: \n") + ".csv"

    with open(file_name, "w") as file:
        file.write(f"{fields[0]}, {fields[1]}, {fields[2]}\n")
        for person in people:
            person["Nombre"]

    return success

def perform_action(option = 0):

    if option == 1:
        display_data(people_all_data, "\n ■ El listado de todas las personas registradas es: ")
    elif option == 2:
        display_data(filter_data_by(2), "\n ■ El listado de las personas registradas filtradas por ese rango de edad es: ")
    elif option == 3:
        display_data(filter_data_by(3), "\n ■ El listado de las personas registradas en esa ciudad es: ")
    elif option == 4:
        print("¡Adiós!")
        return
    else:
        print("¡Opción inválida!")
        show_menu()
        option = get_int_from_input()
        perform_action(option)

def main():
    global people_all_data 
    people_all_data = load_data_into_dict(people_file_path)

    show_menu()
    option = get_int_from_input()
    perform_action(option)

main()



