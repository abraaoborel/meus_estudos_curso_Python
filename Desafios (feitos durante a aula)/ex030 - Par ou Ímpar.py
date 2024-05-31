# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('\033[1;7;97;40mDigite um número qualquer:\033[m '))
resultado = num % 2
if resultado == 0:
    print(f'\033[97;42mO número {num} é PAR\033[m')
else:
    print(f'\033[97;41mO número {num} é IMPAR\033[m')
