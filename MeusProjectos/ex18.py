# Criar um programa que leia nome, sexo e idade
# de varias pessoas. guardando os dados de cada pessoa em
# um dicionario e todos os dicionarios em uma lista
dados = {}
geral = []
soma = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    geral.append(dados.copy())
    dados.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer Continuar? [S/N]: ')).strip().upper()
    if resposta == 'N':
        break
print('='*30)
print(f'A) Ao todo foram cadastrada {len(geral)} Pessoas')
media = soma / len(geral)
print(f'B) A media de idade do grupo é de {media:.2f} anos.')
print(f'C) As mulheres Cadastradas são: ', end='')
for k, valor in enumerate(geral):
    if valor['Sexo'] == 'F':
        print(f'[{valor['Nome']}]', end='')
print()
print('D) Os cadastrados acima da media: ')
for k, valor in enumerate(geral):
    if valor['idade']>= media:
        print(f'Nome = {valor['Nome']}; Sexo = {valor['Sexo']}; idade = {valor['idade']}.')






