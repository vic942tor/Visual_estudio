# Se pide implementar un programa modular que simule el juego para 3 jugadores,
# teniendo en cuenta que:
# Tanto los 4 datos de cada jugador, como los valores para A y B se introducirán por
# teclado. En todos los casos, el programa detectará la entrada de números
# erróneos, solicitando nuevamente el dato hasta que sea válido.
# Se deben mostrar por pantalla no solo los aciertos de cada jugador sino los datos
# que ha introducido cada jugador y los que ha seleccionado el árbitro. Por último,
# hay que imprimir la media aritmética de los aciertos de todos los jugadores

jugadores = [[], [], []]
#Aquí estamos estableciendo las opciones de cada uno de los participantes, teniendo en cuenta que son 3 y que cuando cometan errores el programa debe seguir pidiendole opciones
for i in range(len(jugadores)):
    print (f'Introduce los número del jugador número {i+1}: ')
    while len(jugadores[i]) < 4:
        try:
            numero_jugador = int(input('Establece un número entre 0 y 10: '))
            if numero_jugador >= 0 and numero_jugador <= 10:
                jugadores[i].append(numero_jugador)
            else:
                print('Debes introducir un número entre 0 y 10')
        except:
            print('Debes introducir un número')
#Aquí estamos estableciendo los número del arbitro y comprobando que son correctos
while True:
    A = int(input('Inserte un número comprendido entre el 0 y el 5: ' ))
    B = int(input('Inserte un número comprendido entre el 6 y el 10: '))
    try:  
        if A >= 0 and A <= 5 and B >= 6 and B <= 10:
            break
        else:
            print('Debes introducir un número entre los anteriormente indicados')
    except:
        print('Debes introducir un número')
aciertos = []
#Aquí estamos estableciendo los aciertos de los jugadores diciendo si los numeros que eligieron estan entre los elegidos por el arbitro
for i in range(3):
    cuenta = 0
    for numero in jugadores[i]:
        if A <= numero <= B:
            cuenta += 1
    aciertos.append(cuenta)
#Aquí estamos diciendo que números estableció el arbitro y a su vez establecemos la información de los jugadores
print(f'El arbitro a seleccionado los valores entre {A} y {B}')
for i in range(len(jugadores)):
    print(f'El jugador número {i+1} el cual tiene las siguientes opciones {jugadores[i]} ha tenido una cantidad de {aciertos[i]} aciertos.')
 #Aquí estamos calculando la media  de aciertos para luego establecerla como media aritmetica para los usuarios   
media_de_aciertos = sum(aciertos) / len(aciertos)
print(f'La media aritmetica de los aciertos en esta partida es de {media_de_aciertos:.2f}')