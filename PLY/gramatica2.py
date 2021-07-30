tokens  = (
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'ENTERO',
)

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'

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

# Caracteres ignorados
t_ignore = " \t"
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )


# Definición de la gramática=====================================================
def p_inicio(t):
    '''inicio : suma '''
    print(t[1])

#====================================================
def p_suma(t):
    '''suma : suma MAS suma
            | suma MENOS suma
            | mult
    '''
    if (len(t) == 4):
        if t[2] == '+'  : t[0] = t[1] + t[3]
        elif t[2] == '-': t[0] = t[1] - t[3]
    elif (len(t) == 2):
        t[0] = t[1]

#====================================================
def p_mult(t):
    '''mult : mult POR mult
            | mult DIVIDIDO mult
            | valor
    '''
    if (len(t) == 4):
        if t[2] == '*'  : t[0] = t[1] * t[3]
        elif t[2] == '/': t[0] = t[1] / t[3]
    elif (len(t) == 2):
        t[0] = t[1]

#====================================================
def p_valor(t):
    '''valor    : ENTERO
                | DECIMAL
                | MENOS suma %prec UMENOS
                | PARIZQ suma PARDER
    '''
    if (len(t) == 2):
        t[0] = t[1]
    elif (len(t) == 3):
        t[0] = -t[2]
    elif (len(t) == 4):
        t[0] = t[2]
#====================================================

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

#====================================================
#====================================================
#====================================================

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entrada.txt", "r")
input = f.read()
print(input)
parser.parse(input)