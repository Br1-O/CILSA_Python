"""
Contar vocales
Escribe una función llamada contar_vocales que reciba una palabra y devuelva cuántas vocales contiene.

La función debe ignorar si las letras son mayúsculas o minúsculas.
Usen la siguiente variable que guarda todas las vocales: vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
Al final, prueba la función con diferentes palabras.
(Nota: Asumimos que el usuario ingresará una palabra).
"""

def count_vowels(word = ""):
    vowels_list = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    vowels_in_word = 0
    
    for letter in word.strip().lower():
        if letter in vowels_list:
            vowels_in_word += 1
    return vowels_in_word

print("casa tiene: " + str(count_vowels("casa")) + " vocales.")
print("muñeco tiene: " + str(count_vowels("muñeco")) + " vocales.")
print("supercalifragilisticoespiralidoso tiene: " + str(count_vowels("supercalifragilisticoespiralidoso")) + " vocales.")