numero = [1, 2, 3, 4, 5]

def suma_recursiva(numero) -> int:
    if len(numero) == 1:
        return numero[0]
    else:
        return numero[0] + suma_recursiva(numero[1:])
print(suma_recursiva(numero))
