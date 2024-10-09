#Una palabra se considera creciente se considera que sus letras van en forma creciente
palabra = input("Escriba una palabra: ").lower()
anterior = palabra[0]
for posicion in palabra:
    if posicion < anterior:
        print("No es creciente")
        break
    anterior = posicion
else:
    print("Es creciente")
