from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression

class ConsoleLog(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression


    def execute(self, environment: Environment):
        tempExp = self.expression.execute(environment)

        if(not tempExp.isArray()):
            print(tempExp.getValue())
        else:
            self.printArray(tempExp.getValue(),1)


    def printArray(self,arr,tab):
        print(('   '*(tab-1)) + '[')

        for exp in arr:
            if(exp.isArray()):
                self.printArray(exp.getValue(),tab + 1)
            else:
                print(('   '*tab) + str(exp.getValue()))
                
        print(('   '*(tab-1)) + ']')