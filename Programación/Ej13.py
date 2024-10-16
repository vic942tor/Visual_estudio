#se lee un número por teclado y se imprime por pantalla todos los divisores que tiene 

numero = int(input("Introduce un número: "))
# for i in range(1, numero +1):
for i in range(1, numero //2):
    if numero % i == 0:
        print(i, end =" ")
print()
