# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.

num = [[], []]        # Estou declarando que está lista, tem duas listas internas, uma para o par e outra pro impar
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:  # Se esse valor for par, vou colocar na primeira [lista] dentro de [[num]]
        num[0].append(valor)        # num[0] = par
    else:   # Se não for par, é impar!
        num[1].append(valor)        # num[1] = impar
print('-=' * 30)
# Agora eu preciso ordenar as listas separadamente como eu faço isso?
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
