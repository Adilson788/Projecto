import datetime
print('='*30)
print('Alistamento Militar'.center(30))
print('='*30)
Nome = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.datetime.today().year
idade = ano_atual - nascimento
if idade == 18:
    print(f'{Nome}, voce deve se Apresentar, porque neste ano de {ano_atual} completas {idade} anos')
elif idade < 18:
    faltam = 18 - idade
    print(f'{Nome}, tens {idade} anos, falta(m) {faltam} anos, deves se alistar no ano de {ano_atual + faltam}')
elif idade > 18:
    passaram = idade - 18
    print(f'{Nome}, tens {idade} anos, ja passaram {passaram} anos, voce se apresentou no ano de {ano_atual - passaram}')
