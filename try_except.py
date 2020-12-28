"""
try/except

Caputa erros que podem ocorrer na execução, evitando que mensagens de erro inesperadas sejam exibidas para o usuário.

Síntaxe:

try:
    # código
except:
    # se ocorrer algum erro cairá aqui
"""

# Erro genérico
try:
    alex()
except:
    print('Ocorreu algum problema.')

try:
    len(10)
except:
    print('Ocorreu algum prblema.')

# Erro específico
try:
    alex()
    len(20)
except NameError:
    print('Função indefinida.')
except TypeError:
    print('Tipo incompatível.')

# Definindo um alias para o erro para recuperar os detalhes desse erro
try:
    alex()
except NameError as err:
    print(f'Ocorreu o seguinte erro: {err}')

# Dentro de função


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return 'Chave não encontrada.'


dic = {'nome': 'Alex', 'sobrenome': 'Melo'}
print(pega_valor(dic, 'nome'))
