"""
Sorted

O sorted() pode ser usado em qualquer iterável, diferente do sort() que só pode ser utilizado em listas.
Ele cria uma nova lista ordenada, mantendo a lista base intacta.
"""

numeros = [6, 1, 4, 20, 3]
print(numeros)
print(sorted(numeros))
print(numeros)  # Manteve a ordenação original

# Usando parâmetros
# Ordem inversa
print(sorted(numeros, reverse=True))

# Ordenação complexa
usuarios = [
    {'username': 'alex', 'tweets': ['Tweet 1', 'Tweet 2', 'Tweet 3']},
    {'username': 'alida', 'tweets': ['Tweet 1', 'Tweet 2', 'Tweet 3', 'Tweet 4', 'Tweet 5', 'Tweet 6']},
    {'username': 'douglas', 'tweets': ['Tweet 1', 'Tweet 2']},
    {'username': 'maria', 'tweets': ['Tweet 1']},
    {'username': 'diego', 'tweets': []},
    {'username': 'lucas', 'tweets': []}
]
print(usuarios)

# Ordenando pelo nome de usuário
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo nome de usuário inversamente
print(sorted(usuarios, key=lambda usuario: usuario['username'], reverse=True))

# Ordenando pelo total de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

# Ordenando pelo total de tweets inversamente
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))

#
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 40},
    {'titulo': 'One', 'tocou': 22},
    {'titulo': 'Creep', 'tocou': 85},
    {'titulo': 'I am the Highway', 'tocou': 123},
    {'titulo': 'Starway to Heaven', 'tocou': 52}
]

# Ordena pelas músicas menos tocadas
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena pelas músicas mais tocadas
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
