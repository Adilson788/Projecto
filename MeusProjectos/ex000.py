from datetime import datetime
print('-'*52)
print('Programa que encontra a Idade e o numero do Calcado'.center(52))
print('-'*52)
calcado = int(input('N_Calçado: '))
multiplicador = 100
tenho = calcado * multiplicador
ano_nascimento = int (input('Ano de Nascimento: '))
reducao = tenho - ano_nascimento
ano_atual = datetime.today().year
resultado = reducao + ano_atual
convertido = str(resultado)

print(f'O numero do teu  Calçado é {convertido[:2]} e a tua idade é {convertido[2:]} anos')