#Lo mismo que el Ej1 pero con un menú y la opción inversa
menu = 1

while menu == 1:
    print("Presiona 1 para pasar de ºC a ºF")
    print("Presiona 2 para pasar de ºF a ºC")
    print("presiona 0 para salir del programa")
    respuesta = input()

    if respuesta == "1":
        try:
            a = input("Establece un número que se representará en ºC para pasarlo a ºF: ")
            temp_gc = float(a)
            temp_gf = temp_gc *1.8 +32.0
            print(f"{temp_gc}ºC son {temp_gf}ºF")
            menu = 0
        except:
            print("Tu eres tonto?")
    elif respuesta == "2":
            try:
                b = input("Establece un número que se representará en ºF para pasarlo a ºC: ")
                temp_gf = float(b)
                temp_gc = (temp_gf - 32) * (5/9)
                print(f"{temp_gc}ºC son {temp_gf}ºF")
                menu = 0
            except:
                 print("Y si aprendemos a leer?")
    elif respuesta == "0":
         menu = 0
    else:
         print("Selecciona una de las opciones, subnormal")
         menu = 0