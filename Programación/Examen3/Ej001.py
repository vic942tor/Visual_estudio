#Escriba un programa en python que defina una función recursiva que recibe una lista cuyos elementos pueden ser números o letras y retorne dos listas, una de las cuales tendrá
#todos los números de la lista original y la otra tendrá todas las letras. Ambas listas deberán estar ordenadas de forma creciente y NO DEBEN CONTENER VALORES DUPLICADOS
# Ejemplo:
# lista = ['a', 1, 'z', 9, 'c', 3, 'b', 2, 'a', 3, 7, 'c', 9, 'a']
def separar(lista, numeros=None, letras=None):
    if numeros is None:
        numeros = set()
    if letras is None:
        letras = set()
#Lo que hacemos aqui, es revisar si la lista está vacía, retornamos los resultados
    if not lista:
        return sorted(numeros), sorted(letras)
    elemento = lista[0]
#Aquí verificamos si es un número
    if isinstance(elemento, (int, float)):
        numeros.add(elemento)
#Aquí, verificamos si es una letra
    elif isinstance(elemento, str):
        letras.add(elemento)
    return separar(lista[1:], numeros, letras)
def main():
    # lista = ['a', 1, 'z', 9, 'c', 3, 'b', 2, 'a', 3, 7, 'c', 9, 'a']
    #Aquí dejo varias listas de prueba, para ver si todo funciona correctamente.
    # lista = ['m', 6, 'd', 2, 'j', 7, 'a', 5, 'a', 0, 8, 'h', 5, 'h']
    lista = ['a', 1, 'a', 1, 'a', 1, 'a', 1, 'a', 1, 1, 'a', 1, 'a']
    # lista = ['b', 3, 'y', 3, 'b', 5, 'c', 5, 'h', 1, 9, 'h', 5, '1']
    numeros_ordenados, letras_ordenadas = separar(lista)
    print("Números:", numeros_ordenados)
    print("Letras:", letras_ordenadas)

if __name__ == "__main__":
    main()