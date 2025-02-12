
"""
Autores: Víctor Fernandez Díaz ~ Marcos Javier Pérez Gómez
"""

def validar_nif_nie_cif(identificador):
    """
    Valida un NIF, NIE o CIF según el formato español.
    """
    if len(identificador) == 9:
        if identificador[:8].isdigit() and identificador[-1].isalpha():
            return True
        if identificador[0] in "XYZ" and identificador[1:8].isdigit() and identificador[-1].isalpha():
            return True
        if identificador[0] in "ABCDEFGHJKLMNPQRSUVW" and identificador[1:8].isdigit():
            return True
    return False

def validar_fecha(fecha, formato="%Y-%m-%d"):
    """
    Valida una fecha según un formato dado.
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

def validar_matricula(matricula: str) -> bool:
    """
    Valida una matrícula de coche en formato español.
    """    
    # Comprobar que la matrícula tiene la longitud correcta
    if len(matricula) != 7:
        return False
    
    # Separar los componentes de la matrícula
    numeros = matricula[:4]
    letras = matricula[4:]
    
    # Validar que los primeros 4 caracteres son dígitos
    if not numeros.isdigit():
        return False
    
    # Validar que los últimos 3 caracteres son letras
    if not letras.isalpha():
        return False
    
    return True