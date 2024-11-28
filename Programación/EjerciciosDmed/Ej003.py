# Escriba un programa en Python que partiendo de un diccionario de nombre Ciudades
# donde las ciudades son las claves y poblaciones los valores -suponiendo que estas
# ciudades son las únicas que existen en el planeta- calcule en un nuevo diccionario de
# nombre Porcentaje el porcentaje relativo de cada una de ellas con respecto al total.
# Luego de crear el diccionario Porcentaje se debe mostrar por pantalla el nombre de las
# ciudades y su porcentaje relativo. Luego se debe imprimir la media de población con
# una precisión de 3 decimales. 

# Diccionario de ciudades y sus poblaciones
Ciudades = {
    'Ciudad A': 5000000,
    'Ciudad B': 3000000,
    'Ciudad C': 2000000,
    'Ciudad D': 1000000
}

# Calcular el total de la población
total_poblacion = sum(Ciudades.values())

# Crear un diccionario para los porcentajes
Porcentaje = {}

# Calcular el porcentaje de cada ciudad con respecto al total
for ciudad, poblacion in Ciudades.items():
    porcentaje = (poblacion / total_poblacion) * 100
    Porcentaje[ciudad] = porcentaje

# Mostrar los porcentajes de cada ciudad
print("Porcentaje de cada ciudad respecto al total:")
for ciudad, porcentaje in Porcentaje.items():
    print(f"{ciudad}: {porcentaje:.2f}%")

# Calcular la media de población
media_poblacion = total_poblacion / len(Ciudades)

# Mostrar la media de población con 3 decimales
print(f"\nMedia de población: {media_poblacion:.3f}")
