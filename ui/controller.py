import ui.menu_manager as m
from piezas.Torre import Torre
from piezas.Alfil import Alfil
from piezas.Reina import Reina
from piezas.Rey import Rey
from piezas.Caballo import Caballo
from piezas.Peon import Peon


def procesar_opcion(opcion):
    acciones = {
        1: consultar_posibles_movimientos,
        2: consultar_movimiento_posible,
    }

    if opcion in acciones:
        tipo = seleccionar_tipo_pieza()
        pieza = leer_info_pieza(tipo)
        acciones[opcion](pieza)
    elif opcion == 3:
        print("Gracias por jugar! Nos vemos :)")
    else:
        print("\nOpción inválida. Seleccione una de las listadas en el menú.")

def seleccionar_tipo_pieza():
    m.imprimir_menu_piezas()
    opcion = int(input("Ingrese un número: "))

    piezas = {
        1: Torre,
        2: Alfil,
        3: Reina,
        4: Rey,
        5: Caballo,
        6: Peon
    }

    return piezas[opcion]

def leer_info_pieza(tipo):
    columna = input("\nIngrese la columna de la pieza (a - h): ").lower()
    fila = int(input("\nIngrese la fila de la pieza (1 - 8): "))

    if tipo is Peon:
        color = input("\nIngrese el color de la pieza (blanco/negro): ").lower()
        return tipo(columna, fila, color)

    return tipo(columna, fila)


def consultar_posibles_movimientos(pieza):
    movimientos = pieza.listar_movimientos_posibles()

    print("\nMovimientos posibles:")
    if not movimientos:
        print("La pieza no puede moverse.")
    else:
        for mov in movimientos:
            print(f"- {mov}")

def leer_info_movimiento():
    columna_destino = input("\nIngrese la columna destino para verificar (a - h): ")
    fila_destino = input("\nIngrese la fila destino para verificar (1 - 8): ")
    return f"{columna_destino}-{fila_destino}"

def consultar_movimiento_posible(pieza):
    destino = leer_info_movimiento()

    if pieza.consultar_movimiento(destino):
        print(f"\nEl movimiento a {destino} es válido.")
    else:
        print(f"\nEl movimiento a {destino} NO es válido.")
