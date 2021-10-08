from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression

class ConsoleLog(Instruction):

    def __init__(self, exp: Expression) -> None:
        super().__init__()
        self.exp = exp

    def compile(self, environment: Environment) -> Value:

        self.exp.generator = self.generator
        
        tempValue: Value = self.exp.compile(environment)

        if(tempValue.type == typeExpression.INTEGER):
            self.generator.addPrintf("d","(int)" + str(tempValue.getValue()))

        elif(tempValue.type == typeExpression.FLOAT):
            self.generator.addPrintf("f","(double)" + str(tempValue.getValue()))

        elif(tempValue.type == typeExpression.BOOL):
            newLabel = self.generator.newLabel()
            self.generator.addLabel(tempValue.trueLabel)
            self.generator.addCallFunc("print_true_proc")
            
            self.generator.addGoto(newLabel)
            self.generator.addLabel(tempValue.falseLabel)
            self.generator.addCallFunc("print_false_proc")

            self.generator.addLabel(newLabel)

        else:
            print("Error en print")

        self.generator.addNewLine()

    