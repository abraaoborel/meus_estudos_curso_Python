# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr = str(input('Digite a expressão: '))      # Toda string é uma lista, eu consigo utilizar um for para pegar cada letra/simbolo
pilha = list()
for simbolo in expr:
    if simbolo == '(':          # Se o simbolo for igual ao parenteses abrindo "(" ele vai fazer alguma coisa:
        pilha.append('(')       # Cada vez que o parenteses abrir eu vou jogar nessa pilha
    elif simbolo == ')':        # Aqui eu tenho 2 possiblidades, ou a minha lista está vazia, ou a minha lista está cheia, porque pode ser que o parenteses ")" esteja no final da lista
        if len(pilha) > 0:      # Se o tamanho da minha pilha foi maior do que zero, é sinal de que ele não está vazio
            pilha.pop()         # Remove o ultimo elemento de uma lista
        else:                   # se a pilha estiver vazia
            pilha.append(')')
            break
if len(pilha) == 0:             # Se a minha lista não tiver nenhum parenteses aberto:
    print('Sua expressão está válida!')
else:                           # Se ela ainda tiver um parenteses aberto:
    print('Sua expressão está errada!')

# Um resumo da expressão acima:
# Toda vez que eu digitar um "(", ele vai adicionar este parenteses à lista
# Então exemplo eu digitei (((, ele vai adicionar na lista (((
# E toda vez que eu digitar um ")", ele vai excluir um "("
# exemplo: ((( + ))) = 0
# exemplo: ((( + )) = 1
