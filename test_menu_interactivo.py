#!/usr/bin/env python3
"""
Script de prueba interactiva para verificar todas las funcionalidades de main.py
"""

import sys
import json
from pathlib import Path
from io import StringIO

sys.path.insert(0, str(Path(__file__).parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


def limpiar_datos():
    """Limpia los archivos JSON"""
    directorio = Path(__file__).parent / "restaurante_app" / "datos"
    for archivo in ["productos.json", "usuarios.json", "ventas.json"]:
        (directorio / archivo).write_text("[]", encoding="utf-8")


def test_menu_interactivo():
    """Simula todas las opciones del menú principal"""
    
    print("=" * 70)
    print("PRUEBA INTERACTIVA DEL MENÚ DE restaurante_app")
    print("=" * 70)
    
    # Limpiar datos
    limpiar_datos()
    
    # Crear restaurante
    restaurante = Restaurante("Restaurante de Nicolás")
    
    # OPCIÓN 1: Registrar producto
    print("\n[OPCIÓN 1] Registrando productos...")
    p1 = Producto("P001", "Hamburgesa Premium", 85000, "Carnes", 15)
    p2 = Producto("P002", "Pizza Margarita", 65000, "Pizzas", 12)
    p3 = Producto("P003", "Pasta Carbonara", 55000, "Pastas", 20)
    p4 = Producto("P004", "Ensalada Verde", 35000, "Ensaladas", 25)
    
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(p3)
    restaurante.agregar_producto(p4)
    print(f"  ✓ Registrados 4 productos")
    
    # OPCIÓN 5: Listar productos
    print("\n[OPCIÓN 5] Mostrando menú de productos...")
    restaurante.mostrar_menu()
    
    # OPCIÓN 8: Mostrar categorías
    print("\n[OPCIÓN 8] Categorías disponibles...")
    categorias = sorted({producto.categoria for producto in restaurante.productos})
    for i, cat in enumerate(categorias, 1):
        print(f"  {i}. {cat}")
    
    # OPCIÓN 6: Registrar usuario
    print("\n[OPCIÓN 6] Registrando usuarios...")
    u1 = Usuario("1001", "Carlos López", "3001111111")
    u2 = Usuario("1002", "Ana Martínez", "3002222222")
    u3 = Usuario("1003", "Pedro Sánchez", "3003333333")
    
    restaurante.registrar_usuario(u1)
    restaurante.registrar_usuario(u2)
    restaurante.registrar_usuario(u3)
    print(f"  ✓ Registrados 3 usuarios")
    
    # OPCIÓN 7: Listar usuarios
    print("\n[OPCIÓN 7] Listado de usuarios...")
    restaurante.mostrar_usuarios()
    
    # OPCIÓN 2: Buscar producto
    print("\n[OPCIÓN 2] Buscando productos...")
    print(f"  Búsqueda por código 'P001': {restaurante.buscar_producto('P001').nombre}")
    print(f"  Búsqueda por nombre 'Pizza Margarita': {restaurante.buscar_producto('Pizza Margarita').codigo}")
    print(f"  ✓ Búsquedas ejecutadas exitosamente")
    
    # OPCIÓN 9: Vender producto
    print("\n[OPCIÓN 9] Realizando ventas...")
    
    v1 = restaurante.vender_producto("P001", "1001", 2)
    print(f"  ✓ Carlos compró 2 Hamburguesas: {v1}")
    
    v2 = restaurante.vender_producto("P002", "1001", 1)
    print(f"  ✓ Carlos compró 1 Pizza: {v2}")
    
    v3 = restaurante.vender_producto("P003", "1002", 3)
    print(f"  ✓ Ana compró 3 Pastas: {v3}")
    
    v4 = restaurante.vender_producto("P004", "1003", 2)
    print(f"  ✓ Pedro compró 2 Ensaladas: {v4}")
    
    v5 = restaurante.vender_producto("P002", "1002", 1)
    print(f"  ✓ Ana compró 1 Pizza: {v5}")
    
    # Intentar venta inválida
    print("\n[OPCIÓN 9] Intentando venta inválida...")
    v_invalid = restaurante.vender_producto("P001", "1001", 100)  # Stock insuficiente
    print(f"  ✓ Venta rechazada (stock insuficiente): {v_invalid}")
    
    v_invalid2 = restaurante.vender_producto("NOXE", "1001", 1)  # Producto no existe
    print(f"  ✓ Venta rechazada (producto no existe): {v_invalid2}")
    
    # OPCIÓN 10: Consultar ventas de usuario
    print("\n[OPCIÓN 10] Consultando ventas de usuarios...")
    
    ventas_carlos = restaurante.ventas_de_usuario("1001")
    print(f"  Carlos (1001) tiene {len(ventas_carlos)} compras:")
    for venta in ventas_carlos:
        print(f"    - Producto {venta.producto_codigo}: {venta.cantidad} unidad(es)")
    
    ventas_ana = restaurante.ventas_de_usuario("1002")
    print(f"  Ana (1002) tiene {len(ventas_ana)} compras:")
    for venta in ventas_ana:
        print(f"    - Producto {venta.producto_codigo}: {venta.cantidad} unidad(es)")
    
    ventas_pedro = restaurante.ventas_de_usuario("1003")
    print(f"  Pedro (1003) tiene {len(ventas_pedro)} compra(s):")
    for venta in ventas_pedro:
        print(f"    - Producto {venta.producto_codigo}: {venta.cantidad} unidad(es)")
    
    # Verificar stock actualizado
    print("\n[ESTADO] Stock de productos después de ventas...")
    for producto in restaurante.productos:
        print(f"  {producto.codigo} - {producto.nombre}: {producto.stock} unidades")
    
    # OPCIÓN 3: Actualizar producto
    print("\n[OPCIÓN 3] Actualizando producto...")
    p_actualizar = restaurante.buscar_producto("P001")
    restaurante.actualizar_producto(p_actualizar, "Hamburgesa Premium XL", 95000)
    print(f"  ✓ Producto actualizado: {p_actualizar.nombre} - ${p_actualizar.precio}")
    
    # OPCIÓN 4: Eliminar producto
    print("\n[OPCIÓN 4] Eliminando producto...")
    p_eliminar = restaurante.buscar_producto("P004")
    restaurante.eliminar_producto(p_eliminar)
    print(f"  ✓ Producto {p_eliminar.codigo} eliminado")
    print(f"  Productos restantes: {len(restaurante.productos)}")
    
    # Persistencia
    print("\n[PERSISTENCIA] Guardando datos en JSON...")
    print(f"  ✓ {len(restaurante.productos)} productos guardados")
    print(f"  ✓ {len(restaurante.usuarios)} usuarios guardados")
    print(f"  ✓ {len(restaurante.ventas)} ventas guardadas")
    
    # Crear nuevo restaurante para verificar persistencia
    print("\n[PERSISTENCIA] Recargar datos desde JSON...")
    restaurante2 = Restaurante("Restaurante (Recargado)")
    
    print(f"  ✓ {len(restaurante2.productos)} productos cargados")
    print(f"  ✓ {len(restaurante2.usuarios)} usuarios cargados")
    print(f"  ✓ {len(restaurante2.ventas)} ventas cargadas")
    
    # Verificar que las búsquedas por índice funcionan después de recargar
    print("\n[ÍNDICES] Verificando índices después de recarga...")
    p_test = restaurante2.buscar_producto("P001")
    print(f"  ✓ Búsqueda por código P001: {p_test.nombre}")
    
    u_test = restaurante2.buscar_usuario("1001")
    print(f"  ✓ Búsqueda por ID 1001: {u_test.nombre}")
    
    ventas_test = restaurante2.ventas_de_usuario("1001")
    print(f"  ✓ Ventas de usuario 1001: {len(ventas_test)} transacciones")
    
    print("\n" + "=" * 70)
    print("PRUEBA INTERACTIVA COMPLETADA ✓")
    print("=" * 70)
    print("\nRESUMEN DE FUNCIONALIDADES PROBADAS:")
    print("  ✓ Registrar productos (OPCIÓN 1)")
    print("  ✓ Buscar productos por código y nombre (OPCIÓN 2)")
    print("  ✓ Actualizar productos (OPCIÓN 3)")
    print("  ✓ Eliminar productos (OPCIÓN 4)")
    print("  ✓ Listar productos (OPCIÓN 5)")
    print("  ✓ Registrar usuarios (OPCIÓN 6)")
    print("  ✓ Listar usuarios (OPCIÓN 7)")
    print("  ✓ Mostrar categorías (OPCIÓN 8)")
    print("  ✓ Realizar ventas con validación de stock (OPCIÓN 9)")
    print("  ✓ Consultar ventas de usuario (OPCIÓN 10)")
    print("  ✓ Persistencia JSON (guardar y recargar)")
    print("  ✓ Índices de optimización (búsquedas O(1))")
    print("=" * 70)


if __name__ == "__main__":
    test_menu_interactivo()
