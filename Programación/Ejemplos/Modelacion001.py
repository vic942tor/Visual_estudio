class Persona:
    def __init__(self, nombre, edad, nif):
        self.nombre = nombre
        self.edad = edad
        self.nif = nif
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, value):
        if not value.isdigit() or int(value) <= 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        self._edad = int(value)
    @property
    def nif(self):
        return self._nif
    @nif.setter
    def nif(self, value):
        if len(value) != 9 or not value[:-1].isdigit() or not value[-1].isalpha():
            raise ValueError("El NIF debe tener 8 números seguidos de una letra.")
        self._nif = value.upper()
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nNIF: {self.nif}"
while True:
    try:
        nombre = input("Introduce el nombre: ")
        edad = input("Introduce la edad: ")
        nif = input("Introduce el NIF: ")
        persona1 = Persona(nombre, edad, nif)
        break
    except ValueError as e:
        print(f"Error: {e}. Inténtalo de nuevo.")
print("\nDatos ingresados:")
print(persona1)
