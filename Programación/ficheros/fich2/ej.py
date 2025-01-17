
if __name__ == '__main__':
    try:
       fichero = open('datos_ejemplo02.txt')
    except:
        print('Ha ocurrido un error con la ruta seleccionada, por favor vuelva a introducirla.')
    else:
        palabra_clave = input('Introduzca la palabra que desea buscar en el fichero: ')
        incidencias = []

        for num_linea, linea in enumerate(fichero, start=1):
            if palabra_clave in linea:  # Verificar si la palabra está en la línea
                incidencias.append((num_linea, linea.strip()))

        fichero.close()

        if incidencias:
            print(f"Se encontraron {len(incidencias)} incidencias de la palabra '{palabra_clave}':")
            for num_linea, contenido in incidencias:
                print(f"Línea {num_linea}: {contenido}")
        else:
            print(f"No se encontraron incidencias de la palabra '{palabra_clave}' en el fichero.")
