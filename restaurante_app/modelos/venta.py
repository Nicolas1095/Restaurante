class Venta:
    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int):
        if not usuario_id or not producto_codigo:
            raise ValueError("La venta debe tener usuario y producto.")
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")
        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    def mostrar_informacion(self) -> str:
        return f"Producto {self.producto_codigo}: {self.cantidad} unidad(es)"