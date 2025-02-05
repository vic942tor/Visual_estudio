class Usuario:
    def __init__(self, nif, nombre, apellido1, apellido2):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.nif = nif

    def __str__(self) -> str:
        return f"{self.nombre}\n{self.apellido1} {self.apellido2}\nnif = {self.nif}"

user01 = Usuario('12345678F','Pepe','García')
print(user01)