#Crear un modo de lectura de nombre y apellidos separados por una ,
# nombre = input("Introduzca su(s) nombre: ")
# apellido = input("Introduzca su(s) apellidos: ")

# print(f"{apellido},{nombre}")

#Leer nombre y apellidos conjuntos
lista = input("Intoduce su(s) nombre y apellido: ").split()
cantidad = len(lista)
if cantidad == 1:
    print(f"{lista[1]}, {lista[0]}")
elif cantidad == 3:
    pregunta = input("Cuantos nombres tienes (intoduce un número)")
    if pregunta == "1":
        print(f"{lista[1]} {lista[2]}, {lista[0]}")
    else:
        print(f"{lista[2]}, {lista[0]} {lista[1]}")
elif cantidad == 4:
    print(f"{lista[2]} {lista[3]}, {lista[0]} {lista[1]}")