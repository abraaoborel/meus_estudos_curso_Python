# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retângular(largura e comprimento)
# e mostre a área do terreno.

# Para calcular a área de um terreno retangular, basta multiplicar o comprimento pela largura.
# Por exemplo, se temos um terreno com 20 metros de largura e 25 metros de comprimento,
# a fórmula para encontrar a área é simples: 20 m x 25 m (largura x comprimento) = 500 m².


'''
def área(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')


print('Controle de Terrenos')
print('-' * 30)
área(l=float(input('Largura (m): ')), c=float(input('Comprimento (m): ')))
'''

# Eu consegui fazer o exercício sozinho,
# Mas vou fazer o do Guanabara junto também!

def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

# parecido com o meu, ficou um pouco mais organizado eu acho
