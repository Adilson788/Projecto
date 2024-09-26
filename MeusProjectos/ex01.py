n_extensao = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')

while True:
    n = int(input('Digite o valor: '))
    if 0 <= n <=10:
        print(f'Voce digitou o numero: \033[32m{n_extensao[n]}\033[m')
    else:
        print('\033[31mLamentamos. O numero digitado esta fora da margem\033[m')
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?: ')).strip().upper()                                    
    if resp == 'N':
        break
print('Obrigado. Volte Sempre')