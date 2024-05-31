# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''from random import randint
win = 0
while True:
    player = int(input('Digite um valor: '))
    computer = randint(0,10)
    total = player + computer
    option = ' '
    while option not in 'PI':
        option = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {computer}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if option == 'P':
        if total % 2 == 0:
            print('VOcê ganhou!')
            win += 1
        else:
            print('Você perdeu!')
            break
    elif option == 'I':
        if total % 2 == 1:
            print('Você ganhou!')
            win += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {win}x')'''

# CÓDIGO ACIMA FOI FEITO JUNTO COM A RESOLUÇÃO DO GUANABARA
# EU NÃO CONSEGUI FAZER, PORQUE EU NÃO ENTENDI COMO FUNCIONAVA O PAR OU IMPAR
# SEMPRE QUE EU JOGAVA PAR OU IMPAR, JOGAVA COM 2 DEDOS PARA PAR E A OUTRA PESSOA COM 1 DEDO PARA IMPAR
# FIQUEI SEM SABER O QUE USARIA NO RANDOM.RANDINT
# EM RESUMO:
# VOU TENTAR FAZER A MINHA SOLUÇÃO!

from random import randint
from time import sleep

print('-='*20)
print('Vamos jogar PAR ou ÍMPAR?')
print('-='*20)

win = 0

while True:

    n_player = int(input('Digite um valor: '))
    n_computer = randint(0, 10)
    total = n_player + n_computer
    option = ' '
    while option not in 'PI':
        option = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]

    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)

    print('-'*20)
    print(f'Você jogou: {n_player}')
    print(f'Computador: {n_computer} ')
    print(f'🧐 ({n_player} + {n_computer} = {total})')
    print('-' * 20)

    print('.', end='')
    sleep(0.5)
    print('.', end='')
    sleep(0.5)
    print('.')
    sleep(0.5)

    print('💁‍♂️ DEU PAR!' if total % 2 == 0 else '💁‍♂️ DEU IMPAR!')

    if 'P' in option:
        if total % 2 == 0:
            print('VOCÊ GANHOU! 🎉🎉🎉🎊')
            print('-' * 20)
            win += 1
        else:
            print('VOCÊ PERDEU! 🤖🎉🎉🎊 ')
            print('-' * 20)
            break
    elif 'I' in option:
        if total % 2 == 1:
            print('VOCÊ GANHOU! 🎉🎉🎉🎊')
            print('-' * 20)
            win += 1
        else:
            print('VOCÊ PERDEU! 🤖🎉🎉🎊')
            print('-' * 20)
            break

    print('😈 Vamos jogar novamente...')
    print('-' * 20)
print(f'💀GAME OVER!💀 Você venceu {win} vezes.')


# OK DEI UMA CAPRICHADA, CONSEGUI FAZER SOZINHO DEPOIS QUE ENTENDI A LÓGICA
# PARECE BESTA, MAS FOI ISSO MESMO.
