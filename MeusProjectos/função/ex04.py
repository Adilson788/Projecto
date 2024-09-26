def ficha(n='<desconhecido>', gol=0):
    print(f'O {n} fez tantos {gol} golos')
#programa principal
nome = str(input('Jogador: '))
golos = str(input('Golos: '))
if golos.isnumeric():
    golos =int(golos)
else:
    golos = 0
if nome.strip() =='':
    ficha(gol=golos)
else:
    ficha(nome, golos)


