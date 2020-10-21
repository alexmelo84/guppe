"""
Mapas são os dicionários em Python, são representados por {}
"""
receita = {'jan': 200, 'fev': 500, 'mar': 800}
print(receita)

# Iterar
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave}: {receita[chave]}')

# Recuperar apenas as chaves (Pythônico)
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Recuperando apenas os valores (Pythônico)
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento
print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma, máximo, mínimo e quantidade de elementos
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
