#se pide el NIF o NIE y se comprueba su validez
#12345678B -> NIF
#
#@1234567X -> @ = "x","y","z"
LETRANIF = "TRWAGMYFPDXBNJZSQVHLCKE"
nif_nie = input("Introduce tu NIF/NIE: ").upper()
if nif_nie[0].isnumeric():
    calculo = int(nif_nie[:8]) % 23
    letra = LETRANIF[calculo]
    if letra == nif_nie[8]:
        print("El NIF es valido")
    else:
        print("El NIF no es valido")
elif nif_nie[0] == "X":
    calculo2 = int(nif_nie[1:8]) % 23
    letra = LETRANIF[calculo2]
    if letra == nif_nie[8]:
        print("El NIE es valido")
    else:
        print("El NIE no es valido")
elif nif_nie[0] == "Y":
    calculo3 = int("1" + nif_nie[1:8]) % 23
    letra = LETRANIF[calculo3]
    if letra == nif_nie[8]:
        print("El NIE es valido")
    else:
        print("El NIE no es valido")
elif nif_nie[0] == "Z":
    calculo3 = int("2" + nif_nie[1:8]) % 23
    letra = LETRANIF[calculo3]
    if letra == nif_nie[8]:
        print("El NIE es valido")
    else:
        print("El NIE no es valido")
else:
    print("Introduzca un NIF o un NIE valido")