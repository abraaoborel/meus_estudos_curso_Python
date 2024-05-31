# Crie um programa que crie uma matriz 3x3 e preencha os valores lidos pelo teclado.
# No final mostre a matriz na tela, com a formatação correta.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]      # Dentro de cada linha eu vou ter 3 valores, Pq 0? pra não precisar usar o append,
# O que eu vou fazer agora é substituir esse monte de zero por valores
# Agora eu vou ter que fazer um laço dentro do outro pra conseguir suprir todas as linhas e colunas
for l in range(0, 3):   # primeiro laço para as linhas, como tem 3 zeros dentro de cada lista na matriz, range de 0 a 3, sendo que o 3 é ignorado
    for c in range(0, 3):   # agora um laço para as colunas
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))      # Eu não posso colocar dentro de matriz só, tenho que colocar na linha l, e na coluna c
# print(matriz)   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('-=' * 30)
# A primeira estrutura de for foi para alimentar a matriz, apenas para colocar os números lá dentro
# vamos fazer agora de novo o for com a linha dentro da coluna
# E essa segunda estrutura de for, são estrutura de repetição para mostrar na tela
for l in range(0, 3):
    for c in range(0, 3):
        #print(f'[{matriz[l][c]}]', end='')      # [1][2][3][4][5][6][7][8][9]
        print(f'[{matriz[l][c]:^5}]', end='')   # {:^5} isso faz com que fique em 5 espaços centralizados
    print()     # Volto uma identação. E aqui, toda vez que ele terminar as colunas ele quebra pra poder fazer uma linha

