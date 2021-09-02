# from Environment.Environment import Environment
# from Enum.typeExpression import typeExpression
# from Enum.Dominant import Dominant
# from Enum.arithmeticOperation import arithmeticOperation
# from Expression.Primitive import Primitive
# from Expression.Arithmetic import Arithmetic
# from Instruction.consoleLog import ConsoleLog

# var = Environment(None)
# var.saveVariable("var1",8200,typeExpression.INTEGER)
# #var.getVariable("var1")
# #print(typeExpression.INTEGER.value)
# #print(Dominant[typeExpression.INTEGER.value][typeExpression.INTEGER.value])

# ex = Primitive(8.45,typeExpression.FLOAT)
# ex2 = Primitive(5,typeExpression.INTEGER)
# #print(ex.execute(var).getValue())

# op = Arithmetic(ex,ex2,arithmeticOperation.DIV)
# ins = ConsoleLog(op)
# ins.execute(var)
from AnalyzerTree.PantherTree import parser

f = open("./entrada.txt", "r")
input = f.read()
#print(input)
parser.parse(input)
