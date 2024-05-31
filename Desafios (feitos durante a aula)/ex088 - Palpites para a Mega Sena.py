# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
# Como eu preciso de números aleatórios já vou chamar da biblioteca random o randint

lista = list()      # lista temporária
jogos = list()      # lista permanente
print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)
qntd = int(input('Quantos jogos você quer que eu sorteie? '))   # Eu preciso sortear quantas vezes o usuário pedir
total = 1   # total de vezes que ele vai sortear
while total <= qntd:    # Enquanto total, for menor igual à qntd, a estrutura a seguir vai ser executada
    cont = 0
    while True:     # Loop infinito
        num = randint(1, 60)    # Primeiro: fazer um número ser randomizado, enunciado pediu de 1 até 60
        if num not in lista:    # Se o número não estiver na lista
            lista.append(num)   # Ele vai ser adicionado
            cont += 1       # Se ele for adicionado cont recebe ele mesmo + 1
        if cont >= 6:       # Isto é, ele já sorteou 6 números
            break           # Eu dou um break
    lista.sort()    # Antes de mostrar a lista, vamos organizar ela
    jogos.append(lista[:])      # crio uma cópia da lista e dou um append() para a lista jogos
    lista.clear()           # e essa lista temporária vai receber um clear(), zerando a mesma
    total += 1      # Aqui eu faço total += 1 para interrromper o loop infinito
print('-=' * 3, f' SORTEANDO {qntd} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):   # o enumerate() trata o i (inidice) e a, l (lista). Exmp. se eu colocar 2 jogos, 0 e 1
    print(f'Jogo {i+1}: {l}')   # {i+1} para não começar com o 0
    sleep(1)    # intervalo de 1 seg, entre os jogos que forem sorteados
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
