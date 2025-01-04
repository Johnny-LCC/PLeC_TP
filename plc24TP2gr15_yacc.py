'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.yacc as yacc
import sys

from plc24TP2gr15_lex import tokens


def p_Programa(p):
	"Programa : Imports Funcs"
	
def p_Imports1(p):
	"Imports : Import"

def p_Imports2(p):
	"Imports : Import Imports" 

def p_Import(p):
	"Import : INCLUDE BIBLIO"

def p_Funcs1(p):
	"Funcs : Func"

def p_Funcs2(p):
	"Funcs : Func Funcs"

def p_Func(p):
	"Func : Tipos ID '(' ')' '{' Lines Output '}'"

def p_Tipo1(p):
	"Tipo : INTT"
	parser.aux.append("PUSHI")

def p_Tipo2(p):
	"Tipo : FLOATT"
	parser.aux.append("PUSHF")

def p_Lines1(p):
	"Lines : Line"

def p_Lines2(p):
	"Lines : Line Lines"

def p_Line1(p):
	"Line : Declaration"

def p_Line2(p):
	"Line : Atribuition"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line3(p):
	"Line : DecAt"

def p_Line4(p):
	"Line : Math"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line5(p):
	"Line : Select"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line6(p):
	"Line : Cicle"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line7(p):
	"Line : Read"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line8(p):
	"Line : Write"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line9(p):
	"Line : COMENT"

def p_Declaration(p):
	"Declaration : Tipo VarList ';'"

def p_VarList1(p):
	"VarList : ID"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])

def p_VarList2(p):
	"VarList : ID ',' VarList"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])

def p_Atribuition(p):
	"Atribuition : EqList ATRIBUICAO Expression ';'"
	#parser.mv = parser.mv + f"PUSHG {}"
	#parser.mv = parser.mv + f"STOREG {}"

def p_EqList1(p):
	"EqList : ID"

def p_EqList2(p):
	"EqList : ID ATRIBUICAO EqList"

def p_DecAt1(p):
	"DecAt : Tipo ID ATRIBUICAO Expression';'"
	if p[2] not in parser.reg:
		parser.reg.append(p[2])
	parser.mv = parser.mv + parser.aux.pop() + " 0\n"
	parser.mv = parser.mv + f"PUSHG {parser.reg.index(p[4])}\n"
	parser.mv = parser.mv + f"STOREG {parser.reg.index(p[2])}\n"

def p_Math(p):
	"Math : ID ATRIBUICAO Expression ';'"
	while len(parser.stack) > 0:
		c = parser.stack.pop()
		parser.mv = parser.mv + c

def p_Expression1(p):
	"Expression : Expression ADD Expression"
	parser.stack.append("ADD\n")

def p_Expression2(p):
	"Expression : Expression SUB Expression"
	parser.stack.append("SUB\n")

def p_Expression3(p):
	"Expression : Expression MUL Expression"
	parser.stack.append("MUL\n")

def p_Expression4(p):
	"Expression : Expression DIV Expression"
	parser.stack.append("DIV\n")

def p_Expression5(p):
	"Expression : '(' Expression ')'"

def p_Expression6(p):
	"Expression : ID" #Index
	parser.stack.append(f"PUSHG {parser.reg.index(p[1])}\n")

def p_Expression7(p):
	"Expression : Value"

def p_Expression8(p):
	"Expression : Call"

def p_Value1(p):
	"Value : INT"
	# check

def p_Value2(p):
	"Value : FLOAT"
	# check

def p_Call(p):
	"Call : ID '(' ')' ';'"

def p_Select(p):
	"Select : IF '(' Conditions ')' '{' Lines '}' Else"
	#parser.control = parser.control + 1
	#parser.stack.append("EndIf: \n")
	parser.stack.append("JZ Else\n")

def p_Else1(p):
	"Else : ELSE '{' Lines '}' EndIf"
	aux = parser.stack.pop()
	while aux:
		parser.mv = parser.mv + parser.stack.pop()
	parser.mv = parser.mv + "JUMP EndIf\nElse: \n"

def p_Else2(p):
	"Else : "
	aux = parser.stack.pop()
	while aux:
		parser.mv = parser.mv + parser.stack.pop()
	parser.stack.pop()
	parser.mv = parser.mv + "Else: NOP\n"
	#pass

def p_EndIf(p):
	"EndIf : "
	parser.mv = parser.mv + "EndIf: \n"
	#pass

def p_Cicle1(p):
	"Cicle : WHILE '(' Conditions ')' '{' Lines '}'"
	###

def p_Cicle2(p):
	"Cicle : FOR '(' ID ATRIBUICAO INT ';' Conditions ';' Maths ')' '{' Lines '}'"
	###

def p_Conditions1(p):
	"Conditions : Condition"

def p_Conditions2(p):
	"Conditions : Condition AND Conditions"
	parser.stack.append("AND\n")
           
def p_Conditions3(p):
	"Conditions : Condition OR Conditions"
	parser.stack.append("OR\n")

def p_Condition1(p):
	"Condition : Expression EQ Expression"
	parser.stack.append("EQUAL\n")

def p_Condition2(p):
	"Condition : Expression NEQ Expression" 
	parser.stack.append("NOT\n")
	parser.stack.append("EQUAL\n")

def p_Condition3(p):
	"Condition : Expression LT Expression"
	parser.stack.append("INF\n")

def p_Condition4(p):
	"Condition : Expression LE Expression" 
	parser.stack.append("INFEQ\n")

def p_Condition5(p):
	"Condition : Expression GT Expression" 
	parser.stack.append("SUP\n")

def p_Condition6(p):
	"Condition : Expression GE Expression"
	parser.stack.append("SUPEQ\n")

def p_Condition7(p):
	"Condition : NOT '(' Condition ')'"
	parser.stack.append("NOT\n")

def p_Maths1(p):
	"Maths : Math"

def p_Maths2(p):
	"Maths : Math ',' Maths"

def p_Read(p):
	"Read : READ '(' STRING ',' Addresses ')' ';'"

def p_Addresses1(p):
	"Addresses : Address"

def p_Addresses2(p):
	"Addresses : Address ',' Addresses"

def p_Address(p):
	"Address : '&' ID"

def p_Write1(p):
	"Write : WRITE '(' STRING ')' ';'"
	parser.mv = parser.mv + f"PUSHS {p[3]}\nWRITE\n"

def p_Write2(p):
	"Write : WRITE '(' STRING ',' VarList ')' ';'"

def p_Output(p):
	"Output : RETURN Ret ';'"
	parser.mv = parser.mv + f"STOP\n//Return: {p[2]}\n"

def p_Ret1(p):
	"Ret : ID"

def p_Ret2(p):
	"Ret : Value"

def p_Ret3(p):
	"Ret : "
	pass

def p_error(p):
    print(f"Erro Sintático: {p.value} - Reescreva a frase")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True
parser.reg = []
parser.aux = []
parser.stack = []
parser.control = 0
parser.start = True
parser.mv = ""

fonte = ""

c = open("teste.c", "r")
for linha in c:
    fonte += linha
c.close()
parser.parse(fonte)

with open("mv.txt", "w") as a:
    a.write(parser.mv)

if parser.exito:
	print("Parsing terminou com sucesso.")
if parser.mv:
    print("Código máquina gerado com sucesso.")