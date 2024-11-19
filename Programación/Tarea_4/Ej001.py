# Escribir un programa en Python para eliminar clavees con los mismos valores en un
# diccionario.
# Ejemplo:
# d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
individuales = {}
resultado = {}
for clave, valor in d1.items():
    if valor not in individuales:
        individuales[valor] = clave
        resultado[clave] = valor
    else:
        if individuales[valor] in resultado:
            del resultado[individuales[valor]]
print (resultado)