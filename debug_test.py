#!/usr/bin/env python3
"""Script de debugging para investigar el problema con ventas_de_usuario"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


restaurante = Restaurante("Debug Test")

# Agregar usuario
u1 = Usuario("12345", "Juan Pérez", "3001234567")
restaurante.registrar_usuario(u1)
print(f"Usuario registrado: {u1.identificacion}")

# Agregar producto
p1 = Producto("P001", "Hamburguesa", 50000, "Comida Rápida", 10)
restaurante.agregar_producto(p1)
print(f"Producto agregado: {p1.codigo}")

# Hacer venta
resultado = restaurante.vender_producto("P001", "12345", 2)
print(f"Venta realizada: {resultado}")

# Debugging: Verificar estado del índice
print(f"\nDebug info:")
print(f"Tipo de ventas_de_usuario: {type(restaurante.ventas_de_usuario('12345'))}")
print(f"Ventas de Juan: {restaurante.ventas_de_usuario('12345')}")
print(f"Número de ventas de Juan: {len(restaurante.ventas_de_usuario('12345'))}")

# Verificar la venta en la lista principal
print(f"\nVentas totales en la lista: {len(restaurante.ventas)}")
for venta in restaurante.ventas:
    print(f"  - Venta: usuario={venta.usuario_id}, producto={venta.producto_codigo}, cantidad={venta.cantidad}")
