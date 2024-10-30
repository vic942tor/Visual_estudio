num_asignaturas = 9
max_intentos = 3
notas = []

for i in range(1, num_asignaturas + 1):
    intento = 0
    while intento < max_intentos:
        try:
            # Leer la nota como string para verificar decimales
            nota_str = input(f"Ingrese la nota de la asignatura {i} (0 a 10, hasta 1 decimal): ")
            nota = float(nota_str)
            
            # Validar que la nota esté en el rango y tenga hasta 1 decimal
            if 0 <= nota <= 10 and ('.' not in nota_str or len(nota_str.split(".")[1]) <= 1):
                notas.append(nota)
                print(f"Nota registrada para la asignatura {i}: {nota}")
                break  # Sale del bucle si la nota es válida
            else:
                raise ValueError("La nota debe estar entre 0 y 10, con hasta 1 decimal.")
        
        except (ValueError, IndexError):
            intento += 1
            print(f"Intento {intento} fallido. Asegúrate de ingresar una nota válida entre 0 y 10, con hasta 1 decimal.")
        
        if intento == max_intentos:
            print(f"Asignatura {i} marcada como 'No válida' después de 3 intentos fallidos.")
            notas.append(None)  # Marca como no válida

# Filtrar notas válidas para cálculos
notas_validas = [nota for nota in notas if nota is not None]

# Calcular la media, nota más alta y más baja si hay notas válidas
if notas_validas:
    media = sum(notas_validas) / len(notas_validas)
    nota_max = max(notas_validas)
    nota_min = min(notas_validas)

    print("\nResultados finales:")
    print(f"Notas ingresadas: {notas}")
    print(f"Media de las notas válidas: {media:.1f}")
    print(f"Nota más alta: {nota_max}")
    print(f"Nota más baja: {nota_min}")
else:
    print("No se ingresaron notas válidas.")
