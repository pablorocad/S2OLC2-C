from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression

class Array(Expression):
    
    def __init__(self, values) -> None:
        self.values = values

    def compile(self, environment: Environment) -> Value:
        
        newTemp = self.generator.newTemp()

        self.generator.addExpression(newTemp,'H','','')
        self.generator.addSetHeap('H',len(self.values))
        self.generator.addExpression('H','H','1','+')

        for exp in self.values:
            exp.generator = self.generator

            valExp = exp.compile(environment)

            self.generator.addSetHeap('H',valExp.getValue())
            self.generator.addExpression('H','H','1','+')

        return Value(newTemp,True,typeExpression.ARRAY)

            