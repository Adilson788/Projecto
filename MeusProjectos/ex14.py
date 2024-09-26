#condição do aluno
# Usando Dicionario.
classificação = {}
classificação['Nome'] = str(input('Nome: '))
classificação['Média'] = float(input('Media: '))
if classificação['Média'] >= 10:
    classificação['Situação'] = 'Aprovado'
else:
    classificação['situação'] = 'Reprovado'
for k, valores in classificação.items():
    print(f'{k} é igual á {valores}')