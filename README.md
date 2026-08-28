# restaurante_app

## Nicolás Galarraga

## Descripción del sistema

restaurante_app es una aplicación de consola para gestionar productos, usuarios y ventas de un restaurante. La Semana 11 incorpora stock, la relación `Usuario + Producto -> Venta` y persistencia JSON de las tres colecciones.

## Estructura del proyecto

La organización del proyecto está diseñada para separar responsabilidades:

- [restaurante_app/main.py](restaurante_app/main.py): archivo principal que ejecuta el menú interactivo de la aplicación.
- [restaurante_app/modelos/](restaurante_app/modelos): carpeta con las clases del dominio.
  - [restaurante_app/modelos/producto.py](restaurante_app/modelos/producto.py): define `Producto`, sus validaciones y el stock disponible.
  - [restaurante_app/modelos/usuario.py](restaurante_app/modelos/usuario.py): define `Usuario` con identificación, nombre y teléfono.
  - [restaurante_app/modelos/venta.py](restaurante_app/modelos/venta.py): representa usuario, producto y cantidad vendida.
- [restaurante_app/servicios/](restaurante_app/servicios): carpeta con la lógica de negocio del restaurante.
  - [restaurante_app/servicios/restaurante.py](restaurante_app/servicios/restaurante.py): administra colecciones, búsquedas, stock y ventas.
  - [restaurante_app/servicios/archivo_servicio.py](restaurante_app/servicios/archivo_servicio.py): carga y guarda objetos mediante JSON.
- [restaurante_app/datos/](restaurante_app/datos): contiene `productos.json`, `usuarios.json` y `ventas.json`.
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
- Registrar ventas solo para usuarios y productos existentes.
- Validar cantidad y stock, disminuyendo el stock cuando la venta es válida.
- Consultar las ventas asociadas a un usuario.
- Recuperar productos, usuarios y ventas al iniciar el programa.
- Salir de la aplicación.

## Clases principales

- `Producto`: representa un producto del menú con `codigo`, `nombre`, `precio`, `categoria` y `stock`.
- `Usuario`: representa a un cliente registrado mediante `identificacion`, nombre y teléfono.
- `Venta`: relaciona la identificación del usuario, el código del producto y la cantidad.
- `Restaurante`: administra las colecciones y concentra las reglas de negocio.
- `ArchivoServicio`: centraliza la persistencia JSON.

## Ejecución

Para iniciar la aplicación, se ejecuta desde la carpeta raíz:

```bash
python restaurante_app/main.py
```

> La aplicación corre en consola y muestra un menú con opciones numéricas para gestionar el restaurante.

## Prueba de funcionamiento

1. Registrar un usuario y un producto con stock.
2. Seleccionar `Vender producto` e indicar identificación, código y cantidad.
3. Confirmar que el stock disminuya y que la venta aparezca en `datos/ventas.json`.
4. Seleccionar `Consultar ventas de usuario`.
5. Reiniciar el programa para comprobar la recuperación de los tres archivos JSON.
6. Intentar vender más unidades que el stock disponible y verificar que sea rechazada sin modificar los datos.
