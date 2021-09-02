from Environment.Symbol import Symbol
from Expression.Primitive import Primitive
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instruction

class Parameter(Instruction):

    def __init__(self, id: str, type: typeExpression) -> None:
        self.id = id
        self. type = type
        self.value = None

    def setValue(self, value: Expression):
        self.value = value

    def execute(self, environment: Environment):
        
        tempValue = self.value.execute(environment)

        if(self.type.value != tempValue.getType().value):
            print("Los tipos no coinciden")
            environment.saveVariable('None',Primitive(0,typeExpression.INTEGER).execute(environment),typeExpression.INTEGER)
            return

        environment.saveVariable(self.id,tempValue,self.type)
