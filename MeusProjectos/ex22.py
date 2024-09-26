from time import sleep
def contador(i, f, p):
    print(f'Contando de {i} ate {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        while cont <= f:
            sleep(0.5)
            print(cont, end=' ')
            cont += p
    if i > f:
        cont = i
        while cont >= f:
            sleep(0.5)
            print(cont, end=' ')
            cont -= p
    print('Pronto')
    print('-' * 30)


#programa principal
contador(1, 10, 1)
contador(10, 2, 2)
print('Agora é a sua de personalizar a contagem')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


