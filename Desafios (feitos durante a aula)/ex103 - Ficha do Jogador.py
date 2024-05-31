# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


# Aqui em cima eu tenho que transformar os 2 parâmetros como opcionais, colocando um = ao lado deles

def ficha(nome='<desconhecido>', gol=0):   # Se eu não infomar o nome. nome=desconhecido/Se eu não iformar o gol. Gol=0
    print(f'O jogador {nome}, fez {gol} gol(s) no campeonato.')      # Aqui eu posso usar tanto o print quanto o return


# Programa Principal (Vamos começar por aqui)
n = str(input('Nome do Jogador: '))

# Número de gols nesse caso, não pode ser int, porque o input não a resposta vazia. Vamos trocar para str
g = str(input('Número de Gols: '))
if g.isnumeric():   # para verificar se (g) pode ser um número ou não
    g = int(g)      # Se o (g) for númerico, vou fazer com que (g) seja o int de (g)
else:       # Senão
    g = 0

# Vamos tratar agora a variável n
if n.strip() == '':     # Se eu tirei todos os espaços e ficou vazio
    ficha(gol=g)     # Se eu passei o nome como vazio, vou mostrar a qntd de gols (caso tiver apenas 1 parâmetro)
else:
    ficha(n, g)     # Aqui se tiver os 2 parâmetros preenchidos, vai passar o nome e a qntd de gols

# isso ta longe de ser uma validação de dados, más é uma proto validação!
