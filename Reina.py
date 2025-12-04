from Pieza import Pieza
from data import constantes as c

class Reina(Pieza):

    def __init__(self, columna, fila):
        super().__init__("reina", columna, fila)

    def listar_movimientos_posibles(self):
        movimientos = []
        # Movimiento alfil
        col_indice = c.COLUMNAS.index(self.columna) #6

        direcciones = [
            (1,1),
            (-1,1),
            (1,-1),
            (-1,-1)
        ]

        for dx, dy in direcciones:
            for paso in range(1,8):
                nueva_col = col_indice + dx * paso
                nueva_fila = self.fila + dy * paso
            
                if 0 <= nueva_col <= 7 and 1 <= nueva_fila <= 8:
                    movimientos.append(f"{c.COLUMNAS[nueva_col]}-{nueva_fila}")
                else:
                    break

        # Movimiento torre
        # Vertical
        for fila in c.FILAS:
            if fila != self.fila:
                movimientos.append(f"{self.columna}-{fila}")

        # Horizontal
        for columna in c.COLUMNAS:
            if columna != self.columna:
                movimientos.append(f"{columna}-{self.fila}")

        return movimientos

    def explicacion_de_movimiento(self):
        return f" Puede desplazarse tantas casillas como desee a derecha e izquierda horizontalmente o bien hacia delante o hacia atrás de forma vertical (como la torre). Además, la dama puede moverse también tantas casillas como desee en diagonal (como el alfil)."