from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre: str, precio: float, calorias: int):
        #Toma los atributos de la clase padre Producto para usarlas en la clase Platillo
        super().__init__(nombre, precio)
        #Añade el atributo calorias a la clase Platillo
        self.calorias = calorias

    def __str__(self) -> str:
        #
        return f"{self.nombre} - ${self.obtener_precio():.2f} (Calorías: {self.calorias} cal)"