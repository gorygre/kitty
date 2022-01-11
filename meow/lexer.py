import lex

tokens = ('COMMENT', 'SLEEP', 'STRING', 'FLOAT', 'VARIABLE')
literals = ['$', '{', '}', '(', ')', ',', '=']

# tokens are added by order in lexer file only if they are defined as functions
# if they are regex's then they are ordered by decreasing length of the regex
def t_COMMENT(t):
    r'\#.*'
    return t

def t_SLEEP(t):
    r'sleep'
    return t

def t_STRING(t):
    r'\'.*\''
    return t

def t_FLOAT(t):
    r'[0-9]+(\.[0-9]+)?'
    return t

def t_VARIABLE(t):
    r'[A-Za-z]+[A-Za-z0-9]*(\.[A-Za-z]*[A-Za-z0-9]*)*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

t_ignore = ' \t'

lex.lex()
