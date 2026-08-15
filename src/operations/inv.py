from src.operation import Operation


class Inv(Operation):
    """Operación que calcula la inversa de dos matrices cuadradas de forma independiente.

    Hereda de Operation y sigue el contrato:
    SetMatrix(index, matrix), Compute(), Clear().
    """

    def __init__(self):
        self.matrices = [None, None]

    def SetMatrix(self, index, matrix):
        """Asigna una matriz en la posición indicada.

        Args:
            index (int): Índice de la matriz (0 para A, 1 para B).
            matrix (list[list[float]]): Matriz cuadrada.
        """
        self.matrices[index] = matrix

    def Compute(self):
        """Calcula la inversa de cada matriz asignada.

        Returns:
            list[list[list[float]]]: Lista que contiene las inversas de A y B.

        Raises:
            ValueError: Si falta una matriz, está vacía, no es cuadrada
            o no es invertible.
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

        if rows_a != cols_a:
            raise ValueError(
                "Matrix A must be square in order to calculate its inverse."
            )

        if rows_b != cols_b:
            raise ValueError(
                "Matrix B must be square in order to calculate its inverse."
            )

        inverse_a = self._inverse(matrix_a)
        inverse_b = self._inverse(matrix_b)

        return [inverse_a, inverse_b]

    @staticmethod
    def _inverse(matrix, eps=1e-12):
        """Calcula la inversa mediante eliminación Gauss-Jordan.

        Args:
            matrix (list[list[float]]): Matriz cuadrada.
            eps (float): Tolerancia para considerar un pivote como cero.

        Returns:
            list[list[float]]: Matriz inversa.

        Raises:
            ValueError: Si la matriz no es cuadrada o es singular.
        """
        n = len(matrix)

        # Verifica que todas las filas tengan tamaño n.
        if any(len(row) != n for row in matrix):
            raise ValueError("The matrix must be square to compute its inverse.")

        # Copia la matriz a float para no modificar la matriz original.
        a = [list(map(float, row)) for row in matrix]

        # Construye la matriz identidad.
        identity = []

        for i in range(n):
            row = []

            for j in range(n):
                if i == j:
                    row.append(1.0)
                else:
                    row.append(0.0)

            identity.append(row)

        # Construye la matriz aumentada [A | I].
        augmented = []

        for i in range(n):
            augmented.append(a[i] + identity[i])

        # Gauss-Jordan.
        for i in range(n):
            # Busca el mejor pivote en la columna actual.
            pivot_row = i

            for row in range(i, n):
                if abs(augmented[row][i]) > abs(augmented[pivot_row][i]):
                    pivot_row = row

            # Si el pivote es prácticamente cero, la matriz no es invertible.
            if abs(augmented[pivot_row][i]) < eps:
                raise ValueError("The matrix is not invertible.")

            # Intercambia filas si es necesario.
            if pivot_row != i:
                augmented[i], augmented[pivot_row] = (
                    augmented[pivot_row],
                    augmented[i],
                )

            # Convierte el pivote en 1.
            pivot = augmented[i][i]

            for j in range(2 * n):
                augmented[i][j] /= pivot

            # Convierte en cero los demás elementos de la columna del pivote.
            for row in range(n):
                if row != i:
                    factor = augmented[row][i]

                    for j in range(2 * n):
                        augmented[row][j] -= factor * augmented[i][j]

        # La mitad derecha de [I | A^-1] es la inversa.
        inv = []

        for i in range(n):
            inv.append(augmented[i][n:])

        return inv

    def Clear(self):
        """Restablece ambas matrices a None."""
        self.matrices = [None, None]

