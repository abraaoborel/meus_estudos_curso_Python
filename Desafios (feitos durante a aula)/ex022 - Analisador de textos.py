# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('\033[1;7;30;107mDigite seu nome completo:\033[m ')).strip()
print('\033[1;30;107mAnalisando seu nome...\033[m')
print(f'\033[1;97;44mSeu nome em maíusculas é {(nome.upper())}\033[m')#.format(nome.upper()))
print(f'\033[1;97;43mSeu nome em minúsculas é {(nome.lower())}\033[m')#'.format(nome.lower()))
print(f'\033[1;97;42mSeu nome tem ao todo {len(nome) - nome.count(' ')} caracteres\033[m')#.format(len(nome) - nome.count(' ')))
# - nome.count(' ') para remover os espaços
separa = nome.split()
print(f'\033[1;97;41mSeu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras\033[m')
