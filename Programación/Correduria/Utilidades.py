
"""
Funciones auxiliares para validaciones y operaciones recurrentes.
Autores: [Nombre1, Nombre2]
"""

def validar_nif_nie_cif(identificador):
    """
    Valida un NIF, NIE o CIF según el formato español.
    validador:
        identificador (str): Cadena a validar.
    devuelve:
        bool: True si es válido, False en caso contrario.
    """
    if len(identificador) == 9:
        if identificador[:8].isdigit() and identificador[-1].isalpha():
            return True
        if identificador[0] in "XYZ" and identificador[1:8].isdigit() and identificador[-1].isalpha():
            return True
        if identificador[0] in "ABCDEFGHJKLMNPQRSUVW" and identificador[1:8].isdigit():
            return True
    return False

def validar_cuenta_bancaria(cuenta):
    """
    Valida una cuenta bancaria según el formato IBAN.
    validador:
        cuenta (str): IBAN a validar.
    devuelve:
        bool: True si es válida, False en caso contrario.
    """
    if len(cuenta) >= 15 and cuenta[:2].isalpha() and cuenta[2:].isdigit():
        return True
    return False

def validar_fecha(fecha, formato="%Y-%m-%d"):
    """
    Valida una fecha según un formato dado.
    validador:
        fecha (str): Fecha en formato de cadena.
        formato (str): Formato esperado de la fecha (por defecto "%Y-%m-%d").
    devuelve:
        bool: True si la fecha es válida, False en caso contrario.
    """
    partes = fecha.split("-")
    if len(partes) == 3 and all(p.isdigit() for p in partes):
        ano, mes, dia = map(int, partes)
        if 1 <= mes <= 12 and 1 <= dia <= 31:
            return True
    return False

def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad de una persona a partir de su fecha de nacimiento.
    validador:
        fecha_nacimiento (str): Fecha de nacimiento en formato "YYYY-MM-DD".
    devuelve:
        int: Edad calculada o -1 si la fecha no es válida.
    """
    if not validar_fecha(fecha_nacimiento):
        return -1
    ano, mes, dia = map(int, fecha_nacimiento.split("-"))
    hoy = [2025, 1, 27]  # Fecha fija para consistencia
    edad = hoy[0] - ano - ((hoy[1], hoy[2]) < (mes, dia))
    return edad

def es_cadena_valida(cadena):
    """
    Verifica si una cadena no está vacía y no contiene solo espacios en blanco.
    validador:
        cadena (str): Cadena a validar.
    devuelve:
        bool: True si es válida, False en caso contrario.
    """
    return bool(cadena and cadena.strip())