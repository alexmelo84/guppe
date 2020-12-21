"""
Min e Max

max() -> retorna o maior valor de um iterável ou o maior entre dois ou mais elementos.
min() -> retorna o menor valor de um iterável ou o menor entre dois ou mais elementos.
"""

# max() em iteráveis
lista = [0, 24, 9, 8, 100, 88]
print(max(lista))

tupla = (0, 24, 9, 8, 100, 88)
print(max(tupla))

conjunto = {0, 24, 9, 8, 100, 88}
print(max(conjunto))

dicionario = {'a': 0, 'b': 24, 'c': 9, 'd': 8, 'e': 100, 'f': 88}
print(max(dicionario))  # retorna a maior chave

dicionario = {'a': 0, 'b': 24, 'c': 9, 'd': 8, 'e': 100, 'f': 88}
print(max(dicionario.values()))  # retorna o maior valor

# max() em valores
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(max(val1, val2))

# min() em iteráveis
lista = [0, 24, 9, 8, 100, 88]
print(min(lista))

tupla = (0, 24, 9, 8, 100, 88)
print(min(tupla))

conjunto = {0, 24, 9, 8, 100, 88}
print(min(conjunto))

dicionario = {'a': 0, 'b': 24, 'c': 9, 'd': 8, 'e': 100, 'f': 88}
print(min(dicionario))  # retorna a maior chave

dicionario = {'a': 0, 'b': 24, 'c': 9, 'd': 8, 'e': 100, 'f': 88}
print(min(dicionario.values()))  # retorna o maior valor

# max() em valores
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(min(val1, val2))

# Outros exemplos
nomes = ['Alex', 'Alida', 'Gigi', 'Maria']
# Ordem alfabética
print(max(nomes))
print(min(nomes))

# Ordem pelo total de caracteres
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

# Pegando as músicas mais tocadas
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 40},
    {'titulo': 'One', 'tocou': 22},
    {'titulo': 'Creep', 'tocou': 85},
    {'titulo': 'I am the Highway', 'tocou': 123},
    {'titulo': 'Starway to Heaven', 'tocou': 52}
]

# Usando lambda
print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

mais_tocado = max(musicas, key=lambda musica: musica['tocou'])
print(f'A música mais tocada foi {mais_tocado["titulo"]}, tocou {mais_tocado["tocou"]} vezes.')

menos_tocado = min(musicas, key=lambda musica: musica['tocou'])
print(f'A música menos tocada foi {menos_tocado["titulo"]}, tocou {menos_tocado["tocou"]} vezes.')

# Sem lambda
vezes_tocado_max = 0
musica_mais_tocada = ''
for musica in musicas:
    if musica['tocou'] > vezes_tocado_max:
        vezes_tocado_max = musica['tocou']
        musica_mais_tocada = musica['titulo']
print(f'A música mais tocada foi {musica_mais_tocada}, tocou {vezes_tocado_max} vezes.')

vezes_tocado_min = vezes_tocado_max
musica_menos_tocada = ''
for musica in musicas:
    if musica['tocou'] < vezes_tocado_min:
        vezes_tocado_min = musica['tocou']
        musica_menos_tocada = musica['titulo']
print(f'A música menos tocada foi {musica_menos_tocada}, tocou {vezes_tocado_min} vezes.')
