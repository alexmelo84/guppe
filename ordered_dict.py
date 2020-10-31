"""
Collections - Ordered Dict

Garante que a ordenação dos elementos
"""

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
for chave, valor in dicionario.items():
    print(f'chave={chave} => valor={valor}')

# Diferença
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)

oDict1 = OrderedDict({'a': 1, 'b': 2})
oDict2 = OrderedDict({'b': 2, 'a': 1})
print(oDict1 == oDict2)
