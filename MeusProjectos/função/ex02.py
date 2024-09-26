from datetime import datetime
def voto(valor):
    data = datetime.now()
    ano_atual = data.year
    idade = ano_atual - valor
    if idade < 18:
        return f' Tens {idade} anos! Não votas'
    elif 18 <= idade <= 60:
        return f' Tens {idade} anos! voto Obrigatório'
    else:
        return f' {idade} anos! Voto Opcional'

#programa principal
nas = int(input('Ano de nascimento: '))
print(voto(nas))