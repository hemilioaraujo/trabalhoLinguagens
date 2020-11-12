import re


especificacao_tokens = [
        r'\d+(\.\d*)?',  # Número Inteiro ou Decimal
        r'[+\-*/]',      # Operadores Matemáticos
        r'\(|\)',            # Parênteses
    ]


def zero_espacos(expressao):
    return expressao.replace(' ', '')


def getNumbers(expression, items):
    for m in re.finditer(especificacao_tokens[0], expression):
        data = (m.start(), m.end(), m.group(), "NÚMERO")
        items.append(data)


def getOperators(expression, items):
    for m in re.finditer(especificacao_tokens[1], expression):
        data = (m.start(), m.end(), m.group(), "OPERADOR")
        items.append(data)


def getParentheses(expression, items):
    for m in re.finditer(especificacao_tokens[2], expression):
        data = (m.start(), m.end(), m.group(), "PARÊNTESES")
        items.append(data)


def getTokens(expression):
    items = []
    getNumbers(expression, items)
    getOperators(expression, items)
    getParentheses(expression, items)
    items.sort()

    return items
