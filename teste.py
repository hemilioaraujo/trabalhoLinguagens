from app.controllers import functions as f
from app.models import gramatica as gr
from pprint import pprint

expression = "3+2"

tokens = f.getTokens(expression)
grammar = gr.getGrammar(tokens)

for i in grammar:
    print(i)
