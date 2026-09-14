import tkinter as tk
from tkinter import ttk
from typing import Callable

try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, on_login: Callable[[], None]) -> None:
        super().__init__(master, padding=24)
        self._servicio = servicio
        self._on_login = on_login
        self._identificacion = tk.StringVar()
        self._contrasena = tk.StringVar()
        self._mensaje = tk.StringVar()
        self._construir()

    def _construir(self) -> None:
        ttk.Label(self, text="Restaurante", font=("TkDefaultFont", 18, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 18)
        )
        ttk.Label(self, text="Usuario:").grid(row=1, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=self._identificacion).grid(row=1, column=1, sticky="ew", pady=4)
        ttk.Label(self, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=4)
        ttk.Entry(self, textvariable=self._contrasena, show="*").grid(row=2, column=1, sticky="ew", pady=4)
        ttk.Button(self, text="Ingresar", command=self._ingresar).grid(
            row=3, column=0, columnspan=2, pady=(14, 6)
        )
        ttk.Label(self, textvariable=self._mensaje, foreground="firebrick").grid(
            row=4, column=0, columnspan=2
        )
        self.columnconfigure(1, weight=1)

    def _ingresar(self) -> None:
        identificacion = self._identificacion.get().strip()
        contrasena = self._contrasena.get()
        if not identificacion or not contrasena:
            self._mensaje.set("Ingrese usuario y contraseña.")
        elif not self._servicio.validar_acceso(identificacion, contrasena):
            self._mensaje.set("Las credenciales no son válidas.")
        else:
            self._on_login()
