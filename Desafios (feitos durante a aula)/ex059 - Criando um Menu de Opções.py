# Crie um programa que leia dois valores
# E mostre um menu na tela:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR DO PROGRAMA
# Seu programa deverá realizar a operação solicitada em cada caso.


from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''\nO que você que deve ser feito com estes valores?

        [ 1 ] SOMAR
        [ 2 ] MULTIPLICA
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA
    ''')
    opçao = int(input('>>>>> Qual é a sua opção? '))
    if opçao == 1:
        print(f'A soma de {n1} + {n2} = {n1+n2}')
    elif opçao == 2:
        print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
    elif opçao == 3:
        if n1 == n2:
            print(f'Não existe valor MAIOR. Porque {n1} é igual à {n2}.')
        else:
            print(f'Entre {n1} e {n2}, o MAIOR número é {max(n1, n2)}')
    elif opçao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-='*20)
sleep(2)
print('Fim do Programa! Volte Sempre!')

