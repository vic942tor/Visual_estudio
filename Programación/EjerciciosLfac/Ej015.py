# Dado un número entero no negativo, genere una lista con los dígitos de dicho número en orden
# inverso. Debe trabajar el valor como número y no pasarlo a string.
# 35231 -> [1, 3, 2, 5, 3]
# 1 -> [1]
# 0 -> [0]
# 100 -> [0, 0, 1]

# Número de ejemplo
numero = 35231

# Lista vacía para almacenar los dígitos
digitos_invertidos = []

# Mientras el número no sea 0
while numero > 0:
    # Obtener el último dígito
    digito = numero % 10
    digitos_invertidos.append(digito)
    
    # Eliminar el último dígito
    numero //= 10

# Si el número era 0, agregarlo a la lista
if len(digitos_invertidos) == 0:
    digitos_invertidos.append(0)

# Mostrar el resultado
print(f"Los dígitos en orden inverso son: {digitos_invertidos}")


