# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('\033[1;7;30;107mDigite um número:\033[m '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'\033[1;30;107mAnalisando o número: {num} \033[m')
print(f'\033[1;7;31;107mUnidade: {u} \033[m')
print(f'\033[1;31;40mDezena: {d} \033[m')
print(f'\033[1;30;41mCentena: {c} \033[m')
print(f'\033[1;7;32;107mMilhar: {m} \033[m')
