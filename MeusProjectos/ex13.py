pauta = []
aluno = []
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    for nota in aluno:
        if len(aluno) >= 0:
            media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    pauta.append(aluno[:])
    aluno.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str (input('Quer continuar ? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('='*30)
print('No'.ljust(4), 'Nome'.ljust(15), 'Media'.rjust(7))
print('='*30)
for i, v in enumerate(pauta):
    print(f'{i}'.ljust(4), f'{v[0]}'.ljust(15), f'{v[3]}'.rjust(7))
print('-'*30)
while True:
    visualizar = int (input('Codigo do aluno para ver as Notas [interroper: 999]: '))
    print('-'*30)
    if visualizar == 999:
        print('Estamos encerrando o Programa.')
        break
    elif 0 <= visualizar <= len(pauta) - 1:
        print(f'Notas do Aluno: \033[32m {pauta[visualizar][0]} \033[m'.center(30))
        print('Nota1'.ljust(6), 'Nota2'.ljust(10), 'Média'.rjust(7) )
        print(f'{pauta[visualizar][1]}'.ljust(6), f'{pauta[visualizar][2]}'.ljust(10), f'{pauta[visualizar][3]}'.rjust(7) )
        print('-' * 30)
    else:
        print('Lamentamos! O Registo Solicitado não Existe.')
print('Volte sempre!')
