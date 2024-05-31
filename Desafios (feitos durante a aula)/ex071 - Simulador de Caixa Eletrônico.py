# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20 e R$10 e R$1.

print('=' * 40)
print('{:^40}'.format('BANCO CEV'))
print('=' * 40)

valor = int(input('Quanto você quer sacar? R$ '))
total = valor       # total recebe o valor total a ser sacado (total)

ced = 50            # a partir da cedula de 50 eu vou tirar as outras
totced = 0          # total de cedulas a serem tiradas
while True:
    if total >= ced:        # Se o (total) for maior igual à ced de 50
        total -= ced        # Então o (total) será: total = total - ced (50),
        totced += 1         # totced, vai contar o número de cedulas de acordo com o número de loops que for realizado acima
    else:               # Senão... Senão der pra tirar... Vou verificar a minha ced atual
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')

        if ced == 50:       # Se a ced atual for igual a 50, então eu não posso mais tirar 50
            ced = 20        # Então a proxima ced vai virar uma cédula de 20, vai receber um novo valor
        elif ced == 20:     # Respectivamente o que foi feito abaixo
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0          # Cada vez que eu mudo de ced, eu tenho que fazer o total de ced voltar à 0
        if total == 0:      # Quando vai parar? Se o total for igual à 0, ou seja não tenho mais nada pra tirar
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')