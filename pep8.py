"""
PEP8 - Python Enhancement Proposals

São propostas de melhoria para a linguagem Python

The Zen Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] Utlize Camel Case para nomes de classes;

[2] Utilize nomes em minúsculo separados por _ para funções ou variáveis;

[3] Utilize 4 espaços para identação

[4] Linhas em branco:
- separar funções e definições de classe com duas linhas em branco;
- métodos de uma classe devem ser separados com uma única linha em branco.

[5] Imports:
- devem ser feitos em linhas separadas.

[6] Espaços em expressões e instruções

[7] Termine uma instrução com uma nova linha

"""

# [1]
class Teste:
    pass

# [2]
def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

# [3]
if 'a' in 'banana':
    print('letra existe');

# [4]


class Primeira:
    pass


class Segunda:
    pass

# [5]

# Errado
import sys, os

# Certo
import sys
import os

# Sem problemas
# from types import StringType, LisType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer o seguinte:
""""
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
"""

# Imports devem ser colocados no topo do arquivo, logo após quaisquer comentários ou docstrings e antes de quaisquer
# constantes ou variáveis globais

# [6]
# Não faça
#funcao( algo[ 1 ], { outro: 2 } )

# Faça
#funcao(algo[1], {outro: 2})

# Não faça
#algo (1)

# Faça
#algo(1)

# Não faça
#dict ['chave'] = list ['indice']

# Faça
#dict['chave'] = list['indice']

# Não faça
#x            = 1
#y            = 3
#variavelzona = 5

# Faça
#x = 1
#y = 3
#variavelzona = 5

#[7]
import this
