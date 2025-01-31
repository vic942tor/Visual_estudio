# Diseña un programa en Python para analizar los datos de ventas almacenados en
# un archivo CSV. El objetivo es procesar los datos y generar estadísticas útiles que
# serán exportadas en un archivo JSON.
# Las tareas a realizar por el programa son;
# 1. Leer un archivo CSV llamado 'ventas.csv' que incluye las columnas:
# • 'fecha',
# • 'producto',
# • 'cantidad_vendida',
# • ‘precio_unitario’.
# 2. Realizar los siguientes cálculos:
# • Total de ingresos generados por todas las ventas.
# • Promedio de ventas por producto.
# • Identicar el producto más vendido.
# 3. Guardar los resultados en un archivo llamado ‘informe.json’.
# 4. Mostrar el informe en consola con un formato claro.
# Tener en cuenta que en chero .csv pueden haber líneas de ventas para el mismo
# producto, porque se han realizado en distintos días

import csv
import json
import os
directorio_script = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_CSV = os.path.join(directorio_script, "ventas.csv")
ARCHIVO_JSON = "informe.json"
def leer_csv():
    """Lee los datos del archivo CSV y los retorna como una lista de diccionarios."""
    ventas = []
    try:
        with open(ARCHIVO_CSV, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                fila['cantidad_vendida'] = int(fila['cantidad_vendida'])
                fila['precio_unitario'] = float(fila['precio_unitario'])
                ventas.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ARCHIVO_CSV}")
    return ventas
def calcular_estadisticas(ventas):
    """Calcula el total de ingresos, el promedio de ventas por producto y el producto más vendido."""
    if not ventas:
        return {}
    total_ingresos = sum(venta['cantidad_vendida'] * venta['precio_unitario'] for venta in ventas)
    ventas_por_producto = {}
    for venta in ventas:
        producto = venta['producto']
        if producto not in ventas_por_producto:
            ventas_por_producto[producto] = {'cantidad_total': 0, 'ventas': 0}
        ventas_por_producto[producto]['cantidad_total'] += venta['cantidad_vendida']
        ventas_por_producto[producto]['ventas'] += 1
    promedio_ventas = {producto: datos['cantidad_total'] / datos['ventas'] for producto, datos in ventas_por_producto.items()}
    producto_mas_vendido = max(ventas_por_producto, key=lambda p: ventas_por_producto[p]['cantidad_total'])
    return {
        "total_ingresos": total_ingresos,
        "promedio_ventas_por_producto": promedio_ventas,
        "producto_mas_vendido": producto_mas_vendido
    }
def guardar_json(informe):
    """Guarda las estadísticas calculadas en un archivo JSON."""
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(informe, archivo, indent=4, ensure_ascii=False)
def mostrar_informe(informe):
    """Muestra el informe en consola de manera formateada."""
    print("\n--- INFORME DE VENTAS ---")
    print(f"Total de ingresos: ${informe['total_ingresos']:.2f}")
    print("Promedio de ventas por producto:")
    for producto, promedio in informe['promedio_ventas_por_producto'].items():
        print(f"  - {producto}: {promedio:.2f} unidades")
    print(f"Producto más vendido: {informe['producto_mas_vendido']}")
def principal():
    ventas = leer_csv()
    informe = calcular_estadisticas(ventas)
    if informe:
        guardar_json(informe)
        mostrar_informe(informe)
if __name__ == "__main__":
    principal()

