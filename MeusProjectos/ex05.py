nomes = ('Adilson','Cecilia','Dilcio','Graciel','Leticia','Fausta','Joao','Juliana','Paulino')
print('='*40)
print('Nomes da Familia - Vogais'.center(40))
print('='*40)
for nome in nomes:
    print(f'\nNo nome \033[33m{nome}\033[m temos :', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(f'\033[32m{letra.lower()}\033[m', end=' ')
