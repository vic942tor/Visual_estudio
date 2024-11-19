#Almacenar los datos de los alumenos de 1ro DAM
#alumnos = [(nombre,[bae,pro,lnd,ets,ssf,djk,itk,jkl])]
ASIG = ['BAE','PRO','LND','ETS','SSF','DJK','ITK','JKL']
Alumnos = []
while True:
    nombre = input('Introduzca el nombre, @ para finalizar: ')
    if nombre == '@':
         break
    tupla = (nombre,[])
    for asig in ASIG:
            while True:
                valor = input(f'Nota de {asig}: ')
                if valor.isdigit():
                    nota = int(valor)
                    break
                elif valor.upper() == 'NO':
                    nota = valor
                    break
                else:
                    print('Nota no valida')
            tupla[1].append(nota)
    Alumnos.append(tupla)
print(Alumnos)

                    






