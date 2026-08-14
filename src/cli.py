import typer
from src.utils.json_loader import load_matrices
from src.application import Application


app = typer.Typer()

@app.command()
def sum(file_path: str):
    data = load_matrices(file_path)

    matrix_a = data["matrixA"]["data"]
    matrix_b = data["matrixB"]["data"]

    application = Application()
    operation = application.get_operation("sum")

    operation.SetMatrix(0, matrix_a)
    operation.SetMatrix(1, matrix_b)

    result = operation.Compute()
    
    print(result)

    operation.Clear()

if __name__ == "__main__":
    app()
