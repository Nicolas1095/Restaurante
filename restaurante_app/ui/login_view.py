import tkinter as tk
from tkinter import ttk
from typing import Callable
from pathlib import Path
try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio

base_dir = Path(__file__).resolve().parent.parent 
class LoginView(tk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, on_login: Callable[[str], None]) -> None:
        super().__init__(master, background="#eef3f8")
        self._servicio = servicio
        self._on_login = on_login
        self._identificacion = tk.StringVar()
        self._contrasena = tk.StringVar()
        self._mensaje = tk.StringVar()
        self._mensaje_estado = False
        self.definir_estilos()
        self._construir()
    
    def definir_estilos(self) -> None:
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "Login.TButton",
            background="#ee852f",
            foreground="#ffffff",
            font=("Arial", 13, "bold"),
            padding=(8, 6),
            borderwidth=0,
        )
        estilo.configure(
            "Register.TButton",
            background="#43D3C4",
            foreground="#ffffff",
            font=("Arial", 13, "bold"),
            padding=(8, 6),
            borderwidth=0,
        )
        estilo.configure(
            "TLabel",
            background="#fff",
            foreground="#333333",
            font=("Arial", 13),
        )
        estilo.configure("TEntry", 
            padding=(10, 8), 
            font=("Arial", 13),
            background="#f1f1f1",
            bd=0,
            highlightthickness=0,
        )
        estilo.map("TEntry",
            fieldbackground=[("active", "#f1f1f1", ), ("!disabled", "#f1f1f1")],
            bordercolor=[("focus", "#fff"), ("!focus", "#fff")],
        )
        estilo.map("Login.TButton", background=[("active", "#df651e")])
        estilo.map("Register.TButton", background=[("active", "#1DD8C5")])
        
    def _construir(self) -> None:
        contenedor = tk.Frame(self, background="#fff", padx=30, pady=15)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(contenedor, text="Restaurante", font=("TkDefaultFont", 18, "bold"), style="TLabel").grid(
            row=0, column=0, columnspan=2, pady=5
        )
        ruta_icono = base_dir / "assets" / "perfil.png"
        icono = tk.PhotoImage(file=ruta_icono)
        icono = icono.subsample(7, 7)
        etiqueta_icono = ttk.Label(contenedor, image=icono, style="TLabel")
        etiqueta_icono.image = icono
        etiqueta_icono.grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Label(contenedor, text="Usuario:", style="TLabel").grid(row=2, column=0, pady=5, columnspan=2,)
        identificacion_entry = ttk.Entry(contenedor, textvariable=self._identificacion, style="TEntry", width=30)
        identificacion_entry.grid(
            row=3, column=0, pady=5, columnspan=2
        )
        identificacion_entry.bind("<Return>", self._confirmar_ingreso)
        ttk.Label(contenedor, text="Contraseña:", style="TLabel").grid(row=4, column=0, pady=5, columnspan=2,)
        contrasena_entry = ttk.Entry(contenedor, textvariable=self._contrasena, show="*", style="TEntry", width=30)
        contrasena_entry.grid(
            row=5, column=0, pady=5, columnspan=2, 
        )
        contrasena_entry.bind("<Return>", self._confirmar_ingreso)
        ttk.Label(contenedor, text="Contraseña predeterminada: 1234", style="TLabel", font=("Arial", 8), foreground="#666666").grid(
            row=6, column=0, columnspan=2, pady=5
        )
        botones = ttk.Frame(contenedor, style="TLabel")
        botones.grid(row=7, column=0, pady=(20,10) , columnspan=2)
        ttk.Button(botones, text="Ingresar", command=self._ingresar, style="Login.TButton").grid(
            row=0, column=0, pady=5
        )
        ttk.Button(botones, text="Registrar", command=self._registrar, style="Register.TButton").grid(
            row=1, column=0, pady=5
        )
        self._mensaje_label = ttk.Label(
            contenedor,
            textvariable=self._mensaje,
            style="TLabel",
            font=("Arial", 9),
            foreground="#ff0000",
        )
        self._mensaje_label.grid(row=8, column=0, columnspan=2, pady=5)
        contenedor.columnconfigure(1, weight=1)

    def _establecer_mensaje(self, texto: str, exitoso: bool) -> None:
        self._mensaje_estado = exitoso
        self._mensaje.set(texto)
        color = "#00aa00" if exitoso else "#ff0000"
        self._mensaje_label.configure(foreground=color)

    def _ingresar(self) -> None:
        identificacion = self._identificacion.get().strip()
        contrasena = self._contrasena.get()
        if not identificacion or not contrasena:
            self._establecer_mensaje("Ingrese usuario y contraseña.", False)
        elif not self._servicio.validar_acceso(identificacion, contrasena):
            self._establecer_mensaje("Las credenciales no son válidas.", False)
        else:
            self._establecer_mensaje("Acceso correcto.", True)
            self._on_login(identificacion)

    def _confirmar_ingreso(self, event: tk.Event) -> str:
        self._ingresar()
        return "break"

    def _registrar(self) -> None:
        ventana_registro = tk.Toplevel(self)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.minsize(680, 620)
        ventana_registro.configure(background="#eef3f8")
        contenedor = tk.Frame(ventana_registro, background="#fff", padx=30, pady=15)
        contenedor.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(contenedor, text="Registro de Usuario", font=("TkDefaultFont", 14, "bold"), style="TLabel").pack(pady=10)
        ruta_icono = base_dir / "assets" / "perfil.png"
        icono = tk.PhotoImage(file=ruta_icono)
        icono = icono.subsample(7, 7)
        etiqueta_icono = ttk.Label(contenedor, image=icono, style="TLabel")
        etiqueta_icono.image = icono
        etiqueta_icono.pack()
        ttk.Label(contenedor, text="Ingrese su nombre:", style="TLabel").pack(pady=5)
        nombre_entry = ttk.Entry(contenedor, style="TEntry")
        nombre_entry.pack(pady=5)
        ttk.Label(contenedor, text="Ingrese su número de teléfono:", style="TLabel").pack(pady=5)
        telefono_entry = ttk.Entry(contenedor, style="TEntry")
        telefono_entry.pack(pady=5)
        ttk.Label(contenedor, text="Ingrese su contraseña:", style="TLabel").pack(pady=5)
        contrasena_entry = ttk.Entry(contenedor, show="*", style="TEntry")
        contrasena_entry.pack(pady=5)
        def confirmar_registro(event: tk.Event) -> str:
            self._guardar_registro(
                ventana_registro,
                nombre_entry.get(),
                contrasena_entry.get(),
                telefono_entry.get(),
            )
            return "break"

        for entrada in (nombre_entry, telefono_entry, contrasena_entry):
            entrada.bind("<Return>", confirmar_registro)
        ttk.Button(contenedor, text="Registrar", command=lambda: self._guardar_registro(ventana_registro, nombre_entry.get(), contrasena_entry.get(), telefono_entry.get()), style="Register.TButton").pack(pady=10)
        ttk.Label(contenedor, textvariable=self._mensaje, style="TLabel", foreground="#ff0000", font=("Arial", 9)).pack(pady=5)
    
    def _guardar_registro(self, ventana: tk.Toplevel, nombre: str, contrasena: str, telefono: int) -> None:
        if not nombre or not contrasena:
            self._establecer_mensaje("Ingrese todos sus datos.", False)
            return
        try:
            self._servicio.registrar_usuario(nombre, telefono, contrasena)
            self._establecer_mensaje("Usuario registrado con éxito.", True)
            ventana.destroy()
        except ValueError as e:
            self._establecer_mensaje(str(e), False)