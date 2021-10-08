from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression

class Declaration(Instruction):

    def __init__(self, id:str, exp: Expression, type:typeExpression) -> None:
        super().__init__()
        self.id = id
        self.exp = exp
        self.type = type

    def compile(self, environment: Environment) -> Value:

        self.exp.generator = self.generator
        
        newValue: Value = self.exp.compile(environment)

        tempVar: Symbol = environment.saveVariable(self.id,self.type)

        if(self.type != typeExpression.BOOL):
            self.generator.addSetStack(str(tempVar.position),newValue.getValue())
        else:
            newLabel = self.generator.newLabel()
            self.generator.addLabel(newValue.trueLabel)
            self.generator.addSetStack(str(tempVar.position),'1')
            self.generator.addGoto(newLabel)
            self.generator.addLabel(newValue.falseLabel)
            self.generator.addSetStack(str(tempVar.position),'0')
            self.generator.addLabel(newLabel)



    