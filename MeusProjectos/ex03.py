import random
n_aleatorios = (random.randint(1,10),
                random.randint(1,10),
                random.randint(1,10),
                random.randint(1,10),
                random.randint(1,10))
print('Os numeros gerados são: ', end='')
for n in n_aleatorios:
    print(n, end=' ')
print()
maior = max(n_aleatorios)
print(f'O Maior valor é o {maior}')
menor = min(n_aleatorios)
print(f'O Menor valor é o {menor} ')
