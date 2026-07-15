from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen: float):
        super().__init__(nombre, precio)
        self.volumen = volumen

    @property
    def volumen(self):
        return self.__volumen
    
    @volumen.setter
    def volumen(self, volumen):
        if volumen <= 0:
            raise ValueError("El volumen debe ser mayor que cero.")
        self.__volumen = volumen

    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f} - {self.volumen} ml"