# restaurante_app

## Nicolas Galarraga

## Descripción del sistema

restaurante_app es una aplicación de gestión básica para un restaurante. El sistema permite registrar clientes, definir productos del menú, organizar pedidos y manejar la interacción con el usuario a través de un menú sencillo. Su objetivo es facilitar la administración de los elementos del restaurante y demostrar el uso de programación orientada a objetos en un contexto real.

## Estructura del proyecto

La organización del proyecto está diseñada para separar responsabilidades y facilitar su mantenimiento:

- `main.py`: archivo principal que inicia la aplicación y ejecuta el menú interactivo.
- `models/`: carpeta donde se encuentran las clases principales del sistema.
  - `producto.py`: contiene la clase `Producto`, con sus atributos y validaciones.
  - `cliente.py`: contiene la clase `Cliente`, implementada con `@dataclass`.
- `services/` o `utils/`: puede contener funciones auxiliares para mostrar el menú, validar entradas y procesar datos.
- `README.md`: documentación del proyecto.

## Uso del constructor en la clase `Producto`

La clase `Producto` utiliza un constructor (`__init__`) para inicializar los atributos del objeto al momento de crearlo. Esto permite crear una instancia con datos específicos como el nombre, el precio y la categoría del producto.

Ejemplo de uso:

```python
producto = Producto("Pizza", 15.50, "Comida")