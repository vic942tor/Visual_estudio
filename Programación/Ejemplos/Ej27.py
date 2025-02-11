# recursivo
numero = [1, 2, 3, 4, 5]

def suma_recursiva(numero) -> int:
    if len(numero) == 1:
        return numero[0]
    else:
        return numero[0] + suma_recursiva(numero[1:])
print(suma_recursiva(numero))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# n = int(input('Introduce un número para ver su factorial: '))
# print(factorial(n))

