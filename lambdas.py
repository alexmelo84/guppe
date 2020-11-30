"""
Lambdas

São funções anônimas.
"""

lambda x: 3 * x + 1

calc = lambda x: 3 * x + 1
print(calc(5))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('Alex', 'Melo'))

autores = ['Isaac Asimov', 'Neil Gaiman', 'J. R. R. Tolkien', 'Machado de Assis', 'Dan Brown', 'Orson Wells']
print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


def quadratica(a, b, c):
    """
    Retorna a função quadrática f(x) = a * x ** 2 + b * x + c
    :param a:
    :param b:
    :param c:
    :return:
    """
    return lambda x: a * x ** 2 + b * x + c


funcao = quadratica(2, 4, 7)
print(funcao(0))
print(funcao(1))
print(funcao(2))
print(quadratica(2, 4, 7)(3))
