
def notas(*num, sit = False):
    '''
     -->
    :param num: recebe varias notas do aluno
    :param sit: Valor opcional para mostrar a situação do aluno
    :return: retorna um dicionario com as informações dos alunos (Qtdade de notas, media, maior e menor nota)
    '''
    dic = {}
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Media'] = sum(num) / len(num)
    if sit:
        if dic['Media'] >= 17:
            dic['Situação'] = 'Excelente'
        elif dic['Media'] >= 14:
            dic['Situação'] = 'Boa'
        elif dic['Media'] >= 10:
            dic['Situação'] = 'Razoavel'
        elif dic['Media'] >= 7:
            dic['Situação'] = 'Mal'
        elif dic['Media'] < 7:
            dic['Situação'] = 'Pessima'
    return dic

#programa principal
resp = notas(15, 18, 18, 19, sit=True)
print(resp)