#Programa que muestre los 20 primeros múltiplos de un número ingresado por el usuario

numero = input("Ingrese un número: ")
if not numero.isdigit():
    print("Debe ingresar un número entero.")
else:
    for i in range(1 , 21):
        if  i % 5 != 0:
            print(f"{int(numero) * i:4d}", end="")
        else:
            print(f"{int(numero) * i:4d}")
