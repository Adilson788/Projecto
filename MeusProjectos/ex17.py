jogador = {}
gols = []
jogador['Nome'] = str(input('Nome: '))
partidas = int(input('Quantas partidas jogou: '))
for c in range (1, partidas + 1):
    gols.append(int(input(f'  Quantos gols marcou na {c}º partida?: ')))
jogador['Gols'] = gols
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O Jogador {jogador['Nome']} jogou {partidas} partidas.')
for k, v in enumerate(gols):
    print(f'Na {k +1}º patida, fez {v} gols')
