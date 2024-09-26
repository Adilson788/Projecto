gerar = [[], []]
for c in range(1,8):
    num = int(input(f'Digite o {c}º Numero: '))
    if num % 2 == 0 and num != 0:
        gerar[0].append(num)
    elif num % 2 == 1:
       gerar[1].append(num)
print(f'Os pares sao: {sorted(gerar[0])}')
print(f'Os impares sao: {sorted(gerar[1])}')
