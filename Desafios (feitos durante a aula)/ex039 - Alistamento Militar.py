# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#==================================================================================

from datetime import date
atual = date.today().year
print('Qual o seu sexo?')
sexo = str(input('Digite M para masculino, ou F para feminino: ')).strip()
if sexo.lower() == 'm':
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        saldo = idade - 18  #
        print(f'Você já deveria ter se alistado há {saldo} anos')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda faltam {saldo} anos para o alistamento.')
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}')
elif sexo.lower() == 'f':
    print('Você não precisa fazer alistamento militar obrigatório.')
else:
    print('Opção inválida! Tente novamente!')
