# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor for impar, desconsidere-o.

soma = 0
contador = 0
for x in range(1, 7):
    num = int(input(f'Digite o {x} valor: '))
    if num % 2 == 0:
        soma += num
        contador +=  1
print(f'Você informou {contador} números PARES, e a soma deles foi de {soma}')