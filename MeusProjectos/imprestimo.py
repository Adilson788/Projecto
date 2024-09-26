empréstimo = float(input('Empréstimo de: '))
salario = float(input('Seu Salario Mensal: '))
parcelas = int(input('Com quantas parcelas pretende pagar? :'))
salario_30_p = salario * 30 /100
juro_16_p_empréstimo = empréstimo * 16 / 100
total_apagar = empréstimo + juro_16_p_empréstimo
prestação = total_apagar / parcelas
print('='*38)
if 6 <= parcelas <= 36:
    if prestação <= salario_30_p:
        print(f'\033[33mEmpréstimo Concedido.\033[m')
        print(f'Felizmente, o valor da prestação mensal de : {prestação:.2f}kz, '
              f'\nnão passou os 30 % do seu Salário, que é de {salario_30_p:.2f} kz')
        print(f'durante os {parcelas} meses, vais pagar um total de {total_apagar} kz,'
              f'\njá com uma taxa de juros de 16 % do valor do Empréstimo.'
              f'\nO seu Salário será de: {salario - prestação:.2f} kz')
    else:
        print('\033[31mEmpréstimo Negado\033[m')
        print('A prestação a pagar, passou os 30% do seu salário')
else:
    print('\033[31mEmprestimo Negado')
    print('Infelizmente não Aceitamos menos de 6 parcelas, nem mais de 37 parcelas\033[m')
print('Obrigado! Volte Sempre.')