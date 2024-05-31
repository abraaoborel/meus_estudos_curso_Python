# Faça um programa que tenha uma função chamada maior(),
# que recebe vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

'''
def maior(* num):
    print('-=' * 30)
    print('Analisando valores passados...')

    if len(num) <= 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        print(f'{num} Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''

# Tentei me aproximar ao máximo daquilo que o Guanabara pediu!
# Ficou quase tudo certo, mas o resultado dele não apresenta parenteses quando mostra os números
# Só isso, fora isso eu fiz tudo certo! Consegui fazer sozinho!!!
# E também o sleep eu não fiz, dos números aparencendo em sequência, talvez deva ter sido feito com o laço while

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()