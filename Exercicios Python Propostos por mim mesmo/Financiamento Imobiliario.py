# Faça um programa que simule um "financiamento imobiliário MCMV"

print('-'*20)
print('Simulação do Financiamento:')
print('Minha Casa Minha Vida')
print('-'*20)

renda_bruta = float(input('Digite o valor da sua Renda Mensal Bruta: R$ '))
imovel = float(input('Digite o valor do imóvel: R$ '))
entrada = imovel * 20 / 100 # funcionando! = 20% do valor do imóvel = ENTRADA
renda_minima30 = renda_bruta * 30 / 100 # funcionando! = 30% da Renda Bruta = SE FOR MAIOR DO QUE 30% NÃO FINANCIA.
renda_minima35 = renda_bruta * 35 / 100
#Faixa1
if renda_bruta <= 2640:
    print('Você se enquadra na Faixa 1 do Programa Minha Casa Minha Vida')
    print(f'Para um imóvel de \033[97;43mR$ {imovel:.2f}\033[m, o seu valor de entrada será de \033[97;43m{entrada:.2f}\033[m')
    print(f'Para o seu financiamento ser aprovado a sua \033[97;42mparcela\033[m, tem de estar entre \033[97;42mR$ {renda_minima30:.2f} e R$ {renda_minima35:.2f}\033[m')
    print('Para saber se será ou não aprovado, os seus documentos precisam ser enviados ao banco para uma analise de crédito.')
#Faixa2
elif renda_bruta > 2640 or renda_bruta <= 4.400:
    print('Você se enquadra na Faixa 2 do Programa Minha Casa Minha Vida')
    print(f'Para um imóvel de \033[97;43mR$ {imovel:.2f}\033[m, o seu valor de entrada será de \033[97;43m{entrada:.2f}\033[m')
    print(f'Para o seu financiamento ser aprovado a sua \033[97;42mparcela\033[m, tem de estar entre \033[97;42mR$ {renda_minima30:.2f} e R$ {renda_minima35:.2f}\033[m')
    print('Para saber se será ou não aprovado, os seus documentos precisam ser enviados ao banco para uma analise de crédito.')
#Faixa3
elif renda_bruta > 4.400 or renda_bruta <= 8000:
    print('Você se enquadra na Faixa 3, do Programa Minha Casa Minha Vida')
    print(f'Para um imóvel de \033[97;43mR$ {imovel:.2f}\033[m, o seu valor de entrada será de \033[97;43m{entrada:.2f}\033[m')
    print(f'Para o seu financiamento ser aprovado a sua \033[97;42mparcela\033[m, tem de estar entre \033[97;42mR$ {renda_minima30:.2f} e R$ {renda_minima35:.2f}\033[m')
    print('Para saber se será ou não aprovado, os seus documentos precisam ser enviados ao banco para uma analise de crédito.')