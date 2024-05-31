from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transaçao:
    descricao: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print(
            f'DESCRIÇÃO: {self.descricao} | VALOR: {self.valor} | CATEGORIA: {self.categoria.nome}'
        )
        