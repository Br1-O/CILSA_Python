"""
Calcular el área de un triángulo
Escribe una función llamada calcular_area_triangulo que reciba la base y la altura de un triángulo y devuelva su área.

Prueba la función con diferentes valores de base y altura.
Puedes incluir manejo de excepciones (opcional).
"""

def calculate_triangle_area(b=0, h=0):
    total_area = 0

    try:
        total_area = (b*h)/2
    except TypeError:
        print("¡La base y altura deben ser números!")
        
    return total_area

print("El triangulo de base 5m y altura 2m tiene: " + str(calculate_triangle_area(5, 2)) + "m de area.")
print("El triangulo de base 2m y altura 5m tiene: " + str(calculate_triangle_area(2, 5)) + "m de area.")
print("El triangulo de base 2m y altura 2m tiene: " + str(calculate_triangle_area(2, 2)) + "m de area.")

print("El triangulo de base hormiga y altura 2m tiene: " + str(calculate_triangle_area("hormiga", 2)) + "m de area.")