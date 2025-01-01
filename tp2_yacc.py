'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.yacc as yacc
import sys

from tp2_lex import tokens

def p_Program(p):
	"Program : Includes Declarations Statements"

def p_Includes1(p):
	"Includes : Include"

def p_Includes2(p):
	"Includes : Include Includes"

def p_Include(p):
	"Include : INCLUDE BIBLIO"

def p_Declarations1(p):
	"Declarations : Declaration"

def p_Declarations2(p):
	"Declarations : Declaration Declarations"

def p_Declaration(p):
	"Declaration : TIPO VarList ';'"

def p_VarList1(p):
	"VarList : ID"

def p_VarList2(p):
	"VarList : VarList ',' ID"

def p_Statements1(p):
	"Statements : Statement"

def p_Statements2(p):
	"Statements : Statement Statements"

def p_Statement1(p):
	"Statement : ID ATRIBUICAO Expression ';'"
	
def p_Statement2(p):
	"Statement : WRITE '(' Expression ')' ';'"

def p_Statement3(p):
	"Statement : WRITE '(' STRING ')' ';'"
	
def p_Statement3(p):
    "Statement : IF '(' Condition ')' '{' Statements '}'"

def p_Statement4(p):
	"Statement : IF '(' Condition ')' '{' Statements '}' ELSE '{' Statements '}'"

def p_Statement5(p):
    "Statement : WHILE '(' Condition ')' '{' Statements '}'"

def p_Statement6(p):
    "Statement : FOR '(' ID ATRIBUICAO Expression ';' Condition ';' Expression ')' '{' Statements '}'"

def p_Statement7(p):
    "Statement : RETURN Expression ';'"

def p_Expression1(p):
	"Expression : Expression Operator Expression"

def p_Expression2(p):
	"Expression : '(' Expression ')'"

def p_Expression3(p):
	"Expression : ID"
	
def p_Expression4(p):
	"Expression : INT"
	
def p_Expression5(p):
	"Expression : FLOAT"

def p_Operator1(p):
	"Operator : ADD"
	
def p_Operator2(p):
    "Operator : SUB"
	
def p_Operator3(p):
	"Operator : MUL"
	
def p_Operator4(p):
	"Operator : DIV"

def p_Condition1(p):
	"Condition : Expression EQ Expression"

def p_Condition2(p):
	"Condition : Expression NEQ Expression"

def p_Condition3(p):
	"Condition : Expression LT Expression"

def p_Condition4(p):
	"Condition : Expression LE Expression"
	
def p_Condition5(p):
	"Condition : Expression GT Expression"

def p_Condition6(p):
	"Condition : Expression GE Expression"

def p_Condition7(p):
	"Condition : '(' Condition ')'"

def p_Condition8(p):
	"Condition : Condition AND Condition"

def p_Condition9(p):
	"Condition : Condition OR Condition"

def p_Condition10(p):
	"Condition : NOT Condition"

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