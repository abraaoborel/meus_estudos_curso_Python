def leiaInt(msg):
    while True:
        try:    # Tenta fazer isso:
            n = int(input(msg))
        except (ValueError, TypeError):     # Se der problema faz isso:
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue    # Vai jogar pro laço dnv, ou seja vai tentar novamente
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:   # Se não der problema (ou seja, se tudo der certo), faz isso:
            return n


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção:\033[m ')
    return opc