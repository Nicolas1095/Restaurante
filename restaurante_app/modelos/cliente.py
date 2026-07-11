class Cliente:
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono

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
