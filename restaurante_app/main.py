from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

restaurante = Restaurante("Restaurante de Nicolás")

OPCIONES_MENU = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir",
)

# Muestra el menú de opciones en bucle hasta que el usuario salga del programa
while True:
    print("")
    print("=" * 40)
    print(f"  Bienvenido al {restaurante.nombre}")
    print("=" * 40)
    print("Menú de opciones:")

    for i, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{i}. {opcion}")
        if i == 5 or i == 7:
            print("-" * 40)

    opcion = input("Seleccione una opción: ")

    # 1. Registrar producto
    if opcion == "1":
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoría del producto: ")

        restaurante.agregar_producto(
            Producto(codigo, nombre, precio, categoria)
        )
        print(f"Producto {nombre} registrado exitosamente.")

    # 2. Buscar producto
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a buscar: ")

        producto_encontrado = restaurante.buscar_producto(nombre)

        if producto_encontrado:
            print(
                f"Producto encontrado: "
                f"{producto_encontrado.mostrar_informacion()}"
            )
        else:
            print("Producto no encontrado.")

    # 3. Actualizar producto
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a actualizar: ")

        producto_encontrado = restaurante.buscar_producto(nombre)

        if producto_encontrado:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))

            producto_encontrado.actualizar_informacion(
                nuevo_nombre,
                nuevo_precio
            )

            print(f"Producto {nombre} actualizado.")
        else:
            print("Producto no encontrado.")

    # 4. Eliminar producto
    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a eliminar: ")

        producto_encontrado = restaurante.buscar_producto(nombre)

        if producto_encontrado:
            restaurante.eliminar_producto(producto_encontrado)
            print(f"Producto {nombre} eliminado.")
        else:
            print("Producto no encontrado.")

    # 5. Listar productos
    elif opcion == "5":
        restaurante.mostrar_menu()

    # 6. Registrar usuario
    elif opcion == "6":
        nombre = input("Ingrese el nombre del usuario: ")
        telefono = input("Ingrese el teléfono del usuario: ")

        restaurante.registrar_usuario(
            Usuario(nombre, telefono)
        )
        print(f"Usuario {nombre} registrado exitosamente.")

    # 7. Listar usuarios
    elif opcion == "7":
        restaurante.mostrar_usuarios()

    # 8. Mostrar categorías
    elif opcion == "8":
        categorias = set()
        for producto in restaurante.productos:
            categorias.add(producto.categoria)
        
        if categorias:
            print("\nCategorías disponibles:")
            for i, categoria in enumerate(sorted(categorias), start=1):
                print(f"{i}. {categoria}")
        else:
            print("No hay categorías registradas.")

    # 9. Salir
    elif opcion == "9":
        print("Saliendo del programa.")
        break

    # Opción inválida
    else:
        print("Opción no válida. Intente nuevamente.")