# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou
# não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

maior18 = tot_m = tot_f = 0
while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        maior18 += 1

    if sexo == 'M':
        tot_m += 1

    if sexo == 'F' and idade < 20:
        tot_f += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{maior18} pessoas são maiores de 18 anos.')
print(f'Foram cadastrados {tot_m} homens.')
print(f'{tot_f} mulheres tem menos de 20 anos.')