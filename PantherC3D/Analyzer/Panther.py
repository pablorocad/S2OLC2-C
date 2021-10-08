reservadas = {
    'int' : 'RINT',
    'float' : 'RFLOAT',
    'string' : 'RSTRING',
    'boolean' : 'RBOOLEAN',
    'console' : 'CONSOLE',
    'log' : 'LOG',
    'let' : 'LET',
    'while': 'RWHILE'
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
    'IGUAL',
    'DOSPT',
        'ID',
    'LLAVEDER',
    'LLAVEIZQ'
 ] + list(reservadas.values())

#Tokens
t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_LLAVEIZQ          = r'\{'
t_LLAVEDER          = r'\}'
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
from Expression.Relational.Menor import Menor
from Instructions.ConsoleLog import ConsoleLog
from Expression.Primitive.NumberVal import NumberVal
from Expression.Arithmetic.Plus import Plus
from Expression.Arithmetic.Minus import Minus
from Expression.Arithmetic.Multiply import Multiply
from Expression.Arithmetic.Division import Division
from Environment.Environment import Environment
from Enum.typeExpression import typeExpression
from Generator.Generator import Generator
from Expression.Relational.Equal import Equal
from Instructions.Declaration import Declaration
from Expression.Primitive.VariableCall import VariableCall
from Instructions.While import While

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

    generator: Generator = Generator()
    globalEnv = Environment(None)
    for ins in t[1]:
        ins.generator = generator
        ins.compile(globalEnv)

    
    t[0] = generator.getCode()

    #print(globalEnv.function)

#====================================================
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if(len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

#====================================================
def p_instruction(t):
    '''instruction  : consoleLog
                    | declaration
                    | whileSt
    '''
    t[0] = t[1]

#====================================================
def p_block(t):
    '''block    : LLAVEIZQ instructions LLAVEDER
                | LLAVEIZQ LLAVEDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    else:
        t[0] = []

def p_whileSt(t):
    '''whileSt  : RWHILE PARIZQ exp PARDER block 
    '''
    t[0] = While(t[3],t[5])

def p_consoleLog(t):
    '''consoleLog : CONSOLE PUNTO LOG PARIZQ exp PARDER PTCOMA
    '''
    t[0] = ConsoleLog(t[5])

def p_declaration(t):
    '''declaration  : LET ID DOSPT typeDef IGUAL exp PTCOMA
    '''
    #print(t[5])
    t[0] = Declaration(t[2],t[6],t[4])

#====================================================

def p_typeDef(t):
    '''typeDef  : RSTRING
                | RINT
                | RFLOAT
                | RBOOLEAN
    '''
    if t[1] == 'string' : t[0] = typeExpression.STRING
    elif t[1] == 'int' : t[0] = typeExpression.INTEGER
    elif t[1] == 'float' : t[0] = typeExpression.FLOAT
    elif t[1] == 'boolean' : t[0] = typeExpression.BOOL

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
    if t[2] == '+'  : t[0] = Plus(t[1],t[3])
    elif t[2] == '-': t[0] = Minus(t[1],t[3])
    elif t[2] == '*': t[0] = Multiply(t[1],t[3])
    elif t[2] == '/': t[0] = Division(t[1],t[3])
    # elif t[2] == '>': t[0] = Relational(t[1],t[3],relationalOperation.MAYOR)
    elif t[2] == '<': t[0] = Menor(t[1],t[3])
    elif t[2] == '==': t[0] = Equal(t[1],t[3])

def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    t[0] = t[2]

def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = NumberVal(typeExpression.INTEGER,t[1])

def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = NumberVal(typeExpression.FLOAT,t[1])

def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    t[0] = None

def p_exp_variable(t):
    '''exp  : ID
    '''
    t[0] = VariableCall(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import Analyzer.ply.yacc as yacc
parser = yacc.yacc()
