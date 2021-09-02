from Enum.typeExpression import typeExpression
from Enum.arithmeticOperation import arithmeticOperation
from Enum.Dominant import Dominant
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class Array(Expression):

    def __init__(self, listExp) -> None:
        self.listExp = listExp

    def execute(self, environment: Environment) -> Symbol:
        
        tempExp = []
        for exp in self.listExp:
            tempExp.append(exp.execute(environment))

        tempSymbol: Symbol = Symbol('',tempExp,tempExp[0].getType())
        tempSymbol.array = True

        return tempSymbol