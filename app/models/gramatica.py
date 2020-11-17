number = ('E','IOE', 'I', 'N','D')
operator = ('E','IOE','O')
parentheses = ('E','IOE','O')

def getGrammar(token):
    count = 0
    value = token[2]
    cod = token[3]
    size = len(value)
    
    if cod == 'NÚMERO':
        print('entrou')
        for digito in value:
            for i, j in enumerate(number):
                if i < len(number) - 1:
                    print(f'{j} -> {number[i+1]}')
                else:
                    print(f'{number[-1]} -> {digito}')
    elif token[3] == 'OPERADOR':
        ...
    elif token[3] == 'PARÊNTESES':
        ...
    else:
        ...


def getNumberGrammar(token):
    ...


def getOperatorGrammar(token):
    ...


def getParenthesesGrammar(token):
    ...
