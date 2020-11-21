from app.controllers import grammar
from app.controllers import token
from pprint import pprint

expression = "3+2"

tokens = token.getTokens(expression)
grammar = grammar.getGrammar(tokens)

for i in grammar:
    print(i)
