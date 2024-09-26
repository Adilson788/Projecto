num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o ultomo  valor: ')))
print('='*30)
print('Os numero da dupla são:', end=' ')
for n in num:
    print(n, end=' ')
print(f'\nO numero 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 foi digitado na {num.index(3)+1}º posição')
else:
    print('O numero 3 noa foi encontrado em nenhuma posiçao')
print('Numeros pares: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')