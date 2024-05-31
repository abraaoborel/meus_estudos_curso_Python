# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.

print('\033[31m-\033[33m#\033[m'*30)
print('''\033[30;47mVou te mostrar o tipo primitivo, e todas as\033[m 
\033[30;47minformações possíveis sobre o que foi digitado.\033[m''')
print('\033[31m-\033[33m#\033[m'*30)

n1 = (input('\033[31mVamos lá, digite algo:\033[m '))

print('\033[1;29mO tipo primitivo desse valor é ', type(n1))
print('É um número? ', n1.isnumeric())
print('Só tem espaços? ', n1.isspace())
print('É alfabético? ', n1.isalpha())
print('É alfanumérico? ', n1.isalnum())
print('Está em maiusculas? ', n1.isupper())
print('Está em minusculas? ', n1.islower())
print('Está capitalizada? ', n1.istitle())
