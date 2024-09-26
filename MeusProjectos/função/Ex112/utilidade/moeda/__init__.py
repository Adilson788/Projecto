def metade(valor = 0, formato = False):
    preço = valor / 2
    return preço if formato is False else moeda(preço)


def dobro(valor=0, formato = False):
    d = valor * 2
    return d if formato is False else moeda(d)


def aumento(valor=0, taxa=0, formato = False):
    acrescimotaxa = valor * taxa / 100
    adicional = valor + acrescimotaxa
    return adicional if formato is False else moeda(adicional)


def reduzir(valor=0, taxa=0, formato = False):
    redução = valor * taxa /100
    desconto = valor - redução
    return desconto if formato is False else moeda(desconto)


def moeda(valor=0, moeda='Kz'):
    return f'{valor:.2f}{moeda}'.replace('.',',')


def resumo(valor=0, taxaa=10, taxar=5):
    print('-'*30)
    print(f'Resumo'.center(30))
    print('-' * 30)
    print(f'\033[32mAnalzando o Valor {moeda(valor)}\033[m'.center(30))
    print(f'O  Aumento:{moeda(aumento(valor, taxaa)).rjust(20)}')
    print(f'O Desconto:{moeda(reduzir(valor, taxar)).rjust(20)}')
    print(f'     dobro:{moeda(dobro(valor)).rjust(20)}')
    print('-'*30)
