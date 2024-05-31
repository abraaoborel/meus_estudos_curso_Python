# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario,
# com 15% de aumento.

salario = float(input('\033[31;40mQual o seu salário?\033[m R$ '))
aumento = float(input('\033[31;40mQuanto de aumento você recebeu?\033[m % '))
novosalario = salario + (salario * aumento / 100)
print(f'\033[32;40mSeu novo salario é igual à: \033[97;42mR$ {novosalario:.2f}\033[m')#.format(novosalario))

# Graças à dica da resolução do desafio 012, eu consegui concertar esse codigo!