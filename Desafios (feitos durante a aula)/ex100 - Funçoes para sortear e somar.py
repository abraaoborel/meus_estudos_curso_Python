# Faça um programa que tenha uma lista chamada números
# e duas funções chamadas sorteia()e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 5)       # n recebe 5 valores aleatórios de randint      # Guanabara fez randint(1, 10)
        lista.append(n)         # lista vai receber os 5 valores aleatórios recebidos em n
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    s = 0       # soma recebe 0
    for v in lista:     # Para cada valor em lista
        if v % 2 == 0:      # Se for um número par
            s += v      # s recebe ele mesmo + valor
    print(f'Somando os valores pares da {lista}, temos {s}')


# Programa Principal
numeros = list()
sorteia(numeros)
somaPar(numeros)
