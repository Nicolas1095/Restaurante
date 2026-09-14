import tkinter as tk

try:
    from .servicios.restaurante_servicio import RestauranteServicio
    from .ui.login_view import LoginView
    from .ui.main_view import MainView
except ImportError:
    from servicios.restaurante_servicio import RestauranteServicio
    from ui.login_view import LoginView
    from ui.main_view import MainView


class RestauranteApp:
    def __init__(self, root: tk.Tk, servicio: RestauranteServicio) -> None:
        self._root = root
        self._servicio = servicio
        self._vista = None
        self._mostrar_login()

    def _cambiar_vista(self, vista) -> None:
        if self._vista is not None:
            self._vista.destroy()
        self._vista = vista
        self._vista.pack(fill="both", expand=True)

    def _mostrar_login(self) -> None:
        self._cambiar_vista(LoginView(self._root, self._servicio, self._mostrar_principal))

    def _mostrar_principal(self) -> None:
        self._cambiar_vista(MainView(self._root, self._servicio, self._mostrar_login))


def main() -> None:
    root = tk.Tk()
    root.title("Restaurante")
    root.minsize(620, 400)
    RestauranteApp(root, RestauranteServicio())
    root.mainloop()


if __name__ == "__main__":
    main()
