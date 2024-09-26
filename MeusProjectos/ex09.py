geral = []
pares = []
impares = []
while True:
    n = int(input('digite um valor: '))
    geral.append(n)
    if n % 2 == 0 and n!=0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar: S/N: ')).strip().upper()
    if resposta == 'N':
        break
print(f'Os numero d lista geral sao {geral}')
print(f'Os pares sao: {pares}')
print(f'Os ipares sao {impares}')
