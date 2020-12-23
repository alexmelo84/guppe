"""
Erros mais comuns

SyntaxError - erro de síntaxe, ou seja, algo está escrito erroneamente.
NameError - quando uma variável ou função não foi definida.
TypeError - ocorre quando uma ação é executada em um tipo errado.
IndexError - acontece quando tenta acessar um índice inválido.
ValueError - valor inapropriado em uma ação.
KeyError - chave inválida no dicionário.
AttributeError - ocorre quando uma variável não tem um atributo ou função.
IdentationError - erro de identação (não respeitar os 4 espaços).

Exceptions e Erros são sinônimos.
"""

# Exemplos de SyntaxError

# Função definida sem os parênteses para de entrada
#def funcao:
#    print('Erro de síntaxe.')

# None não pode ser atribuído
#None = 1

# return fora de função
#return

# Exemplos de NameError

# Variável não definida
#print(teste)

# Função não definida
#teste()

# Variável inicializada dentro de um escopo e utilizada fora dele
#a = 2
#if a < 10:
#    msg = 'Menor que 10.'
#print(msg)

# Exemplos de TypeError

# len() só pode ser usado em iterávels
#print(len(True))

# Não dá para concatenar string com lista
#print('Alex ' + [])

# Exemplos de IndexError

# Índice inválido de uma lista
#lista = ['Alex']
#print(lista[1])
#print(lista[0][4])

# Exemplos de ValueError

# Convertendo string para inteiro
#print(int('Alex'))

# Exemplos KeyError

#dic = {}
#print(dic['a'])

# Exemplos de AttributeError

# Ordenação na tupla
#tupla = (1, 2, 3, 6, 7, 5)
#tupla.sort()
#print(tupla)

# Exemplos de IdentationError

# Identação dentro de função
#def nova():
#return 'nova função.'

# Identação no loop
#for i in range(10):
#print(i)
