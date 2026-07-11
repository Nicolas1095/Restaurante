from modelos.producto import Producto
class Bebida(Producto):
    def __init__(self, nombre: str, precio: float, volumen: int):
        #Toma los atributos de la clase padre Producto para usarlas en la clase Bebida
        super().__init__(nombre, precio)
        #Añade el atributo volumen a la clase Bebida
        self.volumen = volumen

    def __str__(self) -> str:
        #Cuando se imprima una bebida, se mostrará como string el nombre, el precio y el volumen de la bebida en mililitros
        return f"{self.nombre} - ${self.obtener_precio():.2f} (Volumen: {self.volumen} ml)"