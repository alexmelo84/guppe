"""
Geradores

Geradores (Generators) sõa iteradores (Iterators), mas nem qualquer iterador é um gerador.
Generators podem ser criados com funções geradoras.
Funções geradores usam a palavra yield.
Generators podem ser criados com expressões geradoras.

Diferença entre função e função geradora:

------------------------------------------------------------------------------
| Funções                            | Funções geradoras                     |
------------------------------------------------------------------------------
| utilizam return                    | utilizar yield                        |
| retorna uma vez                    | podem utilizar o yield várias vezes   |
| retorna um valor/void              | retorna um generator                  |
"""

# Generator function (não é um Generator, retorna um Generator)


def conta_ate(maximo):
    contador = 1
    while contador <= maximo:
        yield contador  # execução para aqui, esperando um next() ser executado
        contador = contador + 1


gen = conta_ate(20)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for n in conta_ate(8):
    print(n)
