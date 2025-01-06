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
	"Func : Tipo ID '(' ')' '{' Declarations Lines Output '}'"

def p_Tipo1(p):
	"Tipo : INTT"
	parser.stack.append("PUSHI")

def p_Tipo2(p):
	"Tipo : FLOATT"
	parser.stack.append("PUSHF")

def p_Declarations1(p):
	"Declarations : Declaration"
	parser.mv = parser.mv + "START\n"

def p_Declarations2(p):
	"Declarations : Declaration Declarations"

def p_Declaration1(p):
	"Declaration : Tipo VarList ';'"
	parser.stack.pop()

def p_Declaration2(p):
	"Declaration : Tipo ID ATRIBUICAO Expression ';'"
	if p[2] not in parser.reg:
		parser.reg.append(p[2])
	else:
		parser.mv = parser.mv + "ERR \"Variável já declarada\"\n"

def p_VarList1(p):
	"VarList : ID "
	if p[1] not in parser.reg:
		parser.reg.append(p[1])
		t = parser.stack[-1]
		parser.mv = parser.mv + f"{t} 0 //{p[1]}\n"
	else:
		parser.mv = parser.mv + "ERR \"Variável já declarada\"\n"

def p_VarList2(p):
	"VarList : ID ',' VarList"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])
		t = parser.stack[-1]
		parser.mv = parser.mv + f"{t} 0 //{p[1]}\n"
	else:
		parser.mv = parser.mv + "ERR \"Variável já declarada\"\n"

def p_Expression1(p):
	"Expression : Expression ADD Expression"
	parser.mv = parser.mv + "ADD\n"

def p_Expression2(p):
	"Expression : Expression SUB Expression"
	parser.mv = parser.mv + "SUB\n"

def p_Expression3(p):
	"Expression : Expression MUL Expression"
	parser.mv = parser.mv + "MUL\n"

def p_Expression4(p):
	"Expression : Expression DIV Expression"
	parser.mv = parser.mv + "DIV\n"

def p_Expression5(p):
	"Expression : '(' Expression ')'"

def p_Expression6(p):
	"Expression : ID"
	parser.mv = parser.mv + f"PUSHG {parser.reg.index(p[1])}\n"

def p_Expression7(p):
	"Expression : Value"

def p_Expression8(p):
	"Expression : Call"

def p_Value1(p):
	"Value : INT"
	t = parser.stack.pop()
	if t == "PUSHI":
		parser.mv = parser.mv + f"{t} {p[1]}"
	else:
		parser.mv = parser.mv + "ERR \"Erro com os tipos (1)\"\n"

def p_Value2(p):
	"Value : FLOAT"
	t = parser.stack.pop()
	if t == "PUSHF":
		parser.mv = parser.mv + f"{t} {p[1]}"
	else:
		parser.mv = parser.mv + "ERR \"Erro com os tipos (2)\"\n"

def p_Call(p):
	"Call : ID '(' ')'"
	parser.mv = parser.mv + f"JUMP {p[1]}" ###

def p_Lines1(p):
	"Lines : Line"
	#

def p_Lines2(p):
	"Lines : Line Lines"
	#

def p_Line1(p):
	"Line : Atribuition"
	#

def p_Line2(p):
	"Line : Math"
	#

def p_Line3(p):
	"Line : Select"
	parser.mv = parser.mv + f"EndIf{parser.s}: \n"
	parser.s = parser.s - 1

def p_Line4(p):
	"Line : Cicle"
	parser.mv = parser.mv + f"EndIf{parser.c}: \n"
	parser.c = parser.c - 1

def p_Line5(p):
	"Line : Read"
	#

def p_Line6(p):
	"Line : Write"
	#

def p_Line7(p):
	"Line : COMENT"
	parser.mv = parser.mv + f"{p[1]}" ###
	
def p_Atribuition(p):
	"Atribuition : EqList ATRIBUICAO Expression ';'"
	#

def p_EqList1(p):
	"EqList : ID "
	#

def p_EqList2(p):
	"EqList : ID ATRIBUICAO EqList"
	#

def p_Math(p):
	"Math : ID ATRIBUICAO Expression ';'"
	parser.mv = parser.mv + f"STOREG {parser.reg.index(p[1])}\n" ###

def p_Select(p):
	"Select : IF '(' Conditions ')' '{' Lines '}' Else"
	#

def p_Else1(p):
	"Else : ELSE '{' Lines '}'"
	#

def p_Else2(p):
	"Else : "
	#
	pass

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
	parser.mv = parser.mv + "AND\n"
           
def p_Conditions3(p):
	"Conditions : Condition OR Conditions"
	parser.mv = parser.mv + "OR\n"

def p_Condition1(p):
	"Condition : Expression EQ Expression"
	parser.mv = parser.mv + "EQ\n"

def p_Condition2(p):
	"Condition : Expression NEQ Expression"
	parser.mv = parser.mv + "EQ\nNOT\n"

def p_Condition3(p):
	"Condition : Expression LT Expression"
	parser.mv = parser.mv + "INF\n"

def p_Condition4(p):
	"Condition : Expression LE Expression"
	parser.mv = parser.mv + "INFEQ\n"

def p_Condition5(p):
	"Condition : Expression GT Expression"
	parser.mv = parser.mv + "SUP\n"

def p_Condition6(p):
	"Condition : Expression GE Expression"
	parser.mv = parser.mv + "SUPEQ\n"

def p_Condition7(p):
	"Condition : NOT '(' Condition ')'"
	parser.mv = parser.mv + "NOT\n"

def p_Maths1(p):
	"Maths : Math"
	#

def p_Maths2(p):
	"Maths : Math ',' Maths"
	#

def p_Read(p):
	"Read : READ '(' STRING ',' Addresses ')' ';'"
	###

def p_Addresses1(p):
	"Addresses : Address"
	###

def p_Addresses2(p):
	"Addresses : Address ',' Addresses"
	###

def p_Address(p):
	"Address : '&' ID"
	###

def p_Write1(p):
	"Write : WRITE '(' STRING ')' ';'"
	parser.mv = parser.mv + f"PUSHS {p[3]}\nWRITE\n"

def p_Write2(p):
	"Write : WRITE '(' STRING ',' VarList ')' ';'"
	###

def p_Output(p):
	"Output : RETURN Ret ';'"
	parser.mv = parser.mv + f"STOP"

def p_Ret1(p):
	"Ret : ID"
	parser.mv = parser.mv + f"PUSHG {parser.reg.index(p[1])}\n"

def p_Ret2(p):
	"Ret : Value"
	v = parser.stack.pop()
	parser.mv = parser.mv + f"PUSHI {v}\n"

def p_Ret3(p):
	"Ret : "
	pass

def p_error(p):
    print(f"Erro Sintático: {p.value} - Reescreva a frase")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True
parser.reg = []
parser.stack = []
parser.s = parser.c = 0
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
'''if parser.mv:
    print("Código máquina gerado com sucesso.")'''