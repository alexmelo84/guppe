"""
Zip

zip() - cria um iterável do tipo Zip Object agregando os valores de entrada em pares.
"""

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
zip1 = zip(lista1, lista2)

print(lista1)
print(lista2)
print(zip1)
print(list(zip1))
print(dict(zip(lista1, lista2)))  # No dictionary ele cria chave => valor

nome1 = 'Alex Melo'
nome2 = 'Alex Melo'
print(list(zip(nome1, nome2)))

# Se um dos iteráveis for maior que o outro o zip() irá só até o último item do menor iterável.
lista3 = [7, 8, 9, 10, 11]
lista4 = [12, 13, 14]
print(list(zip(lista3, lista4)))

# Com o desempacotamento
dados = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*dados)))

# Pega a maior nota de um aluno
prova1 = [80, 88, 72]
prova2 = [90, 92, 98]
alunos = ['Pedro', 'Maria', 'João']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Com o map()
final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final2))
