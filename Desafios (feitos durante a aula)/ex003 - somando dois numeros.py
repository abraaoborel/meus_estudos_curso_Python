# Crie um programa que leia dois numeros e mostre a soma entre eles.

print('\033[33m-\033[32m=\033[m'*20)
n1 = int(input('\033[7;40mDigite um numero:\033[m '))
n2 = int(input('\033[7;40mDigite outro numero:\033[m '))
print('\033[33m-\033[32m=\033[m'*20)
s = n1 + n2
print(f'O resultado da soma entre os números \033[4m{n1}\033[m e \033[4m{n2}\033[m é igual à \033[4m{s}\033[m.')
