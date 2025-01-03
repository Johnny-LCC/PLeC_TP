'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.lex as lex
import sys

literals = ['(' , ')' , '{' , '}', ';' , ',' , '[' , ']', '&']

tokens = ('ID','CHAR', 'INT', 'FLOAT',
          'INTT', 'CHART', 'FLOATT', 'VOID',
          'STRING', 'ADD','SUB', 'MUL', 'DIV',
          'EQ', 'NEQ', 'LT', 'LE', 'GT', 'GE',
          'WRITE','READ', 'INCLUDE', 'BIBLIO',
          'IF', 'ELSE', 'FOR', 'WHILE','RETURN',
          'COMENT', 'ATRIBUICAO', 'NOT', 'AND', 'OR')

def t_COMENT(t):
    r'//[^\n]*' #|(/\*(.*)\*/)'
    return t

def t_BIBLIO(t):
    r'<[A-z0-9][A-z0-9_-]*\.h>'
    return t

def t_ADD(t):
    r'\+'
    return t

def t_SUB(t):
    r'-'
    return t

def t_MUL(t):
    r'\*'
    return t

def t_DIV(t):
    r'/'
    return t

def t_EQ(t):
    r'=='
    return t

def t_NEQ(t):
    r'\!='
    return t

def t_NOT(t):
    r'\!(?!=)'
    return t

def t_LT(t):
    r'<'
    return t

def t_GT(t):
    r'>'
    return t

def t_LE(t):
    r'<='
    return t

def t_GE(t):
    r'>='
    return t

def t_AND(t):
    r'&&'
    return t

def t_OR(t):
    r'\|\|'
    return t

def t_ATRIBUICAO(t):
    r'=(?!=)'
    return t

def t_INTT(t):
    r'int'
    return t

def t_CHART(t):
    r'char'
    return t

def t_FLOATT(t):
    r'float'
    return t

def t_VOID(t):
    r'void'
    return t

def t_INCLUDE(t):
    r'\#[ ]?include'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_WRITE(t):
    r'printf'
    return t

def t_READ(t):
    r'scanf'
    return t

def t_CHAR(t):
    r'\"[A-z]\"'
    return t

def t_STRING(t):
    r'\".+\"'
    return t

def t_INT(t):
    r'[0-9]+(?!\.)'
    return t

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_ID(t):
    r'[A-z][A-z0-9_]*'
    return t

t_ignore = ' \n\t'

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
c = open("teste.c", "r")
for linha in c:
    lexer.input(linha) 
    for tok in lexer:
        print(tok)
c.close()
print("Fim (Lexer)")