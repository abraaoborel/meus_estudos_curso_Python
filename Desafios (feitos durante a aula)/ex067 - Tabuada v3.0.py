# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# Para cada valor digitado pelo usuário.
# O programa será interrompido quando número solicitado for negativo.

n = 0
while True:
    print('=' * 40)
    n = int(input('Digite um número para saber a sua tabuada: '))
    print('=' * 40)

    if n < 0:
        break

    print('Multiplicação:')
    print('-'*15)
    for x in range(1, 11):
        print(f'{n} x {x} = {n*x}')

    print('-' * 15)
    print('Divisão:')
    print('-' * 15)
    for x in range(1, 11):
        print(f'{n*x} / {n} = {(n*x)//n}')

print('PROGRAMA DA TABUADA ENCERRADO. Volte Sempre!')
