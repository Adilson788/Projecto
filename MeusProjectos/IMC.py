print('='*32)
print('Calculo do IMC'.center(32))
print('Índice de Massa Corporal'.center(32))
print('='*32)
nome = str(input('Nome: '))
while True:
    try:
        altura = float(input('Sua Altura: '))
        if isinstance(altura, float):
            break
    except ValueError:
        print('\033[31mErro! valor invalido. apenas numero. Tente Novamente\033[m')
while True:
    try:
        peso = float(input('Seu Peso: '))
        if isinstance(peso, float):
            break
    except ValueError:
        print('\033[31mErro! valor invalido. apenas numero. Tente Novamente\033[m')
m = peso / pow(altura, 2)
if m < 18.5:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('É provavél que estais a enfrentar uma carência nutricional'
          '\ne risco de saúde associada a desnutrição.')
elif 18.5 <= m < 24.9:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('Tens um peso ideal e está associada '
          '\nao menor risco de doenças crônicas e complicações de saúde.')
elif 25 <= m < 29.9:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('Estais a baixo da Obesidade,'
          '\nmas se o peso aumentar corres o risco de desenvolver diabetes do tipo 2.')
elif 30 <= m < 34.9:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('Estais na Obesidade. Podes acarretar uma série de problemas de saúde, '
          '\nincluindo doenças cardiovasculares, problemas respiratórios e articulares.')
elif 35 <= m < 39.9:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('Estais com Obesidade de Grau II. Os riscos à saúde são significativamente elevados, e a possibilidade '
          '\nde desenvolver diabetes tipo 2, apneia do sono e outras condições graves é maior. ')
elif m >= 40:
    print(f'{nome}, O seu IMC é de {m:.2f}.')
    print('Estais com Obesidade Grau III. Os riscos à saúde é extremamente grave. Suas complicações podem incluir '
          '\nproblemas cardíacos graves, dificuldades respiratórias e maior suscetibilidade a infecções. ')
print(f'{nome}, Volte sempre para confirmar se estais com o peso ideal.')