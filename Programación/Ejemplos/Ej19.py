#Ordenar la lista de temperaturas en orden ascendente según la temperatura
temp = [['Tfe',27.3,14.5],
            ['Lpa',26.2,16.3],
                ['Gom',20.3,17.3],
                    ['hie',25.2,13.7]]

temp_max = temp[0][1]
lugar_max = temp[0][0]
lugar_min = temp[0][0]
temp_min = temp[0][2]

for datos in temp:
    if datos[1] > temp_max:
        temp_max = datos[1]
        lugar_max = datos[0]
        

