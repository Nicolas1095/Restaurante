from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

Platillo1 = Platillo("Hamburguesa", 5.99, 500)
Platillo2 = Platillo("Pizza", 3.99, 800)
Bebida1 = Bebida("Coca Cola", 0.99, 250)
Bebida2 = Bebida("Agua", 1.99, 500)

restaurante = Restaurante("Mi Restaurante")

restaurante.agregar_producto(Platillo1)
restaurante.agregar_producto(Platillo2)
restaurante.agregar_producto(Bebida1)
restaurante.agregar_producto(Bebida2)

restaurante.mostrar_menu()
Platillo1.cambiar_precio(3.99)
print("Descuento aplicado al producto:", Platillo1.nombre)
print(f"Nuevo precio: ${Platillo1.obtener_precio():.2f}")
# restaurante.mostrar_clientes()