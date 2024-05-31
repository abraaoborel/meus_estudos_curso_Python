# Melhore o jogo do DESAFIO 028 onde o computador
# vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

'''from random import randint
from time import sleep

print('=='*20)
print('VOU PENSAR EM UM NÚMERO DE, 0 À 10!')
print('=='*20)

sleep(0.25)
print('.', end='')
sleep(0.25)
print('.', end='')
sleep(0.25)
print('.', end=' ')
sleep(0.25)
print('PRONTO!')

n_a = randint(0, 10)

n_p = int(input('Agora, adivinhe se for capaz: '))
contador = 1
while n_a != n_p:
    n_p = int(input('Tente novamente: '))
    if n_a < n_p:
        print('É menos...')
    else:
        print('É mais...')
    contador += 1
if contador <= 1:
    print('NA CADAGA EM!')
print(f'Acertou com {contador} tentativas! Parabéns!')'''

# MINHA SOLUÇÃO ACIMA! FICOU TOP!
# O GUANABARA FEZ A DELE, FICOU ASSIM!

from random import randint
na_pc = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertar = False
palpites = 0
while not acertar:
    n_player = int(input('Qual é o seu palpite? '))
    palpites += 1
    if n_player == na_pc:
        acertar = True
    else:
        if n_player < na_pc:
            print('É mais... Tente novamente: ')
        elif n_player > na_pc:
            print('É menos... Tente novamente: ')
print(f'Acertou, com {palpites} tentativas. Parabens!')

# A maior diferença aqui, é que ele colocou o chute do jogador como False, e uma condição para se tornar True
# Caso o chute for igual ao número aleatório.
