from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    #Crea la clase recibiendo el parametro del nombre del restaurante y crea dos listas vacias para el menu y los usuarios
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.__productos : list[Producto] = []
        self.__usuarios : list[Usuario] = []

    def agregar_producto(self, producto) -> None:
        #Añade a la lista menú el producto que se le pasa por el parametro
        self.__productos.append(producto)

    def mostrar_menu(self) -> None:
        print("-" * 30)
        print(f"Menú de {self.nombre}:")
        #recorre la lista de productos que hay en la lista menú y los muestra
        for producto in self.__productos:
            print(producto.mostrar_informacion())
        print("-" * 30)

    def buscar_producto(self, nombre: str):
        #Busca un producto en la lista menú que tenga el mismo nombre que el parametro y lo devuelve, si no lo encuentra devuelve None
        for producto in self.__productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def registrar_usuario(self, usuario) -> None:
        #Añade a la lista usuarios el usuario que se le pasa por el parametro
        self.__usuarios.append(usuario)

    def mostrar_usuarios(self) -> None:
        print("-" * 30)
        print(f"usuarios de {self.nombre}:")
        for usuario in self.__usuarios:
            print(usuario.mostrar_informacion())
        print("-" * 30)

    def buscar_usuario(self, nombre: str):
        #Busca un usuario en la lista usuarios que tenga el mismo nombre que el parametro y lo devuelve, si no lo encuentra devuelve None
        for usuario in self.__usuarios:
            if usuario.nombre.lower() == nombre.lower():
                return usuario
        return None
    
    def eliminar_producto(self, producto) -> None:
        #Elimina un producto de la lista de productos
        if producto in self.__productos:
            self.__productos.remove(producto)
    
    @property
    def productos(self):
        #Retorna la lista de productos
        return self.__productos