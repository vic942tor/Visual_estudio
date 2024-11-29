# Una lista1 se considera capicúa si los elementos que la conforman mantienen el
# mismo orden recorridos de izquierda a derecha como de derecha a izquierda.
# Veamos un par de ejemplos: [1,2,3,3,2,1] [7,6,5,7,6]
# Una lista1 se considera suma-capicúa si todos los elementos que están en la parte
# izquierda están en la parte derecha en otro orden (sino sería capicúa) y la suma de
# los valores sellado izquierdo es la misma que la suma de valores de la mitad
# derecha. Veamos los siguientes ejemplos
# Todos los elementos de la mitad izquierda se encuentran en otro orden en la mitad derecha.
# La suma de los valores de la mitad izquierda es igual que la suma de los valores de la mitad
# derecha.
# Escriba un programa en Python que dada una lista1 verifique si es suma-capicúa.

lista1 = [1,2,3,3,2,1]
lista2 = [7,6,5,7,6]
capicua_usuario = input(f"Ingresa una lista de números separados por comas (ejemplos: {lista1} o {lista2}): ")
#Convertimos la capicua_usuario en una lista de enteros.
lista = []
try:
    for num in capicua_usuario.split(','):
        lista.append(int(num))
except:
    print("La lista ingresada no es válida.")
#Iniciamos dando por hecho que suma_capicua va a ser true, y luego haremos los cambios para verificarlo
suma_capicua = True
#Verificamos si la longitud de la lista es impar para luego aplicarle las configuraciones necesarias
if len(lista) % 2 != 0:
#Si es impar eliminamos el número del medio para que no afecte a la hora de operar con las mitades
    mitad = len(lista) // 2
    lista.pop(mitad)
#Dividimos la lista en dos mitades
mitad = len(lista) // 2
izquierda = lista[:mitad]
derecha = lista[mitad:]
#Verificamos si ambas mitades tienen los mismos elementos en diferente orden
if sorted(izquierda) != sorted(derecha):
    suma_capicua = False
#Verificamos si la suma de ambas mitades no es igua, para en el caso de que no lo sea la variable suma_capicua pase a ser false
if sum(izquierda) != sum(derecha):
    suma_capicua = False
if suma_capicua == True:
    print(f"La lista {capicua_usuario} es suma-capicúa.")
else:
    print(f"La lista {capicua_usuario} no es suma-capicúa.")









