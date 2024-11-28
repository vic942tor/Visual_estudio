# Modifique el ejercicio anterior para que ahora las ciudades del diccionario Porcentaje
# se ordenen de mayor a menor porcentaje relativo. 

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

# Ordenar el diccionario Porcentaje de mayor a menor porcentaje
Porcentaje_ordenado = dict(sorted(Porcentaje.items(), key=lambda item: item[1], reverse=True))

# Mostrar los porcentajes de cada ciudad, ordenados de mayor a menor
print("Porcentaje de cada ciudad respecto al total (ordenado de mayor a menor):")
for ciudad, porcentaje in Porcentaje_ordenado.items():
    print(f"{ciudad}: {porcentaje:.2f}%")

# Calcular la media de población
media_poblacion = total_poblacion / len(Ciudades)

# Mostrar la media de población con 3 decimales
print(f"\nMedia de población: {media_poblacion:.3f}")
