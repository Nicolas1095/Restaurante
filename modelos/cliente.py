class Cliente:
    # Crea la clase cliente recibiendo el nombre y telefono como parametro
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    # Cuando se imprima un cliente, se mostrará como string el nombre y el teléfono del cliente
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
        if not telefono.isdigit() or len(telefono) != 10:
            raise ValueError("El teléfono debe contener exactamente 10 dígitos.")
        self.__telefono = telefono
        
    def mostrar_informacion(self) -> str:
        return f"{self.nombre} - {self.telefono}"