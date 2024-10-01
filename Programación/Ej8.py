#Crear un modo de lectura de nombre y apellidos separados por una ,
# nombre = input("Introduzca su(s) nombre: ")
# apellido = input("Introduzca su(s) apellidos: ")

# print(f"{apellido},{nombre}")
#Leer nombre y apellidos conjuntos

lista = input("Intoduce su(s) nombre y apellido: ").split()
ja = len(lista)
if ja == 1:
    print(f"{lista[1]}, {lista[0]}")
elif ja == 3:
    pregunta1 = input("Cuantos nombres tienes (intoduce un número)")
    if pregunta1 == "1":
        print(f"{lista[1]} {lista[2]}, {lista[0]}")
    else:
        print(f"{lista[2]}, {lista[0]} {lista[1]}")
elif ja == 4:
    print(f"{lista[2]} {lista[3]}, {lista[0]} {lista[1]}")