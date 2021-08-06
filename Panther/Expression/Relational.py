from Enum.relationalOperation import relationalOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class Relational(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: relationalOperation) -> None:
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:
        
        leftValue = self.leftExp.execute(environment)
        rightValue = self.rightExp.execute(environment)

        if(self.operation == relationalOperation.MAYOR):
            return Symbol(
                "",
                int(leftValue.getValue()) > int(rightValue.getValue()),
                typeExpression.BOOL
            )
        
        elif(self.operation == relationalOperation.MENOR):
            return Symbol(
                "",
                int(leftValue.getValue()) < int(rightValue.getValue()),
                typeExpression.BOOL
            )
        
        elif(self.operation == relationalOperation.IGUAL):
            return Symbol(
                "",
                leftValue.getValue() == rightValue.getValue(),
                typeExpression.BOOL
            )
            