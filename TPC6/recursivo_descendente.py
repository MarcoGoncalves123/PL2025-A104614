import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'LPARENT',
    'RPARENT',
    'NUMBER',
    'NEWLINE',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_LPARENT = r'\('
t_RPARENT = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = 'NEWLINE'
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def parse_exp(tokens):
    term_value = parse_termo(tokens)
    return parse_exp2(tokens, term_value)

def parse_exp2(tokens, term_value):
    if tokens and tokens[0][0] == "PLUS":
        tokens.pop(0)
        exp_value = parse_exp(tokens)
        return term_value + exp_value
    elif tokens and tokens[0][0] == "MINUS":
        tokens.pop(0)
        exp_value = parse_exp(tokens)
        return term_value - exp_value
    else:
        return term_value

def parse_termo(tokens):
    fator_value = parse_fator(tokens)
    return parse_termo2(tokens, fator_value)

def parse_termo2(tokens, fator_value):
    if tokens and tokens[0][0] == "TIMES":
        tokens.pop(0)
        termo_value = parse_termo(tokens)
        return fator_value * termo_value
    else:
        return fator_value
    

def parse_fator(tokens):
    if tokens and tokens[0][0] == "NUMBER":
        return  tokens.pop(0)[1]
    elif tokens and tokens[0][0] == "LPARENT":
        tokens.pop(0)
        exp_value = parse_exp(tokens) 
        if tokens and tokens[0][0] == "RPARENT":
            tokens.pop(0)
            return exp_value
        else:
            raise SyntaxError("Parentheses não fechados")
    else:
        raise SyntaxError("Token não esperado: ")


def main():
    str1 = """ 
        2+3
        67-(2+3*4)
        (9-2)*(13-4) """
    lexer = lex.lex()
    lexer.input(str1)

    token_list = []
    for tok in lexer:
        if tok.type == "NEWLINE" and len(token_list) != 0:
            result = parse_exp(token_list)
            print(result)
            token_list = []
        elif tok.type != "NEWLINE":
            token_list.append((tok.type, tok.value))

    if token_list:
        result = parse_exp(token_list)
        print(result)


if __name__ == "__main__":
    main()
