from base.interface import *
from base.arquivo import *
from time import sleep

arq ='familiaagostinho.txt'
if not arquivoExiste(arq):
    criarquivo(arq)

while True:
    resp = lista(['Cadastrar Pessoas', 'Listar Pessoas', 'Saindo do Programa... ate logo'])
    if resp == 1:
        #Cadastrar uma nova pessoa
        cabeçalho('\033[32mNovo Cadastro\033[m')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 2:
        #listar pessoas cadastrads
        leraquivo(arq)
    elif resp == 3:
        sleep(1.5)
        cabeçalho('\033[31mSaindo do Programa... Ate logo\033[m')
        break
    else:
        print('\033[31mValor Invalido. Digite um valor Valido.\033[m')


