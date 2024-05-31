# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois ele vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for x in range(0, total):
        partidas.append(int(input(f'   Quantos gols na partida {x+1}? ')))
# Eu quero que o valor digitado nessa lista, vá para o meu dicionário
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k}, tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]}, jogou {total} partidas.')   # ou invés do {len(jogador["gols"]}
for i, v, in enumerate(jogador['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
