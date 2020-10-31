"""
Collections - Named Tuple

São tuplas que definimos um nome para ela e para os parâmetros
"""

# Tuple padrão
# tupla = (1, 2, 3)
# print(tupla)
# print(tupla[0])

from collections import namedtuple

# Forma 1
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2
gato = namedtuple('gato', 'idade, raca, nome')

# Forma 3
peixe = namedtuple('peixe', ['idade', 'raca', 'nome'])

pet1 = cachorro(idade=5, raca='Pinscher', nome='Demon')
print(pet1)

# Acessando dados via índice
print(pet1[0])
print(pet1[1])
print(pet1[2])

# Acessando via parâmetro
print(pet1.idade)
print(pet1.raca)
print(pet1.nome)
