try:
    from .archivo_servicio import ArchivoServicio
except ImportError:
    from servicios.archivo_servicio import ArchivoServicio


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
