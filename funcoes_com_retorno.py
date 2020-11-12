"""
Funções com retorno

Quando a função não retorna algum valor, o Python considerará o retorno como None.
"""


def quadrado_sete():
    return 7*7


ret = quadrado_sete()
print(f'Retorno em uma variável: {ret}')
print(f'Retorno de uma função diretamente: {quadrado_sete()}')


# Refazendo a função da primeira aula
def diz_oi():
    return 'Oi!'


print(diz_oi())


# Múltiplos retornos
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())

# Múltiplos valores como retorno


def outra_funcao():
    return 1, 2, 3, 4, 5


print(outra_funcao())

# Desempacontando o retorno com múltiplos valores
ret1, ret2, ret3, ret4, ret5 = outra_funcao()
print(ret1, ret2, ret3, ret4, ret5)

# Função de cara ou coroa
from random import random


def cara_coroa():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(cara_coroa())
