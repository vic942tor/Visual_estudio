# Un número de n dígitos es un número de Armstrong si es igual a la suma de las nésimas potencias de sus dígitos. 
# Por ejemplo, 371, 8208 y 4210818 son números de Armstrong.
# Escriba un programa en Python que muestre los 20 primeros números de
# Armstrong.

numeros_armstrong = []
num = 0
while len(numeros_armstrong) < 20:
    digitos = str(num)
    n = len(digitos)
    suma_potencias = sum(int(digito) ** n for digito in digitos)
    if suma_potencias == num:
        numeros_armstrong.append(num)
    num += 1
print("Los primeros 20 números de Armstrong son los siguientes:", numeros_armstrong)
