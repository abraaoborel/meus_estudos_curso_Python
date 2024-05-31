# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores.

from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for indiv in range(1, 8):
    nasc = int(input(f'Em que ano a {indiv}a pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade')
print(f'E também tivemos {total_menor} pessoas menores de idade')
