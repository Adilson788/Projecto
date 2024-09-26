class carro:
    #caracteristicas da minha classe
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def valordocarro(self, preco):
        if preco >= 600000:
            print('Carro muito caro')
        else:
            print('Preco acessivel e recomendando')


meu_carro = carro("toyota","XTV25")
print(meu_carro.marca)
meu_carro.valordocarro(int(input("Preço: ")))


