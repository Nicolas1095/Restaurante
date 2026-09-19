import tkinter as tk
from tkinter import messagebox, ttk
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
        self._codigo = tk.StringVar()
        self._nombre = tk.StringVar()
        self._precio = tk.StringVar()
        self._categoria = tk.StringVar()
        self._stock = tk.StringVar()
        self._estado = tk.StringVar()
        self._identificacion_usuario = tk.StringVar()
        self._nombre_usuario = tk.StringVar()
        self._telefono_usuario = tk.StringVar()
        self._codigo.set(self._servicio.siguiente_codigo_producto())
        self._construir()

    def _construir(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        ttk.Label(self, text="Panel principal", font=("TkDefaultFont", 16, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        navegacion = ttk.Frame(self)
        navegacion.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        ttk.Button(navegacion, text="Productos", command=self._mostrar_productos).pack(
            side="left", padx=(0, 6)
        )
        ttk.Button(navegacion, text="Usuarios", command=self._mostrar_usuarios).pack(
            side="left", padx=6
        )
        ttk.Button(navegacion, text="Cerrar sesión", command=self._on_logout).pack(
            side="right"
        )

        self._contenido = ttk.Frame(self)
        self._contenido.grid(row=2, column=0, sticky="nsew")
        self._contenido.columnconfigure(1, weight=1)
        self._contenido.rowconfigure(0, weight=1)
        self._mostrar_productos()

    def _limpiar_contenido(self) -> None:
        for widget in self._contenido.winfo_children():
            widget.destroy()

    def _mostrar_productos(self) -> None:
        self._limpiar_contenido()
        self._contenido.columnconfigure(0, weight=0)
        self._contenido.columnconfigure(1, weight=1)

        formulario = ttk.LabelFrame(self._contenido, text="Datos del producto", padding=12)
        formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        campos = (
            ("Código", self._codigo),
            ("Nombre", self._nombre),
            ("Precio", self._precio),
            ("Categoría", self._categoria),
            ("Stock", self._stock),
        )
        for fila, (etiqueta, variable) in enumerate(campos):
            ttk.Label(formulario, text=f"{etiqueta}:").grid(row=fila, column=0, sticky="w", pady=4)
            entrada = ttk.Entry(formulario, textvariable=variable, width=24)
            entrada.grid(row=fila, column=1, sticky="ew", pady=4)
            if etiqueta == "Código":
                entrada.configure(state="readonly")
        acciones = ttk.Frame(formulario)
        acciones.grid(row=len(campos), column=0, columnspan=2, pady=(12, 0))
        ttk.Button(acciones, text="Registrar", command=self._registrar).grid(row=0, column=0, padx=2)
        ttk.Button(acciones, text="Cargar", command=self._cargar).grid(row=0, column=1, padx=2)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar).grid(row=1, column=0, padx=2, pady=5)
        ttk.Button(acciones, text="Eliminar", command=self._eliminar).grid(row=1, column=1, padx=2, pady=5)
        ttk.Button(formulario, text="Limpiar", command=self._limpiar_formulario).grid(
            row=len(campos) + 1, column=0, columnspan=2
        )
        ttk.Label(formulario, textvariable=self._estado, wraplength=190).grid(
            row=len(campos) + 2, column=0, columnspan=2, pady=(12, 0)
        )

        tabla_frame = ttk.LabelFrame(self._contenido, text="Productos registrados", padding=8)
        tabla_frame.grid(row=0, column=1, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        self._tabla = ttk.Treeview(
            tabla_frame,
            columns=("codigo", "nombre", "precio", "categoria", "stock"),
            show="headings",
        )
        encabezados = (("codigo", "Código"), ("nombre", "Nombre"), ("precio", "Precio"),
                       ("categoria", "Categoría"), ("stock", "Stock"))
        for columna, texto in encabezados:
            self._tabla.heading(columna, text=texto)
            self._tabla.column(columna, width=100, anchor="center")
        self._tabla.grid(row=0, column=0, sticky="nsew")
        desplazamiento = ttk.Scrollbar(tabla_frame, orient="vertical", command=self._tabla.yview)
        desplazamiento.grid(row=0, column=1, sticky="ns")
        self._tabla.configure(yscrollcommand=desplazamiento.set)
        self._refrescar_productos()

    def _refrescar_productos(self) -> None:
        if not hasattr(self, "_tabla"):
            return
        for item in self._tabla.get_children():
            self._tabla.delete(item)
        for producto in self._servicio.listar_productos():
            self._tabla.insert(
                "", "end",
                values=(producto.codigo, producto.nombre, f"${producto.precio:,.2f}",
                        producto.categoria, producto.stock),
            )

    def _mostrar_usuarios(self) -> None:
        self._limpiar_contenido()
        self._contenido.columnconfigure(1, weight=1)
        formulario = ttk.LabelFrame(self._contenido, text="Datos del usuario", padding=12)
        formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        campos = (
            ("Identificación", self._identificacion_usuario),
            ("Nombre", self._nombre_usuario),
            ("Teléfono", self._telefono_usuario),
        )
        for fila, (etiqueta, variable) in enumerate(campos):
            ttk.Label(formulario, text=f"{etiqueta}:").grid(row=fila, column=0, sticky="w", pady=4)
            entrada = ttk.Entry(formulario, textvariable=variable, width=24)
            entrada.grid(row=fila, column=1, sticky="ew", pady=4)
        acciones = ttk.Frame(formulario)
        acciones.grid(row=3, column=0, columnspan=2, pady=(12, 0))
        ttk.Button(acciones, text="Registrar", command=self._registrar_usuario).grid(row=0, column=0, padx=2)
        ttk.Button(acciones, text="Cargar", command=self._cargar_usuario).grid(row=0, column=1, padx=2)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_usuario).grid(row=1, column=0, padx=2, pady=5)
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_usuario).grid(row=1, column=1, padx=2, pady=5)
        ttk.Button(formulario, text="Limpiar", command=self._limpiar_usuario).grid(
            row=4, column=0, columnspan=2
        )
        ttk.Label(formulario, textvariable=self._estado, wraplength=190).grid(
            row=5, column=0, columnspan=2, pady=(12, 0)
        )

        tabla_frame = ttk.LabelFrame(self._contenido, text="Usuarios registrados", padding=8)
        tabla_frame.grid(row=0, column=1, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        tabla = ttk.Treeview(tabla_frame, columns=("id", "nombre", "telefono"), show="headings")
        for columna, texto in (("id", "Identificación"), ("nombre", "Nombre"), ("telefono", "Teléfono")):
            tabla.heading(columna, text=texto)
            tabla.column(columna, width=180, anchor="center")
        tabla.grid(row=0, column=0, sticky="nsew")
        self._tabla_usuarios = tabla
        for usuario in self._servicio.listar_usuarios():
            tabla.insert("", "end", values=(usuario.identificacion, usuario.nombre, usuario.telefono))

    def _usuario_seleccionado(self):
        seleccion = self._tabla_usuarios.selection()
        if not seleccion:
            return None
        identificacion = self._tabla_usuarios.item(seleccion[0], "values")[0]
        return self._servicio.buscar_usuario(identificacion)

    def _cargar_usuario(self) -> None:
        usuario = self._usuario_seleccionado()
        if usuario is None:
            self._estado.set("Seleccione un usuario de la tabla.")
            return
        self._identificacion_usuario.set(usuario.identificacion)
        self._nombre_usuario.set(usuario.nombre)
        self._telefono_usuario.set(usuario.telefono)
        self._estado.set("Usuario cargado.")

    def _registrar_usuario(self) -> None:
        try:
            self._servicio.registrar_usuario(
                self._identificacion_usuario.get(),
                self._nombre_usuario.get(),
                self._telefono_usuario.get(),
            )
            self._limpiar_usuario()
            self._estado.set("Usuario registrado correctamente.")
            self._mostrar_usuarios()
        except ValueError as error:
            self._estado.set(str(error))

    def _actualizar_usuario(self) -> None:
        try:
            self._servicio.actualizar_usuario(
                self._identificacion_usuario.get(),
                self._nombre_usuario.get(),
                self._telefono_usuario.get(),
            )
            self._estado.set("Usuario actualizado correctamente.")
            self._mostrar_usuarios()
        except ValueError as error:
            self._estado.set(str(error))

    def _eliminar_usuario(self) -> None:
        usuario = self._usuario_seleccionado()
        if usuario is None:
            self._estado.set("Seleccione un usuario de la tabla.")
            return
        if not messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el usuario «{usuario.nombre}»?",
            parent=self.winfo_toplevel(),
        ):
            return
        try:
            self._servicio.eliminar_usuario(usuario.identificacion)
            self._limpiar_usuario()
            self._estado.set("Usuario eliminado correctamente.")
            self._mostrar_usuarios()
        except ValueError as error:
            self._estado.set(str(error))

    def _limpiar_usuario(self) -> None:
        for variable in (self._identificacion_usuario, self._nombre_usuario, self._telefono_usuario):
            variable.set("")
        self._estado.set("")

    def _valores_formulario(self) -> tuple[str, str, float, str, int]:
        try:
            precio = float(self._precio.get().strip())
            stock = int(self._stock.get().strip())
        except ValueError as error:
            raise ValueError("Precio debe ser numérico y stock debe ser un entero.") from error
        return self._codigo.get(), self._nombre.get(), precio, self._categoria.get(), stock

    def _registrar(self) -> None:
        try:
            self._servicio.registrar_producto(*self._valores_formulario())
            self._limpiar_formulario()
            self._estado.set("Producto registrado correctamente.")
            self._refrescar_productos()
        except ValueError as error:
            self._estado.set(str(error))

    def _cargar(self) -> None:
        producto = self._producto_seleccionado()
        if producto is None:
            self._estado.set("Seleccione un producto de la tabla.")
            return
        self._codigo.set(producto.codigo)
        self._nombre.set(producto.nombre)
        self._precio.set(str(producto.precio))
        self._categoria.set(producto.categoria)
        self._stock.set(str(producto.stock))
        self._estado.set("Producto cargado.")

    def _actualizar(self) -> None:
        try:
            self._servicio.actualizar_producto(*self._valores_formulario())
            self._estado.set("Producto actualizado correctamente.")
            self._refrescar_productos()
        except ValueError as error:
            self._estado.set(str(error))

    def _eliminar(self) -> None:
        codigo = self._codigo.get().strip()
        producto = self._servicio.buscar_producto(codigo)
        if producto is None:
            self._estado.set("No se encontró el producto.")
            return
        if not messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Desea eliminar el producto «{producto.nombre}»?",
            parent=self.winfo_toplevel(),
        ):
            return
        try:
            self._servicio.eliminar_producto(codigo)
            self._limpiar_formulario()
            self._estado.set("Producto eliminado correctamente.")
            self._refrescar_productos()
        except ValueError as error:
            self._estado.set(str(error))

    def _limpiar_formulario(self) -> None:
        self._codigo.set(self._servicio.siguiente_codigo_producto())
        for variable in (self._nombre, self._precio, self._categoria, self._stock):
            variable.set("")
        self._estado.set("")

    def _producto_seleccionado(self):
        seleccion = self._tabla.selection()
        if not seleccion:
            return None
        codigo = self._tabla.item(seleccion[0], "values")[0]
        return self._servicio.buscar_producto(codigo)
