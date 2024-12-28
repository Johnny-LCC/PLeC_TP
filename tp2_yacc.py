import ply.yacc as yacc
import sys

from tp2_lex import tokens

def p_tp2_grammar(p):
    """
    program : includes declarations statements
includes : include includes
         | include
include : INCLUDE BIBLIO
declarations : declaration declarations
             | declaration
declaration : TIPO var_list ';'
var_list : ID
         | var_list ',' ID
statements : statement
           | statements statement
statement : ID ATRIBUICAO expression ';'
          | WRITE '(' expression ')' ';'
          | WRITE '(' STRING ')' ';'
          | IF '(' condition ')' '{' statements '}' ELSE '{' statements '}'
          | IF '(' condition ')' '{' statements '}'
          | WHILE '(' condition ')' '{' statements '}'
          | FOR '(' ID ATRIBUICAO expression ';' condition ';' expression ')' '{' statements '}'
          | RETURN expression ';'
expression : expression ADD expression
           | expression SUB expression
           | expression MUL expression
           | expression DIV expression
           | '(' expression ')'
           | ID
           | INT
           | FLOAT
           | CHAR
condition : expression EQ expression
          | expression NEQ expression
          | expression LT expression
          | expression LE expression
          | expression GT expression
          | expression GE expression
          | '(' condition ')'
          | condition AND condition
          | condition OR condition
          | NOT condition
    """

def p_error(p):
    print("Erro Sintático! Reescreva a frase!")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True

fonte = ""
for linha in sys.stdin:
    fonte += linha

if parser.exito:
    print("Parsing terminou com sucesso.")