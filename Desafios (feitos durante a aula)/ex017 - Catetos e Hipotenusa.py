# Faça um programa que leia o comprimento do cateto oposto ao
# cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.

'''from math import hypot
cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = cateto_oposto/cateto_adjacente
print('O comprimento da Hipotenusa é: {}'.format(hipotenusa))'''

# Fiz o codigo acima, mas deu erro. Mas ao menos tentei bora fazer a resolução deste problema:
# 1a Solução:
'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) **(1/2) #FORMULA PARA CALCULAR A HIPOTENUSA
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
# 2a Solução:
'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
# 3a Solução:
from math import hypot
co = float(input('\033[1;7;97;40mComprimento do cateto oposto:\033[m '))
ca = float(input('\033[1;7;97;40mComprimento do cateto adjacente:\033[m '))
hi = hypot(co, ca)
print(f'\033[1;7;30;107mA hipotenusa vai medir {hi:.2f}\033[m')#.format(hi))