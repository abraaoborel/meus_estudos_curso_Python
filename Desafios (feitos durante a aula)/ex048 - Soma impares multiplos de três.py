# Faça um programa que calcule a soma entre todos os
# números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0 # ACUMULADOR: soma vai começar com 0 porque? porque eu não tenho nenhum numero que é divisivel por 3
contador = 0 # CONTADOR: 0 porque ate agora não contei numero nenhum
for x in range(1, 501, 2):
    if x % 3 == 0:
      # contador = contador + 1     # Cada vez que o comando acima achar um numero divisivel por 3 ele vai contar + 1, partindo do 0
      # soma = soma + x             # Aqui ele vai acumulando(somando) os valores
        contador += +1      # Tinha feito conforme as linhas acima, mas este exemplo abaixo é mais simples
        soma += x           # Tinha feito conforme as linhas acima, mas este exemplo abaixo é mais simples
print(f'A SOMA de todos os {contador} valores que são divisíveis por 3, é {soma}.')
