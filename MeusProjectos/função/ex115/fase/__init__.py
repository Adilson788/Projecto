def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
            break
        except (ValueError, TypeError):
            print('ERRO: Digite um valor valido. Tente Novamente')
        except KeyboardInterrupt:
            print('O Usuario preferiu interroper o programa')
            return 0
    return inteiro

def cabeçalho(msg):
    print('-' * 35)
    print(f'{msg}'.center(35))
    print('-' * 35)

def lista(lista):
    cabeçalho('Menu Princital')
    c = 1
    for l in lista:
        print(f'{c} - {l}')
        c += 1
    print('-'*35)
    opc = leiaint('Qual a sua Opção: ')
    return opc

