from src.operation import Operation


class Det(Operation):
    """Operación que calcula el determinante de dos matrices cuadradas de forma independiente.

    Hereda de Operation y sigue el contrato SetMatrix(index, matrix), Compute(), Clear().
    """

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Asigna una matriz en la posición indicada (0 para A, 1 para B).

        Args:
            index (int): Índice de la matriz (0 o 1).
            matrix (list[list[float]]): Matriz cuadrada como lista de filas.
        """
        self.matrices[index] = matrix

    def Compute(self):
        """Calcula el determinante de cada matriz asignada de forma independiente.

        Returns:
            list[list[float]]: [[det_a], [det_b]], el determinante de cada matriz
            envuelto como fila, para mantener consistencia con la estructura de resultado.

        Raises:
            ValueError: Si falta alguna matriz, si están vacías, o si no son cuadradas.
        """
        matrix_a = self.matrices[0]
        matrix_b = self.matrices[1]

        if matrix_a is None or matrix_b is None:
            raise ValueError("Both matrices must be set before computing.")

        if len(matrix_a) == 0 or len(matrix_b) == 0:
            raise ValueError("Matrices must not be empty.")

        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])

        # comprobación de compatibilidad: cada matriz debe ser cuadrada para el determinante
        if rows_a != cols_a:
            raise ValueError("Matrix A must be square in order to calculate its determinant.")
        if rows_b != cols_b:
            raise ValueError("Matrix B must be square in order to calculate its determinant.")

        det_a = self._determinant(matrix_a)
        det_b = self._determinant(matrix_b)

        result = [[det_a], [det_b]]
        return result

    @staticmethod
    def _determinant(matrix, eps=1e-12):
        """Calcula el determinante de una matriz cuadrada mediante eliminación
        gaussiana con pivoteo parcial.

        Args:
            matrix (list[list[float]]): Matriz cuadrada de entrada.
            eps (float): Umbral por debajo del cual un pivote se considera cero.

        Returns:
            float: El determinante de la matriz.

        Raises:
            ValueError: Si la matriz no es cuadrada.
        """
        n = len(matrix)
        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix must be square to compute its determinant.")

        # copia profunda a float para no modificar la original
        A = [list(map(float, row)) for row in matrix]
        swap_count = 0

        for i in range(n):
            # pivoteo parcial: buscar fila con mayor valor absoluto en la columna i
            pivot_row = max(range(i, n), key=lambda r: abs(A[r][i]))
            if abs(A[pivot_row][i]) < eps:
                # pivote ~ 0 => determinante cero
                return 0.0
            if pivot_row != i:
                A[i], A[pivot_row] = A[pivot_row], A[i]
                swap_count += 1

            # eliminación hacia abajo
            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]

        # determinante = producto de la diagonal con signo según intercambios de filas
        det = 1.0
        for i in range(n):
            det *= A[i][i]
        if swap_count % 2 == 1:
            det = -det
        return det

    def Clear(self):
        """Restablece ambas matrices a None."""
        self.matrices = [None, None]