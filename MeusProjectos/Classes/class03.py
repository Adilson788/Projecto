class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self, idade):
        if self.idade >= idade:
            print(f'Ola, meu nome é {self.nome} tenho {self.idade} anos, sou um homem adulto')
        else:
            print(f'eu sou o {self.nome} ainda não atingui a madureza')


humano = Pessoa("Adilson", 45)
humano.apresentar(40)