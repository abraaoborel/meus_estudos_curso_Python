# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#
# Formúla:
# Para saber se um ano é bissexto, devemos verificar se ele se encaixa em
# um dos casos:
#
# Caso 1) É um número divisível por 4, mas não é divisível por 100.
# Caso 2) É um número divisível por 4, por 100 e por 400.
#
# Lembre-se que um número é divisível por outro quando o
# resto da divisão é zero, ou seja,
# quando o resultado da conta é um número inteiro, sem vírgula.
#
# Exemplos:
# a) 1964 é um ano bissexto, pois se encaixa no caso 1.
# → 1964 é divisível por 4 (1964 ÷ 4 = 491).
# → 1964 não é divisível por 100 (1964 ÷ 100 = 19,64).
#
# b) 2000 é um ano bissexto, pois se encaixa no caso 2.
# → 2000 é divisível por 4 (2000 ÷ 4 = 500).
# → 2000 é divisível por 100 (2000 ÷ 100 = 20).
# → 2000 é divisível por 400 (2000 ÷ 400 = 5).
#
# c) 1950 não é um ano bissexto, pois não se encaixa em nenhum dos casos.
# → 1950 não é divisível por 4 (1950 ÷ 4 = 487,5).
#
# d) 5000 não é um ano bissexto, pois não se encaixa em nenhum dos casos.
# → 5000 é divisível por 4 (5000 ÷ 4 = 1250).
# → 5000 é divisível por 100 (5000 ÷ 100 = 50).
# → 5000 não é divisível por 400 (5000 ÷ 400 = 12,5).
#
# Assim, podemos definir um algoritmo para saber se um ano é ou não bissexto.
#-----------------------//-------------------------
from datetime import date
year = int(input('\033[1;97;41mQue ano quer analisar? 🤔\033[m \n\033[1;7;97;40m Coloque 0 para analisar o ano atual:\033[m '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'\033[97;42mO ano {year} é BISSEXTO.\033[m')
else:
    print(f'\033[97;41mO ano {year} NÃO é BISSEXTO.\033[m')
