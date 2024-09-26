lista = []
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? S/N: ')).upper().strip()
    if resp == 'N':
        break
print(f'Lista dos Valores {lista}')
print(f'A) Ao todo foram digitados {len(lista)} Numeros')
print(f'B) Lista dos Valores em ordem decrescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print('C) O valor 5 foi digitado na lista')
else:
    print('C) O valor 5 não foi digitado na lista')








