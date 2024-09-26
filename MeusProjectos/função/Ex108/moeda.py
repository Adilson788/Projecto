def metade(valor = 0):
    preço = valor / 2
    return preço


def dobro(valor=0):
    d = valor * 2
    return d


def aumento(valor=0):
    aumento_10 = valor + (valor * 10 / 100)
    return aumento_10


def reduzir(valor=0):
    desconto = valor - (valor * 13 /100)
    return desconto


def moeda(valor=0, moeda='Kz'):
    return f'{valor:.2f}{moeda}'.replace('.',',')
