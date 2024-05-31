# A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
#=========================================================================================

from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else: # Tinha colocado elif idade > 25, mas pela simples lógica só o else já da o resultado correto
    print('Classificação: MASTER')
