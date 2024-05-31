# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO,
# OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(ano):      # Esse def voto, vai receber um parâmetro que é ano
    from datetime import date       # Utilize essa função dentro da estrutura def, dessa forma o programa é otimizado
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:        # entre 16 e 18 é OPICIONAL, só que tbm acima de 65 é voto OPICIONAL
        return f'Com {idade} anos: VOTO OPICIONAL.'
    else:       # Se ele não está abaixo de 16, não está entre 16 e 18, não está acima de 65. Ele está de 18 à 65.
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#print(voto(2000))        #Como que eu quero que o programa funcione? Eu quero dar um print do resultado da minha função
#print(voto(2010))
#print(voto(1900))

# Também posso fazer como um input
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))