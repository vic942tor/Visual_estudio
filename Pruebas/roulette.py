import os
import random
def apagar_pc():
    """
    Apaga el PC utilizando comandos del sistema operativo.
    """
    try:
        print("El sistema se apagará en breve...")
        os.system("shutdown /s /t 0")
    except Exception as e:
        print(f"Error al intentar apagar el PC: {e}")
while True:
    numero = random.randint(1, 50)  # Número aleatorio entre 1 y 50
    respuesta = input('Inserte un número del 1 al 50. Si lo adivinas, ganas; de lo contrario, tu equipo será apagado: ') 
    # Convertir la respuesta a entero para la comparación
    try:
        respuesta = int(respuesta)
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue
    
    if respuesta == numero:
        print('¡Ganaste!')
        break
    else:
        print(f'El número era {numero}.')
        apagar_pc()
        break


