from random import randint
from time import sleep
def maior(*valores):
    for num in valores:
        sleep(1)
        print(num, end=' ')
    print(f'O total de numeros forma {len(valores)}')
    print(f'O maior valor é {max(valores)}')
    print('-'*32)
#programa principal
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10))
maior(randint(1, 10))
maior(0)