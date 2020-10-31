"""
Collections - Counter

Collections -> High-performance Container Datatypes

Couunter: recebe um iterável e cria um objeto Collection Counter (parecido com dicionário).
"""

from collections import Counter

# A partir de uma lista
lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 11]
res = Counter(lista)
print(type(res))
print(res)

# A partir de uma string
print(Counter('Alex Melo'))

# Recuperar as palavras mais comuns num texto
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
palavras = texto.split()

res2 = Counter(palavras)
print(res2)
print(res2.most_common(3))
