

try:
    from ..modelos.venta import Venta
    from .archivo_servicio import ArchivoServicio
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:
    from servicios.archivo_servicio import ArchivoServicio
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta


class RestauranteServicio:
    """Coordina la información que consumen las vistas de la aplicación."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self.nombre = "Restaurante"
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
    def validar_acceso(self, identificacion: str, contrasena: str) -> bool:
        if not identificacion or not contrasena:
            return False
        return any(
            usuario.identificacion == identificacion
            and usuario.contrasena == contrasena
            for usuario in self.__usuarios
        )

    def listar_productos(self):
        return list(self.__productos)

    def listar_usuarios(self):
        return list(self.__usuarios)

    def identificacion_predeterminada(self) -> str:
        return self.__usuarios[0].identificacion if self.__usuarios else ""

    def siguiente_codigo_producto(self) -> str:
        codigos = []
        for producto in self.__productos:
            if producto.codigo.upper().startswith("P") and producto.codigo[1:].isdigit():
                codigos.append(int(producto.codigo[1:]))
        return f"P{max(codigos, default=0) + 1:03d}"
    
    def siguiente_codigo_usuario(self) -> str:
        identificaciones = [
            int(usuario.identificacion.strip())
            for usuario in self.__usuarios
            if usuario.identificacion.strip().isdigit()
        ]
        return str(max(identificaciones, default=1000) + 1)

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        criterio = identificacion.strip().lower()
        return next(
            (usuario for usuario in self.__usuarios
             if usuario.identificacion.lower() == criterio),
            None,
        ) if criterio else None

    def registrar_usuario(self, nombre: str, telefono: int, contrasena: str, rol = "Cliente") -> Usuario:
        identificacion = self.siguiente_codigo_usuario()
        telefono = str(telefono)
        while self.buscar_usuario(identificacion):
            identificacion = str(int(identificacion) + 1)
        usuario = Usuario(identificacion, nombre.strip(), telefono.strip(), contrasena.strip(), rol.strip())
        self.__usuarios.append(usuario)
        self.__archivo_servicio.guardar_usuarios(self.__usuarios)
        return usuario
    def listar_ventas(self) -> list[Venta]:
        return list(self.__ventas)
    def actualizar_usuario(self, identificacion: str, nombre: str, telefono: str, rol: str) -> Usuario:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            raise ValueError("No se encontró un usuario con esa identificación.")
        if usuario.identificacion == "1001" and usuario.rol != rol.strip():
            raise ValueError("No se puede cambiar el rol del usuario 1001.")
        actualizado = Usuario(
            identificacion.strip(),
            nombre.strip(),
            telefono.strip(),
            usuario.contrasena,
            rol.strip(),
        )
        usuario.nombre = actualizado.nombre
        usuario.telefono = actualizado.telefono
        usuario.rol = actualizado.rol
        self.__archivo_servicio.guardar_usuarios(self.__usuarios)
        return usuario

    def eliminar_usuario(self, identificacion: str) -> None:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            raise ValueError("No se encontró un usuario con esa identificación.")
        if usuario.identificacion == "1001":
            raise ValueError("No se puede eliminar el usuario 1001.")
        self.__usuarios.remove(usuario)
        self.__archivo_servicio.guardar_usuarios(self.__usuarios)

    def buscar_producto(self, identificador: str) -> Producto | None:
        criterio = identificador.strip().lower()
        if not criterio:
            return None
        return next(
            (
                producto
                for producto in self.__productos
                if producto.codigo.lower() == criterio or producto.nombre.lower() == criterio
            ),
            None,
        )

    def registrar_producto(
        self, codigo: str, nombre: str, precio: float, categoria: str, stock: int
    ) -> Producto:
        codigo = codigo.strip()
        codigos_existentes = {producto.codigo.strip().casefold() for producto in self.__productos}
        if codigo.casefold() in codigos_existentes:
            codigo = self.siguiente_codigo_producto()
            while codigo.casefold() in codigos_existentes:
                codigo = f"P{int(codigo[1:]) + 1:03d}"
        producto = Producto(codigo, nombre.strip(), precio, categoria.strip(), stock)
        self.__productos.append(producto)
        self.__archivo_servicio.guardar_productos(self.__productos)
        return producto

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        categoria: str,
        stock: int,
    ) -> Producto:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró un producto con ese código.")
        actualizado = Producto(
            producto.codigo, nombre.strip(), precio, categoria.strip(), stock
        )
        producto.nombre = actualizado.nombre
        producto.precio = actualizado.precio
        producto.categoria = actualizado.categoria
        producto.stock = actualizado.stock
        self.__archivo_servicio.guardar_productos(self.__productos)
        return producto
    def vender_producto(self, usuario_id: str, codigo: str, cantidad: int, precio: float) -> None:
        if self.buscar_usuario(usuario_id) is None:
            raise ValueError("No se encontró el usuario de la venta.")
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró el producto de la venta.")
        if cantidad > producto.stock:
            raise ValueError("La cantidad excede el stock disponible.")
        venta = Venta(usuario_id, codigo, cantidad, precio)
        producto.stock -= cantidad
        self.__archivo_servicio.guardar_productos(self.__productos)
        self.__ventas.append(venta)
        self.__archivo_servicio.guardar_ventas(self.__ventas)
    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró un producto con ese código.")
        self.__productos.remove(producto)
        self.__archivo_servicio.guardar_productos(self.__productos)
