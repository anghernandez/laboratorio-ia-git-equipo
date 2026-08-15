from src.operations.sum import Sum
from src.operations.mul import Mul
from src.operations.det import Det
from src.operations.inv import Inv
class Application:
    def __init__(self):
        self.operations = {
            "sum": Sum(),
            "mul": Mul(),
            "det": Det(),
            "inv": Inv(),
        }

    def get_operation(self, operation_name):
        if operation_name in self.operations:
            return self.operations[operation_name]

        raise ValueError(f"Operation '{operation_name}' is not supported.")