"""
Raise - disparando os próprios erros.

Lança exceções na execução. Não é uma fumção, mas uma palavra reservada.

raise ValueError('Valor incorreto.')
"""


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma string.')
    print(f'O texto {texto} será impresso na cor {cor}.')


colore('Alex', 'preto')


def colore2(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')

    if type(texto) is not str:
        raise TypeError('O texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('A cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f'Cor inválida, somente as seguintes cores são aceitas: {cores}')

    print(f'O texto {texto} será impresso na cor {cor}.')


#colore2('Alex', 'preto')
colore2('Alex', 'azul')
