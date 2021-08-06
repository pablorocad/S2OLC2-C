from Enum.typeExpression import typeExpression
from Enum.arithmeticOperation import arithmeticOperation
from Enum.Dominant import Dominant
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression

class Arithmetic(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: arithmeticOperation):
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    
    def execute(self, environment: Environment) -> Symbol:
        # Resolvemos la expresion que viene de lado izquierdo
        leftValue = self.leftExp.execute(environment)
        # Resolvemos la expresion que viene de lado derecho
        rightValue = self.rightExp.execute(environment)
        #Obtenemos nuestro dominante
        dominant = Dominant[leftValue.getType().value][rightValue.getType().value]
        
        if(self.operation == arithmeticOperation.PLUS):
            if(dominant == typeExpression.STRING):
                return Symbol(
                    "",
                    str(leftValue.getValue()) + str(rightValue.getValue()),
                    typeExpression.STRING
                    )
            elif(dominant == typeExpression.INTEGER):
                return Symbol(
                    "",
                    int(leftValue.getValue()) + int(rightValue.getValue()),
                    typeExpression.INTEGER
                    )
            elif(dominant == typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) + float(rightValue.getValue()),
                    typeExpression.FLOAT
                    )
            else:
                print("No es posible sumar " + leftValue.getValue() + " y " + rightValue.getValue())
        
        elif(self.operation == arithmeticOperation.MINUS):
            if(dominant == typeExpression.INTEGER):
                return Symbol(
                    "",
                    int(leftValue.getValue()) - int(rightValue.getValue()),
                    typeExpression.INTEGER
                    )
            elif(dominant == typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) - float(rightValue.getValue()),
                    typeExpression.FLOAT
                    )
            else:
                print("No es posible restar " + leftValue.getValue() + " y " + rightValue.getValue())

        elif(self.operation == arithmeticOperation.MULTIPLY):
            if(dominant == typeExpression.INTEGER):
                return Symbol(
                    "",
                    int(leftValue.getValue()) * int(rightValue.getValue()),
                    typeExpression.INTEGER
                    )
            elif(dominant == typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) * float(rightValue.getValue()),
                    typeExpression.FLOAT
                    )
            else:
                print("No es posible multiplicar " + leftValue.getValue() + " y " + rightValue.getValue())

        elif(self.operation == arithmeticOperation.DIV):
            if(dominant == typeExpression.INTEGER):
                return Symbol(
                    "",
                    int(leftValue.getValue()) / int(rightValue.getValue()),
                    typeExpression.FLOAT
                    )
            elif(dominant == typeExpression.FLOAT):
                return Symbol(
                    "",
                    float(leftValue.getValue()) / float(rightValue.getValue()),
                    typeExpression.FLOAT
                    )
            else:
                print("No es posible dividir " + leftValue.getValue() + " y " + rightValue.getValue())
        
        return Symbol('',0,typeExpression.INTEGER)