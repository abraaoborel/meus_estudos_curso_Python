# Faça um programa que leia um número inteiro qualquer e
# mostre na tela a sua tabuada.

#n1 = int(input('Você quer saber a tabuada de qual número? '))
#t1 = n1 * 1
#t2 = n1 * 2
#t3 = n1 * 3
#t4 = n1 * 4
#t5 = n1 * 5
#t6 = n1 * 6
#t7 = n1 * 7
#t8 = n1 * 8
#t9 = n1 * 9
#t10 = n1 * 10
#acima a multiplicação e abaixo a divisão:
#d1 = t1 // n1
#d2 = t2 // n1
#d3 = t3 // n1
#d4 = t4 // n1
#d5 = t5 // n1
#d6 = t6 // n1
#d7 = t7 // n1
#d8 = t8 // n1
#d9 = t9 // n1
#d10 = t10 // n1
#print('='*20)
#print('A tabuada da multiplicação de {} é: \n {} x 1 = {} \n {} x 2 = {} \n {} x 3 = {} \n {} x 4 = {} \n {} x 5 = {} \n {} x 6 = {} \n {} x 7 = {} \n {} x 8 = {} \n {} x 9 = {} \n {} x 10 = {}'.format(n1, n1, t1, n1, t2, n1, t3, n1, t4, n1, t5, n1, t6, n1, t7, n1, t8, n1, t9, n1, t10))
#print('='*20)
#print('\n A tabuada da divisão de {} é: \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {} \n {} / {} = {}'.format(n1, t1, n1, d1, t2, n1, d2, t3, n1, d3, t4, n1, d4, t5, n1, d5, t6, n1, d6, t7, n1, d7, t7, n1, d8, t9, n1, d9, t10, n1, d10))
#print('='*20)
#-------------------//-------------------
# da pra ser feito também dessa forma:
# n1 = int('Digite um número para ver a sua tabuada: ')
# print('{} x {} = {}'.format(n1, 1, n1*1)
# etc...
#----------------//-----------------

n = int(input('\033[1;30;107mDigite um número para ver a sua tabuada:\033[m '))
print('\033[33m=\033[m'*20)
print('\033[1;97;41mMultiplicação:\033[m')
print('\033[33m=\033[m'*20)

print(f'\033[97;41m{n} x {1} = {n*1}\033[m')#.format(n, 1, n*1))
print(f'\033[97;41m{n} x {2} = {n*2}\033[m')#.format(n, 2, n*2))
print(f'\033[97;41m{n} x {3} = {n*3}\033[m')#.format(n, 3, n*3))
print(f'\033[97;41m{n} x {4} = {n*4}\033[m')#. format(n, 4, n*4))
print(f'\033[97;41m{n} x {5} = {n*5}\033[m')#.format(n, 5, n*5))
print(f'\033[97;41m{n} x {6} = {n*6}\033[m')#.format(n, 6, n*6))
print(f'\033[97;41m{n} x {7} = {n*7}\033[m')#.format(n, 7, n*7))
print(f'\033[97;41m{n} x {8} = {n*8}\033[m')#.format(n, 8, n*8))
print(f'\033[97;41m{n} x {9} = {n*9}\033[m')#.format(n, 9, n*9))
print(f'\033[97;41m{n} x {10} = {n*10}\033[m')#.format(n, 10, n*10))

print('\033[32m=\033[m'*20)
print('\033[1;97;44mDivisão:\033[m')
print('\033[32m=\033[m'*20)

print(f'\033[97;44m{n*1} / {n} = {(n*1)//n}\033[m')#.format(n*1, n, (n*1)//n))
print(f'\033[97;44m{n*2} / {n} = {(n*2)//n}\033[m')#.format(n*2, n, (n*2)//n))
print(f'\033[97;44m{n*3} / {n} = {(n*3)//n}\033[m')#.format(n*3, n, (n*3)//n))
print(f'\033[97;44m{n*4} / {n} = {(n*7)//n}\033[m')#.format(n*4, n, (n*4)//n))
print(f'\033[97;44m{n*5} / {n} = {(n*5)//n}\033[m')#.format(n*5, n, (n*5)//n))
print(f'\033[97;44m{n*6} / {n} = {(n*6)//n}\033[m')#.format(n*6, n, (n*6)//n))
print(f'\033[97;44m{n*7} / {n} = {(n*7)//n}\033[m')#.format(n*7, n, (n*7)//n))
print(f'\033[97;44m{n*8} / {n} = {(n*8)//n}\033[m')#.format(n*8, n, (n*8)//n))
print(f'\033[97;44m{n*8} / {n} = {(n*8)//n}\033[m')#.format(n*9, n, (n*9)//n))
print(f'\033[97;44m{n*10} / {n} = {(n*10)//n}\033[m')#.format(n*10, n, (n*10)//n))
print('\033[32m=\033[m'*20)

#Essa da divisão da pra quebrar a cuca!