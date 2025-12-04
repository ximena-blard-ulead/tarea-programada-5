from Pieza import Pieza
from data import constantes as c

class Alfil(Pieza):

    def __init__(self, columna, fila):
        super().__init__("alfil", columna, fila)

    def listar_movimientos_posibles(self):
        movimientos = []
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

        return movimientos