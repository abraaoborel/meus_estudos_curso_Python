# Crie um programa que tenha uma tupla com várias palavas (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais vogais são as suas vogais.

versos = ('Porque', 'Deus', 'Amou', 'o', 'mundo',
          'de', 'tal', 'maneira', 'que', 'deu', 'seu',
          'unico', 'filho', 'para', 'que', 'todo', 'aquele',
          'que', 'nele', 'crer', 'não', 'pereça', 'mas',
          'tenha', 'a', 'vida', 'eterna'
          )
for p in versos:
    print(f'\nNa palavra {p.upper()}, temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':        # Caso eu quisesse pegar as palavras com acentos, era só colocar as letras aqui
            print(letra, end=' ')
