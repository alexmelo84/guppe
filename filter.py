"""
Filter

Filtra dados em uma coleção.
Ela recebe dois parâmetros, sendo uma função e um iterável.
"""

import statistics

dados = [1.3, 0.6, 9.9, 20.1, -2, 13.16, 9.4]

# Cálculo de média
media = statistics.mean(dados)
print(media)

res = filter(lambda x: x > media, dados)
print(list(res))

# Dados faltantes
paises = ['', 'Argentina', 'Brasil', '', 'Chile', '', '', 'Colômbia', '', 'Equador', '', 'Venezuela']
res2 = filter(None, paises)
print(list(res2))
res3 = filter(lambda pais: len(pais) > 0, paises)
print(list(res3))

# Outro exemplo
usuarios = [
    {'username': 'alex', 'tweets': ['Tweet 1', 'Tweet 2', 'Tweet 3']},
    {'username': 'alida', 'tweets': ['Tweet 1', 'Tweet 2', 'Tweet 3', 'Tweet 4', 'Tweet 5', 'Tweet 6']},
    {'username': 'douglas', 'tweets': ['Tweet 1', 'Tweet 2']},
    {'username': 'maria', 'tweets': ['Tweet 1']},
    {'username': 'diego', 'tweets': []},
    {'username': 'lucas', 'tweets': []}
]
print(usuarios)

# Filtrar usuários que estão inativos no Twitter
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

inativos2 = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos2)

# Combinar filter() e map()
nomes = ['Alex', 'Alida', 'Maria']
print(list(map(lambda nome: f'Seu instrutor é {nome}', filter(lambda nome: len(nome) < 5, nomes))))
