# restaurante_app

## Nicolás Galarraga

## Descripción del sistema

restaurante_app es una aplicación de consola para gestionar un restaurante de forma básica. Permite registrar productos, buscarlos, actualizarlos, eliminarlos, listarlos, además de registrar usuarios y ver la lista de usuarios y categorías disponibles.

## Estructura del proyecto

La organización del proyecto está diseñada para separar responsabilidades:

- [restaurante_app/main.py](restaurante_app/main.py): archivo principal que ejecuta el menú interactivo de la aplicación.
- [restaurante_app/modelos/](restaurante_app/modelos): carpeta con las clases del dominio.
  - [restaurante_app/modelos/producto.py](restaurante_app/modelos/producto.py): define la clase `Producto` con validaciones para código, nombre, categoría y precio.
  - [restaurante_app/modelos/usuario.py](restaurante_app/modelos/usuario.py): define la clase `Usuario` con validaciones de nombre y teléfono.
- [restaurante_app/servicios/](restaurante_app/servicios): carpeta con la lógica de negocio del restaurante.
  - [restaurante_app/servicios/restaurante.py](restaurante_app/servicios/restaurante.py): contiene la clase `Restaurante`, que administra la lista de productos y usuarios.
- [README.md](README.md): documentación del proyecto.

## Funcionalidades principales

- Registrar productos con código, nombre, precio y categoría.
- Buscar un producto por nombre.
- Actualizar la información de un producto.
- Eliminar productos del menú.
- Listar todos los productos registrados.
- Registrar usuarios con nombre y teléfono.
- Listar usuarios registrados.
- Mostrar las categorías disponibles entre los productos.
- Salir de la aplicación.

## Clases principales

- `Producto`: representa un producto del menú con atributos como `codigo`, `nombre`, `precio` y `categoria`.
- `Usuario`: representa a un cliente o usuario registrado con `nombre` y `telefono`.
- `Restaurante`: administra los productos y usuarios del restaurante.

## Ejecución

Para iniciar la aplicación, se ejecuta desde la carpeta raíz:

```bash
python restaurante_app/main.py
```

> La aplicación corre en consola y muestra un menú con opciones numéricas para gestionar el restaurante.
