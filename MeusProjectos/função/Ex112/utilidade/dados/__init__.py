def leiadinheiro(msg):
    verdade = False
    while not verdade:
        numero = str(input(msg)).replace(',','.').strip()
        if numero.isalpha() or numero == " ":
            print(f'O valor de nebtrda é invalido')
        else:
            verdade = True
        return float(numero)

