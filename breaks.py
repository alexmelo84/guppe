"""
Saindo de loops com break
"""

for num in range(1, 10):
    if num == 6:
        break
    else:
        print(num)

print('\n')

while True:
    comando = input('Digite \'sair\' para terminar a execução.')
    if comando == 'sair':
        break
