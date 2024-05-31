# Crie um aplicativo que leia um numero pelo teclado e
# mostre na tela a sua porção inteira.
# Exemplo:
# Digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6
# --------------------------------//-------------------------------

'''from math import trunc
num = float(input('Digite um número: '))
int = trunc(num)
print('O número {} tem a parte inteira {}'.format(num, int))'''

# Fiz sozinho!!! Muito bom!!! Mas depois de assistir a aula ficou com menos linhas, segue o resultado:

'''from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))'''

# Mais linhas nos codigos acima e menos linha nesse codigo final, todavia todos funcionam!

num = float(input('\033[1;7;40mDigite um número, para saber a sua parte inteira:\033[m '))
print(f'\033[7;31;40mO número {num} tem a parte inteira {int(num)}\033[m')#.format(num, int(num)))


