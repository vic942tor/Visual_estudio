# Se quiere diseñar un programa que permita llevar el control de tareas pendientes
# en la que se podrá realizar serialización mediante el uso del formato .json o
# mediante pickle.
# Las tareas deben almacenar los siguientes datos:
# nombre
# fecha_limite
# estado ( pendiente o completada ).
# El programa debe:
# • Agregar tareas nuevas
# En este caso se agregan nuevas tareas al chero elegido para la serialización
# • Modicar el estado de una tarea (de pendiente a completada)
# Se modica el estado de una tarea
# • Eliminar una tarea (sólo si está completada)
# Se elimina una tarea
# • Listar todas las tareas de la aplicación
# Se listan todas las tareas
# • Cambiar el formato de serialización

import json
import os
ARCHIVO_TAREAS = "tareas.json"
def cargar_tareas():
    """Carga las tareas desde un archivo JSON.
    Si el archivo no existe o tiene un formato incorrecto, retorna una lista vacía.
    """
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Error: El archivo JSON tiene un formato incorrecto.")
                return []
    return []
def guardar_tareas(tareas):
    """Guarda la lista de tareas en un archivo JSON."""
    with open(ARCHIVO_TAREAS, "w") as f:
        json.dump(tareas, f, indent=4)
def agregar_tarea():
    """Permite agregar una nueva tarea con nombre, fecha y estado 'pendiente'."""
    tareas = cargar_tareas()
    nombre = input("Ingrese el nombre de la tarea: ")
    fecha = input("Ingrese la fecha límite (YYYY-MM-DD): ")
    tareas.append({"nombre": nombre, "fecha_limite": fecha, "estado": "pendiente"})
    guardar_tareas(tareas)
    print("Tarea agregada.")
def modificar_estado():
    """Cambia el estado de una tarea a 'completada' si existe en la lista."""
    tareas = cargar_tareas()
    listar_tareas()
    nombre = input("Ingrese el nombre de la tarea a completar: ")
    for tarea in tareas:
        if tarea["nombre"] == nombre:
            tarea["estado"] = "completada"
            guardar_tareas(tareas)
            print("Estado actualizado.")
            return
    print("Tarea no encontrada.")
def eliminar_tarea():
    """Elimina una tarea solo si está marcada como 'completada'."""
    tareas = cargar_tareas()
    listar_tareas()
    nombre = input("Ingrese el nombre de la tarea a eliminar: ")
    for tarea in tareas:
        if tarea["nombre"] == nombre and tarea["estado"] == "completada":
            tareas.remove(tarea)
            guardar_tareas(tareas)
            print("Tarea eliminada.")
            return
    print("No se puede eliminar la tarea, sólo se eliminan tareas completadas.")
def listar_tareas():
    """Muestra todas las tareas almacenadas en el archivo JSON."""
    tareas = cargar_tareas()
    if not tareas:
        print("No hay tareas.")
    else:
        for tarea in tareas:
            print(f"{tarea['nombre']} - {tarea['fecha_limite']} - {tarea['estado']}")
def menu():
    """Proporciona un menú interactivo."""
    opciones = {
        "1": agregar_tarea,
        "2": modificar_estado,
        "3": eliminar_tarea,
        "4": listar_tareas,
        "5": exit
    }
    while True:
        print("\n1. Agregar tarea\n2. Modificar estado\n3. Eliminar tarea\n4. Listar tareas\n5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    menu()
