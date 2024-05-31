# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e qual foi o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

'''n1 = int(input('Digite um número: '))
c = 1
opção = str(input('Quer continuar? [S/N] '))
while opção in 'Ss':
    c += 1
    n2 = int(input('Digite um número: '))
    soma = n1 + n2
    media = soma / c
    opção = str(input('Quer continuar? [S/N] '))
print(f'Contei {c} números, e somei {soma}, e a média é {media}')'''

# Eu fiz isso acima, péssimo!

resp = 'S'
soma = qntd = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    qntd += 1
    if qntd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / qntd
print(f'Você digitou {qntd} números, e a média foi {media}, o maior valor é {maior} e o menor valor é {menor}')

# CABULOSO NÃO SEI SE É PORQUE ESTOU CANSADO, MAS NÃO CONSEGUI FAZER!
# DEU ERRO USANDO O MAX E O MIN