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
	"Func : Tipos ID '(' Params ')' '{' Lines Output '}'"

def p_Tipos1(p):
	"Tipos : Tipo"

def p_Tipos2(p):
	"Tipos : VOID"

def p_Tipo1(p):
	"Tipo : INTT"
	parser.aux.append["PUSHI"]

def p_Tipo2(p):
	"Tipo : CHART"
	parser.aux.append["PUSHS"]

def p_Tipo3(p):
	"Tipo : FLAOTT"
	parser.aux.append["PUSHF"]

def p_Params1(p):
	"Params : Param"

def p_Params2(p):
	"Params : Param ',' Params"

def p_Param1(p):
	"Param : Tipo ID"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])

def p_Param1(p):
	"Param : "

def p_Lines1(p):
	"Lines : Line ';'"

def p_Lines2(p):
	"Lines : Line ';' Lines"

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
	"Line : Call"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line6(p):
	"Line : Select"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line7(p):
	"Line : Cicle"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line8(p):
	"Line : Read"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line(p):
	"Line : Write"
	if parser.start:
		parser.mv = parser.mv + "START\n"
		parser.start = False

def p_Line(p):
	"Line : COMENT"

def p_Declaration(p):
	"Declaration : Tipo VarList"

def p_VarList1(p):
	"VarList : ID Index"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])

def p_VarList2(p):
	"VarList : ID Index ',' VarList"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])

def p_Index1(p):
	"Index : '[' INT ']'"
	parser.mv = parser.mv + "PUSHN 0\n"

def p_Index2(p):
	"Index : " 
	parser.mv = parser.mv + f"{parser.aux[0]} 0\n"
	parser.aux.pop()

def p_Atribuition1(p):
	"Atribuition : EqList '=' ID Index"
	#parser.mv = parser.mv + f"PUSHG {}"
	#parser.mv = parser.mv + f"STOREG {}"

def p_Atribuition2(p):
	"Atribuition : EqList '=' Value"
	#parser.mv = parser.mv + f"PUSHI {}" ...
	#parser.mv = parser.mv + f"STOREG {}"

def p_EqList1(p):
	"EqList : ID Index"

def p_EqList2(p):
	"EqList : ID Index '=' EqList"

def p_DecAt1(p):
	"DecAt : Tipo ID '=' ID Index"
	# pushi 0
	# pushg index(ID0)
	# storeg index(ID1)

def p_DecAt2(p):
	"DecAt : Tipo ID '=' Value"
	#
	# 

def p_Values1(p):
	"Values : Value"

def p_Values1(p):
	"Values : Value ',' Values"

def p_Value1(p):
	"Value : INT"

def p_Value2(p):
	"Value : FLOAT"

def p_Value3(p):
	"Value : CHAR"

def p_Value4(p):
	"Value : Array"

def p_Array(p):
	"Array : '{' Values '}'"

def p_Math(p):
	"Math : ID '=' Expression"
	'''
	while len(parser.math) > 0:
		c = parser.math.pop()
		parser.mv = parser.mv + c
	'''

def p_Expression1(p):
	"Expression : Expression ADD Expression"
	parser.math.append("ADD\n")

def p_Expression2(p):
	"Expression : Expression SUB Expression"
	parser.math.append("SUB\n")

def p_Expression3(p):
	"Expression : Expression MUL Expression"
	parser.math.append("MUL\n")

def p_Expression4(p):
	"Expression : Expression DIV Expression"
	parser.math.append("DIV\n")

def p_Expression5(p):
	"Expression : '(' Expression ')'"

def p_Expression6(p):
	"Expression : ID"
	parser.math.append(f"PUSHG {parser.reg.index(p[1])}\n")

def p_Expression7(p):
	"Expression : INT"
	parser.math.append(f"PUSHI {p[1]}\n")

def p_Expression8(p):
	"Expression : FLOAT"
	parser.math.append(f"PUSHF {p[1]}\n")

def p_Call(p):
	"Call : ID '(' Inputs ')'"

def p_Inputs1(p):
	"Inputs : Input"

def p_Inputs2(p):
	"Inputs : Input ',' Inputs"

def p_Input1(p):
	"Input : ID Index"

def p_Input2(p):
	"Input : Value"

def p_Select1(p):
	"Select : IF '(' Conditions ')' '{' Lines '}' "

def p_Select2(p):
	"Select : IF '(' Conditions ')' '{' Lines '}' ELSE '{' Lines '}'"

def p_Cicle1(p):
	"Cicle : WHILE '(' Conditions ')' '{' Lines '}'"

def p_Cicle2(p):
	"Cicle : FOR '(' ID ATRIBUICAO INT ';' Conditions ';' Maths ')' '{' Lines '}'"

def p_Conditions1(p):
	"Conditions : Condition"

def p_Conditions2(p):
	"Conditions : Condition AND '(' Conditions ')'"
	parser.math.append("AND\n")
           
def p_Conditions3(p):
	"Conditions : Condition OR '(' Conditions ')'"
	parser.math.append("OR\n")

def p_Condition1(p):
	"Condition : Expression EQ Expression"
	parser.math.append("EQUAL\n")

def p_Condition2(p):
	"Condition : Expression NEQ Expression" 
	parser.math.append("NOT\n")
	parser.math.append("EQUAL\n")

def p_Condition3(p):
	"Condition : Expression LT Expression"
	parser.math.append("INF\n")

def p_Condition4(p):
	"Condition : Expression LE Expression" 
	parser.math.append("INFEQ\n")

def p_Condition5(p):
	"Condition : Expression GT Expression" 
	parser.math.append("SUP\n")

def p_Condition6(p):
	"Condition : Expression GE Expression"
	parser.math.append("SUPEQ\n")

def p_Condition7(p):
	"Condition : NOT Condition"
	parser.math.append("NOT\n")

def p_Maths1(p):
	"Maths : Math"

def p_Maths2(p):
	"Maths : Math ',' Maths"

def p_Read(p):
	"Read : READ '(' STRING ',' Addresses ')'"

def p_Addresses1(p):
	"Addresses : Address"

def p_Addresses2(p):
	"Addresses : Address ',' Addresses"

def p_Address(p):
	"Address : '&' ID"

def p_Write1(p):
	"Write : WRITE '(' STRING ')'"

def p_Write2(p):
	"Write : WRITE '(' STRING ',' Values ')'"

def p_Output(p):
	"Output : RETURN Ret"
	parser.mv = parser.mv + "STOP"

def p_Ret1(p):
	"Ret : ID Index"

def p_Ret2(p):
	"Ret : Value"

def p_Ret3(p):
	"Ret : "

def p_error(p):
    print("Erro Sintático! Reescreva a frase!")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True
parser.reg = []
parser.aux = []
parser.math = []
parser.start = True
parser.mv = ""

fonte = ""

c = open("teste.c", "r")

for linha in c:
    fonte += linha

c.close()

a = open("mv.txt", "w")
a.write(parser.mv)
#a.write("//Fim")
a.close

if parser.exito:
    print("Parsing terminou com sucesso.")