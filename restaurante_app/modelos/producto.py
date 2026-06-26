class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
    # Cuando se imprima un producto, se mostrará como string el nombre y el precio del producto
    def __str__(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"
