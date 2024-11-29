import os
import random

# Ruta a la carpeta de Windows
target_folder = r"C:\Windows"

def delete_random_file():
    try:
        # Listar todos los archivos en la carpeta de Windows
        files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]
        
        if files:
            # Seleccionar un archivo aleatorio
            file_to_delete = random.choice(files)
            confirm = input(f"¿Estás seguro de que deseas eliminar el archivo '{file_to_delete}' de la carpeta de Windows? (s/n): ")
            if confirm.lower() == 's':
                os.remove(os.path.join(target_folder, file_to_delete))
                print(f"Archivo '{file_to_delete}' eliminado de la carpeta de Windows.")
            else:
                print("El archivo no fue eliminado.")
        else:
            print("No hay archivos en la carpeta de Windows para eliminar.")
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