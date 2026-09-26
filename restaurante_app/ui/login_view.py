import tkinter as tk
from tkinter import ttk
from typing import Callable
from pathlib import Path
try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio

base_dir = Path(__file__).resolve().parent.parent 
class LoginView(ttk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, on_login: Callable[[str], None]) -> None:
        super().__init__(master, padding=24)
        self._servicio = servicio
        self._on_login = on_login
        self._identificacion = tk.StringVar()
        self._contrasena = tk.StringVar()
        self._mensaje = tk.StringVar()
        self._construir()

    def _construir(self) -> None:
        ttk.Label(self, text="Restaurante", font=("TkDefaultFont", 18, "bold")).grid(
            row=0, column=0, columnspan=2, pady=5
        )
        ruta_icono = base_dir / "assets" / "perfil.png"
        icono = tk.PhotoImage(file=ruta_icono)
        icono = icono.subsample(8, 8)
        etiqueta_icono = ttk.Label(self, image=icono)
        etiqueta_icono.image = icono
        etiqueta_icono.grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Label(self, text="Usuario:").grid(row=2, column=0, pady=5, columnspan=2,)
        ttk.Entry(self, textvariable=self._identificacion).grid(
            row=3, column=0, pady=5, columnspan=2
        )
        ttk.Label(self, text="Contraseña:").grid(row=4, column=0, pady=5, columnspan=2,)
        ttk.Entry(self, textvariable=self._contrasena, show="*").grid(
            row=5, column=0, pady=5, columnspan=2,
        )
        ttk.Label(self, text="Contraseña predeterminada: 1234").grid(
            row=6, column=0, columnspan=2, pady=5
        )
        botones = ttk.Frame(self)
        botones.grid(row=7, column=0, pady=5, columnspan=2)
        ttk.Button(botones, text="Ingresar", command=self._ingresar).grid(
            row=0, column=0, pady=5, padx=(0, 5)
        )
        ttk.Button(botones, text="Registrar", command=self._registrar).grid(
            row=0, column=1, pady=5, padx=(5, 0)
        )
        ttk.Label(self, textvariable=self._mensaje).grid(
            row=8, column=0, columnspan=2, pady=5
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
            self._on_login(identificacion)
    def _registrar(self) -> None:
        ventana_registro = tk.Toplevel(self)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("400x300")
        ttk.Label(ventana_registro, text="Registro de Usuario", font=("TkDefaultFont", 14, "bold")).pack(pady=10)
        ruta_icono = base_dir / "assets" / "perfil.png"
        icono = tk.PhotoImage(file=ruta_icono)
        icono = icono.subsample(10, 10)
        etiqueta_icono = ttk.Label(ventana_registro, image=icono)
        etiqueta_icono.image = icono
        etiqueta_icono.pack()
        ttk.Label(ventana_registro, text="Ingrese su identificación:").pack(pady=5)
        identificacion_entry = ttk.Entry(ventana_registro)
        identificacion_entry.pack(pady=5)
        ttk.Label(ventana_registro, text="Ingrese su contraseña:").pack(pady=5)
        contrasena_entry = ttk.Entry(ventana_registro, show="*")
        contrasena_entry.pack(pady=5)
        ttk.Button(ventana_registro, text="Registrar", command=lambda: self._guardar_registro(ventana_registro, identificacion_entry.get(), contrasena_entry.get())).pack(pady=10)
        ttk.Label(ventana_registro, textvariable=self._mensaje).pack(pady=5)
    
    def _guardar_registro(self, ventana: tk.Toplevel, identificacion: str, contrasena: str) -> None:
        if not identificacion or not contrasena:
            self._mensaje.set("Ingrese identificación y contraseña.")
            return
        try:
            self._servicio.registrar_usuario(identificacion, "Nombre", "Teléfono")
            self._mensaje.set("Usuario registrado exitosamente.")
            ventana.destroy()
        except ValueError as e:
            self._mensaje.set(str(e))