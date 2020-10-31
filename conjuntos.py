"""
Conjuntos
No Python são chamados de Sets.
- não possuem valores duplicados;
- não possuem valores ordenados;
- elementos não são acessados por índice.

São referenciados por chaves {}. A diferença entre sets e dicionários é que o set só tem valor, enquanto dicionário
tem chave -> valor.
"""

# Definir um set
# Forma 1
s = set({1, 3, 5, 7, 5, 3, 2, 4})
print(s)
print(type(s))

# Forma 2 (mais comum)
s2 = {1, 3, 5, 7, 5, 3, 2, 4}
print(s2)
print(type(s2))

# Verifica se um valor existe
if 2 in s:
    print('O 2 existe no conjunto.')
else:
    print('O 2 não existe no conjunto.')

# Ordenação (conjuntos não têm ordenação)
lista = [50, 25, 80, 2, 12, 25, 30, 12]
print(f'lista: {lista} com {len(lista)} elementos.')

tupla = (50, 25, 80, 2, 12, 25, 30, 12)
print(f'tupla: {tupla} com {len(tupla)} elementos.')

dicionario = {}.fromkeys([50, 25, 80, 2, 12, 25, 30, 12], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos.')

conjunto = {50, 25, 80, 2, 12, 25, 30, 12}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos.')

# Aceita qualquer tipo de dados e misturados
s3 = {'s', 1, 'abc', 1.8, (1, 2, 3)}
print(s3)
print(type(s3))

for valor in s3:
    print(valor)

# Total de registros numa lista excluindo os valores repetidos
cidades = ['São Paulo', 'Campinas', 'Santos', 'Brotas', 'Ubatuba', 'Guarulhos', 'Campinas', 'São Paulo']
print(cidades)
print(len(cidades))
print(len(set(cidades)))

# Adicionar elementos
s4 = {1, 2, 3}
print(s4)
s4.add(4)
print(s4)

# Remover elementos
# Forma 1 (dá erro se o valor não for encontrado)
s5 = {'a', 'b', 'c', 'e'}
print(s5)
s5.remove('e')
print(s5)

# Forma 2 (não dá erro se o valor não for encontrado)
s6 = {1, 2, 3, 4, 5, 6, 7, 9}
print(s6)
s6.discard(9)
print(s6)

# Copiar
s7 = {1, 2, 3, 4, 5}
print(s7)

# Forma 1 (deep copy)
novoConjunto = s7.copy()
print(novoConjunto)
novoConjunto.add(6)
print(s7)
print(novoConjunto)

# Forma 2 (shallow copy)
novoConjunto2 = s7
print(novoConjunto2)
novoConjunto2.add(7)
print(s7)
print(novoConjunto2)

# Remover todos os itens
s8 = {'a', 'b', 'c', 'd'}
print(s8)
s8.clear()
print(s8)

# Métodos matemáticos
estudantes_python = {'Alex', 'Maria', 'João', 'José', 'Cremilda'}
estudantes_java = {'Lucas', 'Diego', 'Raquel', 'Ana', 'Josinelson', 'Alex', 'Maria'}

# Valores únicos com o Union (gera um registro com valores únicos, excluindo as repetições)
estudantes1 = estudantes_java.union(estudantes_java)
print(estudantes1)

# Valores únicos com o pipe |
estudantes2 = estudantes_java | estudantes_python
print(estudantes2)

# Valores que se repetem nos dois conjuntos com o Intersection
repetidos1 = estudantes_java.intersection(estudantes_python)
print(repetidos1)

# Valores que se repetem nos dois conjuntos com o &
repetidos2 = estudantes_java & estudantes_python
print(repetidos2)

# Valores que não se repetem nos conjuntos
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, máximo, mínimo e tamanho
s9 = {2, 4, 8, 16, 32, 64}
print(sum(s9))
print(max(s9))
print(min(s9))
print(len(s9))
