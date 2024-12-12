# Se sabe que al lanzar dos dados normales (valores de 1 al 6) se pueden tener valores de suma obtenida que van
# desde el 2 hasta el 12.
# Se pide que diseñe un programa en Python con las dos funciones siguientes:
# calculo_combinaciones()
# esta función se encarga de calcular el número de maneras distintas en obtener cada uno de los valores de la suma
# de los dos dados.
# Por ejemplo, el valor 2, sólo se obtiene de sacar 1 en los dos dados, el valor 4 se puede obtener de 3 maneras
# distintas:
# Dado1: 1 Dado2: 3,
# Dado1: 2 Dado2: 2,
# Dado1: 3 Dado2: 1.
# Esta función debe retornar un diccionario donde la clave representa la suma de los puntos de los dos dados (2 al
# 12) y el valor el número de maneras distintas en que se puede obtener esa puntuación.
# calculo_probabilidades( ocasiones_por_valor )
# esta función recibe como parámetro el diccionario que se ha retornado de la función anterior y debe calcular la
# probabilidad de que al lanzar los dos dados salga cada uno de los valores del 2 al 12.
# Para ello se debe recordar que la probabilidad de que un suceso ocurra se calcula como
# P = numero de casos posibles / total de casos probables
# En el diccionario se tiene guardado en numero de casos posibles para cada uno de los posibles valores de la suma.
# Esta función debe retornar un diccionario similar al de la función anterior, salvo que ahora el valor es la
# probabilidad de que salga cada uno de las claves.
# El programa principal se encarga de las llamadas a las funciones y de escribir los valores de los diccionarios con
# los resultados obtenidos.

def calculo_combinacoes() -> dict:
    dic01 = {}
    for clave in range(2,13):
        dic01[clave] = 0
        for dado1 in range(1,7):
            for dado2 in range(1,7):
                if dado1 + dado2 == clave:
                    dic01[clave] += 1
    return dic01
if __name__ == '__main__':
    dict_posibilidades = calculo_combinacoes()
    print(dict_posibilidades)
# def calculo_probabilidades():