"""
Reduce

A partir do Python3+ o reduce() não é mais built-in, agora precisa executar a partir do módulo functools.
A função precisa ter dois parâmetros.
"""

from functools import reduce

dados = [1, 2, 4, 8, 16]
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Como seria isso num loop
res2 = 1
for n in dados:
    res2 = res2 * n

print(res2)
