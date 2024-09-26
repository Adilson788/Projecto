from random import randint
from time import sleep


def sorteia(valores):
    print('Os Valores Sorteados foram: ', end=' ')
    for v in valores:
        sleep(1)
        print(v, end=' ')
    print('Pronto')

def somapar(pares):
    soma = 0
    for par in pares:
        if par % 2 == 0:
            soma += par
    print(f' A lista do valores {pares} a Soma de todos os pares é {soma}')

#principal
numeros = []
for valor in range(0, 5):
    numeros.append(randint(1, 10))
sorteia(numeros)
somapar(numeros)