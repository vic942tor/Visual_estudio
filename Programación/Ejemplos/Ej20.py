#Realizar un programa que dado dos listas verifique que las listas estén solapadas o no

A = [1,2,3,4]
C = [2,0,9]

for valor in A:
    if valor in C:
        print(f"Las listas están solapadas por {valor}")
        break
else:
    print("Las listas no están solapadas")

