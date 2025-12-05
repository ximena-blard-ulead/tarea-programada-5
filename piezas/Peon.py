from piezas.Pieza import Pieza

class Peon(Pieza):

    def __init__(self, columna, fila, color):
        super().__init__("peon", columna, fila)
        self.__color = color

    def listar_movimientos_posibles(self):
        movimientos = []
        filas_iniciales = [2,7]

        if self.__color == "blanco":
            direccion = 1
        else:
            direccion = -1

        if 1 <= self.fila + direccion <= 8:
            movimientos.append(f"{self.columna}-{self.fila + direccion}")

        if self.fila in filas_iniciales:
            movimientos.append(f"{self.columna}-{self.fila + 2 * direccion}")

        return movimientos