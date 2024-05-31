# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex:
# 5! = 5x4x3x2x1 = 120
# fazer com o while e com for

'''from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

# Essa é uma maneira mais facil de fazer o fatorial, mas ainda não está de acordo com o que foi pedido.
# E nem todas as linguagens de programação, tem essa função. Então vamos fazer o fatorial de outra forma:

'''n = int(input('Digite um número para calcular o seu fatorial: '))
c = n       # O fatorial vai começar sempre com o número que foi digitado.
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:        # Enquanto (c)contador for maior do que 0:
    print(f'{c}', end='')         # Escrever na tela o valor do contador
    print(' x ' if c > 1 else ' = ', end='')        # Escreva ' x ' se contador for maior do que 1, do contrário escreva ' = '
    f *= c          # f começa com 1, multiplica vezes o loop em que o contador se encontra
    c -= 1          # O valor do contador, vai ser contador = contador - 1. Ou seja n = 5: loop de contador -1 até o 0
print(f'{f}')'''

# Eu faria este exercício, usando math fatorial
# desafio fazer este exercício usando o laço for, porque da pra saber o limite

from math import factorial

n = int(input('Digite um número para calcular o seu fatorial: '))
c = 0
f = factorial(n)
print(f'Calculando: {n}! = ', end='')
for c in range(n, c, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(f)

# consegui fazer com o for, desta forma!
# tentei colocar dentro de um unico print a estrutura if mas deu erro. preferi fazer desta forma!
# DEU CERTO !!! SHOW!!!
