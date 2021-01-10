"""
Seek e Cursors

Cursor é a posição do arquivo em que o Python está.

Seek - seek() - serve para movimentar o cursor pelo arquivo.
"""

arquivo = open('teste.txt')
arquivo.seek(40)
print(arquivo.read())

# Ler cada linha do arquivo
arquivo.seek(0)
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

# Ler cada linha do arquivo num loop
for linha in arquivo.readlines():
    print(linha)

# Fechamento do arquivo
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado
arquivo.close()
print(arquivo.closed)
