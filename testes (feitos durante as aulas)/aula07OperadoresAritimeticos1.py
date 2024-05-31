# Simbolos de contas no Python
#       + Adição
#       - Subtração
#       * Multiplicação
#       / Divisão
#       ** Potência
#       // Divisão inteira
#       % Resto da divisão
# --------------------//--------------------------------------
# Ordem de Precedência (O que vai executar primeiro?)
# 1 entre parênteses vai executar primeiro: ()
# 2 potência vai executar segundo: **
# 3 multiplicação, divisão, divisãi inteira e resto da divisão em terceiro: * / // %
# 4 e os ultimos a serem executados são mais e menos: + -
#--------------------//----------------------------------------

# nome = str(input('Qual é o seu nome? '))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))