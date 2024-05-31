# Na resolução deste exercício, no programa do Guanabara dando import moeda
# estava um sublinhado em vermelho embaixo da moeda em import moeda
# ele resolveu isso fazendo isso:   from ex107 import moeda
# Eu não consegui fazer isso no meu, porque eu coloquei no titulo da pasta espaços, e outros caracteres
# Mas como o meu não apareceu isso! OK!
# Deixo isso apenas como anotação, e uma observação na hora de criar o nome do diretorio/pastas/arquivos.py

import moeda

p = float(input('Digite um preço: R$ '))
print(f'A metade de R$ {p} é R$ {moeda.metade(p)}')
print(f'O dobro de R$ {p} é R$ {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
