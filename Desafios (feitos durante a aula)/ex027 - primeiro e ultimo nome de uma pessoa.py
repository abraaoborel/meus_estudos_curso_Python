# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('\033[97;41mDigite seu nome completo:\033[m ')).strip().split()
# strip para reitrar os espaços
# split para organizar a variável nome em uma lista

print(f'\033[97;44mSeu primeiro nome é {nome[0]}\033[m')
# da variável nome pegue a parte 0 que foi splitada

print(f'\033[97;43mSeu último nome é {nome[len(nome)-1]}\033[m')
# se a variável nome foi splitada, e 0 é a primeira parte
# utilizando o comando len na variável nome que foi splitada,
# ele vai me dizer quantas posições tem a varável nome
# O [-1] pode ser utilizado para se referir ao último objeto de uma lista,
# assim como [-2] seria a penúltima e assim por diante.
