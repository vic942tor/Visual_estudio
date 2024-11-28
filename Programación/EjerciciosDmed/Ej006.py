# En un diccionario de nombre Examen tenemos almacenadas las notas de un examen
# en un diccionario. Es necesario separar al alumnado que aprobó y al que suspendió en
# dos diccionarios de nombre Aprobados y Suspendidos Igualmente habrá que pasar a
# mayúsculas el nombre del alumnado que aprobó y a minúsculas el nombre del
# alumnado que suspendió.
# Escriba un programa en Python que realice esta operación solicitada y muestre de
# forma detallada los alumnos que han aprobado, los que han suspendido y la media de
# notas de todo el grupo. 

# Diccionario de notas del examen
Examen = {
    'Juan': 7.5,
    'Ana': 4.3,
    'Pedro': 5.9,
    'Maria': 8.2,
    'Carlos': 3.4,
    'Laura': 6.7
}

# Diccionarios para los aprobados y suspendidos
Aprobados = {}
Suspendidos = {}

# Separar a los alumnos aprobados y suspendidos
for alumno, nota in Examen.items():
    if nota >= 5:  # Consideramos aprobado si la nota es 5 o más
        Aprobados[alumno.upper()] = nota  # Convertimos el nombre a mayúsculas para los aprobados
    else:
        Suspendidos[alumno.lower()] = nota  # Convertimos el nombre a minúsculas para los suspendidos

# Mostrar los alumnos aprobados
print("Alumnos que han aprobado:")
for alumno, nota in Aprobados.items():
    print(f"{alumno}: {nota:.2f}")

# Mostrar los alumnos suspendidos
print("\nAlumnos que han suspendido:")
for alumno, nota in Suspendidos.items():
    print(f"{alumno}: {nota:.2f}")

# Calcular la media de notas de todo el grupo
total_notas = sum(Examen.values())
media_notas = total_notas / len(Examen)

# Mostrar la media de las notas
print(f"\nMedia de las notas del grupo: {media_notas:.2f}")
