# #Escribir un programa en Python que comienza pidiendo una frase o palabra al
# usuario. Una vez leída la frase o palabra el programa deberá generar un nuevo
# string a partir de las letras que contengan.
# En el string construído deben aparecer todas las letras (sin repetir) que estén
# dentro de la frase o palabra leída ordenadas de forma decreciente. Los espacios
# en blanco en la frase se deben omitir.

frase = input("Introduce una frase: ")
#Aquí lo que estamos haciendo es reemplazar los espacios en blanco a una cadena vacía 
frase_limpia = frase.replace(" ", "").lower()
#Con el set podemos quitar las letras repetidas de la frase ya que un conjunto no permite los duplicados
letras_unicas = set(frase_limpia)
letras_ordenadas = sorted(letras_unicas)
# Une las letras ordenadas en un string
resultado = ''.join(letras_ordenadas)
print(resultado)
