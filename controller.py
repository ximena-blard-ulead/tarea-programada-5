import menu_manager as m
from Torre import Torre
from Alfil import Alfil
from Reina import Reina
from Rey import Rey
from Caballo import Caballo
from Peon import Peon

def procesar_opcion(opcion):
    if opcion == 1:
        tipo = seleccionar_tipo_pieza()
        pieza = leer_info_pieza(tipo)
        consultar_posibles_movimientos(pieza)
    elif opcion == 2:
        tipo = seleccionar_tipo_pieza()
        pieza = leer_info_pieza(tipo)  
        consultar_movimiento_posible(pieza)
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

    return piezas.get(opcion)

def leer_info_pieza(tipo):
    columna = input("\nIngrese la columna de la pieza (a - h): ").lower()
    fila = int(input("\nIngrese la fila de la pieza (1 - 8): "))

    # Crear la pieza con la posición indicada
    if tipo == "Peon":
        color = input("\nIngrese la columna de la pieza (a - h): ")
        pieza = tipo(columna, fila)
    pieza = tipo(columna, fila)

    return pieza

def consultar_posibles_movimientos(pieza):
    movimientos = pieza.listar_movimientos_posibles()

    print("\nMovimientos posibles:")
    if not movimientos:
        print("La pieza no puede moverse.")
    else:
        for mov in movimientos:
            print(f"- {mov}")

def consultar_movimiento_posible(pieza):
    columna_destino = input("\nIngrese la columna destino para verificar: ")
    fila_destino = input("\nIngrese la fila destino para verificar: ")
    destino = f"{columna_destino}-{fila_destino}"

    movimientos = pieza.listar_movimientos_posibles()

    if destino in movimientos:
        print(f"\nEl movimiento a {columna_destino}-{fila_destino} es válido.")
    else:
        print(f"\nEl movimiento a {columna_destino}-{fila_destino} NO es válido.")
