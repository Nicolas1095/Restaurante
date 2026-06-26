from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

Producto1 = Producto("Hamburguesa", 5.99)
Producto2 = Producto("Pizza", 8.99)

Cliente1 = Cliente("Juan", "123456789")
Cliente2 = Cliente("Maria", "987654321")

restaurante = Restaurante("Mi Restaurante")

restaurante.agregar_producto(Producto1)
restaurante.agregar_producto(Producto2)

restaurante.registrar_cliente(Cliente1)
restaurante.registrar_cliente(Cliente2)

restaurante.mostrar_menu()

restaurante.mostrar_clientes()