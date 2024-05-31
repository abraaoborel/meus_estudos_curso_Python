# Escreva um programa que leia um valor em metros e
# o exiba convertido em centimetros e milimetros.

medida = float(input('\033[1;30;107mEscreva uma distância em metros:\033[m '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'\033[1;97;41mA medida de {medida}m corresponde a:\033[m')
print(f'\033[1;97;41m{km:.0f}km;\033[m')
print(f'\033[1;97;41m{hm:.0f}hm;\033[m')
print(f'\033[1;97;41m{dam:.0f}dam;\033[m')
print(f'\033[1;97;41m{dm:.0f}dm;\033[m')
print(f'\033[1;97;41m{cm:.0f}cm;\033[m')
print(f'\033[1;97;41m{mm:.0f}mm.\033[m')

# Errei no começo, porque eu usei o tipo primitivo int, e deveria ter usado o tipo primitivo float.