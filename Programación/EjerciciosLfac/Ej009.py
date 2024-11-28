# Escriba un programa en Python que genere una lista con los n primeros múltiplos de x, donde n y
# x son parámetros de entrada pedidos al usuario y que deben ser valores enteros mayores que 0
# (se debe verificar).
# Ejemplo:
# Si x = 3 y n = 8 la lista debe ser: [0, 3, 6, 9, 12, 15, 18, 21] 

# Pedir al usuario los valores de x y n
x = int(input("Introduce un número entero x (mayor que 0): "))
n = int(input("Introduce un número entero n (mayor que 0): "))

# Verificar si ambos valores son mayores que 0
if x > 0 and n > 0:
    # Generar la lista de múltiplos de x
    lista_multiples = [x * i for i in range(n)]
    print(f"La lista de los primeros {n} múltiplos de {x} es: {lista_multiples}")
else:
    print("Ambos valores deben ser mayores que 0.")

