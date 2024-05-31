# Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição da tabela está o time da Chapecoense.


tabela = ('Botafogo FR RJ', 'Atletico Mineiro MG', 'Red Bull Bragantino SP', 'CA Paranaense PR',
          'Bahia', 'Internacional RS', 'Cruzeiro', 'Flamengo', 'Gremio', 'Criciúma', 'Fortaleza CE',
          'Palmeiras SP', 'EC Juventude RS', 'São Paulo FC SP', 'Corinthians SP', 'Fluminense RJ',
          'Vasco Gama', 'EC Vitória BA', 'AC Goianiense GO', 'Cuiabá Esporte Clube MT')

'''for t in tabela:
    print(t)'''

topo = tabela[:5]
lanterna = tabela[-4:]
ordem_alfab = sorted(tabela)
posiçao = tabela.index("Cruzeiro")+1

while True:
    print('''
    O que você quer ver na Tabela do Brasileirão:
    
    a) Os 5 primeiros colocados
    b) Os 4 últimos colocados
    c) A lista com todos os times em ordem alfabética
    d) Em que posição está o Cruzeiro
    ''')

    opçao = ' '
    while opçao not in 'abcd':
        opçao = str(input('Digite a sua opção: ')).strip().lower()[0]
        if opçao == 'a':
            print(f'Os 5 times no topo da tabela são: \n{topo}')
        elif opçao == 'b':
            print(f'Os 4 times da lanterna são: \n{lanterna}')
        elif opçao == 'c':
            print(f'A lista com todos os times em ordem alfabética são: {ordem_alfab}')
        elif opçao == 'd':
            print(f'O Cruzeiro está em {posiçao}° lugar na Tabela')
        else:
            print('Opção inválida! Tente Novamente. ', end='')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nQuer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('FIM')
