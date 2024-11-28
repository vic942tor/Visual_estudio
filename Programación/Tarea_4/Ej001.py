# Escribir un programa en Python para eliminar clavees con los mismos valores en un
# diccionario.
# Ejemplo:
# d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
# Diccionario inicial con claves y valores.
d1 = {"one": "eleven", "2": 2, "three": 3, "11": "eleven", "four": 44, "two": 2}
individuales = {}
resultado = {}
# Recorre el diccionario inicial clave por clave y valor por valor.
for clave, valor in d1.items():
#Si el valor no está en el diccionario 'individuales', lo consideramos único hasta el momento.
    if valor not in individuales:
        individuales[valor] = clave
        resultado[clave] = valor
    else:
#Si el valor ya existe en 'individuales', es un duplicado.
#Comprobamos si la clave asociada al valor duplicado aún está en 'resultado'.
        if individuales[valor] in resultado:
#Si está en 'resultado', significa que antes lo habíamos agregado como único,
#pero ahora descubrimos que no lo es, así que lo eliminamos.
            del resultado[individuales[valor]]
print(resultado)
