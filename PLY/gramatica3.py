tokens  = (
    'PARIZQ',
    'PARDER',
    'MENOS',
    'DECIMAL',
    'ENTERO',
    'PTCOMA',
    'COMA',
    'UP',
    'DOWN',
    'RIGHT',
    'LEFT'
)

# Tokens
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MENOS     = r'-'
t_PTCOMA    = r';'
t_COMA      = r','
t_UP        = r'u'
t_DOWN      = r'd'
t_RIGHT     = r'r'
t_LEFT      = r'l'

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


# Definición de la gramática=====================================================
def p_s(t):
    '''s : r '''

#====================================================
def p_r(t):
    '''r : pi mov'''

#====================================================
def p_pi(t):
    '''pi : PARIZQ valor COMA valor PARDER'''
    t[0] = [t[2],t[4]]
    print('x: ' + str(t[2]) + ', y: ' + str(t[4]))

#====================================================
def p_valor(t):
    '''valor    : ENTERO
                | MENOS ENTERO
    '''
    if(len(t) == 2):
        t[0] = t[1]
    elif(len(t) == 3):
        t[0] = -t[2]

#====================================================
def p_mov(t):
    '''mov  : mov PTCOMA pos
            | pos
    '''
    if(len(t) == 4):
        t[0] = [ t[1][0] + t[3][0] , t[1][1] + t[3][1] ]
        print('x: ' + str(t[0][0]) + ', y: ' + str(t[0][1]))

    elif(len(t) == 2):
        stack = t[-1]
        print(t[-1])
        t[0] = [ stack[0] + t[1][0] , stack[1] + t[1][1] ]
        print('x: ' + str(t[0][0]) + ', y: ' + str(t[0][1]))

#====================================================
def p_pos(t):
    '''pos  : UP
            | DOWN
            | RIGHT
            | LEFT
    '''
    if t[1] == 'u'  : t[0] = [0,1]
    elif t[1] == 'd': t[0] = [0,-1]
    elif t[1] == 'r': t[0] = [1,0]
    elif t[1] == 'l': t[0] = [-1,0]

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