# restaurante_app - Semana 14

Aplicación de restaurante con interfaz gráfica Tkinter. La Semana 14 evoluciona
la interfaz mediante componentes, contenedores y gestores de geometría para
consultar usuarios y gestionar productos con persistencia en archivos JSON.

## Estructura

- `restaurante_app/modelos/`: modelos `Producto` y `Usuario`.
- `restaurante_app/servicios/archivo_servicio.py`: lectura y escritura de JSON.
- `restaurante_app/servicios/restaurante_servicio.py`: valida el acceso y
  centraliza la consulta, registro, actualización y eliminación de productos.
- `restaurante_app/datos/`: `productos.json`, `usuarios.json` y `ventas.json`.
- `restaurante_app/ui/login_view.py`: pantalla de usuario, contraseña y
  mensajes de validación.
- `restaurante_app/ui/main_view.py`: panel organizado con `Frame`,
  `LabelFrame`, `Entry`, `Button`, `Treeview` y `Scrollbar` para consultar
  usuarios y gestionar productos.
- `restaurante_app/main.py`: crea una única ventana `Tk` y coordina las vistas.

## Flujo de la aplicación

`main.py` carga `RestauranteServicio` y muestra `LoginView`. Una credencial
válida abre `MainView`; sus botones solicitan los datos al servicio, sin leer
los JSON directamente. Cerrar sesión vuelve al login dentro de la misma
ventana.

## Mejoras de la Semana 14

La vista principal separa navegación, formulario y presentación mediante
`Frame` y `LabelFrame`, y organiza los elementos con `grid`, `pack` y un
`Treeview` con desplazamiento. Productos permite registrar, cargar por código
o nombre, actualizar y eliminar. Cada acción usa `command=` y delega las
validaciones y la persistencia a `RestauranteServicio`; la vista no manipula
directamente los archivos JSON. La tabla se actualiza después de cada cambio.

El acceso permite seleccionar o escribir cualquier usuario registrado y
muestra la contraseña predeterminada `1234`, que aparece precargada. Los
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

## Ejecución

Desde la raíz del repositorio:

```bash
python -m restaurante_app.main
```

También funciona `python restaurante_app/main.py`.

## Comprobación rápida

1. Verificar que aparece la pantalla de acceso.
2. Ingresar `1001` y `1234`.
3. Consultar `Productos` y `Usuarios`.
4. Seleccionar `Cerrar sesión` y comprobar el regreso al login.
