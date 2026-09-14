# restaurante_app - Semana 13

Aplicación base de restaurante con una interfaz gráfica Tkinter. Esta etapa
mantiene el acceso simulado y la consulta de productos y usuarios; las ventas
quedan identificadas como una funcionalidad futura.

## Estructura

- `restaurante_app/modelos/`: modelos `Producto` y `Usuario`.
- `restaurante_app/servicios/archivo_servicio.py`: lectura y escritura de JSON.
- `restaurante_app/servicios/restaurante_servicio.py`: valida el acceso y
  entrega productos y usuarios a las vistas.
- `restaurante_app/datos/`: `productos.json`, `usuarios.json` y `ventas.json`.
- `restaurante_app/ui/login_view.py`: pantalla de usuario, contraseña y
  mensajes de validación.
- `restaurante_app/ui/main_view.py`: panel para consultar productos y usuarios,
  y opción de cerrar sesión.
- `restaurante_app/main.py`: crea una única ventana `Tk` y coordina las vistas.

## Flujo de la aplicación

`main.py` carga `RestauranteServicio` y muestra `LoginView`. Una credencial
válida abre `MainView`; sus botones solicitan los datos al servicio, sin leer
los JSON directamente. Cerrar sesión vuelve al login dentro de la misma
ventana.

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
