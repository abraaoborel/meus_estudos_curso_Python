# Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

# Dados três segmentos de reta distintos,
# se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.
# Por exemplo, dados os segmentos AB = 16 cm, CD = 20 cm e EF = 30 cm,
# é possível usá-los para construir um triângulo, pois as somas abaixo são verdadeiras: 16 + 20 = 36 > 30
print('\033[31m-\033[35m=\033[m'*20)
print('\033[1;97;40mAnalisador de Triângulos\033[m')
print('\033[31m-\033[35m=\033[m'*20)
pri_valor = float(input('\033[97;41mPrimeiro segmento:\033[m '))
seg_valor = float(input('\033[97;42mSegundo segmento:\033[m '))
ter_valor = float(input('\033[97;44mTerceiro segmento:\033[m '))
# Codigo que o Guanabara fez na resolução do exercicio
# r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2
# Esse codigo abaixo, eu mesmo que fiz de acordo com a resolução matemática encontrada acima, proximo ao enunciado.
# Não apresentou nenhum, erro. E todos os resultados foram os mesmos que o Guanabara obteve.
if pri_valor < seg_valor + ter_valor and seg_valor < pri_valor + ter_valor and ter_valor < pri_valor + seg_valor:
    print('\033[4;97;42mOs segmentos acima PODEM FORMAR um triângulo!\033[m')
else:
    print('\033[97;41mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m')
#no final acabei copiando o codigo que o Guanabará fez, pq mostrou um resultado errado