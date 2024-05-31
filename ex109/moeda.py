
# Vou adicionar esse parâmetro para formatar, como o padrão não é formatar format=False
def aumentar(preço=0, taxa=0, formato=False):
    """
    --> Aumenta o preço R$, de acordo com a taxa em %
    :param preço: Recebe um preço do usuário
    :param taxa: A taxa/porcentagem a ser aumentada(somada)
    :param formato: Para formatar, o preço somado. Caso formato=True
    :return: retorna preço + taxa/porcentagem
    """
    res = preço + (preço * taxa/100)   # para aumentar o preço, calculo a porcentagem a ser aumentada e somo ao preço
    return res if formato is False else moeda(res)
# Retorne res por padrão se o format é falso, senão ele vai chamar o método moeda, (que foi criado aqui dentro)


def diminuir(preço=0, taxa=0, formato=False):
    """
    --> Diminui do preço R$, de acordo com a taxa em %
    :param preço: Recebe um preço do usuário
    :param taxa: A taxa/porcentagem a ser subtraída do preço
    :param formato: Para formatar, o preço subtraído. Caso formato=True
    :return: retorna preço - taxa/porcentagem
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    Dobra o preço! *2
    :param preço: Recebe um preço do usuário.
    :param formato: Para formatar, o preço dobrado. Caso formato=True
    :return: retorna o dobro do preço.
    """
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    """
    Metade do preço! /2
    :param preço: Recebe um preço do usuário.
    :param formato: Para formatar, a metade do preço. Caso formato=True
    :return: retorna a metade do preço.
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$',):     # lembre-se: dentro das aspas () está o parâmetro!
    """
    --> Formata o resultado, para reais. Com R$ e virgula, ao invés do ponto.
    :param preço: Recebe um preço do usuário.
    :param moeda: Adiciona a esse valor uma string "R$" ao preço, e substituí o ponto pela vírgula.
    :return: Retorna preço, formatado. (Padrão: moeda Brasileira)
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')      # onde tiver ponto, vou colocar uma vírgula
