# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input('\033[1;34;107mQual é a altura da sua parede?\033[m '))
alt = float(input('\033[1;34;107mQual é a largura da sua parede?\033[m '))
area = larg * alt
print(f'\033[97;44mSua parede tem a dimenssão de {larg:.2f}x{alt:.2f}m e a sua área total é de {area:.2f}m\033[m')#.format(larg, alt, area))
tinta = area / 2
print(f'\033[97;44mVocê precisa de {tinta:.1f}l de tinta, para pintar esta parede.\033[m')#.format(tinta))

# Essa eu acertei, diminui apenas a linha do print, desnecessário ter colocado a quantidade de tinta por litro, e abreviei as medidas.