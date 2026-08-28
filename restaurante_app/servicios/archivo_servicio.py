import json
from pathlib import Path
from typing import Any

try:
    from ..modelos.producto import Producto
    from ..modelos.usuario import Usuario
    from ..modelos.venta import Venta
except ImportError:
    from modelos.producto import Producto
    from modelos.usuario import Usuario
    from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, directorio: str | Path | None = None) -> None:
        self.directorio = Path(directorio) if directorio else Path(__file__).parent.parent / "datos"

    def cargar_productos(self) -> list[Producto]:
        productos = []
        for registro in self._cargar("productos.json"):
            try:
                productos.append(
                    Producto(
                        registro["codigo"],
                        registro["nombre"],
                        registro["precio"],
                        registro["categoria"],
                        registro.get("stock", 0),
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue
        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        usuarios = []
        for registro in self._cargar("usuarios.json"):
            try:
                usuarios.append(
                    Usuario(
                        registro["identificacion"],
                        registro["nombre"],
                        registro["telefono"],
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue
        return usuarios

    def cargar_ventas(self) -> list[Venta]:
        ventas = []
        for registro in self._cargar("ventas.json"):
            try:
                ventas.append(
                    Venta(
                        registro["usuario_id"],
                        registro["producto_codigo"],
                        registro["cantidad"],
                    )
                )
            except (KeyError, TypeError, ValueError):
                continue
        return ventas

    def guardar_productos(self, productos: list[Producto]) -> None:
        self._guardar(
            "productos.json",
            [
                {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                    "categoria": producto.categoria,
                    "stock": producto.stock,
                }
                for producto in productos
            ],
        )

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._guardar(
            "usuarios.json",
            [
                {
                    "identificacion": usuario.identificacion,
                    "nombre": usuario.nombre,
                    "telefono": usuario.telefono,
                }
                for usuario in usuarios
            ],
        )

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        self._guardar(
            "ventas.json",
            [
                {
                    "usuario_id": venta.usuario_id,
                    "producto_codigo": venta.producto_codigo,
                    "cantidad": venta.cantidad,
                }
                for venta in ventas
            ],
        )

    def _cargar(self, nombre_archivo: str) -> list[dict[str, Any]]:
        try:
            with open(self.directorio / nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = json.load(archivo)
        except FileNotFoundError:
            return []
        except (json.JSONDecodeError, PermissionError) as error:
            raise RuntimeError(f"No se pudo leer {nombre_archivo}: {error}") from error
        if not isinstance(contenido, list):
            raise ValueError(f"{nombre_archivo} debe contener una lista JSON.")
        return contenido

    def _guardar(self, nombre_archivo: str, registros: list[dict[str, Any]]) -> None:
        try:
            self.directorio.mkdir(parents=True, exist_ok=True)
            with open(self.directorio / nombre_archivo, "w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, ensure_ascii=False, indent=4)
        except PermissionError as error:
            raise RuntimeError(f"No se pudo guardar {nombre_archivo}: {error}") from error