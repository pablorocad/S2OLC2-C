from Environment.Symbol import Symbol
from Expression.Primitive import Primitive
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression

class VariableCall(Expression):

    def __init__(self, id: str) -> None:
        self.id = id

    def execute(self, environment: Environment) -> Symbol:
        retValue = environment.getVariable(self.id)

        if(retValue == None):
            retValue = Primitive(0,typeExpression.INTEGER).execute(environment)

        return retValue
        