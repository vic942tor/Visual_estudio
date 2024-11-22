#Escribe un programa en python que tome un diccionario donde las claves son categorias y los valores son listas de elementos. 
# Devuelve un nuevo diccionario donde las claves son los elementos y los valores son los conjuntis 
# con las categorias a las que pertenecen

categorias = {
 "Ropa": ["Camisa", "Pantalón", "Zapatos"],
 "Electrónica": ["Laptop", "Teléfono", "Pantalón"],
 "Hogar": ["Silla", "Mesa", "Zapatos"]
}
nuevo_diccionario = {}
for clave, valor in categorias.items():
    for elemento in valor:
        if elemento not in nuevo_diccionario:
            nuevo_diccionario[elemento] = set()
        nuevo_diccionario[elemento].add(clave)
print(nuevo_diccionario)
    


