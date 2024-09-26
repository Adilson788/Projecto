def factorial(valor, show = False):
    print(f'{n}! = ', end='')
    f = 1
    for c in range (valor, 0, -1):
        if show:
            if c > 1:
                print(c, 'x', end=' ')
            else:
                print(c, '=', end=' ')
        f *= c
    return f

#programa princiapl
n = int(input('Digite o numero: '))
print(factorial(n, show=True))