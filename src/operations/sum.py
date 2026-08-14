from src.operation import Operation
#Herada Operation 

class Sum(Operation):
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

        if rows_a != rows_b or cols_a != cols_b:
            raise ValueError("Matrix dimension is different.")

        result = []

        for i in range(rows_a): #range genera indices de las fila
            row_c = []

            for j in range(cols_a):
                sum_value = matrix_a[i][j] + matrix_b[i][j]
                row_c.append(sum_value)
            result.append(row_c)

        return result


    def Clear(self):
        self.matrices = [None, None]


"""
Test sencillo

matrix_a = [
    [1.0, 2.0],
    [3.0, 4.0]
]

matrix_b = [
    [5.0, 6.0],
    [7.0, 8.0]
]

sum_operation = Sum()

sum_operation.SetMatrix(0, matrix_a)
sum_operation.SetMatrix(1, matrix_b)

result = sum_operation.Compute()

print(result)
sum_operation.Clear()
print(sum_operation.matrices)


"""