def metade(valor = 0, formato = False):
    preço = valor / 2
    return preço if formato is False else moeda(preço)


def dobro(valor=0, formato = False):
    d = valor * 2
    return d if formato is False else moeda(d)


def aumento(valor=0, formato = False):
    aumento_10 = valor + (valor * 10 / 100)
    return aumento_10 if formato is False else moeda(aumento_10)


def reduzir(valor=0, formato = False):
    desconto = valor - (valor * 13 /100)
    return desconto if formato is False else moeda(desconto)


def moeda(valor=0, moeda='Kz'):
    return f'{valor:.2f}{moeda}'.replace('.',',')
