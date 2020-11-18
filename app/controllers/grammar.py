number = ('E','IOE', 'I', 'N','D')
operator = ('O')
parentheses = ('E','IOE','O')


def getGrammar(tokens):
    items = []
    for token in tokens:
        cod = token[3]
        if cod == 'NÚMERO':
            getNumberGrammar(token, items)
        elif token[3] == 'OPERADOR':
            getOperatorGrammar(token, items)
        elif token[3] == 'PARÊNTESES':
            ...
        else:
            ...

    return items


def getNumberGrammar(token, items):
    count = 0
    value = token[2]
    cod = token[3]
    size = len(value)

    for digito in value:
        for i, j in enumerate(number):
            if i < len(number) - 1:
                # print(f'{j} -> {number[i+1]}')
                items.append(f'{j} -> {number[i+1]}')
            else:
                # print(f'{number[-1]} -> {digito}')
                items.append(f'{number[-1]} -> {digito}')


def getOperatorGrammar(token, items):
    count = 0
    value = token[2]
    cod = token[3]
    size = len(value)

    for digito in value:
        for i, j in enumerate(operator):
            if i < len(operator) - 1:
                # print(f'{j} -> {operator[i+1]}')
                items.append(f'{j} -> {operator[i+1]}')
            else:
                # print(f'{operator[-1]} -> {digito}')
                items.append(f'{operator[-1]} -> {digito}')


def getParenthesesGrammar(token):
    ...
