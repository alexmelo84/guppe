"""
Modos de abertura de arquivo

https://docs.python.org/3/library/functions.html#open

r -> Abre como leitura (padrão);
w -> Abre para escrita, sobrescrevendo se o arquivo existir ou criando caso o arquivo nãoe exista;
x -> Somente abre o arquivo para escrita caso ele não exista;
a -> Abre para escrita, mas adiciona o ponteiro no final do arquivo, mantendo o conteúdo jã existente (impossível
controlar o cursor);
+ -> Abre o arquivo para leitura e escrita, podendo controlar o cursor.
"""

with open('não_existia.txt', 'x') as arquivo:
    arquivo.write('Arquivo não existia, agora existe.\n')

# Adicionando linhas no começo do arquivo
with open('abrindo_com_o_mais.txt', 'a') as arquivo:
    arquivo.seek(0)
    arquivo.write('Nova linha\n')
