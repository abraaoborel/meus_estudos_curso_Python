# Crie um programa que tenha uma tupla
# totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostrá-lo por extenso.

n_extenso = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
    'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
    'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

num = 0
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Opção inválida! Tente Novamente.')
    else:
        print(f'Você digitou o número {n_extenso[num]}')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' Fim do Programa. Volte Sempre! '))

