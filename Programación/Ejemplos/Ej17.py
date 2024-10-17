# Escribe un prgrama en Python que lea un número en positivo e indique si el número es mágico o no.

def is_magic_number(n):
    # Calculamos el número de digitos
    num_digits = len(str(n))
    
    # Calculamos el número de factores
    num_factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            num_factors += 1
    
    # Calculamos el número de digitos que formarán parte de la suma de factores
    sum_of_factors_digits = sum(int(digit) for digit in str(num_factors))
    
    # Calculamos el número de digitos que formarán parte de la suma de digitos de cada dígito
    sum_of_digits_digits = sum(int(digit) for digit in str(n))
    
    # Calculamos el número mágico
    magic_number = sum_of_digits_digits * num_digits == sum_of_factors_digits * num_factors
    
    return magic_number

# Lectura del número

n = int(input("Introduce un número entero positivo: "))

# Comprobamos si el número es mágico

if is_magic_number(n):
    print(f"{n} es un número mágico.")
else:
    print(f"{n} no es un número mágico.")

# Pruebas

print(is_magic_number(1))  # True
print(is_magic_number(2))  # False
print(is_magic_number(6))  # True
print(is_magic_number(24))  # False
print(is_magic_number(28))  # True

# Ejecutar el código y probarlo con distintos valores de entrada para verificar su correctitud.
