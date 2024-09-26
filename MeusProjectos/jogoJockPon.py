import random
import time
print('='*30)
print('Vamos Jogar "Jock Ken Pon"'.center(30))
print('='*30)
nome = str (input('Digite o teu nome: '))
print(f'''{nome}, Qual das Opções:
[1] - Pedra
[2] - Tesoura
[3] - Papel''')
print('-'*30)
computador = random.randint(1, 3)
opc = int(input('Qual é a sua Opção: '))
print('-'*30)
time.sleep(1)
print('Jock ...')
time.sleep(1)
print('Ken ...')
time.sleep(1)
print('Pon ...')
print('-'*30)
#J Opcão do ogador
if opc == 1:
    print(f'{nome}, Escolheste Pedra')
elif opc == 2:
    print(f'{nome}, Escolheste Tesoura')
elif opc == 3:
    print(f'{nome}, Escolheste Papel')
else:
    print('Opção invalida')
    #Opçao do computador
if computador == 1:
    print('O computador escolheu Pedra')
elif computador == 2:
    print('O computador escolheu Tesoura')
else:
    print('O computador Escolheu Papel')
print('-'*30)
    # Decisao final
if computador == opc:
    print('O Jogo esta empate')
elif computador == 1 and opc == 2:
    print('Computador Ganhou')
elif computador == 1 and opc == 3:
    print(f'{nome}, Ganhaste')
elif computador == 2 and opc == 1:
    print(f'{nome}, Ganhaste')
elif computador == 2 and opc == 3:
    print('O computador Ganhou')
elif computador == 3 and opc == 1:
    print('O computador Ganhou')
elif computador == 3 and opc == 2:
    print(f'{nome}, Ganhaste')
print('Foi prazer Jogar contigo. Ate a proxima')