"""
Escrever em arquivos

Quando se abre um arquivo para escrita, não é possível lê-lo, e vice-versa.
Se o arquivo não existir ele será criado; caso o arquivo exista e o arquivo for aberto no modo escrita (w), o conteúdo
será sobrescrito.
A função write() só aceita string.
"""

with open('escrita.txt', 'w') as arquivo:
    arquivo.write('Primeira linha adicionada programaticamente.\n')
    arquivo.write('Segunda linha adicionada programaticamente.\n')

with open('alex.txt', 'w') as arquivo:
    arquivo.write('alex\n' * 100)

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Adicione uma fruta ou digite sair: ')
        if fruta.lower() == 'sair':
            break;
        else:
            arquivo.write(fruta + '\n')
