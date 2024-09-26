import time

print('='*32)
print('Converta Número Decimal para'.center(32))
print('Binário, Octal e Hexadecimal'.center(32))
print('='*32)
while True:
    try:
        decimal = int(input('Digite um número Decimal: '))
        if decimal >=0:
            if decimal.is_integer():
                break
        else:
            print('Apenas numero inteiro Positivo')
    except ValueError:
        print('Erro! Valor invalido. Tente Novamente')
    except KeyboardInterrupt:
        print('\nO Usuario decidiu interroper o programa')
        break
print('='*32)
print(''''Convertem em:
[1] - BINARIO
[2] - OCTAL
[3] - HEXADECIMAL
[4] - SAIR DO PROGRAMA
''')
print('='*25)
from time import sleep
while True:
    try:
        opc = int(input('Qual a sua Opção: '))
        if opc == 1:
            binario = bin(decimal)
            print(f'A conversão do Número Decimal {decimal} para Binário é {binario[2:]}')
        elif opc == 2:
            octal = oct(decimal)
            print(f'A conversão do Número Decimal {decimal} para Octal é {octal[2:]}')
        elif opc == 3:
            Hex = hex(decimal)
            print(f'A conversão do Número Decimal {decimal} para Binário é {Hex[2:]}')
        elif opc == 4:
            print('Saindo do Programa...')
            time.sleep(1.5)
            break
        else:
            print('Lamentamos! A Opção selecionada nao Existe.')
    except ValueError:
        print('Essa opção nao é valida digite um numero')
    except KeyboardInterrupt:
        print('\nO Usuario decidiu interroper o programa')
        break
print('Obrigado Volte Sempre!')
