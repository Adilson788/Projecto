#Calculo por excesso de velocidade
minha_veloc = float(input('Velocidade percorrrida: '))
vel_maxima = 80
if minha_veloc <= vel_maxima:
    print('Boa viagem! ande com segurança.')
else:
    multa = (minha_veloc - vel_maxima) * 700
    print(f'Excesso de velocidade. Voce foi multado. o Total da Multa foi de {multa} kz.')