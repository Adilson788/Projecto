dados = []
while True:
    n = int(input('Digite um Valor: '))
    if n not in dados:
        dados.append(n)
        print('Valor Adicionado com sucesso')
    else:
        print('Não Vou Adicionar. Valor duplicado.')
    resp = ' '
    while resp not in 'SN':
        resp = str (input('Quer Continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'Os Valores da lista inseridos São: {sorted(dados)}')