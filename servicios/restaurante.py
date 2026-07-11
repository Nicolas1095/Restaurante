class Restaurante:
    #Crea la clase recibiendo el parametro del nombre del restaurante y crea dos listas vacias para el menu y los clientes
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.menu = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        #Añade a la lista menú el producto que se le pasa por el parametro
        self.menu.append(producto)

    def mostrar_menu(self) -> None:
        print("-" * 30)
        print(f"Menú de {self.nombre}:")
        #recorre la lista de productos que hay en la lista menú y los muestra
        for producto in self.menu:
            print(producto.mostrar_informacion())
        print("-" * 30)

    def buscar_producto(self, nombre: str):
        #Busca un producto en la lista menú que tenga el mismo nombre que el parametro y lo devuelve, si no lo encuentra devuelve None
        for producto in self.menu:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def registrar_cliente(self, cliente) -> None:
        #Añade a la lista clientes el cliente que se le pasa por el parametro
        self.clientes.append(cliente)
        
    def mostrar_clientes(self) -> None:
        print("-" * 30)
        print(f"Clientes de {self.nombre}:")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())
        print("-" * 30)

    def buscar_cliente(self, nombre: str):
        #Busca un cliente en la lista clientes que tenga el mismo nombre que el parametro y lo devuelve, si no lo encuentra devuelve None
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower:
                return cliente
        return None