from Environment.Environment import Environment
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction

class Assignment(Instruction):

    def __init__(self, id: str, value: Expression) -> None:
        self.id = id
        self.value = value

    def execute(self, environment: Environment):
        newValue = self.value.execute(environment)
        environment.alterVariable(self.id, newValue)