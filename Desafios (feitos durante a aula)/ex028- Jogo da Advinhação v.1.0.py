# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
num_pc = randint(0,5) # Faz o computador sortear um número, coloquei entre parênteses pq eu quero somente de 0 a 5
print('\033[31m-\033[32m=\033[m'*30)
print('\033[1;97;41mVou pensar em um número de 0 a 5. Advinhe se puder! 🙃\033[m')
print('\033[31m-\033[32m=\033[m'*30)
sleep(3)
num_player = int(input('\033[1;33;40mQual número eu pensei? 🤔\033[m ')) #jogador tenta advinhar
print('\033[97;44mPROCESSANDO... ⏳\033[m')
sleep(2)
if num_player == num_pc:
    print('\033[97;42m👏👏👏PARABENS!🥳🎉 Você conseguiu me vencer! 🤯 Não vou pegar leve na próxima! 😎\033[m')
else:
    print(f'\033[97;41m🤣🤣🤣VOCÊ PERDEU!😂😂😂 Eu pensei no número {num_pc} e não no {num_player}! 😎\033[m')

