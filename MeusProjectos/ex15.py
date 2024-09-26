# cria um programa4 jogoadores joguem um dado,
# é tenha um resultado de forma aleatorios. guardando
#esse resultado em um dicionario. coloque em ordem. para ver o jogador que tirou o maior valor.
from random import randint
from time import sleep
aleatorios = {}
for c in range(1, 5):
    aleatorios[f'Jogador{c}'] = randint(1, 6)
for k, v in aleatorios.items():
    sleep(1)
    print(f'O {k} tirou {v}')
print('Kanking dos Jogadores')
dicionario_ordenado = dict(sorted(aleatorios.items(), key=lambda item: item[1], reverse=True))
cont = 0
for k, c in dicionario_ordenado.items():
    sleep(1)
    cont += 1
    print(f'{cont}ª {k} = {c}')
