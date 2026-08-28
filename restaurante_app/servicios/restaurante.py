try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..modelos.venta import Venta
    from .archivo_servicio import ArchivoServicio
except ImportError:
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta
    from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self, nombre: str, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.nombre = nombre
        self.__archivo_servicio = archivo_servicio or ArchivoServicio()
        self.__productos: list[Producto] = self.__archivo_servicio.cargar_productos()
        self.__usuarios: list[Usuario] = self.__archivo_servicio.cargar_usuarios()
        self.__ventas: list[Venta] = self.__archivo_servicio.cargar_ventas()

    def agregar_producto(self, producto: Producto) -> None:
        self.__productos.append(producto)
        self.__archivo_servicio.guardar_productos(self.__productos)

    def mostrar_menu(self) -> None:
        print("-" * 30)
        print(f"Menú de {self.nombre}:")
        #recorre la lista de productos que hay en la lista menú y los muestra
        for producto in self.__productos:
            print(producto.mostrar_informacion())
        print("-" * 30)

    def buscar_producto(self, identificador: str) -> Producto | None:
        for producto in self.__productos:
            if producto.codigo.lower() == identificador.lower() or producto.nombre.lower() == identificador.lower():
                return producto
        return None
    
    def registrar_usuario(self, usuario: Usuario) -> None:
        self.__usuarios.append(usuario)
        self.__archivo_servicio.guardar_usuarios(self.__usuarios)

    def mostrar_usuarios(self) -> None:
        print("-" * 30)
        print(f"usuarios de {self.nombre}:")
        for usuario in self.__usuarios:
            print(usuario.mostrar_informacion())
        print("-" * 30)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        for usuario in self.__usuarios:
            if usuario.identificacion.lower() == identificacion.lower() or usuario.nombre.lower() == identificacion.lower():
                return usuario
        return None
    
    def eliminar_producto(self, producto: Producto) -> None:
        if producto in self.__productos:
            self.__productos.remove(producto)
            self.__archivo_servicio.guardar_productos(self.__productos)

    def actualizar_producto(self, producto: Producto, nombre: str, precio: float) -> None:
        producto.actualizar_informacion(nombre, precio)
        self.__archivo_servicio.guardar_productos(self.__productos)
    def vender_producto(self, codigo_producto: str, identificacion_usuario: str, cantidad: int) -> bool:
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)
        if usuario is None or producto is None:
            return False
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            return False
        if producto.stock < cantidad:
            return False
        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        producto.vender(cantidad)
        self.__ventas.append(venta)
        self.__archivo_servicio.guardar_productos(self.__productos)
        self.__archivo_servicio.guardar_ventas(self.__ventas)
        return True

    def ventas_de_usuario(self, identificacion_usuario: str) -> list[Venta]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return []
        return [venta for venta in self.__ventas if venta.usuario_id == usuario.identificacion]
    
    @property
    def productos(self):
        return self.__productos

    @property
    def usuarios(self) -> list[Usuario]:
        return self.__usuarios

    @property
    def ventas(self) -> list[Venta]:
        return self.__ventas