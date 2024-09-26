listageral = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    partidas = int(input('Quantas partidas jogou: '))
    gols.clear()
    for c in range (1, partidas + 1):
        gols.append(int(input(f'  Quantos gols marcou na {c}º partida?: ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    listageral.append(jogador.copy())
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer Continuar? [S/N]: '))[0].strip().upper()
    if resposta == 'N':
        break
print('-='*30)
print(f'Cod'.ljust(3), f'Nome'.ljust(15), f'Gols'.ljust(15), f'Total'.rjust(10))
print('-='*30)
for k, v in enumerate(listageral):
    print(f'{k}'.ljust(3), f'{v['Nome']}'.ljust(15), f'{v['Gols']}'.ljust(15), f'{v['Total']}'.rjust(10))
print('-='*30)
while True:
    visualizar = int(input('Digite o codigo do Jogador para Visualizar: [999 para Interroper]: '))
    print('-=' * 30)
    if visualizar == 999:
        break
    elif 0 <= visualizar <= len(listageral) - 1:
        print(f'Dados do Jogador {listageral[visualizar]['Nome']}'.center(30))
        for i, gol in enumerate(listageral[visualizar]['Gols']):
            print(f'   No {i+1}º jogo fez {gol} golos')
            print('-=' * 30)
    else:
        print('Lamentamos o numero solitado nao esta na lista')
print('volte Sempre!')