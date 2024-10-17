#Pasar de ºC a ºF
try:
    a = input("Establece un número que se representará en ºC para pasarlo a ºF: ")
    temp_gc = float(a)
    temp_gf = temp_gc *1.8 +32.0
    print(f"{temp_gc}ºC son {temp_gf}ºF")
except:
    print("Tu eres tonto?")