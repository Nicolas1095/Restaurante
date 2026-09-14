import tkinter as tk
from tkinter import ttk
from typing import Callable

try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio


class MainView(ttk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, on_logout: Callable[[], None]) -> None:
        super().__init__(master, padding=18)
        self._servicio = servicio
        self._on_logout = on_logout
        self._contenido = tk.Text(self, height=14, width=65, state="disabled")
        self._construir()

    def _construir(self) -> None:
        ttk.Label(self, text="Panel principal", font=("TkDefaultFont", 16, "bold")).pack(pady=(0, 12))
        acciones = ttk.Frame(self)
        acciones.pack(fill="x")
        ttk.Button(acciones, text="Productos", command=self._mostrar_productos).pack(side="left", padx=4)
        ttk.Button(acciones, text="Usuarios", command=self._mostrar_usuarios).pack(side="left", padx=4)
        ttk.Button(acciones, text="Ventas (pendiente)", state="disabled").pack(side="left", padx=4)
        ttk.Button(acciones, text="Cerrar sesión", command=self._on_logout).pack(side="right", padx=4)
        self._contenido.pack(fill="both", expand=True, pady=(14, 0))
        self._mostrar_productos()

    def _escribir(self, texto: str) -> None:
        self._contenido.configure(state="normal")
        self._contenido.delete("1.0", tk.END)
        self._contenido.insert("1.0", texto)
        self._contenido.configure(state="disabled")

    def _mostrar_productos(self) -> None:
        texto = "\n".join(
            f"{p.codigo} | {p.nombre} | ${p.precio:.2f} | {p.categoria} | Stock: {p.stock}"
            for p in self._servicio.listar_productos()
        )
        self._escribir(texto or "No hay productos registrados.")

    def _mostrar_usuarios(self) -> None:
        texto = "\n".join(
            f"{u.identificacion} | {u.nombre} | {u.telefono}"
            for u in self._servicio.listar_usuarios()
        )
        self._escribir(texto or "No hay usuarios registrados.")
