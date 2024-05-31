# Crie um programa que leia o nome de uma pessoa e,
# diga se ela tem “SILVA” no nome.

nome = str(input('\033[97;41mDigite um nome:\033[m ')).strip()
print(f'\033[31;107mSeu nome tem Silva? {'SILVA' in nome.upper()}\033[m')

# .strip() para tirar os espaços
# comando in para buscar se existe o resultado da variavel nome dentro da string
