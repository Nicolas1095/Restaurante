from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Restaurante de Nicolás")
# Muestra el menú de opciones en bucle hasta que el usuario se salga del programa
while True:
    print("")
    print("-" * 30)
    print("Menú de opciones:")
    print("  1. Registrar producto")
    print("  2. Mostrar productos")
    print("  3. Registrar cliente")
    print("  4. Mostrar clientes")
    print("  5. Salir")
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
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        #agrega un nuevo cliente a la lista de clientes que hay en la clase Restaurante usando el metodo registrar_cliente() de la clase Cliente
        restaurante.registrar_cliente(Cliente(nombre, telefono))

    elif opcion == "4":
        restaurante.mostrar_clientes() # Muestra los clientes registrados usando el metodo mostrar_clientes()

    elif opcion == "5":
        print("Saliendo del programa.")
        break   