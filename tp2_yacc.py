'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.yacc as yacc
import sys

from tp2_lex import tokens

def p_tp2_grammar(p):
    """
    Program : Includes Declarations Statements
    Includes : Include Includes
            | Include
    Include : INCLUDE BIBLIO
    Declarations : Declaration Declarations
                 | Declaration
    Declaration : TIPO VarList ';'
    VarList : ID
            | VarList ',' ID
    Statements : Statement
               | Statements Statement
    Statement : ID ATRIBUICAO Expression ';'   
              | WRITE '(' Expression ')' ';'
              | WRITE '(' STRING ')' ';'
              | IF '(' Condition ')' '{' Statements '}' ELSE '{' Statements '}'
              | IF '(' Condition ')' '{' Statements '}'
              | WHILE '(' Condition ')' '{' Statements '}'
              | FOR '(' ID ATRIBUICAO Expression ';' Condition ';' Expression ')' '{' Statements '}'
              | RETURN Expression ';'
    Expression : Expression ADD Expression
               | Expression SUB Expression
               | Expression MUL Expression
               | Expression DIV Expression
               | '(' Expression ')'
               | ID
               | INT
               | FLOAT
               | CHAR
    Condition : Expression EQ Expression
              | Expression NEQ Expression
              | Expression LT Expression
              | Expression LE Expression
              | Expression GT Expression
              | Expression GE Expression
              | '(' Condition ')'
              | Condition AND Condition
              | Condition OR Condition
              | NOT Condition
    """

def p_error(p):
    print("Erro Sintático! Reescreva a frase!")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True

fonte = ""
c = open("teste.c", "r")
for linha in c:
    fonte += linha
c.close()
if parser.exito:
    print("Parsing terminou com sucesso.")