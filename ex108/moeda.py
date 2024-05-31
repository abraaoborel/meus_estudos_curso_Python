# O encunciado do ex107 pede o seguinte:
# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar()
# diminuir()
# dobro()
# metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# ========================/=============================

# Como estamos trabalhando com moeda, vou fazer pedir um parâmetro preço, e taxa pra porcentagem

def aumentar(preço=0, taxa=0):
    res = preço + (preço * taxa/100)   # para aumentar o preço, calculo a porcentagem a ser aumentada e somo ao preço
    return res      # lá na frente vc vai ver que isso vai simplificar muito a nossa vida!


def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda='R$'):     # lembre-se: dentro das aspas () está o parâmetro!
    return f'{moeda}{preço:>.2f}'.replace('.', ',')      # onde tiver ponto, vou colocar uma vírgula
