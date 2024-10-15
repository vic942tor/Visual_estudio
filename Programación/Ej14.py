#Crea un programa que lea un número y sume todo sus digitos

valor = input("Introduce un número: ")
suma = 0   
for digito in valor:
    suma += int(digito)
print ("La suma de los dígitos es: ", suma)