from moeda import *
p = float(input('Digite o preço: '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'O Aumentando 10% no valor de {moeda(p)} é {moeda(aumento(p))}')
print(f'O desconto de 13% no valor de {moeda(p)} é {moeda(reduzir(p))}')


