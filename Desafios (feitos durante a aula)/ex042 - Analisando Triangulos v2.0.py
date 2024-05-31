# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
# ======================================================================

print('\033[31m-\033[35m=\033[m'*20)
print('\033[1;97;40mAnalisador de Triângulos\033[m')
print('\033[31m-\033[35m=\033[m'*20)
pri_valor = float(input('\033[97;41mPrimeiro segmento:\033[m '))
seg_valor = float(input('\033[97;42mSegundo segmento:\033[m '))
ter_valor = float(input('\033[97;44mTerceiro segmento:\033[m '))
if pri_valor < seg_valor + ter_valor and seg_valor < pri_valor + ter_valor and ter_valor < pri_valor + seg_valor:
    print('\033[4;97;42mOs segmentos acima PODEM FORMAR um triângulo!\033[m ', end='') # ao digitar end= abrir e fechar aspas para continuar a linha
    if pri_valor == seg_valor == ter_valor:
        print('\033[4;97;42mEQUILÁTERO!\033[m')
    elif pri_valor != seg_valor != ter_valor != pri_valor:
        print('\033[4;97;42mESCALENO!\033[m')
    else:
        print('\033[4;97;42mISÓSCELES!\033[m')

else:
    print('\033[97;41mOs segmentos acima NÃO PODEM FORMAR um triângulo!\033[m')
