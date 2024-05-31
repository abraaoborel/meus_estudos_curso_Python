# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

distance_trip = float(input('\033[1;7;97;40mQual é a distância em km da sua viagem?\033[m '))
print(f'\033[97;42mVocê está prestes a começar uma viagem de {distance_trip:.1f}km.\033[m')
value_trip = distance_trip * 0.50 if distance_trip <= 200 else distance_trip * 0.45 # Da pra fazer em uma unica linha tb
print(f'\033[97;44mO preço da sua passagem é de R$ {value_trip:.2f}\033[m')

# O código abaixo foi colocado como comentário, e o codigo que está rodando tem apenas 1 linha
'''if distance_trip <= 200:
    value_trip = distance_trip * 0.50
    print(f'O preço da sua passagem é de R${value_trip:.2f}')
else:
    long_trip = distance_trip * 0.45
    print(f'O preço da sua passagem é de R${long_trip:.2f}')'''
