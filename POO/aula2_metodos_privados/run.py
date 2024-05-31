class Pessoa:
    def __init__(self, altura, cpf) -> None:        # Porque esse (-> None:) ?
        self.altura = altura
        self.__cpf = cpf        # Posso também declarar este atributo privado com dois __ antes

    def apresetar(self):
        print(f'Olá! Minha altura - {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):      # Ao declarar o método com dois __ na frente, torna este método privado
        print(f'Meu documento - {self.__cpf}')        # E só pode ser acessado dentro da própria classe

# Como um objeto, o método privado se torna inacessível
# Mas dentro da minha classe eu posso, chamar esse método
jorge = Pessoa('1.70', '123456')
jorge.__cpf = '123abc'
print(jorge.__cpf)
jorge.apresetar()
