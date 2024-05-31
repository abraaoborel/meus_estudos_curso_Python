# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

# ---------------------------//------------------------------
# Para calcular sua média final, é necessário somar todos os resultados (4 + 6 + 8 = 18) e dividir a soma pela
# quantidade de resultados somados, que foram três. Portanto, a média aritmética das notas do aluno A
# corresponde a 18/3, que é igual a 6.
#-----------------------------//------------------------------

n1 = float(input('\033[1;97;43mVocê fez duas provas vou te dar a média delas!!!\033[m \n\033[1;33;40mQual foi a sua nota na primeira prova?\033[m🤔 '))
n2 = float(input('\033[1;33;40mQual foi a sua nota na segunda prova?\033[m🤨 '))
media = (n1 + n2)/2
print(f'\033[1;30;107mO resultado da média entre {n1:.1f} e {n2:.1f} é igual à: {media:.1f}.\033[m')
