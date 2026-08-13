
from abc import ABC, abstractmethod #Permite aplicar clases abstractas


class Operation(ABC):
 
    @abstractmethod
    def SetMatrix(self, index, matrix): 
        '''En esta intancia (self), colaca esta matriz (matrix) en posición (index).'''
        pass

    @abstractmethod
    def Compute(self): 
        '''Realiza la op. usando las matrices que tiene.'''
        pass

    @abstractmethod
    def Clear(self):
        '''Esta instancia debe limpiar las matrices almacenadas.'''
        pass


