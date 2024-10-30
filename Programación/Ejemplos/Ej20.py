#Realizar un programa que dado dos listas verifique que las listas estén solapadas o no

A = [1,2,3,4]
C = [2,0,9,3,4]
solapamiento = []

for valor in A:
    if valor in C and valor not in solapamiento:
        solapamiento.append(valor)

if len(solapamiento) > 0:
    print ('Las listas están solapadas')
    for valor in solapamiento:
        print(f'{valor}' , end="  ")
else:
    print ('Las listas no están solapadas')


