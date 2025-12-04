from Pieza import Pieza
from data import constantes as c

class Torre(Pieza):

    def __init__(self, columna, fila):
        super().__init__("torre", columna, fila)

    def listar_movimientos_posibles(self):
        movimientos = []

        # Vertical
        for fila in c.FILAS:
            if fila != self.fila:
                movimientos.append(f"{self.columna}-{fila}")

        # Horizontal
        for columna in c.COLUMNAS:
            if columna != self.columna:
                movimientos.append(f"{columna}-{self.fila}")

        return movimientos
