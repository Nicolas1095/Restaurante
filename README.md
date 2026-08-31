# restaurante_app

## Nicolás Galarraga

## Descripción del sistema

restaurante_app es una aplicación de consola para gestionar productos, usuarios y ventas de un restaurante. La Semana 11 incorpora stock, la relación `Usuario + Producto -> Venta` y persistencia JSON de las tres colecciones. La **Semana 12** mejora el rendimiento mediante índices auxiliares basados en diccionarios para optimizar búsquedas, consultas y validaciones frecuentes.

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

## Mejoras de rendimiento (Semana 12)

### Índices auxiliares implementados

La Semana 12 incorpora tres diccionarios (índices) que mejoran significativamente el rendimiento de las búsquedas, consultas y validaciones sin reemplazar las listas principales:

1. **`__indice_productos_por_codigo`** `dict[str, Producto]`
   - **Propósito:** Búsqueda rápida O(1) de un producto por su código único.
   - **Sincronización:** Se actualiza automáticamente al registrar, actualizar o eliminar productos.
   - **Beneficio:** La búsqueda por código es instantánea, evitando recorrer toda la lista.

2. **`__indice_usuarios_por_id`** `dict[str, Usuario]`
   - **Propósito:** Búsqueda rápida O(1) de un usuario por su identificación única.
   - **Sincronización:** Se actualiza al registrar nuevos usuarios.
   - **Beneficio:** Validaciones rápidas durante ventas; evita recorrer la lista completa de usuarios.

3. **`__indice_ventas_por_usuario`** `dict[str, list[Venta]]`
   - **Propósito:** Acceso O(1) a la lista de ventas de un usuario específico.
   - **Sincronización:** Se actualiza al registrar cada venta.
   - **Beneficio:** Consultas de ventas por usuario sin recorrer toda la colección de ventas.

### Métodos optimizados

- **`buscar_producto(identificador)`:** Intenta primero búsqueda por código (índice, O(1)); si no encuentra, recorre por nombre.
- **`buscar_usuario(identificacion)`:** Intenta primero búsqueda por ID (índice, O(1)); si no encuentra, recorre por nombre.
- **`ventas_de_usuario(identificacion)`:** Usa el índice de ventas para acceso O(1) a todas las transacciones de un usuario.

### Reconstrucción de índices

- Al iniciar la aplicación, el método `__reconstruir_indices()` carga las listas desde JSON y construye los tres índices en O(n).
- Los índices se mantienen sincronizados durante la ejecución mediante actualizaciones incrementales.
- Garantiza coherencia entre las listas principales y los índices auxiliares.

### Impacto en rendimiento

| Operación | Antes (Semana 11) | Después (Semana 12) | Mejora |
|-----------|------------------|------------------|--------|
| Buscar producto por código | O(n) | O(1) | n veces más rápido |
| Buscar usuario por ID | O(n) | O(1) | n veces más rápido |
| Consultar ventas de usuario | O(n) | O(1) | n veces más rápido |
| Realizar venta (con búsquedas) | O(2n) | O(2) | n veces más rápido |

(Donde n = cantidad de registros)

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

## Verificación de optimizaciones (Semana 12)

Se incluye un script `test_week12.py` que verifica:

- ✓ Construcción correcta de índices después de cargar desde JSON.
- ✓ Búsqueda rápida de productos por código (usando índice).
- ✓ Búsqueda de productos por nombre (fallback sin índice).
- ✓ Búsqueda rápida de usuarios por ID (usando índice).
- ✓ Actualización correcta de stock durante ventas.
- ✓ Consulta eficiente de ventas por usuario (usando índice).
- ✓ Sincronización de índices después de agregar y eliminar datos.
- ✓ Persistencia y reconstrucción de índices al reiniciar.

Para ejecutar las pruebas:

```bash
python test_week12.py
```

Resultado esperado: **"TODOS LOS TESTS PASARON ✓"**
