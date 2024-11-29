# Las películas vistas se guardan en un diccionario de nombre películas_vistas
# donde las claves son los nombres de los usuarios y los valores son listas de
# películas vistas por cada uno.
# El programa debe contener un menú que permita dar respuesta a todas las
# preguntas que se plantean a continuación:

# 1. Películas vistas por todos los usuarios (1,00 punto)
# Se trata de encontrar las películas que se han sido vistas por todos los usuarios

# 2. Películas vista en exclusivas por un usuario (1,00 punto)
# Se trata de encontrar las películas que ha visto en exclusiva un usuario. En este
# caso se pide y valida el nombre del usuario.

# 3. Conteo del número de visualizaciones (1,00 punto)
# En este caso se intenta contar el número de cantidad que se ha visto cada película.
# La información se debe almacenar en un lista de nombre visualizaciones en la que cada
# elemento es una tupla con los siguientes valores (película, nro_cantidad_vista). Esta
# lista debe tener ordenada sus tuplas por el número de visualizaciones de cada película.

# 4. Encontrar las películas más populares (1,00 punto)
# En este caso se pide que encuentre la/las películas que más se han visto (por
# número de visualizaciones)

# 5. Recomendar películas a un usuario (1,00 punto)
# Dado el nombre de un usuario que se pide por pantalla y se valida, se debe crear
# una lista con las películas que se le recomiendan ver.
# Diccionario de películas vistas por cada usuario

peliculas_vistas = {
 'Ana': ['Inception', 'Avatar', 'Titanic', 'Matrix'],
 'Luis': ['Matrix', 'Inception', 'El Señor de los Anillos'],
 'Sofía': ['Titanic', 'Avatar', 'Matrix', 'El Rey León'],
 'Carlos': ['Matrix', 'Avatar', 'El Señor de los Anillos'],
}

while True:
    print('1. Películas vistas por todos los usuarios')
    print('2. Películas vistas en exclusiva por un usuario')
    print('3. Número de visualizaciones')
    print('4. Películas más populares')
    print('5. Recomendar películas a un usuario')
    print('6. Salir')

    opcion = input('Seleccione una opción (1-6): ')
    
#Opción 1: Mostrar las películas vistas por todos los usuarios
    if opcion == '1':
#Inicializa el conjunto con las películas vistas por el primer usuario
        peliculas_comunes = set(peliculas_vistas[list(peliculas_vistas.keys())[0]])
        for peliculas in peliculas_vistas.values():
#Actualizamos el conjunto
            peliculas_comunes &= set(peliculas)  
        print(f'Películas vistas por todos los usuarios: {peliculas_comunes}')
#Opción 2: Mostrar las películas vistas en exclusiva por un usuario
    elif opcion == '2':
        usuario = input('Ingrese el nombre del usuario: ')
#Verificamos si el usuario existe en el diccionario
        if usuario in peliculas_vistas:
#Convierte las películas vistas por el usuario en un conjunto
            peliculas_usuario = set(peliculas_vistas[usuario])
#Creamos una copia para poder modificarla
            peliculas_exclusivas = peliculas_usuario.copy()      
            for otro_usuario, peliculas in peliculas_vistas.items():
                if otro_usuario != usuario:
#Eliminamos las vistas por otros usuarios
                    peliculas_exclusivas -= set(peliculas)  
#Mostramos las películas vistas exclusivamente por el usuario
            print(f'Películas vistas en exclusiva por {usuario}: {peliculas_exclusivas}')
        else:
#Si el usuario no existe, se muestra un mensaje de error
            print(f'Usuario {usuario} no encontrado.')

#Opción 3: Mostrar el conteo de visualizaciones de cada película
    elif opcion == '3':
        visualizaciones = []
        peliculas_contadas = {}
#Contamos las veces que cada película ha sido vista por los usuarios
        for peliculas in peliculas_vistas.values():
            for pelicula in peliculas:
                if pelicula not in peliculas_contadas:
#Si es la primera vez que se ve la película le añadimos 1 y lo dejamos así
                    peliculas_contadas[pelicula] = 1
                else:
#Incrementamos el contador si ya se había visto
                    peliculas_contadas[pelicula] += 1
#Convertimos el diccionario de visualizaciones en una lista de tuplas (película, veces vista)
        visualizaciones = [(pelicula, veces) for pelicula, veces in peliculas_contadas.items()]
#Ordenamos la lista manualmente con el algoritmo de ordenación burbuja
        for i in range(len(visualizaciones) - 1):
            for j in range(len(visualizaciones) - 1 - i):
                if visualizaciones[j][1] < visualizaciones[j + 1][1]:
#Intercambiamos las posiciones si el valor en el índice j es menor que el de j+1
                    visualizaciones[j], visualizaciones[j + 1] = visualizaciones[j + 1], visualizaciones[j]
#Mostramos el conteo de visualizaciones ordenado
        print('Número de visualizaciones:')
        for pelicula, veces in visualizaciones:
            print(f'{pelicula}: {veces} veces')
#Opción 4: Mostrar las películas más populares (las más vistas)
    elif opcion == '4':
#Verificamox que se haya calculado previamente el conteo de visualizaciones
        if len(visualizaciones) == 0:
#Si no se ha calculado, muestra un mensaje de error
            print('Primero debe calcular el conteo de visualizaciones (opción 3).')
        else:
#Obtenemos el número máximo de visualizaciones
            max_veces_vista = visualizaciones[0][1]
            populares = [pelicula for pelicula, veces in visualizaciones if veces == max_veces_vista]
            print(f'Películas más populares: {populares}')
#Opción 5: Recomendar películas a un usuario
    elif opcion == '5':
        usuario = input('Ingrese el nombre del usuario: ')
#Verificamos si el usuario existe en el diccionario
        if usuario in peliculas_vistas:
#Convertimos las películas vistas por el usuario en un conjunto
            peliculas_vistas_usuario = set(peliculas_vistas[usuario])
            peliculas_recomendadas = set()  
#Agregamos las películas vistas por otros usuarios
            for otro_usuario, peliculas in peliculas_vistas.items():
                if otro_usuario != usuario:
#Agregamos las películas vistas por otros usuarios
                    peliculas_recomendadas.update(peliculas)  
#Filtramos las películas que ya ha visto el usuario
            peliculas_recomendadas -= peliculas_vistas_usuario
#Mostramos las películas recomendadas para el usuario
            print(f'Películas recomendadas para {usuario}: {peliculas_recomendadas}')
        else:
#Si el usuario no existe, muestra un mensaje de error
            print(f'Usuario {usuario} no encontrado.')
#Opción 6: Salir del programa
    elif opcion == '6':
        break 
    else:
        print('Opción no válida, por favor intente de nuevo.')
