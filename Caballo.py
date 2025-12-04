from Pieza import Pieza
from data import constantes as c

class Caballo(Pieza):

    def __init__(self, columna, fila):
        super().__init__("caballo", columna, fila)

    def listar_movimientos_posibles(self):
        movimientos = []
        col_indice = c.COLUMNAS.index(self.columna)

        direcciones = [
            (col_indice + 1, self.fila + 2),
            (col_indice + 1, self.fila - 2),
            (col_indice - 1, self.fila + 2),
            (col_indice - 1, self.fila - 2),
            (col_indice + 2, self.fila - 1),
            (col_indice + 2, self.fila + 1),
            (col_indice - 2, self.fila - 1),
            (col_indice - 2, self.fila + 1),
        ]

        for dx, dy in direcciones:
            if 0 <= dx < 7 and 1 <= dy <= 8:
                movimientos.append(f"{c.COLUMNAS[dx]}-{dy}")

        return movimientos