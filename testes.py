import re
from modulos.functions import getNumbers, getOperators, getParentheses, getTokens

text = "(134+ 345)* (324 /154)* (866 + 234) * (100-154)"

resultado = getTokens(text)

for i in resultado:
    print(i)

