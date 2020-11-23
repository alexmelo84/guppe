"""
List Comprehension

Pode-se gerar novas listas com dadaos processados de outro iterável.

Síntaxe:
[ dado for dado in iteravel ]
"""

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res2 = [funcao(valor) for valor in numeros]
print(res2)

nome = 'Alex Melo'
print([letra.upper() for letra in nome])

amigos = ['diego', 'lucas', 'douglas', 'marcos']
print([amigo.title() for amigo in amigos])

print([numero * 3 for numero in range(1, 8)])

print([bool(valor) for valor in [0, [], '', True, 1, 2.79]])

print([str(numero) for numero in [2, 4, 6, 8, 10]])

# List comprehension vs Loops
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

print([numero * 2 for numero in numeros])
