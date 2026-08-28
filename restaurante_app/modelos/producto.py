class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int = 0,
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if not codigo:
            raise ValueError("El código no puede estar vacío.")
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if not categoria:
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = categoria

    @property
    def precio(self):
        return self.__precio   
    
    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = precio

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, stock: int) -> None:
        if not isinstance(stock, int) or isinstance(stock, bool) or stock < 0:
            raise ValueError("El stock debe ser un entero no negativo.")
        self.__stock = stock

    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"

    def vender(self, cantidad: int) -> None:
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente.")
        self.stock -= cantidad
    
    def actualizar_informacion(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio