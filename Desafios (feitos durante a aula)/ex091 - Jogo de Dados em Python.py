# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# exemplo:
# Valores sorteados:
# O jogador1 tirou 5
# O jogador2 tirou 2
# O jogador3 tirou 6
# O jogador4 tirou 1
# Ranking dos jogadores:
# 1º Lugar: Jogador3 com 6
# 2º Lugar: Jogador1 com 5
# 3º Lugar: Jogador2 com 2
# 4º Lugar: Jogador4 com 1
# =================//=========================

'''from random import randint

resultado = dict()
print('Valores sorteados:')
for jogador in range(1, 5):
    dado = randint(1, 6)
    print(f'{'':>5}O jogador{jogador} tirou {dado}')
print('Ranking dos jogadores:')'''
# Até esse ponto eu fui, depois daqui eu não consegui continuar
# Pq eu não estava conseguindo jogar o resultando do sorteio de dado, dentro do dicionário

# Vou começar do zero assistindo a resolução deste exercício:
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }

ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)   # (0) representa a key, e (1) representa o valor
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(0.5)