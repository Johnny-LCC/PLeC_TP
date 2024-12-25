import ply.lex as lex
import sys

literals = ['(' , ')' , '{' , '}', ';' , ',' , '[' , ']' , '#', '<', '>']

tokens = ('ID','STRING', 'INT', 'FLOAT',
          'ADD','SUB', 'MUL', 'DIV', 'EQ', 'PRINT',
          'ATRIBUICAO', 'TIPO', 'INCLUDE', 'BIBLIO',
           'IF', 'ELSE', 'FOR', 'WHILE', 'RETURN')

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
    r'/(/)?'
    return t

def t_EQ(t):
    r'=='
    return t

def t_ATRIBUICAO(t):
    r'=(?!=)'
    return t

def t_TIPO(t):
    r'String|int|float'
    return t

def t_INCLUDE(t):
    r'include'
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

def t_PRINT(t):
    r'printf'
    return t

def t_BIBLIO(t):
    r'[A-z0-9][A-z0-9_-]*\.h'
    return t

def t_STRING(t):
    r'\"(.*)\"'
    return t

def t_INT(t):
    r'[0-9]+(?!\.)'
    return t

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    return t

def t_ID(t):
    r'[a-z][A-z0-9_]*'
    return t

t_ignore = ' \n\t'

def t_error(t):
    print('Illegal character: ', t.value[0])
    t.lexer.skip(1)

linha = """#include <stdio.h>

int main(){
    a = 5;
    b = 6;
    c = a - b;
    printf("%d", c);
    return 0
}
"""

lexer = lex.lex()

lexer.input(linha) 
for tok in lexer:
    print(tok)