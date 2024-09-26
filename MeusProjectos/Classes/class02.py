#lista  de cadastrado da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        lista_planos = ['basic', 'premium']
        if plano in lista_planos:
            self.plano = plano
        else:
            raise Exception('Não temos disponivel esse plano')

dados_cliente = Cliente('Adilson', 'Adilson@gmail.com', 'basic')
print(dados_cliente.nome)
dados_cliente.plano