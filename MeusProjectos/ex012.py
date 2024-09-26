ficha = []
castramento = []
maior = menor = 0
while True:
    castramento.append(str(input('Nome: ')))
    castramento.append(int(input('Peso: ')))
    if len(ficha) == 0:
        maior = menor = castramento[1]
    else:
        if castramento[1] > maior:
            maior = castramento[1]
        if castramento[1] < menor:
            menor = castramento[1]
    ficha.append(castramento[:])
    castramento.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar-[S/N]?: ')).strip().upper()
    if resp == 'N':
        break
print(f'O total de pessoas castrados sao {len(ficha)}')
print(f'O maior Peso é de {maior} kg')
for valor in ficha:
    if valor[1] == maior:
        print(f'[{valor[0]}]', end=' ')
print(f'\nO peso mais leve é de {menor} kg', end=' ')
for valor in ficha:
    if valor[1] == menor:
        print(f'[{valor[0]}]', end=' ')
