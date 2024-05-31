class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None     # __valor (atributo privado)
        self.__elem = None

    # método publico
    def setter_valor(self, valor: int) -> None:   # -> None estou dizendo que não é para retornar nada
        self.__valor = valor        # __valor (atributo privado)

    # método publico
    @property   # proporciona agente olhar para um método como se ele fosse um atributo da nossa Classe
    def getter_valor(self) -> int:
        return self.__valor     # __valor (atributo privado)


my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor)

# Apesar de mostrar o property o programador lhama não recomendou a utilização dele para "mascarar" um método
# Ele disse que prefere utilizar métodos como métodos e atributos como atributos