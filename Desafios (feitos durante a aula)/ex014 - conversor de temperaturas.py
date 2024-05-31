# Escreva um programa que converta uma temperatura digitada em °C
# e a converta para, °F.
#
# A formula que eu encontrei no google para essa conversão é: °F = (°C x 1.8) + 32
# ou: ========[   °F = °C x 9 ÷ 5 + 32  ]============
#
# A formula ensinada na resolução desse problema foi a seguinte:
# f = 9 * c / 5 + 32
# A formula acima, é a igual a mesma que eu tinha digitado acima.

c = float(input('\033[1;36;40mInforme a temperatura em °C:\033[m '))
f = c * 1.8 + 32
print(f'\033[1;36;40mA temperatura de {c:.1f}°C corresponde a {f:.1f} °F!\033[m')#.format(c, f))

