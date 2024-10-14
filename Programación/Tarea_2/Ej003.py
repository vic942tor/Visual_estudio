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
    #Lo siguiente muestra el "Progeso que llevamos" nos indica como vamos con el progreso de la palabra, los intentos que nos quedan y nos vuelve a pedir que ingresemos una nueva letra
    print(f"Palabra parcial: {' '.join(palabra_parcial)}")
    print(f"Intentos restantes: {intentos_restantes} - Letras usadas: '{letras_usadas}'")
    letra = input("Indique letra a jugar -> ").strip().lower()
    letras_usadas += letra
    #En esta parte revisa lo que introducimos en input anterior para comprobar si está registrado en leras_usadas, si ya está registrado salta un mesaje para avisar al usuario y si no lo está, la registra
    if letra in letras_usadas:
        print("Ya has usado esa letra. Intenta con otra.")
        continue
    letras_usadas += letra
    #Aquí revisa si la letra está dentro de la palabra, actualiza palabra_parcial para que una vez que se muestre el registro anterior se muestre con la nueva letra y resta un intento si es que la letra no está en la palabra
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                palabra_parcial[i] = letra
    else:
        intentos_restantes -= 1
    #Aquí se revisa si la palabra ya está completa y en caso de que palabra_parcial sea igual que palabra imprime la palabra parcial y la palabra a adivinar y imprime un mensaje para felicitar al jugador por la victoria 
    if ''.join(palabra_parcial) == palabra:
        print(f"Palabra parcial: {' '.join(palabra_parcial)}")
        print(f"Felicidades adivinate la palara: '{palabra}'!")
        break

#Aquí revisa los intentos restantes y si los inteso son igual a 0, imprime un mensaje para avisar al jugador que perdió y muestra cual era la palabra
if intentos_restantes == 0 and ''.join(palabra_parcial) != palabra:
    print(f"Perdiste. \nLa palabra era: {palabra}")
