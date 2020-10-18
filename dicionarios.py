"""
Dicionários

Em outras linguagens, dicionários do Python são conhecidos como mapas.
São coleções chave => valor.
São representados por chaves {}.
"""

# Forma mais comum de criação de dicionário
paises = {'br': 'Brasil', 'eu': 'Estados Unidos', 'gb': 'Grâ Bretanha', 'it': 'Itália'}
print(paises)
print(type(paises))

# Forma menos comum de criação de dicionário
paises2 = dict(ar='Argentina', au='Austrália', id='Índia', pt='Portugal')
print(paises2)
print(type(paises2))

# Acesso a elementos via chave
print(paises['br'])

# Acesso a elementos via get (recomendado pois, se a chave procurada no get() não for encontrada vai retornar o tipo
# 'None' ao invés de KeyError)
pais = paises.get('ar')
if pais:
    print(f'Encontrou o país {pais}.')
else:
    print('Nao encontrou o país.')

# Acesso via get e definindo um valor padrão caso não encontre
pais2 = paises.get('bo', 'Não encontrado')
print(pais2)

# Verificando se índice existe
if 'br' in paises:
    print('País existe no dicionário.')
else:
    print('País não existe no dicionário.')

# Pode-se usar qualquer tipo de dado como chave, incluindo lista, tupla e dicionário
localidades = {
    (35.1234, 36.0192): 'Escritório 1',
    (11.5784, -24.1245): 'Escritório 2',
    (34.0980, 23.1212): 'Escritório 3'
}
print(localidades)

# Adicionar elementos
print(paises2)
paises2['jp'] = 'Japão'
print(paises2)

paises2.update({'ch': 'China'})
print(paises2)

# Alterar elementos
paises2['id'] = 'Indonésia'
print(paises2)

paises2.update({'ar': 'Armênia'})
print(paises2)

# Remover elementos com pop(), que é a mais comum (é obrigatório passar a chave que será removida)
# Quando o elemento é removido, o retorno do pop() retorna o valor da chave removida
paises2.pop('jp')
print(paises2)

# Remover elementos com del()
del paises2['ch']
print(paises2)

# Outros métodos
alfabeto = dict(a=1, b=2, c=3, d=4, e=5)
print(alfabeto)

# Copiar (deep copy)
deepAlfabeto = alfabeto.copy()
print(deepAlfabeto)

# Copiar (shallow copy)
shallowAlfabeto = alfabeto
print(shallowAlfabeto)

# Apagar o conteúdo
alfabeto.clear()
print(alfabeto)

# Criação de dicionário com o fromkeys()
fromKeys = {}.fromkeys('a', 'b')
print(fromKeys)

dadosUsuario = {}.fromkeys(['nome', 'email', 'senha', 'grupo', 'cidade'], 'Não informado')
print(dadosUsuario)
