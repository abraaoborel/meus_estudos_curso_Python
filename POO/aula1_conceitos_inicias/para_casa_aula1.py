class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    def correr(self):
        return 'Estou correndo'

    def comer(self):
        return 'Estou comendo'

# Objeto /Classe(param)     --> Instânciamos um objeto
pessoa = Pessoa(1.70, 30)
print(f'Objeto(Pessoa) -> tem a altura = {pessoa.altura} \nObjeto(Pessoa) -> tem a idade = {pessoa.idade}')
print(f'Realizando o método correr() = {pessoa.correr()}')
print(f'Realizando o método comer() = {pessoa.comer()}')
