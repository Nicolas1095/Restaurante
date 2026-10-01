import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable
from modelos.usuario import Usuario
try:
    from ..servicios.restaurante_servicio import RestauranteServicio
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio


class MainView(tk.Frame):
    def __init__(self, master: tk.Misc, servicio: RestauranteServicio, usuario: Usuario, on_logout: Callable[[], None]) -> None:
        super().__init__(master, background="#eef3f8")
        self._servicio = servicio
        self._usuario_actual = usuario
        self._on_logout = on_logout
        self._codigo = tk.StringVar()
        self._codigo_usuario = tk.StringVar()
        self._nombre = tk.StringVar()
        self._precio = tk.StringVar()
        self._categoria = tk.StringVar()
        self._stock = tk.StringVar()
        self._estado = tk.StringVar()
        self._mensaje_estado = False
        self._estado_label = None
        self._identificacion_usuario = tk.StringVar()
        self._nombre_usuario = tk.StringVar()
        self._telefono_usuario = tk.StringVar()
        self._rol_usuario = tk.StringVar()
        self._desplegable_estado = False
        self._codigo.set(self._servicio.siguiente_codigo_producto())
        self._codigo_usuario.set(self._servicio.siguiente_codigo_usuario())
        self._definir_estilos()
        self._construir()
        self._ventana_principal = self.winfo_toplevel()
        self._escape_binding_id = self._ventana_principal.bind("<Escape>", self._limpiar_todo, add="+")
        self.bind("<Destroy>", self._desvincular_escape, add="+")

    def _definir_estilos(self) -> None:
        estilo = ttk.Style()
        self.option_add("*TCombobox*Listbox*background", "#f1f1f1")
        self.option_add("*TCombobox*Listbox*foreground", "#333333")
        self.option_add("*TCombobox*Listbox*selectBackground", "#f1f1f1")
        self.option_add("*TCombobox*Listbox*selectForeground", "#333333")
        estilo.configure("Main.TFrame", background="#eef3f8")
        estilo.configure("Surface.TFrame", background="#fff")
        estilo.configure("TFrame", background="#fff")
        estilo.configure(
            "TButton",
            background="#ee852f",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(8, 6),
            borderwidth=0,
        )
        estilo.map("TButton", background=[("active", "#df651e")])
        estilo.configure(
            "Sky.TButton",
            background="#43D3C4",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(8, 6),
            borderwidth=0,
        )
        estilo.map("Sky.TButton", background=[("active", "#1DD8C5")])
        estilo.configure(
            "Blue.TButton",
            background="#3B545E",
            foreground="#ffffff",
            font=("Arial", 11, "bold"),
            padding=(8, 6),
            borderwidth=0,
        )
        estilo.map("Blue.TButton", background=[("active", "#1D4A5C")])
        estilo.configure(
            "TLabelframe",
            background="#fff",
            bordercolor="#eef3f8",
            relief="solid",
        )
        estilo.configure(
            "TLabelframe.Label",
            background="#fff",
            foreground="#000",
            font=("Arial", 16, "bold"),
        )
        estilo.configure(
            "Main.Treeview",
            background="#fff",
            fieldbackground="#fff",
            foreground="#333333",
            font=("Arial", 10),
            rowheight=28,
            borderwidth=0,
        )
        estilo.configure(
            "Main.Treeview.Heading",
            background="#eef3f8",
            foreground="#333333",
            font=("Arial", 10, "bold"),
            padding=(8, 6),
            relief="flat",
        )
        estilo.map(
            "Main.Treeview",
            background=[("selected", "#5BB8AE")],
            foreground=[("selected", "#ffffff")],
        )
        estilo.map("Main.Treeview.Heading", background=[("active", "#dce8ef")])
        estilo.configure(
            "Rol.TCombobox",
            fieldbackground="#f1f1f1",
            background="#43D3C4",
            foreground="#333333",
            arrowcolor="#ffffff",
            padding=(8, 6),
            font=("Arial", 10),
        )
        estilo.map(
            "Rol.TCombobox",
            fieldbackground=[("readonly", "#f1f1f1"), ("focus", "#ffffff")],
            background=[("active", "#fff")],
        )
        estilo.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#eef3f8",
            darkcolor="#eef3f8",
            lightcolor="#eef3f8",
            troughcolor="#f1f1f1",
            bordercolor="#eef3f8",
            arrowcolor="#333333",
        )
    
    def _construir(self) -> None:
        contenedor = ttk.Frame(self, style="Surface.TFrame", padding=12)
        contenedor.pack(fill="both", expand=True)
        contenedor.columnconfigure(0, weight=1)
        contenedor.rowconfigure(2, weight=1)
        ttk.Label(contenedor, text="Panel principal", font=("Arial", 18, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )

        navegacion = ttk.Frame(contenedor, style="Surface.TFrame")
        navegacion.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        ttk.Button(navegacion, text="Productos", command=self._mostrar_productos, style="Blue.TButton").pack(
            side="left", padx=(0, 6)
        )
        if self._usuario_actual != "Cliente":
            ttk.Button(navegacion, text="Usuarios", command=self._mostrar_usuarios, style="Blue.TButton").pack(
                side="left", padx=6
            )
            ttk.Button(navegacion, text="Ventas", command=self._mostrar_ventas, style="Blue.TButton").pack(
                side="left", padx=6
            )
        ttk.Button(navegacion, text="Cerrar sesión", command=self._on_logout, style="Sky.TButton").pack(
            side="right"
        )

        self._contenido = ttk.Frame(contenedor, style="Surface.TFrame", padding=12)
        self._contenido.grid(row=2, column=0, sticky="nsew")
        self._contenido.columnconfigure(1, weight=1)
        self._contenido.rowconfigure(0, weight=1)
        self._mostrar_productos()

    def _establecer_estado(self, mensaje: str, exitoso: bool = False) -> None:
        self._mensaje_estado = exitoso
        self._estado.set(mensaje)
        if self._estado_label is not None and self._estado_label.winfo_exists():
            color = "#00aa00" if exitoso else "#ff0000"
            self._estado_label.configure(foreground=color)

    def _limpiar_contenido(self) -> None:
        for widget in self._contenido.winfo_children():
            widget.destroy()
    def _limpiar_todo(self, event: tk.Event | None = None) -> None:
        self._cerrar_controles_temporales()
        self._limpiar_formulario()
        self._limpiar_usuario()
        for nombre_tabla in ("_tabla", "_tabla_usuarios", "_tabla_ventas"):
            tabla = getattr(self, nombre_tabla, None)
            if tabla is not None and tabla.winfo_exists():
                for item in tabla.selection():
                    tabla.selection_remove(item)

    def _cerrar_controles_temporales(self) -> None:
        selector_temporal = getattr(self, "_dropdown_label", None)
        nombres_widgets = ["_spinbox_label", "_spinbox", "_spinbox_button", "_dropdown_label", "_dropdown_button"]
        if selector_temporal is not None and selector_temporal.winfo_exists():
            nombres_widgets.append("_dropdown")
        for nombre_widget in nombres_widgets:
            widget = getattr(self, nombre_widget, None)
            if widget is not None and widget.winfo_exists():
                widget.destroy()
        self._desplegable_estado = False

    def _desvincular_escape(self, event: tk.Event) -> None:
        if event.widget is self:
            self._ventana_principal.unbind("<Escape>", self._escape_binding_id)
        
    def _mostrar_productos(self) -> None:
        self._desplegable_estado = False
        self._limpiar_contenido()
        self._contenido.columnconfigure(0, weight=0)
        self._contenido.columnconfigure(1, weight=1)
        self._formulario = ttk.LabelFrame(self._contenido, text="Datos del producto", padding=12)
        self._formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        acciones = ttk.Frame(self._formulario, style="Surface.TFrame")
        campos = (
            ("Código", self._codigo),
            ("Nombre", self._nombre),
            ("Precio", self._precio),
            ("Categoría", self._categoria),
            ("Stock", self._stock),
        )
        acciones.grid(row=len(campos), column=0, columnspan=2, pady=(28, 0))

        if self._usuario_actual.rol != "Cliente":
            for fila, (etiqueta, variable) in enumerate(campos):
                ttk.Label(self._formulario, text=f"{etiqueta}:").grid(row=fila, column=0, sticky="w", pady=8)
                entrada = ttk.Entry(self._formulario, textvariable=variable, width=24)
                entrada.grid(row=fila, column=1, sticky="ew", pady=4)
                if etiqueta == "Código":
                    entrada.configure(state="readonly")
            ttk.Button(acciones, text="Registrar", command=self._registrar).grid(row=0, column=0, padx=2, pady=5)
            ttk.Button(acciones, text="Cargar", command=self._cargar).grid(row=0, column=1, padx=2, pady=5)
            ttk.Button(acciones, text="Actualizar", command=self._actualizar).grid(row=1, column=0, padx=2, pady=5)
            ttk.Button(acciones, text="Eliminar", command=self._eliminar).grid(row=1, column=1, padx=2, pady=5)
            ttk.Button(acciones, text="Limpiar", command=self._limpiar_formulario).grid(
                row=2, column=0, padx=2, pady=5
            )
            ttk.Button(acciones, text="Vender", command=self._vender_producto).grid(
                row=2, column=1, padx=2, pady=5
            )
        else:
            ttk.Button(acciones, text="Comprar", command=self._vender_producto).grid(
                row=2, column=1, padx=2, pady=5
            )

        color_estado = "#00aa00" if self._mensaje_estado else "#ff0000"
        self._estado_label = ttk.Label(
            self._formulario,
            textvariable=self._estado,
            wraplength=190,
            foreground=color_estado,
            font=("Arial", 8),
        )
        self._estado_label.grid(row=len(campos) + 2, column=0, columnspan=2, pady=(12, 0))

        tabla_frame = ttk.LabelFrame(self._contenido, text="Productos registrados", padding=8)
        tabla_frame.grid(row=0, column=1, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        self._tabla = ttk.Treeview(
            tabla_frame,
            columns=("codigo", "nombre", "precio", "categoria", "stock"),
            show="headings",
            style="Main.Treeview",
        )
        encabezados = (("codigo", "Código"), ("nombre", "Nombre"), ("precio", "Precio"),
                       ("categoria", "Categoría"), ("stock", "Stock"))
        for columna, texto in encabezados:
            self._tabla.heading(columna, text=texto)
            self._tabla.column(columna, width=100, anchor="center")
        self._tabla.grid(row=0, column=0, sticky="nsew")
        desplazamiento = ttk.Scrollbar(tabla_frame, orient="vertical", command=self._tabla.yview, style="Vertical.TScrollbar")
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

    def _vender_producto(self) -> None:
        def validar_numeros(texto_nuevo):
            return texto_nuevo == "" or texto_nuevo.isdigit()
        if not self._desplegable_estado:
            self._establecer_estado("")
            
            producto = self._producto_seleccionado()
            if producto is None:
                self._establecer_estado("Seleccione un producto de la tabla.", False)
                return
            
            vcmd = self._formulario.register(validar_numeros)
            self._spinbox_label = ttk.Label(self._formulario, text="Ingrese la cantidad:")
            self._spinbox_label.grid(row=7, column=0, columnspan=2, pady=(12, 0))
            self._spinbox = tk.Spinbox(
                self._formulario,
                from_=1,
                to=producto.stock,
                increment=1,
                validate="key",
                validatecommand=(vcmd, "%P"),
                font=("Arial", 10),
                width=8,
                background="#f1f1f1",
                foreground="#333333",
                buttonbackground="#43D3C4",
                insertbackground="#333333",
                selectbackground="#3B545E",
                selectforeground="#ffffff",
                relief="flat",
                bd=0,
                highlightthickness=1,
                highlightbackground="#dce8ef",
                highlightcolor="#ee852f",
            )
            self._spinbox.grid(row=8, column=0, columnspan=2, pady=(12, 0))
            self._spinbox_button = ttk.Button(
                self._formulario,
                text="Listo",
                command=lambda: self._procesar_venta(self._spinbox.get()),
            )
            self._spinbox_button.grid(row=9, column=0, columnspan=2, pady=(12, 0))
            self._desplegable_estado = True
        else:
            self._desplegable_estado = False
            self._spinbox_label.destroy()
            self._spinbox.destroy()
            self._spinbox_button.destroy()

    def _procesar_venta(self, cantidad_str: str) -> None:
        try:
            cantidad = int(cantidad_str)
            total = cantidad * self._producto_seleccionado().precio
            if cantidad < 1:
                self._establecer_estado("La cantidad minima es 1.")
            elif cantidad > self._producto_seleccionado().stock:
                self._establecer_estado("La cantidad excede el stock disponible.")
            else:
                self._servicio.vender_producto(
                    self._usuario_actual.identificacion,
                    self._producto_seleccionado().codigo,
                    cantidad,
                    self._producto_seleccionado().precio,
                    total
                )
                self._establecer_estado(
                    f"Venta de {cantidad} unidades por "
                    f"{total}$ realizada correctamente",
                    True,
                )
                self._refrescar_productos()
                self._vender_producto() # llama la funcion de nuevo para ocultar los widgets de venta
        except ValueError as error:
            self._establecer_estado(str(error))

    def _mostrar_usuarios(self) -> None:
        self._limpiar_contenido()
        self._limpiar_formulario()
        self._codigo_usuario.set(self._servicio.siguiente_codigo_usuario())
        self._contenido.columnconfigure(1, weight=1)
        self._formulario = ttk.LabelFrame(self._contenido, text="Datos del usuario", padding=12)
        self._formulario.grid(row=0, column=0, sticky="ns", padx=(0, 12))
        campos = (
            ("Identificación", self._codigo_usuario),
            ("Nombre", self._nombre_usuario),
            ("Teléfono", self._telefono_usuario),
        )
        for fila, (etiqueta, variable) in enumerate(campos):
            ttk.Label(self._formulario, text=f"{etiqueta}:").grid(row=fila, column=0, sticky="w", pady=4)
            entrada = ttk.Entry(self._formulario, textvariable=variable, width=24)
            if etiqueta == "Identificación":
                entrada.configure(state="readonly")
            entrada.grid(row=fila, column=1, sticky="ew", pady=4)
            entrada.bind("<Return>", self._confirmar_registro_usuario)
        ttk.Label(self._formulario, text="Rol").grid(row=5, column=0, sticky="w", pady=4)
        self._dropdown = ttk.Combobox(self._formulario, textvariable=self._rol_usuario, state="readonly", style="Rol.TCombobox")
        self._dropdown["values"] = ("Administrador", "Empleado", "Cliente")
        self._dropdown.grid(row=5, column=1, sticky="ew", pady=4)
        self._dropdown.bind("<Return>", self._confirmar_registro_usuario)
        rol_actual = self._rol_usuario.get()
        valores_rol = self._dropdown["values"]
        self._dropdown.current(valores_rol.index(rol_actual) if rol_actual in valores_rol else 0)
        acciones = ttk.Frame(self._formulario, style="Surface.TFrame")
        acciones.grid(row=6, column=0, columnspan=2, pady=(12, 0))
        ttk.Button(acciones, text="Registrar", command=self._registrar_usuario).grid(row=0, column=0, padx=2)
        ttk.Button(acciones, text="Cargar", command=self._cargar_usuario).grid(row=0, column=1, padx=2)
        ttk.Button(acciones, text="Actualizar", command=self._actualizar_usuario).grid(row=1, column=0, padx=2, pady=5)
        ttk.Button(acciones, text="Eliminar", command=self._eliminar_usuario).grid(row=1, column=1, padx=2, pady=5)
        ttk.Button(acciones, text="Limpiar", command=self._limpiar_usuario).grid(
            row=2, column=0, padx=2, pady=5)
        ttk.Button(acciones, text="Cambiar Rol", command=self._cambiar_rol).grid(
            row=2, column=1, padx=2, pady=5)
        color_estado = "#00aa00" if self._mensaje_estado else "#ff0000"
        self._estado_label = ttk.Label(
            self._formulario,
            textvariable=self._estado,
            wraplength=190,
            foreground=color_estado,
        )
        self._estado_label.grid(
            row=7, column=0, columnspan=2, pady=(12, 0)
        )

        tabla_frame = ttk.LabelFrame(self._contenido, text="Usuarios registrados", padding=8)
        tabla_frame.grid(row=0, column=1, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        tabla = ttk.Treeview(
            tabla_frame,
            columns=("id", "nombre", "telefono", "rol"),
            show="headings",
            style="Main.Treeview",
        )
        for columna, texto in (("id", "Identificación"), ("nombre", "Nombre"), ("telefono", "Teléfono"), ("rol", "Rol")):
            tabla.heading(columna, text=texto)
            tabla.column(columna, width=180, anchor="center")
        tabla.grid(row=0, column=0, sticky="nsew")
        self._tabla_usuarios = tabla
        for usuario in self._servicio.listar_usuarios():
            tabla.insert("", "end", values=(usuario.identificacion, usuario.nombre, usuario.telefono, usuario.rol))
    def _cambiar_rol(self) -> None:
            self._establecer_estado("")
            if not self._desplegable_estado:
                usuario = self._usuario_seleccionado()
                if usuario is None:
                    self._establecer_estado("Seleccione un usuario de la tabla antes de vender.", False)
                    return
                elif str(usuario.identificacion) == "1001":
                    self._establecer_estado("No puede cambiar el rol a este usuario.", False)
                    return
                self._dropdown_label = ttk.Label(self._formulario, text="Seleccione el rol:")
                self._dropdown = ttk.Combobox(self._formulario, textvariable=self._rol_usuario, state="readonly", style="Rol.TCombobox")
                self._dropdown["values"] = ("Administrador", "Empleado", "Cliente")
                self._dropdown_label.grid(row=7, column=0, columnspan=2, pady=(12, 0))
                self._dropdown.grid(row=8, column=0, columnspan=2, pady=(12, 0))
                self._dropdown_button = ttk.Button(
                    self._formulario,
                    text="Listo",
                    command=self._guardar_rol,
                    
                )
                self._dropdown_button.grid(row=9, column=0, columnspan=2, pady=(12, 0))
                self._desplegable_estado = True
            else:
                self._desplegable_estado = False
                self._dropdown_label.destroy()
                self._dropdown.destroy()
                self._dropdown_button.destroy()

    def _guardar_rol(self) -> None:
        usuario = self._usuario_seleccionado()
        if usuario is None:
            self._establecer_estado("Seleccione un usuario de la tabla.")
            return
        if str(usuario.identificacion) == "1001":
            self._establecer_estado("No puede cambiar el rol de este usuario.")
            return
        try:
            self._servicio.actualizar_usuario(
                usuario.identificacion,
                usuario.nombre,
                usuario.telefono,
                self._rol_usuario.get(),
            )
            self._mostrar_usuarios()
            self._establecer_estado("Rol actualizado correctamente.", True)
        except ValueError as error:
            self._establecer_estado(str(error))
    
    def _usuario_seleccionado(self):
        seleccion = self._tabla_usuarios.selection()
        if not seleccion:
            return None
        identificacion = self._tabla_usuarios.item(seleccion[0], "values")[0]
        return self._servicio.buscar_usuario(identificacion)

    def _cargar_usuario(self) -> None:
        usuario = self._usuario_seleccionado()
        if usuario is None:
            self._establecer_estado("Seleccione un usuario de la tabla.")
            return
        if self._rol_usuario == "Administrador":
            self._dropdown.current(0)
        elif self._rol_usuario == "Empleado":
            self._dropdown.current(1)
        else:
            self._dropdown.current(2)
        self._identificacion_usuario.set(usuario.identificacion)
        self._codigo_usuario.set(usuario.identificacion)
        self._nombre_usuario.set(usuario.nombre)
        self._telefono_usuario.set(usuario.telefono)
        self._dropdown.current(self._dropdown["values"].index(usuario.rol))
        self._establecer_estado("Usuario cargado.", True)

    def _registrar_usuario(self) -> None:
        try:
            self._servicio.registrar_usuario(
                self._nombre_usuario.get(),
                self._telefono_usuario.get(),
                "1234",
                self._rol_usuario.get(),
            )
            self._limpiar_usuario()
            self._mostrar_usuarios()
            self._establecer_estado("Usuario registrado correctamente.", True)
        except ValueError as error:
            self._establecer_estado(str(error))

    def _confirmar_registro_usuario(self, event: tk.Event) -> str:
        self._registrar_usuario()
        return "break"

    def _actualizar_usuario(self) -> None:
        try:
            self._servicio.actualizar_usuario(
                self._identificacion_usuario.get(),
                self._nombre_usuario.get(),
                self._telefono_usuario.get(),
                self._rol_usuario.get(),
            )
            self._mostrar_usuarios()
            self._establecer_estado("Usuario actualizado correctamente.", True)
        except ValueError as error:
            self._establecer_estado(str(error))

    def _eliminar_usuario(self) -> None:
        usuario = self._usuario_seleccionado()
        if usuario is None:
            self._establecer_estado("Seleccione un usuario de la tabla.")
            return
        if str(usuario.identificacion) == "1001":
            self._establecer_estado("No puede eliminar este usuario.")
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
            self._mostrar_usuarios()
            self._establecer_estado("Usuario eliminado correctamente.", True)
        except ValueError as error:
            self._establecer_estado(str(error))
    def _mostrar_ventas(self) -> None:
        self._limpiar_contenido()
        self._contenido.columnconfigure(0, weight=1)
        tabla_frame = ttk.LabelFrame(self._contenido, text="Ventas registradas", padding=8)
        tabla_frame.grid(row=0, column=0, sticky="nsew")
        tabla_frame.columnconfigure(0, weight=1)
        tabla_frame.rowconfigure(0, weight=1)
        tabla = ttk.Treeview(
            tabla_frame,
            columns=("usuario", "producto", "cantidad", "precio", "total"),
            show="headings",
            style="Main.Treeview",
        )
        for columna, texto in (("usuario", "Usuario"), ("producto", "Producto"), ("cantidad", "Cantidad"), ("precio", "Precio (c/u)"), ("total", "Total")):
            tabla.heading(columna, text=texto)
            tabla.column(columna, width=180, anchor="center")
        tabla.grid(row=0, column=0, sticky="nsew")
        self._tabla_ventas = tabla
        for venta in self._servicio.listar_ventas():
            tabla.insert("", "end", values=(venta.usuario_id, venta.producto_codigo, venta.cantidad, venta.precio, venta.total))
    def _limpiar_usuario(self) -> None:
        for variable in (
            self._identificacion_usuario,
            self._nombre_usuario,
            self._telefono_usuario,
            self._rol_usuario,
        ):
            variable.set("")
        self._codigo_usuario.set(self._servicio.siguiente_codigo_usuario())
        self._establecer_estado("")

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
            self._establecer_estado("Producto registrado correctamente.", True)
            self._refrescar_productos()
        except ValueError as error:
            self._establecer_estado(str(error))

    def _cargar(self) -> None:
        producto = self._producto_seleccionado()
        if producto is None:
            self._establecer_estado("Seleccione un producto de la tabla.")
            return
        self._codigo.set(producto.codigo)
        self._nombre.set(producto.nombre)
        self._precio.set(str(producto.precio))
        self._categoria.set(producto.categoria)
        self._stock.set(str(producto.stock))
        self._establecer_estado("Producto cargado.", True)

    def _actualizar(self) -> None:
        if self._producto_seleccionado() is None:
            self._establecer_estado("Seleccione un producto de la tabla.")
            return
        elif self._codigo.get() != self._producto_seleccionado().codigo:
            self._cargar()
            self._establecer_estado("Producto cargado, ahora puede actualizarlo.", True)
            return
        elif self._codigo.get() == "":
            self._establecer_estado("Seleccione un producto de la tabla y cargue sus datos.")
            return
        try:
            self._servicio.actualizar_producto(*self._valores_formulario())
            self._establecer_estado("Producto actualizado correctamente.", True)
            self._refrescar_productos()
        except ValueError as error:
            self._establecer_estado(str(error))

    def _eliminar(self) -> None:
        codigo = self._producto_seleccionado().codigo if self._producto_seleccionado() else None
        if codigo is None:
            self._establecer_estado("Seleccione un producto de la tabla.")
            return
        producto = self._servicio.buscar_producto(codigo)
        if producto is None:
            self._establecer_estado("No se encontró el producto.")
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
            self._establecer_estado("Producto eliminado correctamente.", True)
            self._refrescar_productos()
        except ValueError as error:
            self._establecer_estado(str(error))

    def _limpiar_formulario(self) -> None:
        self._codigo_usuario.set(self._servicio.siguiente_codigo_usuario())
        self._codigo.set(self._servicio.siguiente_codigo_producto())
        for variable in (self._nombre, self._precio, self._categoria, self._stock):
            variable.set("")
        self._establecer_estado("")

    def _producto_seleccionado(self):
        seleccion = self._tabla.selection()
        if not seleccion:
            return None
        codigo = self._tabla.item(seleccion[0], "values")[0]
        return self._servicio.buscar_producto(codigo)
