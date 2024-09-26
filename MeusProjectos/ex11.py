from random import randint
sorteiro = []
geral = []
jogadas = int(input('Quanto jogos quer ver: '))
cont = 1
while cont <= jogadas:
    quant = 0
    while True:
        num = randint(1, 60)
        if num not in sorteiro:
            sorteiro.append(num)
            quant += 1
        if quant >= 6:
            break
    sorteiro.sort()
    geral.append(sorteiro[:])
    sorteiro.clear()
    cont += 1
print('=='*3, f'Sorteiados {jogadas} Jogos', '=='*3)
for i, v in enumerate(geral):
    print(f'{i + 1}º Jogo : {v}')