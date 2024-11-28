# Escriba un programa en Python que reciba como entrada una cadena de texto con el
# siguiente formato:
# <city>:<population>;<city>:<population>;<city>:<population>;....
# Y cree un diccionario donde las claves sean las ciudades y los valores la población de
# la ciudad.
# Una vez creado el diccionario se debe recorrer para mostrar por línea las ciudades con
# # su población. 

# Entrada de la cadena con el formato especificado
entrada = input("Introduce las ciudades y sus poblaciones en el formato <ciudad>:<poblacion>;: ")

# Dividimos la cadena en partes usando el punto y coma como separador
ciudades_poblaciones = entrada.split(";")

# Creamos el diccionario vacío
diccionario = {}

# Recorremos cada par de ciudad:población
for ciudad_poblacion in ciudades_poblaciones:
    if ciudad_poblacion:  # Para evitar posibles cadenas vacías
        ciudad, poblacion = ciudad_poblacion.split(":")
        diccionario[ciudad] = int(poblacion)  # Convertimos la población a un entero

# Mostramos las ciudades con su población
print("\nCiudades con su población:")
for ciudad, poblacion in diccionario.items():
    print(f"{ciudad}: {poblacion}")
