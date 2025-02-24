class Electrodomestico:
    COLORES_DISPONIBLES = {"blanco", "negro", "rojo", "azul", "gris"}
    CONSUMO_PERMITIDO = {"A", "B", "C", "D", "E", "F"}

    def __init__(self, precio_base=100, peso=5):
        self.precio_base = precio_base
        self.color = "blanco"
        self.consumo_energetico = "F"
        self.peso = peso

    def __str__(self):
        return (f"Electrodoméstico: Precio={self.precio_base}€, Color={self.color}, "
                f"Consumo={self.consumo_energetico}, Peso={self.peso}kg")

# # Pruebas
# electro1 = Electrodomestico()  
# print(electro1)

electro2 = Electrodomestico(200, 10) 
print(electro2)




        