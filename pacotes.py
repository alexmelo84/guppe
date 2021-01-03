"""
Pacotes

É um diretório contendo uma coleção de módulos.

No Python 2.x era obrigatório que o pacote tivesse o arquivo __init__.py, nas versões 3.x não é mais obrigatório, mas
ainda se usa por compatibilidade.
"""

from geek import geek1, geek2
from geek.university import geek3, geek4

# Do geek1
print(geek1.pi)
print(geek1.funcao1(10, 40))

# Do geek2
print(geek2.curso)
print(geek2.funcao2())

# Do geek3
print(geek3.funcao3())

# Do geek4
print(geek4.funcao4())

# Importando apenas a função
from geek.geek1 import funcao1
print(funcao1(5, 7))
