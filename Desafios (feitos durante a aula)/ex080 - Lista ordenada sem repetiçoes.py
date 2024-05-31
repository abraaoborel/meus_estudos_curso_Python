# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.


lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
            # OK! Agora eu preciso descobrir em qual posição vou ter que adicionar
            # Existem 3 possibilidades:
            # Ou é o primeiro valor(append),
            # ou é o ultimo valor(append),
            # ou então ele vai estar no meio (mais trabalhoso)
    '''if c == 0:      # se c for primeiro valor, vai dar um appenda lá
        lista.append(n)
    elif n > lista[-1]:         # se n for maior do que o ultimo número da um append lá
        lista.append(n)'''      # Para simplificar o código, posso fazer dessa forma:
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:           # Senão... Se não for o primeiro e nem o ultimo...
        posiçao = 0
        while posiçao < len(lista):     # Ele vai da posição 0, até a ultima posição
            if n <= lista[posiçao]:     # Eu vou verificar se o número dentro de cada posição é menor ou igual a ele
                lista.insert(posiçao, n)    # Vou colocar na posição o valor n
                print(f'Adicionado na posição {posiçao} da lista...')
                break
                pos += 1       # Pra eu ir passando pra proxima posição
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')

# Não entendi porque está garrando o programa!
