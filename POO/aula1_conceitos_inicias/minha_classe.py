class MinhaClasse:

    def __init__(self, info, elem):     # metodo construtor é o primeiro a ser executado!
        self.atributo_1 = 'Meu Atributo'
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, 'a']
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):     # Self para dizer que este método está dentro da classe
        print('Minha ação 1')
        print('Minha ação 2')
        print(self.atributo_2)
        return 'Olá Mundo'

    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo_3[1] + numero)

# Objeto         # Classe    -> Instanciamos um objeto
minha_classe = MinhaClasse('info aqui no construtor', 213)

minha_classe.metodo_2(3)