import json


def load_matrices(file_path):
    """
    Carga un archivo JSON que contiene matrices, devuelve y válida su contenido como un diccionario de Python. 
    Args:
        file_path (str): La ruta al archivo JSON que contiene las matrices.

    Returns:
        dict: El contenido del archivo JSON como un diccionario de Python.
    """
   
    with open(file_path, 'r') as file:
        data = json.load(file)

    #Permite acceder a los datos de las matrices A y sus dimensiones
    matrix_a_info = data["matrixA"]
    rows_a = matrix_a_info["rows"]
    cols_a = matrix_a_info["cols"]
    matrix_a = matrix_a_info["data"]

    #Permite acceder a los datos de las matrices B y sus dimensiones
    matrix_b_info = data["matrixB"]
    rows_b = matrix_b_info["rows"]
    cols_b = matrix_b_info["cols"]
    matrix_b = matrix_b_info["data"]

    # Validación de las dimensiones de las matrices
    real_rows_a = len(matrix_a)
    real_cols_a = len(matrix_a[0]) if real_rows_a > 0 else 0
    real_rows_b = len(matrix_b)
    real_cols_b = len(matrix_b[0]) if real_rows_b > 0 else 0

    if real_rows_a != rows_a or real_cols_a != cols_a:
        raise ValueError("Matrix A dimensions do not match the specified rows and columns.")

    if real_rows_b != rows_b or real_cols_b != cols_b:
        raise ValueError("Matrix B dimensions do not match the specified rows and columns.")

    for row in matrix_a:
        if len(row) != cols_a:
            raise ValueError("Matrix A has inconsistent row lengths.")

    for row in matrix_b:
        if len(row) != cols_b:
            raise ValueError("Matrix B has inconsistent row lengths.")

    for row in matrix_a:
        for value in row:
            if not isinstance(value,float):
                raise ValueError("Matrix A contains non-float values.")

    for row in matrix_b:
        for value in row:
            if not isinstance(value,float):
                raise ValueError("Matrix B contains non-float values.")
           
    return data

