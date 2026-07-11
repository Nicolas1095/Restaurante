class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = precio
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio   
    
    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = precio

    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"