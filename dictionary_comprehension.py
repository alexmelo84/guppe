"""
Dictionary comprehension

Síntaxe:
{chave: valor for valor in iteravel}
"""

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrados)

numeros2 = [1, 2, 3, 4, 5]
quadrados2 = {valor: valor ** 2 for valor in numeros2}
print(quadrados2)

chaves = 'abcdef'
valores = [1, 2, 3, 4, 5, 6]
dicionario = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(dicionario)

# Lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in numeros}
print(res)
