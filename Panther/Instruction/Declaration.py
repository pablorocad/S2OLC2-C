from Expression.Primitive import Primitive
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression

class Declaration(Instruction):

    def __init__(self, id: str, type: typeExpression, value: Expression, isArray: bool) -> None:
        self.id = id
        self.type = type
        self.value = value
        self.isArray = isArray

    def execute(self, environment: Environment):
        
        tempValue = self.value.execute(environment)

        if(self.type.value != tempValue.getType().value):
            print("Los tipos no coinciden")
            environment.saveVariable('None',Primitive(0,typeExpression.INTEGER).execute(environment),typeExpression.INTEGER)
            return

        environment.saveVariable(self.id,tempValue,self.type,self.isArray)