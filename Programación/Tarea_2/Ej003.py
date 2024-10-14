#Crear un "Juego de introducir una palabra y adivinar cual es"

while True:
    palabra = input("Introduzca la palabra a adivinar (mínimo 3 letras): ").strip().lower()
    if len(palabra) >= 3:
        break
    print("La palabra debe tener un mínimo de 3 letras.")
palabra_parcial = ['+'] * len(palabra)  
letras_usadas = ""                     
intentos_restantes = 7
while intentos_restantes > 0:
    #Lo siguiente muestra el "Progeso que llevamoas 
    print(f"\nPalabra parcial: {' '.join(palabra_parcial)}")
    print(f"Intentos restantes: {intentos_restantes} - Letras usadas: '{letras_usadas}'")
    letra = input("Indique la letra que desea utilizar ").strip().lower()

    # Verifica si la letra ya ha sido usada
    if letra in letras_usadas:
        print("Ya has usado esa letra. Intenta con otra.")
        continue

    # Agrega la letra a la lista de letras usadas si no está repetida
    letras_usadas += letra

    # Verifica si la letra está en la palabra
    if letra in palabra:
        # Actualiza palabra_parcial donde la letra aparece en la palabra
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_parcial[i] = letra
    else:
        # Resta un intento si la letra no está en la palabra
        intentos_restantes -= 1

    # Verifica si el jugador ha adivinado la palabra
    if ''.join(palabra_parcial) == palabra:
        print(f"\nPalabra parcial: {' '.join(palabra_parcial)}")
        print(f"Enhorabuena, has adivinado la palabra '{palabra}'!")
        break

# Mensaje final si el jugador pierde
if intentos_restantes == 0 and ''.join(palabra_parcial) != palabra:
    print(f"\nEl jugador ha perdido. La palabra es: {palabra}")
