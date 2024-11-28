# Modifique el ejercicio 03 para que ahora las ciudades se muestren por su orden
# alfabético de menor a mayor.

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

# Ordenar el diccionario Porcentaje por el nombre de la ciudad en orden alfabético
Porcentaje_ordenado_alfabeticamente = dict(sorted(Porcentaje.items(), key=lambda item: item[0]))

# Mostrar los porcentajes de cada ciudad, ordenados alfabéticamente
print("Porcentaje de cada ciudad respecto al total (ordenado alfabéticamente):")
for ciudad, porcentaje in Porcentaje_ordenado_alfabeticamente.items():
    print(f"{ciudad}: {porcentaje:.2f}%")

# Calcular la media de población
media_poblacion = total_poblacion / len(Ciudades)

# Mostrar la media de población con 3 decimales
print(f"\nMedia de población: {media_poblacion:.3f}")
