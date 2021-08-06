from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol

class Environment:
    
    def __init__(self, father):
        #Usamos un diccionario para nuestra tabla de simbolos, guardara el id como clave y como cuerpo un simbolo
        self.variable = {}
        #Father es el entorno exterior al cual podemos acceder
        self.father = father

    def saveVariable(self, id: str, value, type: typeExpression):
        if (self.variable.get(id) != None):
            print("La variable " + id + " ya existe")
            return
        tempVar = Symbol(id,value,type)
        self.variable[id] = tempVar
    
    def getVariable(self, id: str):
        tempEnv = self
        while(tempEnv != None):
            if(tempEnv.variable.get(id) != None):
                return tempEnv.variable.get(id)
            tempEnv = tempEnv.father
        print("Error: la variable " + id + " no existe")

