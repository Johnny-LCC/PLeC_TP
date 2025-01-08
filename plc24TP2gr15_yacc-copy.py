'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.yacc as yacc
#import sys

from plc24TP2gr15_lex import tokens

def p_Programa(p):
	"Programa : Imports Funcs"
	print("Programa")
	
def p_Imports1(p):
	"Imports : Import"
	print("Imports1")

def p_Imports2(p):
	"Imports : Import Imports"
	print("Imports2") 

def p_Import(p):
	"Import : INCLUDE BIBLIO"
	print("Import")

def p_Funcs1(p):
	"Funcs : Func"
	print("Funcs1")

def p_Funcs2(p):
	"Funcs : Func Funcs"
	print("Funcs2")

def p_Func(p):
	"Func : Tipo ID '(' ')' '{' Declarations Lines Output '}'"
	print("Func: ", p[1])

def p_Tipo1(p):
	"Tipo : INTT"
	print("Tipo1")

def p_Tipo2(p):
	"Tipo : FLOATT"
	print("Tipo2")

def p_Declarations1(p):
	"Declarations : Declaration"
	print("Declarations1")

def p_Declarations2(p):
	"Declarations : Declaration Declarations"
	print("Declarations2")

def p_Declaration1(p):
	"Declaration : Tipo VarList ';'"
	print("Declaration1")

def p_Declaration2(p):
	"Declaration : Tipo ID ATRIBUICAO Expression ';'"
	print("Declaration2: ", p[2])

def p_VarList1(p):
	"VarList : ID "
	print("VarList1: ", p[1])	

def p_VarList2(p):
	"VarList : ID ',' VarList"
	print("VarList2: ", p[1])

def p_Expression1(p):
	"Expression : Expression ADD Expression"
	print("Expression1 (+)")

def p_Expression2(p):
	"Expression : Expression SUB Expression"
	print("Expression2 (-)")	

def p_Expression3(p):
	"Expression : Expression MUL Expression"
	print("Expression3 (*)")	

def p_Expression4(p):
	"Expression : Expression DIV Expression"
	print("Expression4 (/)")	

def p_Expression5(p):
	"Expression : '(' Expression ')'"
	print("Expression5")

def p_Expression6(p):
	"Expression : ID"
	print("Expression6: ", p[1])	

def p_Expression7(p):
	"Expression : Value"
	print("Expression7 (Value)")

def p_Expression8(p):
	"Expression : Call"
	print("Expression8 (Call)")

def p_Value1(p):
	"Value : INT"
	print("Value1: ", p[1])

def p_Value2(p):
	"Value : FLOAT"
	print("Value2: ", p[1])	

def p_Call(p):
	"Call : ID '(' ')'"
	print("Call: ", p[1])

def p_Lines1(p):
	"Lines : Line"
	print("Lines1")

def p_Lines2(p):
	"Lines : Line Lines"
	print("Lines2")

def p_Line1(p):
	"Line : Atribuition"
	print("Line1 - Atribuition")

'''def p_Line2(p):
	"Line : Math"
	print("Line4 - Math")'''

def p_Line2(p):
	"Line : Select"
	print("Line2 - Select")

def p_Line3(p):
	"Line : Cicle"
	print("Line3 - Cicle")

def p_Line4(p):
	"Line : Read"
	print("Line4 - Read")

def p_Line5(p):
	"Line : Write"
	print("Line5 - Write")

def p_Line6(p):
	"Line : COMENT"
	print("Line6 - COMENT")
	
def p_Atribuition(p):
	"Atribuition : EqList ATRIBUICAO Expression ';'"
	print("Atribuition")

def p_EqList1(p):
	"EqList : ID "
	print("EqList1: ", p[1])

def p_EqList2(p):
	"EqList : ID ATRIBUICAO EqList"
	print("EqList2: ", p[1])

'''def p_Math(p):
	"Math : ID ATRIBUICAO Expression ';'"
	print("Math: ", p[1])'''

def p_Select(p):
	"Select : IF '(' Conditions ')' '{' Lines '}' Else"
	print("Select")

def p_Else1(p):
	"Else : ELSE '{' Lines '}'"
	print("Else1")

def p_Else2(p):
	"Else : "
	print("Else2")
	pass

def p_Cicle1(p):
	"Cicle : WHILE '(' Conditions ')' '{' Lines '}'"
	print("Cicle1")	

def p_Cicle2(p):
	"Cicle : FOR '(' ID ATRIBUICAO INT ';' Conditions ';' Maths ')' '{' Lines '}'"
	print("Cicle2")	

def p_Conditions1(p):
	"Conditions : Condition"
	print("Conditions1")

def p_Conditions2(p):
	"Conditions : Condition AND Conditions"
	print("Conditions2 - AND")
           
def p_Conditions3(p):
	"Conditions : Condition OR Conditions"
	print("Conditions3 - OR")

def p_Condition1(p):
	"Condition : Expression EQ Expression"
	print("Condition1 - EQ")	

def p_Condition2(p):
	"Condition : Expression NEQ Expression"
	print("Condition2 - NEQ") 	

def p_Condition3(p):
	"Condition : Expression LT Expression"
	print("Condition3 - LT")	

def p_Condition4(p):
	"Condition : Expression LE Expression"
	print("Condition4 - LE") 	

def p_Condition5(p):
	"Condition : Expression GT Expression"
	print("Condition5 - GT") 	

def p_Condition6(p):
	"Condition : Expression GE Expression"
	print("Condition6 - GE")	

def p_Condition7(p):
	"Condition : NOT '(' Condition ')'"
	print("Condition7 - NOT")	

def p_Maths1(p):
	"Maths : Atribuition"
	print("Maths1")

def p_Maths2(p):
	"Maths : Atribuition ',' Maths"
	print("Maths2")

def p_Read(p):
	"Read : READ '(' STRING ',' Addresses ')' ';'"
	print("Read")

def p_Addresses1(p):
	"Addresses : Address"
	print("Addresses1")

def p_Addresses2(p):
	"Addresses : Address ',' Addresses"
	print("Addresses2")

def p_Address(p):
	"Address : '&' ID"
	print("Address: &", p[2])

def p_Write1(p):
	"Write : WRITE '(' STRING ')' ';'"
	print("Write1: ",p[3])

def p_Write2(p):
	"Write : WRITE '(' STRING ',' VarList ')' ';'"
	print("Write2",p[3])

def p_Output(p):
	"Output : RETURN Ret ';'"
	print("Output")

def p_Ret1(p):
	"Ret : ID"
	print("Ret1")

def p_Ret2(p):
	"Ret : Value"
	print("Ret2")

def p_Ret3(p):
	"Ret : "
	print("Ret3")
	pass

def p_error(p):
    if p:
        print(f"ERRO SINTÁTICO perto do token '{p.value}'")
    else:
        print("ERRO SINTÁTICO: token inesperado")
    parser.exito = False


parser = yacc.yacc()
parser.exito = True

fonte = ""
c = open("teste1.c", "r")
for linha in c:
    fonte += linha
c.close()

parser.parse(fonte)

if parser.exito:
	print("PARSER TERMINOU COM SUCESSO")