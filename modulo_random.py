"""
Módulo Random

Módulos são outros arquivos Python que podem ser importados e reutilizados.

O módulo random possui várias funções que geram números (pseudo)aleatórios.

Há duas formas de utilizar um módulo: com o import do módulo inteiro e importando apenas a função do módulo.

- com o 'import' ele deixará todas as funções, classes, atributos e propriedades disponíveis em memória;
- com o 'from import' ele importa apenas a função desejada de um módulo.
"""

# Importando módulo (import)
#import random

# Gerando um número aleatório entre 0 e 1
#print(random.random())

# Importando uma função de módulo (from import)
from random import random
from random import uniform
from random import randint
from random import choice
from random import shuffle

for i in range(10):
    print(random())

# Gerando valores aleatórios maiores que 1
for i in range(10):
    print(uniform(2, 8))  # gera um valor aleatório entre os dois valores informados, sem incluir o número maior

# Gerando valores inteiros aleatórios
for i in range(10):
    print(randint(1, 20), end=' - ')

print('\n')

# Seleciona um valor aleatório em um iterável
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# Embaralhamento de dados
cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'C']
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas[0])
