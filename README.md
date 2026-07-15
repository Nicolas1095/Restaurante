# restaurante_app

## Nicolas Galarraga

## Descripción del sistema

restaurante_app es una aplicación de gestión básica para un restaurante. El sistema permite registrar clientes, definir productos y bebidas del menú, mostrar el menú, y buscar productos y clientes mediante un menú interactivo en consola.

## Estructura del proyecto

La organización del proyecto está diseñada para separar responsabilidades y facilitar su mantenimiento:

- `restaurante_app/main.py`: archivo principal que inicia la aplicación y ejecuta el menú interactivo.
- `restaurante_app/modelos/`: carpeta con las clases del dominio.
  - `producto.py`: contiene la clase `Producto`, con validaciones de nombre y precio.
  - `bebida.py`: contiene la clase `Bebida`, que hereda de `Producto` e incluye el volumen.
  - `cliente.py`: contiene la clase `Cliente`, con validaciones de nombre y teléfono.
- `restaurante_app/servicios/`: carpeta con la lógica de gestión del restaurante.
  - `restaurante.py`: contiene la clase `Restaurante`, que administra el menú y los clientes.
- `README.md`: documentación del proyecto.

## Características principales

- Registrar productos y bebidas con validaciones.
- Registrar clientes.
- Mostrar el menú completo de productos y bebidas.
- Buscar productos por nombre.
- Mostrar clientes registrados.
- Buscar clientes por nombre.

## Clases principales

- `Producto`: modelo básico de producto con `nombre` y `precio`.
- `Bebida`: extiende `Producto` y agrega el atributo `volumen`.
- `Cliente`: modelo de cliente con `nombre` y `telefono`.
- `Restaurante`: servicio que administra el menú y la lista de clientes.
