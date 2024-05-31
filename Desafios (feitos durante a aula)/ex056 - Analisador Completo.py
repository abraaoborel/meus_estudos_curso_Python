# Desenvolva um programa que leia o
# nome,
# idade,
# sexo
# de 4 pessoas.
# No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres tem menos de 20 anos.

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulheres_menos_20 = 0
for p in range(1,5):
    print(f'======= {p}ª PESSOA =======')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_menos_20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do gruop é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {total_mulheres_menos_20} mulheres com menos de 20 anos')
