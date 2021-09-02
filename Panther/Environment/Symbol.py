class Symbol:
    #Nuestros simbolos poseen un id, un valor y un tipo
    def __init__(self, id: str, value, type):
        self.id = id
        self.value = value
        self.type = type
        self.array = False

    def getId(self):
        return self.id

    def getValue(self):
        return self.value

    def getType(self):
        return self.type

    def isArray(self):
        return self.array
