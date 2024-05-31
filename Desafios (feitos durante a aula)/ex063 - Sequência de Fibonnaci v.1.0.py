# Escreva um programa que leia um número n inteiro,
# e mostra na tela os N primeiros elementos de uma Sequencia de Fibonacci.
# Ex:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5-> 8 ->

# Lógica:
# "A sequência de Fibonacci é uma sequência numérica em que
# cada termo a partir do terceiro é a soma dos dois antecessores.
# O primeiro termo da sequência de Fibonacci é o número 1 e
# o segundo termo também é o número 1.
# O terceiro termo é 2, pois 1+1=2.
# Já o quarto termo é 3, pois 1+2=3.
# E assim sucessivamente."

# 0 - 1 - 1 - 2 - 3 - 5
            # t1  t2  t3   (Essá é a lógica por trás desse programa)
            # é só ir andando e casa em casa e, t1 passa a ser = t2, e t2 passa a ser = t3, e o t3 = t1 + t2

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
contador = 3        # Começar a contar no 3, porque já mostrei o primeiro e o segundo termo
while contador <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
print('~'*30)
