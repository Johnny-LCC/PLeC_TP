import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'not': 'NOT',
    'elif': 'ELIF',
    'while': 'WHILE',
    'for': 'FOR',
    'def': 'DEF',
    'return': 'RETURN',
    'import': 'IMPORT',
    'as': 'AS',
    'from': 'FROM',
    'class': 'CLASS',
    'try': 'TRY',
    'except': 'EXCEPT',
    'finally': 'FINALLY',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'pass': 'PASS',
    'with': 'WITH',
    'yield': 'YIELD',
    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE',
}

# Lista de tokens
tokens = [
    'IDENTIFIER',    # Identificadores (nomes de variáveis e funções)
    'NUMBER',        # Números (inteiros e flutuantes)
    'STRING',        # Strings (entre aspas simples ou duplas)
    'PLUS',          # Operador de adição (+)
    'MINUS',         # Operador de subtração (-)
    'MULT',          # Operador de multiplicação (*)
    'DIV',           # Operador de divisão (/)
    'EQ',            # Operador de igualdade (==)
    'ASSIGN',        # Operador de atribuição (=)
    'LPAREN',        # Parêntese esquerdo (
    'RPAREN',        # Parêntese direito )
    'LBRACE',        # Chave esquerda {
    'RBRACE',        # Chave direita }
    'COMMA',         # Vírgula
    'COLON',         # Dois pontos
    'NEWLINE',       # Nova linha (quebra de linha)
] + list(reserved.values())  # Adiciona as palavras-chave na lista de tokens


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULT    = r'\*'
t_DIV     = r'/'
t_EQ      = r'=='
t_ASSIGN  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COMMA   = r','
t_COLON   = r':'


t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"|\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  


def t_COMMENT(t):
    r'\#.*'
    pass  


def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()

print("Digite o código Python (ou 'exit' para sair):")

codigo_entrada = ""
while True:
    linha = input()  
    if linha.strip().lower() == 'exit':
        break
    codigo_entrada += linha + '\n'

lexer.input(codigo_entrada)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
