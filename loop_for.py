"""
Loop for

Loop: estruturas de repetição
For: é uma das estruturas

for item in iteravel:
    // execução

Exemplos de iteráveis
- String
    nome = 'Alex'
- Lista
    lista = [0, 1, 2, 3, 4, 5]
- Range
    numeros = range(1, 20)
"""

nome = 'Alex Melo'
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
numeros = range(1, 20)

for caractere in nome:
    print(caractere, end='')

print('\n')

for letra in alfabeto:
    print(letra)

for numero in numeros:
    print(numero)

# Retornando o índice
for indice, caractere in enumerate(nome):
    print(indice)
    print(caractere)

# Descartando o índice
for _, caractere in enumerate(nome):
    print(caractere)

# Trazendo o par key => value
for valor in enumerate(nome):
    print(valor)
    print(valor[0])
    print(valor[1])

qtd = int(input('Quantas voltas o loop deve fazer?'))
for n in range(1, qtd + 1):
    print(f'Volta número {n}')

produtos = int(input('Quantos produtos existem?'))
soma = 0
for n in range(1, produtos + 1):
    preco = int(input(f'Informe o preço do produto {n}/{produtos}: '))
    soma += preco
print(f'O valor total é {soma}')

# Emojis (utilizar o unicode e substituir o '+' por '000' (http://apps.timwhitlock.info/emoji/tables/unicode)
emoji = '\U0001F60B'
for _ in range(3):
    for num in range (1, 11):
        print(f'{emoji * num}')
