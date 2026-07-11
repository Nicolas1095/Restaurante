class Restaurante:
    #Crea la clase recibiendo el parametro del nombre del restaurante y crea dos listas vacias para el menu y los clientes
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.menu = []
        self.clientes = []

    def agregar_producto(self, producto) -> None:
        #Añade a la lista menú el producto que se le pasa por el parametro
        self.menu.append(producto)

   # def registrar_cliente(self, cliente) -> None:
        #Añade a la lista clientes el cliente que se le pasa por el parametro
    #    self.clientes.append(cliente)"""

    def mostrar_menu(self) -> None:
        print("-" * 30)
        print(f"Menú de {self.nombre}:")
        #recorre la lista de productos que hay en la lista menú y los muestra
        for producto in self.menu:
            print(producto)
        print("-" * 30)

    # def mostrar_clientes(self) -> None:
    #     print("-" * 30)
    #     print("Clientes registrados:")
    #     #recorre la lista de clientes que hay en la lista clientes y los muestra
    #     for cliente in self.clientes:
    #         print(cliente)
    #    print("-" * 30)