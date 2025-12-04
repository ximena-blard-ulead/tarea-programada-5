from data import constantes as c

class Pieza:

    def __init__(self, nombre, columna, fila):
        if fila not in c.FILAS:
            print("Fila inválida")
        if columna not in c.COLUMNAS:
            print("Columna inválida")

        self.__nombre = nombre
        self.__columna = columna
        self.__fila = fila

    def __str__(self):
        return f"La pieza: {self.__nombre} se encuentra en la posición: {self.__columna}-{self.__fila}."
    
    def listar_movimientos_posibles(self):
        return f"Esta función se debe implementar en las clases hijas"
    
    def explicacion_de_movimiento(self):
        return "movimiento x"
    
    @property
    def fila(self):
        return self.__fila
    
    @property
    def columna(self):
        return self.__columna
    