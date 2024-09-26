from fase import *
while True:
    resp = lista(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Programa'])
    if resp == 1:
        cabeçalho('Cadastrar Pessoas')
    elif resp == 2:
        cabeçalho('Listar Pessoas')
    elif resp == 3:
        cabeçalho('Sair do sistema... Ate logo.')
        break
    else:
        print('Valor Invalido. Tente Novamente')



