# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('**'*25)
print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIOS')
print('**'*25)

for x in range(10, -1, -1):     # Está o número 10, -1, -1 /Porque depois do 10, -1?
    sleep(0.5)                    # Porque se colocar 0 ele é ignorado, e mostra 1 ao invés de 0
    print(x)
print('BOOWM! FIIIITZZZZZ! BOOOWM! BLOOOOW!')
print('🎆🎆🎆🎆🎆🎆🎆🎇🎇🎇🎇🎇🎇🎇🎇🎇')
