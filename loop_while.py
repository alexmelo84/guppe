"""
Loop while
Exeuta o loop enquanto a condição boolean for verdadeira

while boolean:
    \\ Execução
"""

num = 3
while num < 10:
    print(num)
    num += 1

print('\n')

resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou, Jéssica?')
