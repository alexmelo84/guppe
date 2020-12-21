"""
Reversed

Ao contrário do reverse() que só funciona em listas, o reversed() funciona em qualquer iterável e sua função
é inverter a ordem do iterável.

Pode-se converter o objeto retornado pelo reversed() em uma nova lista, tupla ou conjunto.
"""

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(lista)
print(res)
print(type(res))
print(lista)

# Convertendo
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # O conjunto não tem ordenação.

# Iteração
for letra in reversed('Alex Melo'):
    print(letra, end=' - ')  # O segundo parâmetro é para não quebrar a linha e adicionar um hífen ao lado da letra.

print('\n')

# Iterando sem o for
print(''.join(list(reversed('Alex Melo'))))

# Em string é mais simples inverter usando o slice de strings
print('Alex Melo'[::-1])
