"""
**kwargs

A diferença dele para o *args exige que os parâmetros sejam nomeados e transforma esses valores em um dicionário.
"""


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita da pessoa {pessoa.title()} é {cor}.')


cores_favoritas(Alex='preto', alida='azul')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Quem é você?'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Java'))
print(cumprimento_especial(geek='PHP'))


def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(args)
    if solteiro:
        print(f'{nome} é solteiro.')
    else:
        print(f'{nome} não é solteiro.')
    print(kwargs)


funcao(36, 'Alex')
funcao(39, 'Alida', 1, 2, 3, solteiro=False)
funcao(53, 'Maria', parente='Sim', mae='Sim')
funcao(6, 'Gigi', 4, 5, 6, parente='Sim', mae='Não')

# Desempacotamento


def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Alex', 'sobrenome': 'Melo'}
print(mostra_nomes(**nomes))


# Desempacotamento seo o parâmetro **kwargs ou *args
def soma_multiplos_numeros(a, b, c):
    return a + b + c


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)  # Os nomes das chaves devem ser iguais aos parâmetros da função.

print(soma_multiplos_numeros(*lista))
print(soma_multiplos_numeros(*tupla))
print(soma_multiplos_numeros(*conjunto))
print(soma_multiplos_numeros(**dicionario))
