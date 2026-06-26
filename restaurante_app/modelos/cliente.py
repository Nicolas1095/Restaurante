class Cliente:
    # Crea la clase cliente recibiendo el nombre y telefono como parametro
    def __init__(self, nombre: str, telefono: str):
        self.nombre = nombre
        self.telefono = telefono
    # Cuando se imprima un cliente, se mostrará como string el nombre y el teléfono del cliente
    def __str__(self) -> str:
        return f"{self.nombre} - {self.telefono}"
