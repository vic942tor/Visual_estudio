#Escriba un programa en Python que pida un número al usuario y diga si este está
# o no bien posicionalmente estructurado.

numero = input("Introduce un número para verificar si está posicionalmente bien estructurado: ")
bien_estructurado = True  
for i, n in enumerate(reversed(numero)):
    n = int(n)  
    if (i + 1) % 2 != 0 and n % 2 == 0:
        bien_estructurado = False
        break
    elif (i + 1) % 2 == 0 and n % 2 != 0:
        bien_estructurado = False
        break
if bien_estructurado:
    print("El número está posicionalmente bien estructurado")
else:
    print("El número no está posicionalmente bien estructurado")

