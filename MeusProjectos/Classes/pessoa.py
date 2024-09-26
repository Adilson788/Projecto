class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return self.comendo
        print(f'O {self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f'O {self.nome} parou de comer')
            return
        print(f'O {self.nome} nao esta comendo')
        self.comendo = False

