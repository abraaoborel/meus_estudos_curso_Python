# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('\033[1;97;44mDigite uma frase:\033[m ')).strip().lower()
#strip() para retirar os espaços e lower() para converter tudo pra minúsuclo

print(f'\033[97;41mA letra A aparece {frase.count('a')} vezes na frase.\033[m')
# agora vou contar na frase quantas vezes aparece a letra A

print(f'\033[97;42mA primeira letra A apareceu na posição {(frase.find('a')+1)}\033[m')
# find vai procurar qual posição apareceu determinado caractere na string
# +1 porque a contagem de strings começa da posição 0 e dessa forma comeraça do 1

print(f'\033[97;43mA última letra A apareceu na posição {(frase.rfind('a')+1)}\033[m')
# rfind vai procurar a partir do lado direito determinado caractere na string
# +1 poque a ccontagem de strings começa da posição 0 e dessa forma começará do 1