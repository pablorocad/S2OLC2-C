from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class Block(Instruction):

    def __init__(self, block) -> None:
        self.block = block

    def execute(self, environment: Environment):
        newEnv = Environment(environment)

        for ins in self.block:
            ins.execute(newEnv)