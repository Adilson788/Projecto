from pessoa import Pessoa
from dataclasses import dataclass

humano = Pessoa('Adilson', 35)
humano.comer('Manga')
humano.parar_comer()
humano.comer('Manga')
humano.parar_comer()

@dataclass
class categoria:
    nome: str
    idade: int

