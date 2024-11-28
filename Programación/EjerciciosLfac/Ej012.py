# Escriba un programa en Python que pida al usuario un nombre y apellidos en el formato
# "apellidos, nombre” e imprima las iniciales de dicha persona pasadas a mayúsculas y con punto
# al final.
# A tener en cuenta:
# El nombre puede tener uno o dos elementos.
# El apellido puede tener uno o dos elementos.
# Ejemplos:
# ‘Pérez Ramírez, jesús’ -> J.P.R.
# ´garcía, Marta’ -> M.G.
# ‘Perez rodríguez, María josé’ -> M.J.P.R 

# Pedir el nombre completo
nombre_completo = input("Introduce el nombre en formato 'apellidos, nombre': ")

# Dividir el nombre completo en apellidos y nombre
partes = nombre_completo.split(", ")
apellidos = partes[0].split()  # Dividir los apellidos en partes
nombre = partes[1].split()  # Dividir el nombre en partes

# Obtener las iniciales de los apellidos y el nombre
iniciales = "".join([apellido[0].upper() + "." for apellido in apellidos])
iniciales += "".join([nombre_i[0].upper() + "." for nombre_i in nombre])

# Mostrar las iniciales
print(f"Las iniciales son: {iniciales}")
