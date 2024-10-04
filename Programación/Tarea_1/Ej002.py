# Se desea realizar un programa que permita convertir datos de tiempo expresado
# en días, horas, minutos y segundos a milisegundos y viceversa.
# El programa debe pedir al usuario el tipo de conversión a realizar y debe validar
# todos los datos de entrada. Deben decidir como debe ser la entrada de datos en
# ambos casos y una vez realizados los cálculos correspondientes se debe mostrar
# como respuesta tanto los datos originales y el resultado de la conversión.
modo = input("Pasar a milisegundos (P) o convertir de milisegundos a dias, horas, minutos y segundos (C): ").upper()
if modo == "P":
    tiempo = input("Establece una cantidad de días, horas, minutos y segundos para convertilos en milisegundos, solo se deben insertar números: ").split()
    dias = float(tiempo[0]) * 86400000
    horas =  float(tiempo[1]) * 3600000
    minutos = float(tiempo[2]) * 60000
    segundos = float(tiempo[3]) * 1000
    cantidad = dias + horas + minutos + segundos
    print(f"{cantidad} milisegundos.")
elif modo == "C":
    tipo = input("Convertir en dias (D) en horas (H) en Minutos (M) o en segundos (S): ").upper()
    if tipo == "D":
        cantidad = input("Establece la cantidad de milisegindos: ")
        resultado = float(cantidad) / 86400000
        print(f"{cantidad} de milisegundos son {resultado} días")
    elif tipo == "H":
        cantidad = input("Establece la cantidad de milisegindos: ")
        resultado = float(cantidad) / 3600000
        print(f"{cantidad} de milisegundos son {resultado} horas")
    elif tipo == "M":
        cantidad = input("Establece la cantidad de milisegindos: ")
        resultado = float(cantidad) / 60000
        print(f"{cantidad} de milisegundos son {resultado} minutos")
    elif tipo == "S":
        cantidad = input("Establece la cantidad de milisegindos: ")
        resultado = float(cantidad) / 1000
        print(f"{cantidad} de milisegundos son {resultado} segundos")
else:
    print("Establece una opción valida")