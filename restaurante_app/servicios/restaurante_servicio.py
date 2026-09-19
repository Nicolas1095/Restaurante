try:
    from .archivo_servicio import ArchivoServicio
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
except ImportError:
    from servicios.archivo_servicio import ArchivoServicio
    from modelos.producto import Producto
    from modelos.usuario import Usuario


class RestauranteServicio:
    """Coordina la información que consumen las vistas de la aplicación."""

    def __init__(self, archivo_servicio: ArchivoServicio | None = None) -> None:
        self._archivo_servicio = archivo_servicio or ArchivoServicio()
        self._productos = self._archivo_servicio.cargar_productos()
        self._usuarios = self._archivo_servicio.cargar_usuarios()

    def validar_acceso(self, identificacion: str, contrasena: str) -> bool:
        if not identificacion or not contrasena:
            return False
        return any(
            usuario.identificacion == identificacion
            and usuario.contrasena == contrasena
            for usuario in self._usuarios
        )

    def listar_productos(self):
        return list(self._productos)

    def listar_usuarios(self):
        return list(self._usuarios)

    def identificacion_predeterminada(self) -> str:
        return self._usuarios[0].identificacion if self._usuarios else ""

    def siguiente_codigo_producto(self) -> str:
        codigos = []
        for producto in self._productos:
            if producto.codigo.upper().startswith("P") and producto.codigo[1:].isdigit():
                codigos.append(int(producto.codigo[1:]))
        return f"P{max(codigos, default=0) + 1:03d}"

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        criterio = identificacion.strip().lower()
        return next(
            (usuario for usuario in self._usuarios
             if usuario.identificacion.lower() == criterio),
            None,
        ) if criterio else None

    def registrar_usuario(self, identificacion: str, nombre: str, telefono: str) -> Usuario:
        identificacion = identificacion.strip()
        if self.buscar_usuario(identificacion):
            raise ValueError("Ya existe un usuario con esa identificación.")
        usuario = Usuario(identificacion, nombre.strip(), telefono.strip(), "1234")
        self._usuarios.append(usuario)
        self._archivo_servicio.guardar_usuarios(self._usuarios)
        return usuario

    def actualizar_usuario(self, identificacion: str, nombre: str, telefono: str) -> Usuario:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            raise ValueError("No se encontró un usuario con esa identificación.")
        actualizado = Usuario(identificacion.strip(), nombre.strip(), telefono.strip(), usuario.contrasena)
        usuario.nombre = actualizado.nombre
        usuario.telefono = actualizado.telefono
        self._archivo_servicio.guardar_usuarios(self._usuarios)
        return usuario

    def eliminar_usuario(self, identificacion: str) -> None:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            raise ValueError("No se encontró un usuario con esa identificación.")
        self._usuarios.remove(usuario)
        self._archivo_servicio.guardar_usuarios(self._usuarios)

    def buscar_producto(self, identificador: str) -> Producto | None:
        criterio = identificador.strip().lower()
        if not criterio:
            return None
        return next(
            (
                producto
                for producto in self._productos
                if producto.codigo.lower() == criterio or producto.nombre.lower() == criterio
            ),
            None,
        )

    def registrar_producto(
        self, codigo: str, nombre: str, precio: float, categoria: str, stock: int
    ) -> Producto:
        codigo = codigo.strip()
        if self.buscar_producto(codigo):
            raise ValueError("Ya existe un producto con ese código.")
        producto = Producto(codigo, nombre.strip(), precio, categoria.strip(), stock)
        self._productos.append(producto)
        self._archivo_servicio.guardar_productos(self._productos)
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
        self._archivo_servicio.guardar_productos(self._productos)
        return producto

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError("No se encontró un producto con ese código.")
        self._productos.remove(producto)
        self._archivo_servicio.guardar_productos(self._productos)
