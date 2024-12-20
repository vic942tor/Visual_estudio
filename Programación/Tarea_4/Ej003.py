# El valor de cada clave es una lista que contiene diccionarios con los platos que
# ofrece el restaurante. Estos diccionarios tienen dos claves: plato e ingredientes el
# primero representa el nombre del plato y el segundo una lista de los ingredientes
# que contiene.

comidas = {}  
while True:
    print('1. Agregar plato')
    print('2. Buscar plato por ingredientes')
    print('3. Eliminar plato o categoría')
    print('4. Ver el menú')
    print('5. Salir')
    selección = input('seleccione lo que desea realizar: ')
#Valida que la selección esté entre las opciones permitidas.
    if selección < '1' or selección > '5':
        print('Opción inválida. Intente nuevamente.')
        continue
    if selección == '5':
        break
    if selección == '4':
        print('~~~~~~~~~~~~~~~~~~Menú~~~~~~~~~~~~~~~~~~:')
#Recorre cada categoría y muestra sus platos con ingredientes.
        for categoria, platos in comidas.items():
            print(f'-----------------{categoria}-----------------')
            for plato in platos:
                ingredientes = ', '.join(plato['ingredientes'])
                print(f'- {plato["plato"]} \n  Ingredientes: {ingredientes}')
        continue
    if selección == '1':
        while True:
            categoría = input('Ingrese la categoría del plato, para salir ingrese 0: ')
            if categoría == '0': 
                break
#Valida que la categoría no contenga espacios vacíos o sea inválida.
            if ' ' in categoría or not categoría.strip():  
                print('Categoría inválida. Intente nuevamente.')
                continue
#Si la categoría no existe, la crea en el diccionario.
            if categoría not in comidas:
                comidas[categoría] = []
#Solicita el nombre del plato y valida si está correcto.
            nombre = input('Ingrese el nombre del plato: ')
            if ' ' in nombre or not nombre.strip():
                print('Nombre inválido. Intente nuevamente.')
                continue

#Verifica si el plato ya existe en la categoría.
            if nombre in [plato['plato'] for plato in comidas[categoría]]:
                print('El plato ya existe en esta categoría. Intente nuevamente.')
                continue
#Solicita los ingredientes del plato.
            while True:
                ingredientes = input('Ingrese los ingredientes separados por coma y sin espacios: ').split(',')
                ingredientes = [ingrediente.strip() for ingrediente in ingredientes if ingrediente.strip()]  # Limpia espacios vacíos.
                if len(ingredientes) < 1:  # Valida que haya al menos un ingrediente.
                    print('Debe ingresar al menos un ingrediente. Intente nuevamente.')
                    continue
                break
#Agrega el plato al diccionario bajo la categoría correspondiente.
            comidas[categoría].append({'plato': nombre, 'ingredientes': ingredientes})
            print('Plato agregado exitosamente.')
    if selección == '3':
        while True:
#Solicita al usuario si desea eliminar un plato o una categoría.
            eliminar = input('Desea eliminar una categoría (C) o un Plato (P)?: ').upper()
            categoría = input('Ingrese la categoría de plato para volver ingrese 0: ')
            if categoría == '0':
                break
            if eliminar == 'P':
#Valida que la categoría sea válida.
                if ' ' in categoría:  
                    print('Categoría inválida. Intente nuevamente.')
                    continue
 #Verifica si la categoría existe.                
                if categoría not in comidas: 
                    print('Categoría no encontrada. Intente nuevamente.')
                    continue

#Solicita el nombre del plato a eliminar.
                nombre = input('Ingrese el nombre del plato: ')
                if ' ' in nombre:  # Valida que el nombre sea válido.
                    print('Nombre inválido. Intente nuevamente.')
                    continue
#Busca el plato en la categoría y lo elimina si existe.
                for plato in comidas[categoría]:
                    if plato['plato'] == nombre:
                        comidas[categoría].remove(plato)
                        print('Plato eliminado exitosamente.')
                        break
                else:
                    print('Plato no encontrado. Intente nuevamente.')
                    continue
#Si el usuario elige eliminar una categoría completa.
            elif eliminar == 'C':
                if ' ' in categoría: 
                    print('Categoría inválida. Intente nuevamente.')
                    continue
                if categoría not in comidas:  
                    print('Categoría no encontrada. Intente nuevamente.')
                    continue
#Elimina la categoría del diccionario.
                del comidas[categoría]
                print('Categoría eliminada exitosamente.')
                break
    if selección == '2':
        while True:
#Solicita al usuario que ingrese ingredientes para buscar.
            ingredientes = input('Ingrese el o los ingredientes separados por coma y sin espacios: ').split(',')
            if len(ingredientes) > 0 and ingredientes.isalpha():  # Valida que los ingredientes sean válidos.
                for categoria, platos in comidas.items():
                    print(f'-----------------{categoria}-----------------')
                    for plato in platos:
#Busca si algún ingrediente coincide con los del plato.
                        if any(ingrediente in plato['ingredientes'] for ingrediente in ingredientes):
                            print(f'- {plato["plato"]} \n  Ingredientes: {", ".join(plato["ingredientes"])}')
                            break
            else:
                print('“NO hay platos que contengan todos los ingredientes solicitados.')
                continue

