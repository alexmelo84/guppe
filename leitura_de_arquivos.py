"""
Leitura de arquivos

Usa-se a função integrada open().
A forma mais simples é passando um parâmetro e retorna um objeto do tipo _io.TextIOWrapper e trabalhamos com esse
objeto para manipular o arquivo.

Por padrão, o open() abre o arquivo apenas como leitura e o arquivo deve existir, se não existir retornará o erro
FileNotFoundError.

Após abrir o arquivo deve-se usar o método objeto.read().
"""

arquivo = open('teste.txt')
print(arquivo)
print(arquivo.read())
