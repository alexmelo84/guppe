"""
Criando um loop próprio
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for([1, 2, 3, 4, 5, 6, 7, 8, 9])
meu_for(range(1, 20))
meu_for('Alex Melo')
