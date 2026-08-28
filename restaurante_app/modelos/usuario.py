class Usuario:
    def __init__(self, identificacion: str, nombre: str | None = None, telefono: str | None = None):
        if telefono is None:
            telefono = nombre
            nombre = identificacion
        self.identificacion = identificacion
        self.nombre = nombre
        self.telefono = telefono

    @property
    def identificacion(self) -> str:
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, identificacion: str) -> None:
        if not identificacion:
            raise ValueError("La identificación no puede estar vacía.")
        self.__identificacion = identificacion

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, telefono):
        if not telefono:
            raise ValueError("El teléfono no puede estar vacío.")
        self.__telefono = telefono
    
    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - {self.telefono}"
