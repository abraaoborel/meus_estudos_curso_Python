# Faça um programa que leia um número inteiro e mostre
# seu sucessor e seu antecessor.
#--------------------//-----------------------------

# n1 = int(input('Digite um número: '))
# a1 = n1 - 1
# s1 = n1 + 1
# print('O antecessor de {} é {}, e o sucessor de {} é {}!'.format(n1, a1, n1, s1))

#-------------------//-----------------------------

# eu fiz da forma acima, mas depois de ver o que foi ensinado na resolução do exercício da pra fazer com menos linhas!
print('\033[29m-\033[m\033[36m_\033[m\033[29m*'*25)
print('\033[1;33;107m Te darei o ANTECESSOR e e SUCESSOR, do número inteiro digitado!\033[m')
print('\033[29m-\033[m\033[36m_\033[m\033[29m*\033[m'*25)

n = int(input('\033[1;31;107mDigite um número:\033[m '))
print(f'\033[1;32;107mAnalisando o valor {n}, seu antecessor é {n-1}, e o seu sucessor é {n+1}.\033[m')
