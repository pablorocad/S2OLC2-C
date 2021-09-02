reservadas = {
    'int' : 'RINT',
    'float' : 'RFLOAT',
    'string' : 'RSTRING',
    'console' : 'CONSOLE',
    'log' : 'LOG',
    'let' : 'LET',
    'function' : 'FUNCTION',
    'while' : 'RWHILE',
    'if' : 'RIF',
    'else' : 'RELSE'
}

tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'MAYOR',
    'MENOR',
    'IGUALQUE',
    'PUNTO',
    'ENTERO',
    'DECIMAL',
    'STRING',
    'PTCOMA',
    'COMA',
    'ID',
    'IGUAL',
    'DOSPT',
    'LLAVEIZQ',
    'LLAVEDER',
    'CORDER',
    'CORIZQ'
 ] + list(reservadas.values())

#Tokens
t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_LLAVEIZQ          = r'\{'
t_LLAVEDER          = r'\}'
t_CORIZQ            = r'\['
t_CORDER            = r'\]'
t_MAS               = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACION    = r'\*'
t_DIVISION          = r'/'
t_MAYOR             = r'>'
t_MENOR             = r'<'
t_IGUALQUE          = r'=='
t_IGUAL             = r'='
t_DOSPT             = r':'
t_PUNTO             = r'.'
t_PTCOMA            = r'\;'
t_COMA              = r'\,'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

#Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
from Node.Node import Node

from Instruction.Block import Block
from Instruction.Parameter import Parameter
from Instruction.CallFuncSt import CallFuncSt
from Instruction.Function import Function

import Analyzer.ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','IGUALQUE'),
    ('left','MAYOR','MENOR'),
    ('left','MAS','MENOS'),
    ('left','MULTIPLICACION','DIVISION'),
    )

# Definición de la gramática=====================================================
def p_initial(t):
    '''initial : instructions'''
    
    nodeInitial = Node("initial")
    nodeInitial.insertChild(t[1])

    f = open("./salida.txt", "w")
    f.write(nodeInitial.getGraphAST())

    #print(globalEnv.function)

#====================================================
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    nodeInstructions = Node("instructions")
    if(len(t) == 3):
        nodeInstructions.insertChild(t[1])
        nodeInstructions.insertChild(t[2])
        t[0] = nodeInstructions
    elif(len(t) == 2):
        nodeInstructions.insertChild(t[1])
        t[0] = nodeInstructions

#====================================================
def p_instruction(t):
    '''instruction  : consoleLog 
                    | declaration
                    | function
                    | callFuncSt
                    | assignment
                    | whileSt
                    | ifSt
    '''

    nodeInstruction = Node("instruction")
    nodeInstruction.insertChild(t[1])
    t[0] = nodeInstruction

def p_empty(t):
     'empty :'
     pass

#====================================================
def p_whileSt(t):
    '''whileSt  : RWHILE PARIZQ exp PARDER block 
    '''
    nodeWhile = Node("whileSt")
    nodeWhile.insertChild(Node("while"))
    nodeWhile.insertChild(Node("("))
    nodeWhile.insertChild(t[3])
    nodeWhile.insertChild(Node(")"))
    nodeWhile.insertChild(t[5])
    t[0] = nodeWhile

def p_ifSt(t):
    ''' ifSt  : RIF PARIZQ exp PARDER block elseSt
    '''
    nodeIf = Node("ifSt")
    nodeIf.insertChild(Node("if"))
    nodeIf.insertChild(Node("("))
    nodeIf.insertChild(t[3])
    nodeIf.insertChild(Node(")"))
    nodeIf.insertChild(t[5])
    t[0] = nodeIf

def p_elseSt(t):
    '''elseSt   : RELSE block
                | ifSt
                | empty
    '''
    if(len(t) == 2):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = Block(t[2])

def p_consoleLog(t):
    '''consoleLog : CONSOLE PUNTO LOG PARIZQ exp PARDER PTCOMA
    '''
    nodeConsoleLog = Node("consoleLog")
    nodeConsoleLog.insertChild(Node("console"))
    nodeConsoleLog.insertChild(Node("."))
    nodeConsoleLog.insertChild(Node("log"))
    nodeConsoleLog.insertChild(Node("("))
    nodeConsoleLog.insertChild(t[5])
    nodeConsoleLog.insertChild(Node(")"))
    nodeConsoleLog.insertChild(Node(";"))
    t[0] = nodeConsoleLog

def p_declaration(t):
    '''declaration  : LET ID DOSPT typeDef decArray IGUAL exp PTCOMA
    '''
    #print(t[5])
    nodeDeclaration = Node("declaration")
    nodeDeclaration.insertChild(Node("let"))
    nodeDeclaration.insertChild(Node(t[2]))
    nodeDeclaration.insertChild(Node(":"))
    nodeDeclaration.insertChild(t[4])

    if(t[5] != None):
        nodeDeclaration.insertChild(t[5])

    nodeDeclaration.insertChild(Node("="))
    nodeDeclaration.insertChild(t[7])
    nodeDeclaration.insertChild(Node(";"))
    t[0] = nodeDeclaration


def p_decArray(t):
    '''decArray : CORIZQ CORDER
                | empty 
    '''
    if(len(t) == 3):
        nodeDecArray = Node("decArray")
        nodeDecArray.insertChild(Node("["))
        nodeDecArray.insertChild(Node("]"))
        t[0] = nodeDecArray
    elif(len(t) == 2):
        t[0] = None

def p_function(t):
    '''function : FUNCTION ID parametersFunc DOSPT typeDef block
    '''
    t[0] = Function(t[2],t[3],t[5],t[6])

def p_parametersFunc(t):
    '''parametersFunc   : PARIZQ parameters PARDER
                        | PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = []

def p_parameters(t):
    '''parameters   : parameters COMA parameter
                    | parameter
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_parameter(t):
    '''parameter    : ID DOSPT typeDef
    '''
    t[0] = Parameter(t[1],t[3])

def p_block(t):
    '''block    : LLAVEIZQ instructions LLAVEDER
                | LLAVEIZQ LLAVEDER
    '''
    nodeBlock = Node("block")
    if(len(t) == 4):
        nodeBlock.insertChild(Node("{"))
        nodeBlock.insertChild(t[2])
        nodeBlock.insertChild(Node("}"))
        t[0] = nodeBlock
    else:
        nodeBlock.insertChild(Node("{"))
        nodeBlock.insertChild(Node("}"))
        t[0] = nodeBlock

def p_callFuncSt(t):
    '''callFuncSt   : ID parametersCallFunc PTCOMA
    '''
    t[0] = CallFuncSt(t[1],t[2])

def p_parametersCallFunc(t):
    '''parametersCallFunc   : PARIZQ listValues PARDER
                            | PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = []

def p_assignment(t):
    '''assignment   : ID IGUAL exp PTCOMA
    '''
    nodeAssign = Node("assigment")
    nodeAssign.insertChild(Node(t[1]))
    nodeAssign.insertChild(Node("="))
    nodeAssign.insertChild(t[3])
    nodeAssign.insertChild(Node(";"))
    t[0] = nodeAssign

#====================================================

def p_listValues(t):
    '''listValues   : listValues COMA exp
                    | exp
    '''
    nodeListValues = Node("listValues")
    if(len(t) == 4):
        nodeListValues.insertChild(t[1])
        nodeListValues.insertChild(Node(","))
        nodeListValues.insertChild(t[3])
        t[0] = nodeListValues
    elif(len(t) == 2):
        nodeListValues.insertChild(t[1])
        t[0] = nodeListValues

def p_typeDef(t):
    '''typeDef  : RSTRING
                | RINT
                | RFLOAT
    '''
    nodeTypeDef = Node("typeDef")
    nodeTypeDef.insertChild(Node(t[1]))
    t[0] = nodeTypeDef

#====================================================
def p_exp_aritmetica(t):
    '''exp  : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp IGUALQUE exp
    '''
    nodeExp = Node("exp")
    nodeExp.insertChild(t[1])
    nodeExp.insertChild(Node(t[2]))
    nodeExp.insertChild(t[3])
    t[0] = nodeExp

def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    nodeExpAgrupacion = Node("exp")
    nodeExpAgrupacion.insertChild(Node("("))
    nodeExpAgrupacion.insertChild(t[2])
    nodeExpAgrupacion.insertChild(Node(")"))
    t[0] = nodeExpAgrupacion

def p_exp_array(t):
    'exp : CORIZQ listValues CORDER'
    nodeExpArray = Node("exp")
    nodeExpArray.insertChild(Node("["))
    nodeExpArray.insertChild(t[2])
    nodeExpArray.insertChild(Node("]"))
    t[0] = nodeExpArray

def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = Node(t[1])

def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = Node(t[1])

def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    t[0] = Node(t[1])

def p_exp_variable(t):
    '''exp  : ID
            | ID listArray
    '''
    nodeExpVariable = Node("exp")
    if(len(t) == 2):
        nodeExpVariable.insertChild(Node(t[1]))
        t[0] = nodeExpVariable
    elif(len(t) == 3):
        nodeExpVariable.insertChild(Node(t[1]))
        nodeExpVariable.insertChild(t[2])
        t[0] = nodeExpVariable

def p_list_array(t):
    '''listArray    : listArray  CORIZQ exp CORDER 
                    | CORIZQ exp CORDER
    '''
    nodeListArray = Node("listArray")
    if(len(t) == 5):
        nodeListArray.insertChild(t[1])
        nodeListArray.insertChild(Node("["))
        nodeListArray.insertChild(t[3])
        nodeListArray.insertChild(Node("]"))
        t[0] = nodeListArray
    elif(len(t) == 4):
        nodeListArray.insertChild(Node("["))
        nodeListArray.insertChild(t[2])
        nodeListArray.insertChild(Node("]"))
        t[0] = nodeListArray

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import Analyzer.ply.yacc as yacc
parser = yacc.yacc()
