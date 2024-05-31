# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar
# Considere US$1.00=R$4.89 (valor dolar atualizado para o atual dia de hoje (04/01/2024)

real = float(input('\033[1;97;41mQuanto dinheiro você tem na carteira?\033[m R$ '))
dolar = real / 5.07
print(f'\033[31;107mCom R${real:.2f}, você pode comprar US${dolar:.2f}\033[m')#.format(real, dolar))

# Concertei o codigo, antes desse eu tinha errado no float, e ao inves de dividir o real por dolar, eu estava multiplicando o
# dolar por real e ao inves de usar ponto usei virgula e estava dando erro.