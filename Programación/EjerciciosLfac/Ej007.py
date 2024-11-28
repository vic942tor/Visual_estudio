# Escriba un programa en Python que pida al usuario un número entero no negativo y obtenga una
# lista con todas las potencias de 2 con el exponente variando desde 0 hasta dicho valor (inclusive).
# Si n = 8
# La lista de potencias es: [1, 2, 4, 16, 32, 64, 128, 256] 

# Pedir al usuario un número entero no negativo
n = int(input("Introduce un número entero no negativo: "))

# Verificar si el número es negativo
if n < 0:
    print("Por favor, ingresa un número no negativo.")
else:
    # Crear la lista de potencias de 2
    potencias = [2**i for i in range(n+1)]
    
    # Mostrar la lista de potencias
    print(f"La lista de potencias es: {potencias}")
