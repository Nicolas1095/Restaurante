class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.__precio = precio
    # Cuando se imprima un producto, se mostrará como string el nombre y el precio del producto
    def obtener_precio(self) -> float:
        return self.__precio
    
    def cambiar_precio(self, precio: float) -> None:
        self.__precio = precio

    def __str__(self) -> str:
        return f"{self.nombre} - ${self.__precio:.2f}"
