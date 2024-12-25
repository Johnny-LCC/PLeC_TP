import ply.yacc as yacc
import sys

from tp2_lex import tokens

''' Grammar
Programa : Imports Funcs
Imports : Import Imports
        | Import
Import : '#' INCLUDE '<' BIBLIO '>'
Funcs : Func Funcs
      | Func
Func : TIPO ID '(' Inputs ')' '{' Comandos Output'}'
Inputs : Input ',' Inputs
       | Input
Input : TIPO ID
Comandos : Comando Comandos
         | Comando
Comando : ???????????
Output : RETURN Ret
Ret : ID 
    | INT 
    | FLOAT 
    | STRING
'''