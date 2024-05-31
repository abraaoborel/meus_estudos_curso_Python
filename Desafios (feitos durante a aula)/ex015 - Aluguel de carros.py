# Escreva um programa que pergunte a quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o
# preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por Km rodado.

# Antes de assistir a resolução eu tinha feito assim:
# diaria = dia * 60
# kmrodado = km * 0.15
# depois de assistir a resolução transformei o total em 1 linha!

dias = int(input('\033[1;32;40mQuantos dias alugados?\033[m '))
km = int(input('\033[1;32;40mQuantos Km rodados?\033[m '))
total = (dias * 60) + (km * 0.15)
print(f'\033[1;7;40mO total a pagar é de R$ {total:.2f}\033[m')#.format(total))


