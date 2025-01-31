# Recibos.py
import Polizas  # Para verificar que la póliza existe

# Lista global de recibos
recibos = []

def validar_poliza_existente(nro_poliza):
    """
    Valida que la póliza exista en el sistema.
    Parametros:
    nro_poliza (str): El número de póliza a verificar.
    
    Retorna:
    bool: True si la póliza existe, False si no.
    """
    return any(p['nro_poliza'] == nro_poliza for p in Polizas.polizas)

def crear_recibo():
    """
    Crea un nuevo recibo.
    """
    id_recibo = input("Ingrese el ID del recibo: ")
    
    # Verificar que el recibo no exista
    if any(r['id_recibo'] == id_recibo for r in recibos):
        print("El recibo con este ID ya existe.")
        return

    nro_poliza = input("Ingrese el número de póliza: ")

    # Verificar que la póliza exista
    if not validar_poliza_existente(nro_poliza):
        print("La póliza indicada no existe.")
        return

    # Solicitar y crear el nuevo recibo
    nuevo_recibo = {
        "id_recibo": id_recibo,
        "nro_poliza": nro_poliza,
        "fecha_inicio": input("Ingrese la fecha de inicio (YYYY-MM-DD): "),
        "duracion": input("Ingrese la duración (A: Anual, S: Semestral, T: Trimestral, M: Mensual): "),
        "importe_cobrar": float(input("Ingrese el importe a cobrar: ")),
        "fecha_cobro": input("Ingrese la fecha de cobro (YYYY-MM-DD): "),
        "estado_recibo": input("Ingrese el estado del recibo (Pendiente, Pendiente_banco, Cobrado, Cobrado_banco, Baja): "),
        "importe_pagar": float(input("Ingrese el importe a pagar: ")),
        "estado_liquidacion": input("Ingrese el estado de liquidación (Pendiente, Liquidado): "),
        "fecha_liquidacion": input("Ingrese la fecha de liquidación (YYYY-MM-DD): ")
    }

    recibos.append(nuevo_recibo)
    print("Recibo creado con éxito.")

def modificar_recibo():
    """
    Modifica los datos de un recibo existente, excepto el ID del recibo.
    """
    id_recibo = input("Ingrese el ID del recibo a modificar: ")
    
    # Buscar el recibo
    recibo = next((r for r in recibos if r['id_recibo'] == id_recibo), None)
    
    if recibo:
        # Modificar los campos directamente
        campo = input(f"Recibo actual: {recibo}\n¿Qué campo desea modificar? "
            "(fecha_inicio, duracion, importe_cobrar, fecha_cobro, estado_recibo, importe_pagar, estado_liquidacion, fecha_liquidacion): ")
        
        if campo in recibo:
            nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")
            if campo in ["importe_cobrar", "importe_pagar"]:
                nuevo_valor = float(nuevo_valor)
            recibo[campo] = nuevo_valor
            print(f"Recibo modificado: {recibo}")
        else:
            print("Campo no válido.")
    else:
        print("El recibo con ese ID no existe.")

def eliminar_recibo():
    """
    Elimina un recibo que no esté en estado Pendiente o Cobrado.
    """
    id_recibo = input("Ingrese el ID del recibo a eliminar: ")

    # Buscar y eliminar el recibo si cumple las condiciones
    recibo = next((r for r in recibos if r['id_recibo'] == id_recibo), None)

    if recibo and recibo['estado_recibo'] not in ['Pendiente', 'Cobrado']:
        recibos.remove(recibo)
        print("Recibo eliminado con éxito.")
    else:
        print("No se puede eliminar el recibo o no existe.")

def menu_recibos(datos):
    """
    Muestra el menú de opciones de los recibos y permite interactuar con las opciones.
    """
    opciones = {
        '1': crear_recibo,
        '2': modificar_recibo,
        '3': eliminar_recibo,
        '9': lambda: None  # Regresar al menú principal
    }
    
    while True:
        print("""
        Menú Recibos:
        1. Crear Recibo
        2. Modificar Recibo
        3. Eliminar Recibo
        9. Regresar al menú principal
        """)
        opcion = input("Seleccione una opción: ")
        
        if opcion in opciones:
            if opcion == '9':
                break
            opciones[opcion]()
        else:
            print("Opción no válida.")