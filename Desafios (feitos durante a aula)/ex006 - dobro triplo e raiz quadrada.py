# Crie um algoritmo que leia um numero e mostre o seu dobro,
# triplo e raiz quadrada.

#------------------------------------//----------------------
# n1 = int(input('Digite um número: '))
# m = n1 * 2
# t = n1 * 3
# rq = n1 ** (1/2)
# print('O dobro de {} = {} \nO triplo de {} = {} \nA raiz quadrada de {} = {:.2f}'.format(n1, m, n1, t, n1, rq))
#------------------------------------------//----------------


# errei na raiz quadrada! (X) numero, ** (1/2)
# durante o exercício um código mais curto foi passado, segue:
print('\033[1;34m-\033[1;97m=\033[m'*36)
print('\033[1;30;46mDigite um número e te mostrarei, o seu dobro, triplo e a raiz quadrada.\033[m')
print('\033[1;34m-\033[1;97m=\033[m'*36)

n = int(input('\033[1;97;43mDigite um número:\033[m '))

print(f'\033[1;97;43mO dobro de {n} vale {n*2}.\033[m')
print(f'\033[1;97;43mO triplo de {n} vale {n*3}.\033[m \n\033[1;97;43mA raiz quadrada de {n} é igual a {n**(1/2):.2f}.\033[m')
# outro codigo para calcular a raiz quadrada que também substitui n**(1/2), é: pow(n, (1/2)