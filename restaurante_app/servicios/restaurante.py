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
        
        # Índices auxiliares para optimizar búsquedas
        self.__indice_productos_por_codigo: dict[str, Producto] = {}
        self.__indice_usuarios_por_id: dict[str, Usuario] = {}
        self.__indice_ventas_por_usuario: dict[str, list[Venta]] = {}
        
        # Reconstruir índices después de cargar desde JSON
        self.__reconstruir_indices()

    def __reconstruir_indices(self) -> None:
        """Reconstruye todos los índices auxiliares a partir de las colecciones principales."""
        # Índice de productos por código
        self.__indice_productos_por_codigo.clear()
        for producto in self.__productos:
            self.__indice_productos_por_codigo[producto.codigo.lower()] = producto
        
        # Índice de usuarios por identificación
        self.__indice_usuarios_por_id.clear()
        for usuario in self.__usuarios:
            self.__indice_usuarios_por_id[usuario.identificacion.lower()] = usuario
        
        # Índice de ventas por usuario
        self.__indice_ventas_por_usuario.clear()
        for venta in self.__ventas:
            usuario_id = venta.usuario_id.lower()
            if usuario_id not in self.__indice_ventas_por_usuario:
                self.__indice_ventas_por_usuario[usuario_id] = []
            self.__indice_ventas_por_usuario[usuario_id].append(venta)

    def agregar_producto(self, producto: Producto) -> None:
        self.__productos.append(producto)
        # Sincronizar índice
        self.__indice_productos_por_codigo[producto.codigo.lower()] = producto
        self.__archivo_servicio.guardar_productos(self.__productos)

    def mostrar_menu(self) -> None:
        print("-" * 30)
        print(f"Menú de {self.nombre}:")
        #recorre la lista de productos que hay en la lista menú y los muestra
        for producto in self.__productos:
            print(producto.mostrar_informacion())
        print("-" * 30)

    def buscar_producto(self, identificador: str) -> Producto | None:
        # Primero intenta búsqueda rápida por código usando índice
        producto = self.__indice_productos_por_codigo.get(identificador.lower())
        if producto:
            return producto
        # Si no encuentra por código, busca por nombre recorriendo la lista
        identificador_lower = identificador.lower()
        for producto in self.__productos:
            if producto.nombre.lower() == identificador_lower:
                return producto
        return None
    
    def registrar_usuario(self, usuario: Usuario) -> None:
        self.__usuarios.append(usuario)
        # Sincronizar índice
        self.__indice_usuarios_por_id[usuario.identificacion.lower()] = usuario
        self.__archivo_servicio.guardar_usuarios(self.__usuarios)

    def mostrar_usuarios(self) -> None:
        print("-" * 30)
        print(f"usuarios de {self.nombre}:")
        for usuario in self.__usuarios:
            print(usuario.mostrar_informacion())
        print("-" * 30)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        # Primero intenta búsqueda rápida por identificación usando índice
        usuario = self.__indice_usuarios_por_id.get(identificacion.lower())
        if usuario:
            return usuario
        # Si no encuentra por identificación, busca por nombre recorriendo la lista
        identificacion_lower = identificacion.lower()
        for usuario in self.__usuarios:
            if usuario.nombre.lower() == identificacion_lower:
                return usuario
        return None
    
    def eliminar_producto(self, producto: Producto) -> None:
        if producto in self.__productos:
            self.__productos.remove(producto)
            # Sincronizar índice
            if producto.codigo.lower() in self.__indice_productos_por_codigo:
                del self.__indice_productos_por_codigo[producto.codigo.lower()]
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
        # Sincronizar índice de ventas por usuario
        usuario_id_lower = usuario.identificacion.lower()
        if usuario_id_lower not in self.__indice_ventas_por_usuario:
            self.__indice_ventas_por_usuario[usuario_id_lower] = []
        self.__indice_ventas_por_usuario[usuario_id_lower].append(venta)
        self.__archivo_servicio.guardar_productos(self.__productos)
        self.__archivo_servicio.guardar_ventas(self.__ventas)
        return True

    def ventas_de_usuario(self, identificacion_usuario: str) -> list[Venta]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return []
        # Usar índice para búsqueda rápida de ventas por usuario
        usuario_id_lower = usuario.identificacion.lower()
        return self.__indice_ventas_por_usuario.get(usuario_id_lower, [])
    
    @property
    def productos(self):
        return self.__productos

    @property
    def usuarios(self) -> list[Usuario]:
        return self.__usuarios

    @property
    def ventas(self) -> list[Venta]:
        return self.__ventas