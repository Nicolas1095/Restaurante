from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante("Restaurante de Nicolas")

OPCIONES_MENU = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorias",
    "Vender producto",
    "Consultar ventas de usuario",
    "Salir",
)


while True:
    print("\n" + "=" * 40)
    print(f"  Bienvenido al {restaurante.nombre}")
    print("=" * 40)
    for numero, opcion_menu in enumerate(OPCIONES_MENU, start=1):
        print(f"{numero}. {opcion_menu}")

    opcion = input("Seleccione una opcion: ")

    try:
        if opcion == "1":
            codigo = input("Ingrese el codigo del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            categoria = input("Ingrese la categoria del producto: ")
            stock = int(input("Ingrese el stock disponible: "))
            restaurante.agregar_producto(Producto(codigo, nombre, precio, categoria, stock))
            print(f"Producto {nombre} registrado exitosamente.")

        elif opcion == "2":
            producto = restaurante.buscar_producto(input("Ingrese codigo o nombre: "))
            print(producto.mostrar_informacion() if producto else "Producto no encontrado.")

        elif opcion == "3":
            producto = restaurante.buscar_producto(input("Ingrese codigo o nombre: "))
            if producto:
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                restaurante.actualizar_producto(producto, nuevo_nombre, nuevo_precio)
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            producto = restaurante.buscar_producto(input("Ingrese codigo o nombre: "))
            if producto:
                restaurante.eliminar_producto(producto)
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            restaurante.mostrar_menu()

        elif opcion == "6":
            identificacion = input("Ingrese la identificacion del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            telefono = input("Ingrese el telefono del usuario: ")
            restaurante.registrar_usuario(Usuario(identificacion, nombre, telefono))
            print(f"Usuario {nombre} registrado exitosamente.")

        elif opcion == "7":
            restaurante.mostrar_usuarios()

        elif opcion == "8":
            categorias = sorted({producto.categoria for producto in restaurante.productos})
            print(
                "\n".join(
                    f"{numero}. {categoria}"
                    for numero, categoria in enumerate(categorias, start=1)
                )
                or "No hay categorias registradas."
            )

        elif opcion == "9":
            identificacion = input("Ingrese la identificacion del usuario: ")
            codigo = input("Ingrese el codigo del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            if restaurante.vender_producto(codigo, identificacion, cantidad):
                print("Venta registrada correctamente.")
            else:
                print("Venta rechazada: verifique usuario, producto, cantidad y stock.")

        elif opcion == "10":
            identificacion = input("Ingrese la identificacion del usuario: ")
            ventas = restaurante.ventas_de_usuario(identificacion)
            if ventas:
                for venta in ventas:
                    producto = restaurante.buscar_producto(venta.producto_codigo)
                    nombre = producto.nombre if producto else "Producto no disponible"
                    print(f"{nombre} ({venta.producto_codigo}): {venta.cantidad}")
            else:
                print("No hay ventas para ese usuario.")

        elif opcion == "11":
            print("Saliendo del programa.")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")
    except (ValueError, RuntimeError) as error:
        print(f"Operacion no realizada: {error}")
