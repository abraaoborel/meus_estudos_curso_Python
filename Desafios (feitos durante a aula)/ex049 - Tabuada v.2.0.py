# Refaça o desafio 009, mostrando a tabuada
# de um número que o usuário escolher, só que agora utilizando um laço for.

# ===================================================

# O programa só ficou grande porque eu colori ele!
# Só por causa da Biblioteca de Cores e mais NADA!!!
# Era pra ter 4 LINHAS!!!
# Por exemplo:
'''
# MULTIPLICAÇÃO:
for x in range(1, 11)
    print(f'{num} x {x} = {num*x}')
# DIVISÃO:
for x in range(1, 11)
    print(f'{num*x} / {num} = {(num*x)//num}')

'''
# apenas com as linhas acima eu se resolve as tabuadas!
# ===================================================



# dicionário/ Palheta de cores
colors = {'textwhite_backred':'\033[97;41m',
         'textwhite_backblue':'\033[97;44m',
         'no_colors':'\033[m',
         'titlewhite_red':'\033[1;97;41m',
         'titlewhite_blue':'\033[1;97;44m',
         'titleblack_white':'\033[1;30;107m',
          'text_yellow':'\033[32m'}


num = int(input(f'{colors['titleblack_white']}Digite um número para ver a sua tabuada:{colors['no_colors']} '))

# MULTIPLICAÇÃO:
print(f'{colors['text_yellow']}=={colors['no_colors']}'*20)
print(f'{colors['textwhite_backred']}MULTIPLICAÇÃO:{colors['no_colors']}')
print(f'{colors['text_yellow']}=={colors['no_colors']}'*20)

for x in range(1, 11):
    print(f'{colors['textwhite_backred']}{num} x {x} = {num*x}{colors['no_colors']}')
print(f'{colors['text_yellow']}=={colors['no_colors']}'*20)

# DIVISÃO:
print(f'{colors['textwhite_backblue']}DIVISÃO:{colors['no_colors']}')
print(f'{colors['text_yellow']}=={colors['no_colors']}'*20)

for x in range(1, 11,):
    print(f'{colors['textwhite_backblue']}{num*x} / {num} = {(num*x)//num}{colors['no_colors']}')
print(f'{colors['text_yellow']}=={colors['no_colors']}'*20)

