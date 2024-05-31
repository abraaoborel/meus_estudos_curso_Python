# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

spd_car = float(input('\033[1;97;44mQual a velocidade atual do carro? 🚙💨\033[m '))
if spd_car >80:
    print('\033[97;41mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[m')
    multa = (spd_car - 80) * 7
    print(f'\033[4;97;41mVocê deve pagar uma multa de {multa:.2f} 💸💸💸\033[m') #achei essa sintaxe nova para formatar as casas decimais boleanas
    #print('O estado agradeçe!')
print('\033[97;42mDirija com segurança! Tenha um ótimo dia!\033[m')