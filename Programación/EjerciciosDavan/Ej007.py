# Ejercicio 07: Se quiere crear un traductor de palabras en español a Morse, para esosedebecrearun 
# diccionario que tenga dos elementos: la clave es la letra del alfabeto, el valor su correspondientecodificación 
# en Morse. Diseñe un programa que cree el diccionario de traducción e implemente un bucleparasolicitarpalabras que 
# deben ser traducidas a Morse. El bucle termina cuando se introduzcalasecuencia“*@*”

# Diccionario de traducción de letras a código Morse
morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 
    'z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

# Iniciar bucle para pedir palabras al usuario
while True:
    palabra = input("Introduce una palabra para traducir a Morse (o '@*@' para salir): ").lower()
    
    if palabra == "@*@":
        print("¡Traducción terminada!")
        break

    # Traducir la palabra a código Morse
    traduccion = []
    for letra in palabra:
        if letra in morse_dict:
            traduccion.append(morse_dict[letra])
        else:
            print(f"Caracter no válido: {letra}")
            break
    else:  # Solo se ejecuta si no hubo errores
        print("Traducción a Morse:", " ".join(traduccion))
