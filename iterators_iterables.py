"""
Entendendo Iterators e Iterables

Iterator: é um objeto que pode ser iterado. Ao executar a função next() retornará um elemento por vez.
Iterable: é um objeto que retornará um Iterator quando a função iter() for executada.
"""

# Iterable
nome = 'Alex'
numeros = [1, 2, 3, 4, 5, 6, 7]

iter_nome = iter(nome)
iter_numeros = iter(numeros)

# Iterators (se executar o next() quando não houver mais iten no Iterator)
print(next(iter_nome))
print(next(iter_nome))
print(next(iter_nome))
print(next(iter_nome))

print(next(iter_numeros))
print(next(iter_numeros))
print(next(iter_numeros))
print(next(iter_numeros))
print(next(iter_numeros))
print(next(iter_numeros))
print(next(iter_numeros))

# O next() é o que o Python executa internamente no for
for letra in nome:
    print(letra)
