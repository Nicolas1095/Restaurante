# restaurante_app - Semana 15

Aplicación de restaurante con interfaz gráfica Tkinter. La Semana 14 evoluciona
la interfaz mediante componentes, contenedores y gestores de geometría para
consultar usuarios y gestionar productos con persistencia en archivos JSON.
En la Semana 15 se incorpora el registro de ventas asociado al usuario que
inició sesión y se mejora la pantalla de acceso.

## Estructura

- `restaurante_app/modelos/`: modelos `Producto`, `Usuario` y `Venta`.
- `restaurante_app/servicios/archivo_servicio.py`: lectura y escritura de JSON.
- `restaurante_app/servicios/restaurante_servicio.py`: valida el acceso y
  centraliza la consulta, registro, actualización y eliminación de productos
  y usuarios, además del registro y consulta de ventas.
- `restaurante_app/datos/`: `productos.json`, `usuarios.json` y `ventas.json`.
- `restaurante_app/ui/login_view.py`: pantalla de usuario, contraseña y
  mensajes de validación, imagen de perfil y acceso al registro de usuarios.
- `restaurante_app/ui/main_view.py`: panel organizado con `Frame`,
  `LabelFrame`, `Entry`, `Button`, `Treeview` y `Scrollbar` para consultar
  usuarios, gestionar productos y consultar ventas.
- `restaurante_app/main.py`: crea una única ventana `Tk` y coordina las vistas.

## Flujo de la aplicación

`main.py` carga `RestauranteServicio` y muestra `LoginView`. Una credencial
válida abre `MainView` y conserva la identificación del usuario durante la
sesión. Las vistas solicitan los datos al servicio, sin leer los JSON
directamente. Cerrar sesión vuelve al login dentro de la misma ventana.

## Mejoras de la Semana 14

La vista principal separa navegación, formulario y presentación mediante
`Frame` y `LabelFrame`, y organiza los elementos con `grid`, `pack` y un
`Treeview` con desplazamiento. Productos permite registrar, cargar por código
o nombre, actualizar y eliminar. Cada acción usa `command=` y delega las
validaciones y la persistencia a `RestauranteServicio`; la vista no manipula
directamente los archivos JSON. La tabla se actualiza después de cada cambio.

El acceso utiliza un formulario normal para escribir la identificación y la
contraseña. El login muestra como referencia la contraseña predeterminada
`1234`, pero ambos campos se ingresan manualmente. Los
códigos de producto se generan automáticamente con el
formato `P001`, `P002`, etc.; para actualizar o eliminar un producto se
selecciona primero en la tabla y se carga en el formulario.

La sección de usuarios utiliza el mismo sistema de gestión: permite registrar
usuarios con identificación, nombre y teléfono; cargar un usuario desde la
tabla; actualizar sus datos y eliminarlo con confirmación. Los usuarios nuevos
conservan la contraseña predeterminada `1234` y los cambios se guardan en
`usuarios.json`.

Para la simulación pedagógica, los usuarios existentes usan la contraseña
`1234` (por ejemplo, identificación `1001` y contraseña `1234`). No es
autenticación real.

## Mejoras de la Semana 15

La pantalla de acceso muestra la imagen `assets/perfil.png` y organiza los
botones de ingreso y registro en un contenedor común. El registro de usuarios
se abre en una ventana independiente. La ventana principal establece un tamaño
mínimo para mantener visibles sus controles.

La opción `Vender` permite seleccionar un producto e indicar la cantidad. El
sistema asocia la venta con la identificación del usuario autenticado, valida
el usuario, el producto y el stock disponible, descuenta las unidades vendidas
y guarda los cambios en `productos.json` y `ventas.json`. La sección `Ventas`
muestra el usuario, el código del producto y la cantidad de cada operación.

## Cambios recientes

- En el login, `Return` permite ingresar desde los campos de usuario o
  contraseña. En la ventana de registro, permite enviar el formulario desde
  cualquiera de sus campos.
- En el formulario de usuarios, `Return` confirma el registro desde los
  campos de nombre, teléfono o rol.
- En el panel principal, `Escape` limpia los campos y mensajes, quita las
  selecciones de las tablas y cierra los controles temporales de venta o
  cambio de rol, sin borrar los registros guardados.
- El identificador del usuario nuevo se calcula con el mayor identificador
  numérico existente, aunque los usuarios no estén ordenados en el JSON. Si
  se intenta guardar un producto con un código ya ocupado, se asigna el
  siguiente código disponible.

## Ejecución

Desde la raíz del repositorio:

```bash
python -m restaurante_app.main
```

También funciona `python restaurante_app/main.py`.

## Comprobación rápida

1. Verificar que aparece la pantalla de acceso.
2. Ingresar `1001` y `1234`, probando también `Return` desde el campo de
  contraseña.
3. Abrir el registro desde el login y probar `Return` desde uno de sus campos.
4. Consultar `Productos` y `Usuarios`; en el formulario de usuarios, probar
  el registro con `Return`.
5. En el panel, cargar un formulario o abrir una acción temporal y pulsar
  `Escape`; los datos editables y selecciones deben limpiarse sin borrar filas.
6. En `Productos`, seleccionar uno, pulsar `Vender` e ingresar una cantidad
  disponible.
7. Abrir `Ventas` y comprobar que la operación aparece asociada al usuario.
8. Seleccionar `Cerrar sesión` y comprobar el regreso al login.
