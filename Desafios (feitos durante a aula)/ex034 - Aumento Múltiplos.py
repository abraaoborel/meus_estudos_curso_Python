# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\033[97;40mQuanto ganha o funcionário?\033[m R$ '))
# Esse código funciona também, mas achei mais correto incluir o else economizou algumas linhas.
'''if salario > 1250:
    salario10 = salario + (salario * 10 / 100)
    print(f'Você recebeu 10% de aumento, e seu novo salário é R${salario10:.2f}')'''

if salario <= 1250:
    salario15 = salario + (salario * 15 / 100)
    print(f'\033[97;42mO funcionário que ganhava {salario}, com um aumento de 15% agora passa a ganhar R${salario15:.2f}\033[m')
else:
    salario10 = salario + (salario *10 / 100)
    print(f'\033[97;44mO funcionário que ganhava {salario}, com um aumento de 10% agora passa a ganhar R${salario10}\033[m')
