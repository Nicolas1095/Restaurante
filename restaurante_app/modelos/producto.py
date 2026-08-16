class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

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

    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - ${self.precio:.2f}"
    
    def actualizar_informacion(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio