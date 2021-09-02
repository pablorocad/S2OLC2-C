
class Node:

    def __init__(self, value: str) -> None:
        self.value = value
        self.child = []
        self.contador = 0
        self.grafo = ""

    def insertChild(self,temp):
        self.child.append(temp)


    def getGraphAST(self) -> str:

        self.grafo = "digraph Tree{ \n"
        self.grafo += "nodo0[label=\"" + str(self.value) + "\"];\n"
        self.contador = 1
        self.graphAST("nodo0", self)
        self.grafo += "}"

        return self.grafo
    

    def graphAST(self, padre: str, temp):

        for hijo in temp.child:
            nameChild: str = "nodo" + str(self.contador)
            self.grafo += nameChild + "[label=\"" + str(hijo.value) + "\"];\n"
            self.grafo += padre + "->" + nameChild + ";\n"
            self.contador = self.contador + 1
            self.graphAST(nameChild, hijo)
        
        return
    