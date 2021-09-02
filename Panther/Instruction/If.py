from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression

class If(Instruction):

    def __init__(self, condition: Expression, block, elseBlock) -> None:
        self.condition = condition
        self.block = block
        self.elseBlock = elseBlock

    def execute(self, environment: Environment):
        
        tempCondition: Symbol = self.condition.execute(environment)

        if(tempCondition.getValue() == True):
            self.block.execute(environment)

            tempCondition = self.condition.execute(environment)

        else:
            self.elseBlock.execute(environment)