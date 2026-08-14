from src.operations.sum import Sum

class Application:
    def __init__(self):
        self.operations = {
            "sum": Sum()
        }

    def get_operation(self, operation_name):
        if operation_name in self.operations:
            return self.operations[operation_name]
        else:
            raise ValueError(f"Operation '{operation_name}' not found.")

