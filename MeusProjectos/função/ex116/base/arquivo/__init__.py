from função.ex116.base.interface import *

def arquivoExiste(familia):
   try:
       a = open(familia, 'rt')
       a.close()
   except FileNotFoundError:
       return False
   else:
       return True

def criarquivo(familia):
    try:
        a = open(familia, 'wt+')
        a.close()
    except:
        print('Erro: Houve um Problema na criação do Arquivo')
    else:
        print(f'Arquivo {familia} foi Criado com Sucesso')

def leraquivo(familia):
    try:
        a = open(familia, 'rt')
    except:
        print('Houve um problrma ao ler o Arquivo')
    else:
        cabeçalho('\033[32mPessoas Cadastradas\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1]= dado[1].replace('\n',' ')
            print(f'{dado[0]}{dado[1]}')
    finally:
        a.close()

def cadastrar(familia, nome = 'Desconhecido', idade = 0):
    try:
        a = open(familia, 'at')
    except:
        print('Houve um Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome.ljust(28)};{idade} anos\n')
        except:
            print('Houve um problema ao escrever')
        else:
            print(f'Novo registo de {nome} Adicionado com Sucesso')
            a.close()


