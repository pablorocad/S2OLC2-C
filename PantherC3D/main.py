from Analyzer.Panther import parser

f = open("./entrada.txt", "r")
input = f.read()
C3D = parser.parse(input)

f2 = open("./salida.txt","w")
f2.write(C3D)