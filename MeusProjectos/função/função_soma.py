def soma_pares(*numeros):
    """
    Soma dos os numeros pares da minha lista
    :param num: uma coleçao de numeros impares e pares
    :return: soma de todos os pares na lista
    """
    par = 0
    for numero in numeros:
        if numero % 2 == 0:
            par += numero
    return par

def soma_impares(*numeros):
    """
    Calculo de todos os numero impares
    :param numeros: coleçao de todos os numeros impares e pares
    :return: apenas os numeros impares
    """
    impar = 0
    for numero in numeros:
        if numero % 2 == 1:
            impar += numero
    return impar
