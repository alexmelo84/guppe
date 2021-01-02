"""
Módulos builtin

Sõa módulos integrados que estão disponíveis no Python.

Listagem de módulos:
https://docs.python.org/3/py-modindex.html
"""

# Usando alias nos módulos
import random as rdm
print(rdm.random())

# Importando todas as funções de um módulo. Dessa forma não precisa utilizar o nome do módulo na execução da função.
from random import *
print(random())

# Usando alias nas funções
from random import randint as rdi
print(rdi(1, 10))

# Importando mais de uma função de um mesmo módulo
from random import random, randint
print(random())
print(randint(2, 20))

# Importando funções com tupla (útil para várias importações) (Pythônico)
from random import (
    random,
    randint,
    choice,
    shuffle
)
print(random())
print(randint(10, 14))
print(choice('Alex Melo'))
