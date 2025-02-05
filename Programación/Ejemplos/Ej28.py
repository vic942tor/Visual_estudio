class Persona:
    def __init__(self, nombre: str, edad: int, nif: str):
        self.nombre = nombre
        self.edad = edad
        self.nif = nif

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La edad debe ser un número entero positivo")
        self._edad = valor

    @property
    def nif(self):
        return self._nif

    @nif.setter
    def nif(self, valor):
        if not (isinstance(valor, str) and len(valor) == 8 and valor.isdigit()):
            raise ValueError("El DNI debe tener exactamente 8 caracteres y contener solo números")
        self._nif = valor

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, NIF: {self.nif}"


# Ejemplo de uso
persona = Persona("a", 25, "12345678")
print(persona)  # Salida: Nombre: Juan Pérez, Edad: 25, NIF: 12345678
