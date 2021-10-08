from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression

class VariableCall(Expression):

    def __init__(self, id:str) -> None:
        super().__init__()
        self.id = id

    def compile(self, environment: Environment) -> Value:
        
        retSym:Symbol = environment.getVariable(self.id)
        newTemp = self.generator.newTemp()

        self.generator.addGetStack(newTemp,str(retSym.position))

        if(retSym.type != typeExpression.BOOL):
            return Value(newTemp,True,retSym.type)
        else:
            val = Value("",False,typeExpression.BOOL)

            if(self.trueLabel == ""):
                self.trueLabel = self.generator.newLabel()
                
            if(self.falseLabel == ""):
                self.falseLabel = self.generator.newLabel()

            self.generator.addIf(newTemp,"1","==",self.trueLabel)
            self.generator.addGoto(self.falseLabel)

            val.trueLabel = self.trueLabel
            val.falseLabel = self.falseLabel

            return val