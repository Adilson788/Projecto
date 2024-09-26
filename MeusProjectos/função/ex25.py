def leiaint(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            break
        else:
            print('\033[31mlamentamos, digite um numero valido. \033[m')
    return n

def leiafloat(msg):
    while True:
        try:
            real = float(input(msg))
            break
        except ValueError:
            print('ERRO: Lamentamos. Tente Novamente')
    return real



#programa principal
n = leiaint('Digite um numero inteiro: ')
print(f'O numero Inteiro foi: {n}')

n = leiafloat('Digite um numero Real: ')
print(f'O numero Real foi: {n}')
