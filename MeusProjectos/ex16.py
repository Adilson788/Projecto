# Cadrastamento de funcionario com numero de agente se tiver.
from datetime import datetime
func_publico = {}
func_publico['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento
func_publico['idade'] = idade
func_publico['N_Agente'] = int(input('N_Agente: '))
if func_publico['N_Agente'] == 0:
    print('=' * 30)
    for k, v in func_publico.items():
        print(f'{k} tem o valor de {v}')
else:
    if func_publico['N_Agente'] > 0:
        func_publico['Contração'] = int(input('contração: '))
        func_publico['Salario'] = float(input('Salario: '))
        aposentadoria = (func_publico['Contração'] + 35) - ano_atual
        func_publico['Aposentadoria'] = idade + aposentadoria
        print('='*30)
        for k, v in func_publico.items():
            print(f'{k} tem o valor de {v}')

