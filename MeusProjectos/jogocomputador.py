import random
computador = random.randint(1, 100)
tot = 1
print('-'*35)
print('Ola meu nome é Quilha (sou virtual)'.center(35))
print('Pensei num número de 1 a 100.'.center(35))
print('Tente Acertar!'.center(35))
print('-'*35)
nome = str(input('Qual é o seu nome?: '))
while True:
    jogador = int(input(f'{nome}, diz o numero que pensei: '))
    if 0 < jogador <= 100:
        if jogador > computador:
            print(f'   {nome}, Chute um Valor mais Baixo')
        if jogador < computador:
            print(f'   {nome}, Chute um valor mais alto')
        if jogador == computador:
            print(f'   Parabens {nome}, voce Acertou')
            break
    else:
        print(f'{nome}, Voce digitou um numero invalido')
    tot +=1
print('-'*40)
print(f'O Quilha pensou em {computador}, voce pensou em {jogador} ')
print(f'{nome} para acertar precisaste de {tot} tentativas')