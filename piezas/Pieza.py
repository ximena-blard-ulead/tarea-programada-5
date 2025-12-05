from data import constantes as c
from abc import ABC, abstractmethod

class Pieza(ABC):

    def __init__(self, nombre, columna, fila):
        if fila not in c.FILAS:
            print("Fila inválida")
        if columna not in c.COLUMNAS:
            print("Columna inválida")

        self.__nombre = nombre
        self.__columna = columna
        self.__fila = fila
    
    @abstractmethod
    def listar_movimientos_posibles(self):
        pass

    def consultar_movimiento(self, destino):
        movimientos_posibles = self.listar_movimientos_posibles()
        return destino in movimientos_posibles

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    @property
    def fila(self):
        return self.__fila
    
    @fila.setter
    def fila(self, new_fila):
        self.__fila = new_fila
    
    @property
    def columna(self):
        return self.__columna
    
    @columna.setter
    def columna(self, new_columna):
        self.__columna = new_columna
    