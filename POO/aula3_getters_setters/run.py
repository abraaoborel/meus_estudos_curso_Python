class MinhaClasse:
    def __init__(self) -> None:     # Estou dizendo que não é para retornar
        self.__valor = None     # __valor (atributo privado)
        self.__elem = None

    # método publico
    def setter_valor(self, valor: int) -> None:   # -> None estou dizendo que não é para retornar nada
        self.__valor = valor        # __valor (atributo privado)

    # método publico
    def getter_valor(self) -> int:      # O retorno desejado desse getter_valor é um inteiro
        return self.__valor     # __valor (atributo privado)


my_class = MinhaClasse()
# my_class.valor = 3  # Ferindo o encapsulamento
my_class.setter_valor('4aaa2')
valor = my_class.getter_valor()
print(valor)
