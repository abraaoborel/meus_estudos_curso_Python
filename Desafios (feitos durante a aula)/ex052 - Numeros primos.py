# Faça um programa que leia um número inteiro e
# diga se ele é ou não um número primo.

# Um número primo só pode ser dividido por 1 e por ele mesmo.
# Caso contrário não é um número primo.

num = int(input('Digite um número: '))
total = 0
for x in range (1, num +1):
    if num % x == 0:
        print('\033[1;33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{x} ', end=' ')
print(f'\n\033[mO número {num} foi divisível {total} vezes.')
if total == 2:          # Um número primo só pode ser dividido por 1 e por ele mesmo. Ou seja 2x
    print('\033[1;32mPor isso ele é PRIMO!')
else:
    print('\033[31mPor isso ele não é PRIMO!')
