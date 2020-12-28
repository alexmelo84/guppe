"""
Try | Except | Else | Finally

O else é executado se no try/except não houver erros.
O finally é sempre executado independente se teve erro ou não no try/except. É utilizado geralmente fechar ou
desalocar algum recurso, como o banco de dados, por exemplo.
"""

# Else
try:
    num = int(input('Digite um número: '))
except:
    print('Número inválido.')
else:
    print(f'Você digitou: {num}.')

# Finally
try:
    num = int(input('Digite um número: '))
except ValueError:
    print('Número inválido.')
else:
    print(f'Você digitou o número {num}.')
finally:
    print('Estamos no finally!')
print('Depois do try/except.')

#


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Um dos valores informados está incorreto.'
    except ZeroDivisionError:
        return 'Não é possível dividir por 0.'
    except (NameError, IndexError) as err:
        return f'Ocorreu o seguinte erro: {err}.'


num_a = input('Digite o primeiro número: ')
num_b = input('Digite o segundo número: ')
print(dividir(num_a, num_b))
