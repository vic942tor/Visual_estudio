#Dado un diccionario que contiene autores y las palabras utilizadas en sus textos, escribe un programa en python que identifique
#Las palabras que son únicas para cada autor.
#las palabras compartidas entre todos los autores.

textos = {
    "Autor1": {"Python", "programar", "avanzado", "diseño"},
    "Autor2": {"Python", "diseño", "software", "ingeniería"},
    "Autor3": {"Python", "ingeniería", "algoritmos", "avanzado"}
}
dif01 = textos["Autor1"].difference(textos["Autor2"]).difference(textos["Autor3"])
dif02 = textos["Autor2"].difference(textos["Autor1"]).difference(textos["Autor3"])
dif03 = textos["Autor3"].difference(textos["Autor1"]).difference(textos["Autor2"])

print (f'Palabra unica del Autor1: {dif01}')
print (f'Palabra unica del Autor2: {dif02}')
print (f'Palabra unica del Autor3: {dif03}')

