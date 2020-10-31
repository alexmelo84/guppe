"""
Collections - Default Dict

Ao criar um dicionário com o Default Dict, informa-se um valor defaul/padrão,
assim evita um KeyError. Ao tentar acessar uma chave inexistente, essa chave será
criada e o valor padrão será atribuído a ela.
"""

# Dicionário padrão
# dicionario = {'curso1': 'Python', 'curso2': 'Java'}
# print(dicionario)
# print(dicionario['curso1'])

from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso1'] = 'Python'
print(dicionario)

print(dicionario['curso2'])
print(dicionario)
