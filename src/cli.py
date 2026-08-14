import typer
from src.utils.json_loaders.json_loader import load_matrices
app = typer.Typer()

@app.command()
def sum(file_path: str):
    data = load_matrices(file_path)
    print(data)

if __name__ == "__main__":
    app()
