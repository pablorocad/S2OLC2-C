from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class While(Instruction):

    def __init__(self, condition: Expression, block) -> None:
        self.condition = condition
        self.block = block

    def execute(self, environment: Environment):
        
        tempCondition: Symbol = self.condition.execute(environment)

        while(tempCondition.getValue() == True):
            newEnv = Environment(environment)

            for ins in self.block:
                ins.execute(newEnv)

            tempCondition = self.condition.execute(environment)