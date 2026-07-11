from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Restaurante de Nicolás")
producto1 = Producto("Hamburguesa", 10.99)
restaurante.agregar_producto(producto1)
producto2 = Producto("Pizza", 12.99)
restaurante.agregar_producto(producto2)
producto3 = Producto("Ensalada", 8.99)
restaurante.agregar_producto(producto3)

cliente1 = Cliente("Juan Pérez", "1234567890")
restaurante.registrar_cliente(cliente1)
cliente2 = Cliente("María López", "0987654321")
restaurante.registrar_cliente(cliente2)
cliente3 = Cliente("Carlos García", "5555555555")
restaurante.registrar_cliente(cliente3)
# Muestra el menú de opciones en bucle hasta que el usuario se salga del programa
while True:
    print("")
    print("-" * 30)
    print("Menú de opciones:")
    print("  1. Registrar producto")
    print("  2. Mostrar productos")
    print("  3. Buscar producto")
    print("-"*30)
    print("  4. Registrar cliente")
    print("  5. Mostrar clientes")
    print("  6. Buscar cliente")
    print("-"*30)
    print("  7. Salir")
    print("-" * 30)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        #Agrega un nuevo producto a la lista de menu que hay en la clase Restaurante usando el metodo agregar_producto() de la clase Producto
        restaurante.agregar_producto(Producto(nombre, precio))

    elif opcion == "2":
        restaurante.mostrar_menu() # Muestra el menú del restaurante usando el metodo mostrar_menu()
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        #Busca un producto en la lista de menu que hay en la clase Restaurante usando el metodo buscar_producto() de la clase Producto
        producto_encontrado = restaurante.buscar_producto(nombre)
        if producto_encontrado:
            print(f"Producto encontrado: {producto_encontrado.mostrar_informacion()}")
        else:
            print("Producto no encontrado.")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        #agrega un nuevo cliente a la lista de clientes que hay en la clase Restaurante usando el metodo registrar_cliente() de la clase Cliente
        restaurante.registrar_cliente(Cliente(nombre, telefono))

    elif opcion == "5":
        restaurante.mostrar_clientes() # Muestra los clientes registrados usando el metodo mostrar_clientes()

    elif opcion == "6":
        nombre = input("Ingrese el nombre del cliente a buscar: ")
        #Busca un cliente en la lista de clientes que hay en la clase Restaurante usando el metodo buscar_cliente() de la clase Cliente
        cliente_encontrado = restaurante.buscar_cliente(nombre)
        if cliente_encontrado:
            print(f"Cliente encontrado: {cliente_encontrado.mostrar_informacion()}")
        else:
            print("Cliente no encontrado.")
    elif opcion == "7": 
        print("Saliendo del programa.")
        break   