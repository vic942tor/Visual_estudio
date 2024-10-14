
frase = input("Introduce una frase o palabra: ")
frase_limpia = frase.replace(" ", "").lower()
#Con el set podemos quitar las letras repetidas de la frase ya que un conjunto no permite los duplicados
letras_unicas = set(frase_limpia)
letras_ordenadas = sorted(letras_unicas)
# Une las letras ordenadas en un string
resultado = ''.join(letras_ordenadas)
print(resultado)
