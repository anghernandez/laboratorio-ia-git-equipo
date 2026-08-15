from src.operation import Operation
#Herada Operation 

class Mul(Operation):
    def __init__(self):
        self.matrices = [None, None]


    def SetMatrix(self, index, matrix):
        self.matrices[index] = matrix  


    def Compute(self):

        matrix_a = self.matrices[0]
        matrix_b = self.matrices[1]

        if matrix_a is None or matrix_b is None:
            raise ValueError("Both matrices must be set before computing.")  #Valida que existan las matrices
       

        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])

        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        # comprobación de compatibilidad: cols_a == rows_b
        if cols_a != rows_b:
            raise ValueError("The number of columns in matrix A must equal the number of rows in matrix B.")

        result = []

        for i in range(rows_a): #range genera indices de las fila
            row_c = []
            for j in range(cols_b):
                sum_value = 0
                # Aquí está el bucle interior que multiplica y acumula:
                for k in range(cols_a):  # k recorre la columna de A / fila de B
                   mul_value = matrix_a[i][k] * matrix_b[k][j]
                   sum_value += mul_value
                row_c.append(sum_value)
            result.append(row_c)
        
            

        return result


    def Clear(self):
        self.matrices = [None, None]
