# Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# ========================//=============================

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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro foi {n1} e o valor real foi {n2}')
