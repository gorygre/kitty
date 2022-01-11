import subprocess
import time

import lexer
import yacc
import helpers

tokens = lexer.tokens
variables = {}
def default_send(keys):
    command = ['vbm', 'send', variables['vm'], '-s', keys]
    print('running [%s]' % ('vbm send %s -s %s' % (variables['vm'], keys)))
    subprocess.call(command)

send_keys = default_send

def p_list_1(p):
    '''list : list item'''
    pass

def p_list_2(p):
    '''list : item'''
    pass

# send the keys
def p_item_1(p):
    '''item : STRING'''
    send_keys(p[1])

# subprocess the command string
def p_item_2(p):
    '''item : "$" "(" STRING ")"'''
    print('running [%s]' % str(p[3]))
    command = str(p[3])[1:-1].split(' ')
    subprocess.call(command)

def p_item_3(p):
    '''item : "$" "{" statement "}"'''
    pass

def p_item_4(p):
    '''item : COMMENT'''
    pass

# assignment
def p_statement_1(p):
    '''statement : VARIABLE "=" STRING'''
    variables[p[1]] = p[3][1:-1]

# function
def p_statement_2(p):
    '''statement : function "(" argument_list ")"'''
    p[1](*p[3])

def p_statement_3(p):
    '''statement : COMMENT'''
    pass

# append arguments
def p_argument_list_1(p):
    '''argument_list : argument_list "," argument'''
    p[0] = p[1] + [p[3]]

def p_argument_list_2(p):
    '''argument_list : argument'''
    p[0] = [p[1]]

def p_argument_1(p):
    '''argument : STRING'''
    p[0] = str(p[1])

def p_argument_2(p):
    '''argument : FLOAT'''
    p[0] = float(p[1])

def p_function_1(p):
    '''function : SLEEP'''
    p[0] = helpers.meow_sleep

def p_error(p):
    print(p)
    if p:
        print("Syntax error at '%s'" % p.value)
	exit(1)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
