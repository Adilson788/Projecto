listagem = []
maior = menor = 0
for c in range(0, 5):
    listagem.append(int(input(f'Digite o numero {c}: ')))
    if c == 0:
        maior = menor =listagem[c]
    else:
        if listagem[c] > maior:
            maior = listagem[c]
        if listagem[c] < menor:
            menor = listagem[c]
print(f'Os valores da lista fora {listagem}')
print(f'O maior Valor é {maior} as psicçoes: ', end=' ')
for pos, v in enumerate(listagem):
    if v == maior:
        print(f'{pos}...', end=' ')
print(f'\nO menor Valor é {menor}', end=' ')
for pos, v in enumerate(listagem):
    if v == menor:
        print(f'{pos}...', end=' ')