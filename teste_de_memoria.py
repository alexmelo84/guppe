"""
Teste de memória com Generators
"""


def fib_list(maximo):
    nums = []
    a, b = 0, 1
    while len(nums) < maximo:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_list(20):
    print(n)


def fib_gen(maximo):
    a, b, contador = 0, 1, 0
    while contador < maximo:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(20):
    print(n)
