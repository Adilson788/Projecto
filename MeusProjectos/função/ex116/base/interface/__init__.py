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
    print('-'*35)
    print(f'{msg}'.center(40))
    print('-' * 35)

def lista(lista):
    cabeçalho('\033[33m Menu Principal\033[m')
    c = 1
    for item in lista:
        print(f'\033[32m{c}\033[m - {item}')
        c += 1
    print('-'*35)
    opc = leiaint('Qaul a sua opção: ')
    return opc
