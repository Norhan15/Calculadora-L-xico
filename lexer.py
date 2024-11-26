import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Expresiones regulares para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Regla para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convertir el valor a entero
    return t

# Ignorar espacios
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

def analyze_expression(expression):
    """
    Analiza una expresión matemática y devuelve una lista de tokens.
    """
    lexer.input(expression)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

def count_tokens(tokens):
    """
    Cuenta los tokens por tipo.
    """
    counts = {
        'numbers': 0,
        'operators': 0,
        'parentheses': 0,
    }
    for token in tokens:
        if token.type == 'NUMBER':
            counts['numbers'] += 1
        elif token.type in {'PLUS', 'MINUS', 'TIMES', 'DIVIDE'}:
            counts['operators'] += 1
        elif token.type in {'LPAREN', 'RPAREN'}:
            counts['parentheses'] += 1
    return counts
