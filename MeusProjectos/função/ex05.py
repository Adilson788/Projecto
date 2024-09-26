def leiaint(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric():
            break
        else:
            print('\033[31mlamentamos, digite um numero valido. \033[m')
    return n

#programa principal
n = leiaint('Digite um numero: ')
print(f'O numero digitado foi {n}')