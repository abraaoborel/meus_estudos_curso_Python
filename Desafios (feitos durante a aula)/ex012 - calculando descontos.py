# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

preço = float(input('\033[1;32;40mVocê ganhou 5% de desconto nesse produto, qual o valor deste produto?\033[m R$ '))
desconto =  float(input('\033[1;32;40mQuanto você recebeu de desconto? %\033[m '))
novopreço = preço - (preço * desconto / 100) #descobri a porcentagem, agora eu subtraio o valor da porcentagem pelo valor do produto
print(f'\033[30;42mO valor deste produto com o desconto de \033[4;30;42m{desconto:.0f}%\033[m\033[30;42m = \033[1;4;32;107mR$ {novopreço:.2f}\033[m')#.format(novopreço))

# Dica sobre porcentagem: X por cento = X/100
# 10% - como seria feito? R: 10/100
# 20% - como seria feito? R: 20/100
# 30% - como seria feito? R: 30/100
# 5% - como seria feito? R: 5/100
# Vamos dificultar um pouco mais!!!
# Eu quero 10% de 1500 - Qual a conta? 1500*10/100
# Eu quero 20% de 3000 - Qual a conta? 3000*20/100