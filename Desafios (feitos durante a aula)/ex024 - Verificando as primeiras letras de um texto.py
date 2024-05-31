# Crie um programa que leia o nome de uma cidade e,
# diga se ela começa ou não com o nome “SANTO”.

nome_cidade = str(input('\033[97;41mEm que cidade você nasceu?\033[m ')).strip()
print(nome_cidade[:5].upper() == 'SANTO')

# .strip() para eliminar os espaços
# [:5] para buscar os 5 primeiros caracteres da string
# .upper() para converter tudo pra maiusculo, caso o usuário digite maiusculo ou minusculo vai dar certo
# simbolo de == para saber se o que foi digitado é igual à SANTO