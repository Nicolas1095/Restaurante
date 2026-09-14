#!/usr/bin/env python3
"""
Script de prueba para verificar las optimizaciones de la Semana 12.
Prueba: búsquedas por índice, sincronización de índices, y persistencia.
"""

import sys
from pathlib import Path

# Agregar ruta de modelos
sys.path.insert(0, str(Path(__file__).parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio


def limpiar_datos():
    """Limpia los archivos JSON para comenzar con datos frescos"""
    directorio = Path(__file__).parent / "restaurante_app" / "datos"
    archivos = ["productos.json", "usuarios.json", "ventas.json"]
    
    for archivo in archivos:
        ruta = directorio / archivo
        if ruta.exists():
            ruta.write_text("[]", encoding="utf-8")
    print("[SETUP] Datos JSON limpiados")


def test_restaurant_app():
    print("=" * 60)
    print("PRUEBAS DE OPTIMIZACIÓN - SEMANA 12")
    print("=" * 60)
    
    # Limpiar datos previos
    limpiar_datos()
    
    # Crear instancia del restaurante
    restaurante = Restaurante("Restaurante de Prueba")
    
    # TEST 1: Agregar productos y verificar índice
    print("\n[TEST 1] Agregando productos...")
    p1 = Producto("P001", "Hamburguesa", 50000, "Comida Rápida", 10)
    p2 = Producto("P002", "Pizza", 60000, "Comida Rápida", 8)
    p3 = Producto("P003", "Jugo Natural", 15000, "Bebidas", 20)
    
    restaurante.agregar_producto(p1)
    restaurante.agregar_producto(p2)
    restaurante.agregar_producto(p3)
    print(f"✓ Agregados 3 productos")
    
    # TEST 2: Buscar por código (usando índice)
    print("\n[TEST 2] Buscando producto por código (usando índice)...")
    resultado = restaurante.buscar_producto("P001")
    assert resultado is not None and resultado.nombre == "Hamburguesa"
    print(f"✓ Búsqueda rápida por código 'P001': {resultado.nombre}")
    
    # TEST 3: Buscar por nombre (fallback a iteración)
    print("\n[TEST 3] Buscando producto por nombre...")
    resultado = restaurante.buscar_producto("Pizza")
    assert resultado is not None and resultado.codigo == "P002"
    print(f"✓ Búsqueda por nombre 'Pizza': código {resultado.codigo}")
    
    # TEST 4: Agregar usuarios y verificar índice
    print("\n[TEST 4] Agregando usuarios...")
    u1 = Usuario("12345", "Juan Pérez", "3001234567")
    u2 = Usuario("67890", "María García", "3007654321")
    
    restaurante.registrar_usuario(u1)
    restaurante.registrar_usuario(u2)
    print(f"✓ Agregados 2 usuarios")
    
    # TEST 5: Buscar usuario por ID (usando índice)
    print("\n[TEST 5] Buscando usuario por identificación (usando índice)...")
    resultado = restaurante.buscar_usuario("12345")
    assert resultado is not None and resultado.nombre == "Juan Pérez"
    print(f"✓ Búsqueda rápida por ID '12345': {resultado.nombre}")
    
    # TEST 6: Realizar ventas
    print("\n[TEST 6] Registrando ventas...")
    venta1 = restaurante.vender_producto("P001", "12345", 2)
    assert venta1 == True
    print(f"✓ Venta 1: Juan compró 2 Hamburguesas")
    
    venta2 = restaurante.vender_producto("P002", "12345", 1)
    assert venta2 == True
    print(f"✓ Venta 2: Juan compró 1 Pizza")
    
    venta3 = restaurante.vender_producto("P003", "67890", 3)
    assert venta3 == True
    print(f"✓ Venta 3: María compró 3 Jugos")
    
    # TEST 7: Consultar ventas de usuario (usando índice)
    print("\n[TEST 7] Consultando ventas de usuario (usando índice)...")
    ventas_juan = restaurante.ventas_de_usuario("12345")
    assert len(ventas_juan) == 2
    print(f"✓ Ventas de Juan (12345): {len(ventas_juan)} transacciones")
    for i, venta in enumerate(ventas_juan, 1):
        print(f"  - Venta {i}: Producto {venta.producto_codigo}, Cantidad {venta.cantidad}")
    
    ventas_maria = restaurante.ventas_de_usuario("67890")
    assert len(ventas_maria) == 1
    print(f"✓ Ventas de María (67890): {len(ventas_maria)} transacción")
    
    # TEST 8: Verificar actualización de stock
    print("\n[TEST 8] Verificando stock actualizado...")
    p1_after = restaurante.buscar_producto("P001")
    assert p1_after.stock == 8  # 10 - 2 = 8
    print(f"✓ Stock de Hamburguesa: {p1_after.stock} (10 - 2 vendidas = 8)")
    
    p2_after = restaurante.buscar_producto("P002")
    assert p2_after.stock == 7  # 8 - 1 = 7
    print(f"✓ Stock de Pizza: {p2_after.stock} (8 - 1 vendida = 7)")
    
    # TEST 9: Eliminar producto y verificar índice
    print("\n[TEST 9] Eliminando producto y verificando índice...")
    restaurante.eliminar_producto(p3)
    resultado = restaurante.buscar_producto("P003")
    assert resultado is None
    print(f"✓ Producto P003 eliminado correctamente")
    
    # TEST 10: Crear nuevo restaurante para verificar persistencia
    print("\n[TEST 10] Verificando persistencia (recarga desde JSON)...")
    restaurante2 = Restaurante("Restaurante Recargado")
    
    # Verificar que los datos se recargan
    assert len(restaurante2.productos) == 2  # P001, P002 (P003 fue eliminado)
    assert len(restaurante2.usuarios) == 2
    
    # Verificar búsqueda rápida después de recarga
    producto_recargado = restaurante2.buscar_producto("P001")
    assert producto_recargado is not None
    assert producto_recargado.nombre == "Hamburguesa"
    print(f"✓ Producto recargado desde JSON: {producto_recargado.nombre}")
    
    # Verificar ventas recargadas
    ventas_juan_recargadas = restaurante2.ventas_de_usuario("12345")
    assert len(ventas_juan_recargadas) == 2
    print(f"✓ Ventas de Juan recargadas: {len(ventas_juan_recargadas)} transacciones")
    
    print("\n" + "=" * 60)
    print("TODOS LOS TESTS PASARON ✓")
    print("=" * 60)


if __name__ == "__main__":
    test_restaurant_app()
