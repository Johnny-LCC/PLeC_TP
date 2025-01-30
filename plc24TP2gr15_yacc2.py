'''
Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''

import ply.yacc as yacc

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
	o = parser.aux.pop()
	l = parser.aux.pop()
	d = parser.aux.pop()
	f = f"{p[2]}:\n"
	if p[2] == "main":
		o = o.replace("RETURN", "STOP")
		f = f+d+l+o
	else:
		f = f+l+o
	#parser.aux.append(f)
	parser.mv = parser.mv + f
	parser.aux.clear()

def p_Tipo(p):
	"Tipo : INTT"
	parser.type.append("PUSHI")

def p_Declarations1(p):
	"Declarations : "
	s = ""
	for c in parser.aux:
		s = s + c
	s = s + "START\n"
	parser.aux = []
	parser.aux.append(s)
	parser.aux.append("AUX")
	pass

def p_Declarations2(p):
	"Declarations : Declaration Declarations"

def p_Declaration1(p):
	"Declaration : Tipo VarList ';'"
	parser.type.pop()

def p_Declaration2(p):
	"Declaration : Tipo ID ATRIBUICAO Expression ';'"
	parser.type.pop()
	if p[2] not in parser.reg:
		parser.reg.append(p[2])
	else:
		parser.aux.append(f"ERR \"Variável {p[1]} já declarada\"\n")

def p_VarList1(p):
	"VarList : ID "
	if p[1] not in parser.reg:
		parser.reg.append(p[1])
		t = parser.type[-1]
		parser.aux.append(f"{t} 0 //{p[1]}\n")
	else:
		parser.aux.append(f"ERR \"Variável {p[1]} já declarada\"\n")

def p_VarList2(p):
	"VarList : ID ',' VarList"
	if p[1] not in parser.reg:
		parser.reg.append(p[1])
		t = parser.type[-1]
		parser.aux.append(f"{t} 0 //{p[1]}\n")
	else:
		parser.aux.append(f"ERR \"Variável {p[1]} já declarada\"\n")

def p_Expression1(p):
	"Expression : Expression ADD Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "ADD\n"
	parser.aux.append(s)

def p_Expression2(p):
	"Expression : Expression SUB Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "SUB\n"
	parser.aux.append(s)

def p_Expression3(p):
	"Expression : Expression MUL Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "MUL\n"
	parser.aux.append(s)

def p_Expression4(p):
	"Expression : Expression DIV Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "DIV\n"
	parser.aux.append(s)

def p_Expression5(p):
	"Expression : '(' Expression ')'"

def p_Expression6(p):
	"Expression : ID"
	if p[1] in parser.reg:
		s = f"PUSHG {parser.reg.index(p[1])}\n"
		parser.aux.append(s)
	else:
		parser.aux.append("ERR \"Var não declarada\"\n")

def p_Expression7(p):
	"Expression : Value"

def p_Expression8(p):
	"Expression : Call"

def p_Value1(p):
	"Value : INT"
	t = parser.type[-1]
	if t == "PUSHI":
		s = f"{t} {p[1]}\n"
		parser.aux.append(s)
	else:
		parser.aux.append("ERR \"Valor não é inteiro\"\n")

def p_Call(p):
	"Call : ID '(' ')'"
	s = f"PUSHA {p[1]}\nCALL\n"
	parser.aux.append(s)

def p_Lines1(p):
	"Lines : "
	s = ""
	c = parser.aux.pop()
	while c != "COND" and c != "AUX":
		s = c + s
		c = parser.aux.pop()
	parser.aux.append(s)
	parser.aux.append("AUX")
	pass

def p_Lines2(p):
	"Lines : Line Lines"

def p_Line1(p):
	"Line : Atribuition"

def p_Line2(p):
	"Line : Select"
	parser.c = parser.c + 1
	if parser.c == parser.C:
		parser.c = 0

def p_Line3(p):
	"Line : Cicle"
	parser.c = parser.c + 1
	if parser.c == parser.C:
		parser.c = 0

def p_Line4(p):
	"Line : Read"

def p_Line5(p):
	"Line : Write"

def p_Line6(p):
	"Line : COMENT"
	f"{p[1]}\n"
	
def p_Atribuition(p):
	"Atribuition : ID ATRIBUICAO Expression ';'"
	s = f"STOREG {parser.reg.index(p[1])}\n"
	parser.aux[-1] = parser.aux[-1] + s

def p_Select(p): #####
	"Select : IF '(' Conditions ')' '{' Lines '}' Else"
	e = parser.aux.pop()
	i = parser.aux.pop()
	c = parser.aux.pop()
	s = c + f"JZ Else{parser.C-parser.c}\n" + i + e
	parser.aux.append(s)

def p_Else1(p): #####
	"Else : ELSE '{' Lines '}'"
	parser.aux.pop()
	e = parser.aux.pop()
	s = f"JUMP End{parser.C-parser.c}\n" + f"Else{parser.C-parser.c}: //NOP\n" + e + f"End{parser.C-parser.c}: //NOP\n"
	parser.aux.append(s)

def p_Else2(p): #####
	"Else : "
	parser.aux.pop()
	s = f"Else{parser.C-parser.c}\n"
	parser.aux.append(s)

def p_Cicle1(p):
	"Cicle : WHILE '(' Conditions ')' '{' Lines '}'"
	parser.aux.pop()
	cc = parser.aux.pop()
	c = parser.aux.pop()
	s = "Flag: //NOP\n" + c + f"JZ End{parser.C-parser.c}:\n" + cc +f"JUMP Flag\nEnd{parser.C-parser.c}: //NOP\n"
	parser.aux.append(s)

def p_Cicle2(p):
	"Cicle : FOR '(' ID ATRIBUICAO INT ';' Conditions ';' Math ')' '{' Lines '}'"

def p_Conditions1(p):
	"Conditions : Condition"
	parser.C = parser.C + 1
	parser.aux.append("COND")

def p_Conditions2(p):
	"Conditions : Condition AND Conditions"
	c = parser.aux.pop()
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "AND\n"
	parser.aux.append(s)
	parser.aux.append(c)
           
def p_Conditions3(p):
	"Conditions : Condition OR Conditions"
	c = parser.aux.pop()
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "OR\n"
	parser.aux.append(s)
	parser.aux.append(c)

def p_Condition1(p):
	"Condition : Expression EQ Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "EQUAL\n"
	parser.aux.append(s)

def p_Condition2(p):
	"Condition : Expression NEQ Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "EQUAL\nNOT\n"
	parser.aux.append(s)

def p_Condition3(p):
	"Condition : Expression LT Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "INF\n"
	parser.aux.append(s)

def p_Condition4(p):
	"Condition : Expression LE Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "INFEQ\n"
	parser.aux.append(s)

def p_Condition5(p):
	"Condition : Expression GT Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "SUP\n"
	parser.aux.append(s)

def p_Condition6(p):
	"Condition : Expression GE Expression"
	b = parser.aux.pop()
	a = parser.aux.pop()
	s = a + b + "SUPEQ\n"
	parser.aux.append(s)

def p_Condition7(p):
	"Condition : NOT '(' Condition ')'"
	a = parser.aux.pop()
	s = a + "NOT\n"
	parser.aux.append(s)
	
def p_Math1(p):
	"Math : Atribuition"

def p_Math2(p):
	"Math : Atribuition ',' Math"

def p_Read(p):
	"Read : READ '(' STRING ',' Address ')' ';'"
	a = parser.aux.pop()
	s = "READ\nATOI\n" + a #####
	parser.aux.append(s)

def p_Address(p):
	"Address : '&' ID"
	s = f"STOREG {parser.reg.index(p[2])}\n"
	parser.aux.append(s)

def p_Write1(p):
	"Write : WRITE '(' STRING ')' ';'"
	s = f"PUSHS {p[3]}\nWRITES\n"
	parser.aux.append(s)

def p_Write2(p):
	"Write : WRITE '(' STRING ',' Addresses ')' ';'"
	a = p[3].split("%d")
	s = f"PUSHS \"{a.pop()}\"\n" #####
	for i in range(len(a)):
		s = s + parser.aux.pop() + f"PUSHS \"{a.pop()}\"\nCONCAT\n" ####
		i = i + 1
	s = s + "WRITES\n"
	parser.aux.append(s)

def p_Addresses1(p):
	"Addresses : ID"
	s = f"PUSHG {parser.reg.index(p[1])}\nSTRI\nCONCAT\n"
	parser.aux.append(s)

def p_Addresses2(p):
	"Addresses : ID ',' Addresses"
	e = "PUSHS \" \"\nCONCAT\n"
	s = e + f"PUSHG {parser.reg.index(p[1])}\nSTRI\nCONCAT\n"
	parser.aux.append(s)

def p_Output(p):
	"Output : RETURN Ret ';'"
	parser.type.pop()
	r = parser.aux.pop()
	parser.aux.pop()
	parser.aux.append(r + "RETURN\n")

def p_Ret1(p):
	"Ret : Expression"

def p_Ret2(p):
	"Ret : "
	pass

def p_error(p):
    if p:
        print(f"ERRO SINTÁTICO :'{p.value}'\nReescreva a frase")
    else:
        print("ERRO SINTÁTICO: token inesperado")
    parser.exito = False

parser = yacc.yacc()
parser.exito = True
parser.c = parser.C = 0
parser.reg = []
parser.type =[]
parser.aux = []
parser.mv = ""

fonte = ""
c = open("teste2.c", "r")
for linha in c:
    fonte += linha
c.close()
parser.parse(fonte)

with open("mv2.txt", "w") as a:
    a.write(parser.mv)

if parser.exito:
	print("Parsing terminou com sucesso.\nCompilação Concluída.")
	#print(parser.type,parser.aux)