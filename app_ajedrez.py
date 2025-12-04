import menu_manager
import controller

def ejecutar():
    opcion = 0

    while opcion != 3:
        menu_manager.imprimir_menu_principal()
        opcion = int(input("Seleccione su opción: "))
        controller.procesar_opcion(opcion)
