
cor = (                     # Índice da tupla de cores:
    '\033[m',               # 0 - Zero
    '\033[1;31m',           # 1 - negrito, letra vermelha
    '\033[1;32m',           # 2 - negrito, letra verde
    '\033[1;34m',           # 3 - negrito, letra azul
    '\033[1;97;41m',        # 1 - negrito, letra branca, fundo vermelho
    '\033[1;97;42m',        # 2 - negrito, letra branca, fundo verde
    '\033[1;97;44m',        # 3 - negrito, letra branca, fundo azul
    '\033[1;7;97;41m',      # 4 - negrito, negativo, letra branca, fundo vermelho
    '\033[1;7;97;42m',      # 5 - negrito, negativo, letra branca, fundo verde
    '\033[1;7;97;44m',      # 6 - negrito, negativo, letra branca, fundo azul
)

player = [
    {'nome':'SHEREK'},
    {'level':1},
    {'exp':0},
    {'exp_max':50},
    {'hp':100},
    {'hp_max':100},
    {'atack':30},
    {'defesa':15}
]

monster = [
    {'nome':'MONSTRO DO VALE'},
    {'vida':100},
    {'vida_max':100},
    {'atack':20},
    {'defesa':15}
]

def combate():

    # player ataca
    player_ataca = monster[2]['vida_max'] - player[6]['atack']
    monster.append(player_ataca)
    print(player_ataca)

    # monstro revida
    mostro_revida = player[5]['hp_max'] - monster[3]['atack']
    player.append(mostro_revida)
    print(mostro_revida)

combate()



