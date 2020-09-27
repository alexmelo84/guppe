"""
Recebendo dados do usuário
"""
# Usando print antigo, da versão 2.x do Python
"""
print('Qual o seu nome? ')
nome = input()
print('Seja bem-vindo(a) %s' % nome)

print('Qual sua idade?')
idade = input()
print('%s tem %s anos.' % (nome, idade))
"""

# Usando print moderno, da versão 3.x em diante
"""
print('Qual o seu nome? ')
nome = input()
print('Seja bem-vindo(a) {0}'.format(nome))

print('Qual sua idade?')
idade = input()
print('{0} tem {1} anos'.format(nome, idade))
"""

# Usando print atual
#print('Qual o seu nome? ')
#nome = input()
nome = input('Qual o seu nome?')
print(f'Seja bem-vindo(a) {nome}')

#print('Qual sua idade?')
#idade = input()
idade = int(input('Qual sua idade?'))
print(f'{nome} tem {idade} anos')
print(f'{nome} nasceu em {2020 - idade}')
