"""
Funções com parâmetros
"""


def quadrado(numero):
    return numero ** 2


def cantar_parabens(pessoa):
    print('Parabéns pra você!')
    print('Nessa data querida!')
    print('Muitas felicidades!')
    print('Muitos anos de vida!')
    print(f'Viva {pessoa}')


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg


def nome_completo(nome, sobrenome):
    return f'O nome completo é {nome} {sobrenome}.'


if __name__ == '__main__':
    print(quadrado(2))
    print(quadrado(5))
    print(quadrado(10))

    cantar_parabens('Alex')

    print(soma(2, 38))
    print(multiplica(4, 5))
    print(outra(1, 6, 'Alex'))

    # Argumentos nomeados (keyword arguments)
    print(nome_completo(nome='Alex', sobrenome='Melo'))
    print(nome_completo(sobrenome='Cage', nome='Nicolas'))
